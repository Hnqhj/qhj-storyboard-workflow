#!/usr/bin/env python3
"""Evidence-driven capsule storage for Sophia's local SQLite memory."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import uuid
from pathlib import Path


_default_db = Path(r"D:\SophiaMemory\data\sophia_memory.sqlite")
if not _default_db.exists():
    _default_db = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "memories_1.sqlite"
DEFAULT_DB = Path(os.environ.get("SOPHIA_MEMORY_DB", _default_db))
SCHEMA = Path(__file__).with_name("capsule_schema.sql")
STATUSES = ("candidate", "provisional", "validated", "active", "deprecated", "archived")


def clamp(value: float) -> float:
    return round(max(0.0, min(1.0, value)), 4)


def dumps(values: list[str]) -> str:
    return json.dumps(list(dict.fromkeys(values)), ensure_ascii=False)


def loads(value: str) -> list[str]:
    data = json.loads(value)
    if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
        raise ValueError("Expected a JSON string list")
    return data


def connect(db: Path) -> sqlite3.Connection:
    db.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def init_db(db: Path) -> None:
    with connect(db) as con:
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
    print(json.dumps({"ok": True, "db": str(db), "schema": 1}, ensure_ascii=False, indent=2))


def ensure_schema(con: sqlite3.Connection) -> None:
    row = con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='capsules'"
    ).fetchone()
    if not row:
        raise SystemExit("Capsule schema is missing. Run `init` first.")


def make_id(prefix: str, name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:28] or prefix
    return f"{prefix}_{slug}_{uuid.uuid4().hex[:8]}"


def get_capsule(con: sqlite3.Connection, capsule_id: str) -> sqlite3.Row:
    row = con.execute("SELECT * FROM capsules WHERE id = ?", (capsule_id,)).fetchone()
    if not row:
        raise SystemExit(f"Unknown capsule: {capsule_id}")
    return row


def capsule_dict(row: sqlite3.Row) -> dict:
    out = dict(row)
    for key in ("bound_scenarios", "tags", "source_refs", "target_skills"):
        out[key] = loads(out[key])
    return out


def create_capsule(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        capsule_id = args.id or make_id("capsule", args.name)
        con.execute(
            """
            INSERT INTO capsules(
              id, name, capsule_class, knowledge_kind, summary, what_worked,
              when_to_apply, why_it_works, failure_conditions, bound_scenarios,
              tags, source_refs, evidence_confidence, context_fit, utility_score,
              freshness, stability
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                capsule_id,
                args.name,
                args.capsule_class,
                args.knowledge_kind,
                args.summary,
                args.what_worked,
                args.when_to_apply,
                args.why_it_works,
                args.failure_conditions,
                dumps(args.scenario),
                dumps(args.tag),
                dumps(args.source_ref),
                args.evidence_confidence,
                args.context_fit,
                args.utility_score,
                args.freshness,
                args.stability,
            ),
        )
        con.execute(
            """
            INSERT INTO capsule_events(capsule_id, event_type, context, result, source)
            VALUES (?, 'capture', ?, ?, ?)
            """,
            (capsule_id, args.when_to_apply, args.summary, ", ".join(args.source_ref)),
        )
    print(json.dumps({"ok": True, "id": capsule_id, "status": "candidate"}, ensure_ascii=False, indent=2))


def add_spore(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        spore_id = args.id or make_id("spore", args.statement)
        con.execute(
            """
            INSERT INTO capsule_spores(
              id, kind, statement, context, source, evidence_confidence, tags
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                spore_id,
                args.kind,
                args.statement,
                args.context,
                args.source,
                args.evidence_confidence,
                dumps(args.tag),
            ),
        )
    print(json.dumps({"ok": True, "id": spore_id, "status": "pending"}, ensure_ascii=False, indent=2))


def consume_spore(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        get_capsule(con, args.capsule_id)
        changed = con.execute(
            """
            UPDATE capsule_spores
            SET status='consumed', consumed_by=?, consumed_at=datetime('now')
            WHERE id=? AND status='pending'
            """,
            (args.capsule_id, args.spore_id),
        ).rowcount
        if not changed:
            raise SystemExit("Spore is missing or is not pending.")
    print(json.dumps({"ok": True, "spore_id": args.spore_id, "capsule_id": args.capsule_id}, indent=2))


def distinct_success_contexts(con: sqlite3.Connection, capsule_id: str) -> int:
    return con.execute(
        """
        SELECT count(DISTINCT context_key)
        FROM capsule_events
        WHERE capsule_id=? AND event_type='application_success' AND context_key<>''
        """,
        (capsule_id,),
    ).fetchone()[0]


def latest_counterexample_id(con: sqlite3.Connection, capsule_id: str) -> int:
    return con.execute(
        """
        SELECT coalesce(max(id), 0) FROM capsule_events
        WHERE capsule_id=? AND event_type='counterexample'
        """,
        (capsule_id,),
    ).fetchone()[0]


def latest_success_id(con: sqlite3.Connection, capsule_id: str) -> int:
    return con.execute(
        """
        SELECT coalesce(max(id), 0) FROM capsule_events
        WHERE capsule_id=? AND event_type='application_success'
        """,
        (capsule_id,),
    ).fetchone()[0]


def record_event(args: argparse.Namespace) -> None:
    event_map = {
        "success": "application_success",
        "failure": "application_failure",
        "neutral": "application_neutral",
        "counterexample": "counterexample",
    }
    with connect(args.db) as con:
        ensure_schema(con)
        row = get_capsule(con, args.id)
        event_type = event_map[args.outcome]
        con.execute(
            """
            INSERT INTO capsule_events(capsule_id, event_type, context_key, context, result, source)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (args.id, event_type, args.context_key, args.context, args.result, args.source),
        )

        evidence = row["evidence_confidence"]
        context_fit = row["context_fit"]
        utility = row["utility_score"]
        stability = row["stability"]
        success_count = row["success_count"]
        failure_count = row["failure_count"]
        status = row["status"]

        if args.outcome == "success":
            utility = clamp(utility + 0.05)
            context_fit = clamp(context_fit + 0.03)
            stability = clamp(stability + 0.03)
            success_count += 1
        elif args.outcome == "failure":
            utility = clamp(utility - 0.08)
            context_fit = clamp(context_fit - 0.05)
            stability = clamp(stability - 0.03)
            failure_count += 1
        elif args.outcome == "counterexample":
            evidence = clamp(evidence - 0.15)
            stability = clamp(stability - 0.15)
            failure_count += 1
            if status == "active":
                status = "validated"
            elif status == "validated":
                status = "provisional"

        con.execute(
            """
            UPDATE capsules
            SET status=?, evidence_confidence=?, context_fit=?, utility_score=?,
                stability=?, success_count=?, failure_count=?,
                last_applied_at=datetime('now'), updated_at=datetime('now')
            WHERE id=?
            """,
            (
                status,
                evidence,
                context_fit,
                utility,
                stability,
                success_count,
                failure_count,
                args.id,
            ),
        )

        row = get_capsule(con, args.id)
        contexts = distinct_success_contexts(con, args.id)
        last_counterexample = latest_counterexample_id(con, args.id)
        last_success = latest_success_id(con, args.id)
        next_status = row["status"]
        if next_status == "candidate" and success_count >= 1 and contexts >= 1:
            next_status = "provisional"
        if (
            next_status in ("candidate", "provisional")
            and success_count >= 2
            and contexts >= 2
            and evidence >= 0.70
            and last_success > last_counterexample
        ):
            next_status = "validated"
        if next_status != row["status"]:
            con.execute(
                "UPDATE capsules SET status=?, updated_at=datetime('now') WHERE id=?",
                (next_status, args.id),
            )
            con.execute(
                """
                INSERT INTO capsule_events(capsule_id, event_type, context, result, source)
                VALUES (?, 'promotion', ?, ?, 'capsule-engine')
                """,
                (args.id, args.outcome, f"auto-promoted to {next_status}"),
            )

        final_row = get_capsule(con, args.id)
    print(json.dumps(capsule_dict(final_row), ensure_ascii=False, indent=2))


def activate(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        row = get_capsule(con, args.id)
        policy_ok = (
            args.policy_decision
            and row["capsule_class"] == "architecture"
            and row["knowledge_kind"] in ("rule", "process")
            and row["evidence_confidence"] >= 0.85
        )
        if row["status"] != "validated" and not policy_ok:
            raise SystemExit("Activation requires validated status or a qualified --policy-decision.")
        targets = list(dict.fromkeys(loads(row["target_skills"]) + args.target_skill))
        con.execute(
            """
            UPDATE capsules SET status='active', target_skills=?, updated_at=datetime('now')
            WHERE id=?
            """,
            (dumps(targets), args.id),
        )
        reason = args.reason or ("user-confirmed policy decision" if policy_ok else "validated capsule activation")
        con.execute(
            """
            INSERT INTO capsule_events(capsule_id, event_type, context, result, source)
            VALUES (?, 'activation', ?, ?, ?)
            """,
            (args.id, ", ".join(targets), reason, args.source),
        )
        final_row = get_capsule(con, args.id)
    print(json.dumps(capsule_dict(final_row), ensure_ascii=False, indent=2))


def change_status(args: argparse.Namespace, status: str, event_type: str) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        get_capsule(con, args.id)
        con.execute(
            "UPDATE capsules SET status=?, updated_at=datetime('now') WHERE id=?",
            (status, args.id),
        )
        con.execute(
            """
            INSERT INTO capsule_events(capsule_id, event_type, result, source)
            VALUES (?, ?, ?, ?)
            """,
            (args.id, event_type, args.reason, args.source),
        )
    print(json.dumps({"ok": True, "id": args.id, "status": status}, ensure_ascii=False, indent=2))


def add_link(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        get_capsule(con, args.from_id)
        get_capsule(con, args.to_id)
        con.execute(
            """
            INSERT OR REPLACE INTO capsule_links(from_capsule, to_capsule, relation, notes)
            VALUES (?, ?, ?, ?)
            """,
            (args.from_id, args.to_id, args.relation, args.notes),
        )
        con.execute(
            """
            INSERT INTO capsule_events(capsule_id, event_type, context, result, source)
            VALUES (?, 'link', ?, ?, ?)
            """,
            (args.from_id, args.relation, args.to_id, args.source),
        )
    print(json.dumps({"ok": True, "from": args.from_id, "to": args.to_id, "relation": args.relation}, indent=2))


def show_capsule(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        row = get_capsule(con, args.id)
        events = [
            dict(item)
            for item in con.execute(
                "SELECT * FROM capsule_events WHERE capsule_id=? ORDER BY id",
                (args.id,),
            ).fetchall()
        ]
        links = [
            dict(item)
            for item in con.execute(
                """
                SELECT * FROM capsule_links
                WHERE from_capsule=? OR to_capsule=?
                ORDER BY created_at
                """,
                (args.id, args.id),
            ).fetchall()
        ]
    print(json.dumps({"capsule": capsule_dict(row), "events": events, "links": links}, ensure_ascii=False, indent=2))


def search_capsules(args: argparse.Namespace) -> None:
    query = f"%{args.query}%"
    with connect(args.db) as con:
        ensure_schema(con)
        rows = con.execute(
            """
            SELECT id, name, capsule_class, knowledge_kind, status, summary,
                   evidence_confidence, utility_score, stability, target_skills
            FROM capsules
            WHERE name LIKE ? OR summary LIKE ? OR tags LIKE ? OR bound_scenarios LIKE ?
            ORDER BY CASE status
              WHEN 'active' THEN 0 WHEN 'validated' THEN 1 WHEN 'provisional' THEN 2
              WHEN 'candidate' THEN 3 WHEN 'deprecated' THEN 4 ELSE 5 END,
              utility_score DESC, updated_at DESC
            LIMIT ?
            """,
            (query, query, query, query, args.limit),
        ).fetchall()
        out = []
        for row in rows:
            item = dict(row)
            item["target_skills"] = loads(item["target_skills"])
            out.append(item)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def list_capsules(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        sql = "SELECT * FROM capsules"
        params: list[object] = []
        if args.status:
            sql += " WHERE status=?"
            params.append(args.status)
        sql += " ORDER BY updated_at DESC LIMIT ?"
        params.append(args.limit)
        rows = [capsule_dict(row) for row in con.execute(sql, params).fetchall()]
    print(json.dumps(rows, ensure_ascii=False, indent=2))


def stats(args: argparse.Namespace) -> None:
    with connect(args.db) as con:
        ensure_schema(con)
        counts = {
            row["status"]: row["count"]
            for row in con.execute("SELECT status, count(*) AS count FROM capsules GROUP BY status")
        }
        result = {
            "db": str(args.db),
            "capsules": sum(counts.values()),
            "by_status": {status: counts.get(status, 0) for status in STATUSES},
            "spores_pending": con.execute(
                "SELECT count(*) FROM capsule_spores WHERE status='pending'"
            ).fetchone()[0],
            "events": con.execute("SELECT count(*) FROM capsule_events").fetchone()[0],
            "links": con.execute("SELECT count(*) FROM capsule_links").fetchone()[0],
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))


def validate(args: argparse.Namespace) -> None:
    errors: list[str] = []
    with connect(args.db) as con:
        ensure_schema(con)
        for row in con.execute("SELECT * FROM capsules").fetchall():
            for key in ("bound_scenarios", "tags", "source_refs", "target_skills"):
                try:
                    loads(row[key])
                except (ValueError, json.JSONDecodeError) as exc:
                    errors.append(f"{row['id']}.{key}: {exc}")
            if not row["failure_conditions"].strip():
                errors.append(f"{row['id']}.failure_conditions is empty")
            if row["status"] == "active" and not loads(row["target_skills"]):
                errors.append(f"{row['id']} is active without target_skills")
            if row["status"] in ("validated", "active") and row["evidence_confidence"] < 0.70:
                errors.append(f"{row['id']} has low evidence confidence for {row['status']}")
        integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            errors.append(f"sqlite integrity: {integrity}")
    print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sophia capsule engine")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")
    sub.add_parser("stats")
    sub.add_parser("validate")

    p = sub.add_parser("create")
    p.add_argument("--id")
    p.add_argument("--name", required=True)
    p.add_argument("--capsule-class", choices=("pattern", "synthesis", "architecture", "response"), required=True)
    p.add_argument("--knowledge-kind", choices=("fact", "rule", "process", "opinion", "hypothesis"), required=True)
    p.add_argument("--summary", required=True)
    p.add_argument("--what-worked", required=True)
    p.add_argument("--when-to-apply", required=True)
    p.add_argument("--why-it-works", required=True)
    p.add_argument("--failure-conditions", required=True)
    p.add_argument("--scenario", action="append", default=[])
    p.add_argument("--tag", action="append", default=[])
    p.add_argument("--source-ref", action="append", default=[])
    p.add_argument("--evidence-confidence", type=float, default=0.50)
    p.add_argument("--context-fit", type=float, default=0.50)
    p.add_argument("--utility-score", type=float, default=0.50)
    p.add_argument("--freshness", type=float, default=1.00)
    p.add_argument("--stability", type=float, default=0.50)

    p = sub.add_parser("spore")
    p.add_argument("--id")
    p.add_argument("--kind", choices=("decision", "gotcha", "discovery", "tradeoff", "fix", "hypothesis"), required=True)
    p.add_argument("--statement", required=True)
    p.add_argument("--context", default="")
    p.add_argument("--source", default="")
    p.add_argument("--evidence-confidence", type=float, default=0.50)
    p.add_argument("--tag", action="append", default=[])

    p = sub.add_parser("consume-spore")
    p.add_argument("--spore-id", required=True)
    p.add_argument("--capsule-id", required=True)

    p = sub.add_parser("record")
    p.add_argument("--id", required=True)
    p.add_argument("--outcome", choices=("success", "failure", "neutral", "counterexample"), required=True)
    p.add_argument("--context-key", default="")
    p.add_argument("--context", default="")
    p.add_argument("--result", required=True)
    p.add_argument("--source", default="")

    p = sub.add_parser("activate")
    p.add_argument("--id", required=True)
    p.add_argument("--target-skill", action="append", default=[])
    p.add_argument("--policy-decision", action="store_true")
    p.add_argument("--reason", default="")
    p.add_argument("--source", default="user-confirmed")

    for command in ("deprecate", "archive"):
        p = sub.add_parser(command)
        p.add_argument("--id", required=True)
        p.add_argument("--reason", required=True)
        p.add_argument("--source", default="user-confirmed")

    p = sub.add_parser("link")
    p.add_argument("--from-id", required=True)
    p.add_argument("--to-id", required=True)
    p.add_argument("--relation", choices=("synergy", "complement", "conflict", "tension", "supersedes", "derived_from", "feeds_skill"), required=True)
    p.add_argument("--notes", default="")
    p.add_argument("--source", default="")

    p = sub.add_parser("show")
    p.add_argument("--id", required=True)

    p = sub.add_parser("search")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=10)

    p = sub.add_parser("list")
    p.add_argument("--status", choices=STATUSES)
    p.add_argument("--limit", type=int, default=20)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.cmd == "init":
        init_db(args.db)
    elif args.cmd == "create":
        create_capsule(args)
    elif args.cmd == "spore":
        add_spore(args)
    elif args.cmd == "consume-spore":
        consume_spore(args)
    elif args.cmd == "record":
        record_event(args)
    elif args.cmd == "activate":
        activate(args)
    elif args.cmd == "deprecate":
        change_status(args, "deprecated", "deprecation")
    elif args.cmd == "archive":
        change_status(args, "archived", "archival")
    elif args.cmd == "link":
        add_link(args)
    elif args.cmd == "show":
        show_capsule(args)
    elif args.cmd == "search":
        search_capsules(args)
    elif args.cmd == "list":
        list_capsules(args)
    elif args.cmd == "stats":
        stats(args)
    elif args.cmd == "validate":
        validate(args)


if __name__ == "__main__":
    main()
