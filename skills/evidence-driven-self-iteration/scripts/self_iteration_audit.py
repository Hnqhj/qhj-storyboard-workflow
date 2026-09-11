#!/usr/bin/env python3
"""Read-only structural and evidence audit for Sophia's custom skill system."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import tomllib
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
SKILLS_ROOT = Path(os.environ.get("SOPHIA_SKILLS_ROOT", CODEX_HOME / "skills"))
SOPHIA_ROOT = Path(os.environ.get("SOPHIA_ROOT", CODEX_HOME / "sophia"))
_default_db = Path(r"D:\SophiaMemory\data\sophia_memory.sqlite")
if not _default_db.exists():
    _default_db = CODEX_HOME / "memories_1.sqlite"
DB_PATH = Path(os.environ.get("SOPHIA_MEMORY_DB", _default_db))
AUTOMATIONS_ROOT = Path(
    os.environ.get("SOPHIA_AUTOMATIONS_ROOT", CODEX_HOME / "automations")
)
SYSTEM_DIR = ".system"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS self_iteration_runs (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          started_at TEXT NOT NULL,
          completed_at TEXT NOT NULL,
          summary_json TEXT NOT NULL,
          finding_count INTEGER NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS self_iteration_findings (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          run_id INTEGER NOT NULL REFERENCES self_iteration_runs(id) ON DELETE CASCADE,
          fingerprint TEXT NOT NULL,
          category TEXT NOT NULL,
          severity TEXT NOT NULL,
          subject TEXT NOT NULL,
          evidence TEXT NOT NULL,
          recommendation TEXT NOT NULL,
          created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        CREATE INDEX IF NOT EXISTS idx_iteration_findings_fp
          ON self_iteration_findings(fingerprint);
        """
    )
    return con


def fingerprint(category: str, subject: str, recommendation: str) -> str:
    value = f"{category}|{subject}|{recommendation}".encode("utf-8")
    return hashlib.sha256(value).hexdigest()[:16]


def finding(
    category: str,
    severity: str,
    subject: str,
    evidence: str,
    recommendation: str,
) -> dict:
    return {
        "fingerprint": fingerprint(category, subject, recommendation),
        "category": category,
        "severity": severity,
        "subject": subject,
        "evidence": evidence,
        "recommendation": recommendation,
    }


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def referenced_relative_files(text: str) -> list[str]:
    paths = re.findall(r"\]\((references/[^)#]+|scripts/[^)#]+|assets/[^)#]+)\)", text)
    paths += re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", text)
    return sorted(set(paths))


def source_dates(skill_dir: Path) -> list[str]:
    dates: list[str] = []
    refs = skill_dir / "references"
    if not refs.exists():
        return dates
    for path in refs.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        dates.extend(re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", text))
    return dates


def audit_skills() -> tuple[list[dict], dict]:
    findings: list[dict] = []
    skills: list[dict] = []
    for skill_dir in sorted(
        path for path in SKILLS_ROOT.iterdir() if path.is_dir() and path.name != SYSTEM_DIR
    ):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            findings.append(
                finding(
                    "structure",
                    "high",
                    skill_dir.name,
                    "Custom skill directory has no SKILL.md.",
                    "Add a valid SKILL.md or remove the incomplete directory after review.",
                )
            )
            continue
        text = skill_md.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        headings = [line.strip() for line in text.splitlines() if line.startswith("## ")]
        duplicates = [heading for heading, count in Counter(headings).items() if count > 1]
        missing_refs = [
            rel for rel in referenced_relative_files(text) if not (skill_dir / rel).exists()
        ]
        agents = skill_dir / "agents" / "openai.yaml"
        lines = len(text.splitlines())

        if meta.get("name") != skill_dir.name:
            findings.append(
                finding(
                    "structure",
                    "high",
                    skill_dir.name,
                    f"Frontmatter name is {meta.get('name')!r}; directory is {skill_dir.name!r}.",
                    "Align the frontmatter name and skill directory.",
                )
            )
        if not meta.get("description"):
            findings.append(
                finding(
                    "routing",
                    "high",
                    skill_dir.name,
                    "Frontmatter description is missing.",
                    "Add a trigger-rich description.",
                )
            )
        if re.search(r"(?m)^\s*(?:\[TODO|TODO:)", text):
            findings.append(
                finding(
                    "structure",
                    "medium",
                    skill_dir.name,
                    "SKILL.md contains TODO.",
                    "Resolve the placeholder or remove it.",
                )
            )
        if duplicates:
            findings.append(
                finding(
                    "duplication",
                    "medium",
                    skill_dir.name,
                    f"Duplicate headings: {duplicates}",
                    "Merge or rename duplicate sections.",
                )
            )
        if missing_refs:
            findings.append(
                finding(
                    "structure",
                    "high",
                    skill_dir.name,
                    f"Missing referenced files: {missing_refs}",
                    "Restore the referenced files or remove stale links.",
                )
            )
        if not agents.exists():
            findings.append(
                finding(
                    "structure",
                    "low",
                    skill_dir.name,
                    "agents/openai.yaml is missing.",
                    "Generate UI metadata if the skill should appear in the skill picker.",
                )
            )
        if lines > 500:
            findings.append(
                finding(
                    "system-bloat",
                    "medium",
                    skill_dir.name,
                    f"SKILL.md has {lines} lines.",
                    "Move detailed examples or domain variants into references.",
                )
            )

        skills.append(
            {
                "name": skill_dir.name,
                "lines": lines,
                "modified_at": datetime.fromtimestamp(
                    skill_md.stat().st_mtime, timezone.utc
                ).isoformat(timespec="seconds"),
                "references": len(list((skill_dir / "references").glob("*")))
                if (skill_dir / "references").exists()
                else 0,
                "source_dates": source_dates(skill_dir),
            }
        )
    return findings, {"count": len(skills), "skills": skills}


def audit_capsules() -> tuple[list[dict], dict]:
    findings: list[dict] = []
    if not DB_PATH.exists():
        findings.append(
            finding(
                "structure",
                "critical",
                "capsule database",
                f"Database is missing: {DB_PATH}",
                "Restore the database from backup before running capsule workflows.",
            )
        )
        return findings, {"available": False}

    with connect() as con:
        table = con.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='capsules'"
        ).fetchone()
        if not table:
            findings.append(
                finding(
                    "structure",
                    "critical",
                    "capsule schema",
                    "Capsule table is missing from the Sophia database.",
                    "Run capsule-engine init after backing up the database.",
                )
            )
            return findings, {"available": True, "schema": False}

        integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            findings.append(
                finding(
                    "safety",
                    "critical",
                    "Sophia SQLite integrity",
                    integrity,
                    "Stop writes and restore or repair from backup.",
                )
            )

        status_rows = con.execute(
            "SELECT status, count(*) AS n FROM capsules GROUP BY status"
        ).fetchall()
        statuses = {row["status"]: row["n"] for row in status_rows}
        active_without_targets = con.execute(
            "SELECT id, name FROM capsules WHERE status='active' AND target_skills='[]'"
        ).fetchall()
        for row in active_without_targets:
            findings.append(
                finding(
                    "routing",
                    "medium",
                    row["id"],
                    f"Active capsule {row['name']!r} has no target skills.",
                    "Assign a consuming skill or demote the capsule after review.",
                )
            )
        pending_spores = con.execute(
            "SELECT count(*) FROM capsule_spores WHERE status='pending'"
        ).fetchone()[0]
        counterexamples = con.execute(
            "SELECT count(*) FROM capsule_events WHERE event_type='counterexample'"
        ).fetchone()[0]
        last_events = [
            dict(row)
            for row in con.execute(
                """
                SELECT capsule_id, event_type, context_key, result, created_at
                FROM capsule_events ORDER BY id DESC LIMIT 20
                """
            ).fetchall()
        ]
        return findings, {
            "available": True,
            "integrity": integrity,
            "statuses": statuses,
            "pending_spores": pending_spores,
            "counterexamples": counterexamples,
            "recent_events": last_events,
        }


def load_automations() -> list[dict]:
    automations: list[dict] = []
    if not AUTOMATIONS_ROOT.exists():
        return automations
    for path in sorted(AUTOMATIONS_ROOT.glob("*/automation.toml")):
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            automations.append(
                {
                    "id": data.get("id", path.parent.name),
                    "name": data.get("name"),
                    "status": data.get("status"),
                    "rrule": data.get("rrule"),
                    "path": str(path),
                }
            )
        except (OSError, tomllib.TOMLDecodeError) as exc:
            automations.append(
                {
                    "id": path.parent.name,
                    "path": str(path),
                    "error": str(exc),
                }
            )
    return automations


def automation_claims(text: str) -> list[str]:
    claims: set[str] = set()
    for line in text.splitlines():
        if "automation" not in line.lower() and "自动化" not in line:
            continue
        for token in re.findall(r"`([^`]+)`", line):
            if re.fullmatch(r"[a-z0-9][a-z0-9-]*", token):
                claims.add(token)
    return sorted(claims)


def audit_memory() -> tuple[list[dict], dict]:
    findings: list[dict] = []
    required = [
        SOPHIA_ROOT / "SESSION-STATE.md",
        SOPHIA_ROOT / "LOCAL-MEMORY.md",
        SOPHIA_ROOT / "memory" / "INDEX.md",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        findings.append(
            finding(
                "structure",
                "high",
                "Sophia memory routing",
                f"Missing files: {missing}",
                "Restore the missing memory routing files.",
            )
        )
    automations = load_automations()
    actual_ids = {
        str(item.get("id"))
        for item in automations
        if item.get("id") and not item.get("error")
    }
    session_path = SOPHIA_ROOT / "SESSION-STATE.md"
    claims: list[str] = []
    if session_path.exists():
        session_text = session_path.read_text(encoding="utf-8")
        claims = automation_claims(session_text)
        absent_claims = sorted(set(claims) - actual_ids)
        if absent_claims:
            findings.append(
                finding(
                    "routing",
                    "high",
                    "Sophia cold-start automation state",
                    f"SESSION-STATE.md claims automation ids not found on disk: {absent_claims}. "
                    f"Detected ids: {sorted(actual_ids)}.",
                    "Refresh SESSION-STATE.md from the actual automation TOML files and mark "
                    "unverified historical workflows as historical.",
                )
            )

        newest_skill = max(
            (
                (path / "SKILL.md").stat().st_mtime
                for path in SKILLS_ROOT.iterdir()
                if path.is_dir() and path.name != SYSTEM_DIR and (path / "SKILL.md").exists()
            ),
            default=0,
        )
        if newest_skill - session_path.stat().st_mtime > 86400:
            findings.append(
                finding(
                    "routing",
                    "low",
                    "Sophia cold-start skill inventory",
                    "SESSION-STATE.md is more than 24 hours older than the newest custom SKILL.md.",
                    "Refresh only the compact current setup summary; do not copy a full skill log.",
                )
            )

    return findings, {
        "required_files": [str(path) for path in required],
        "missing": missing,
        "automation_claims": claims,
        "automations": automations,
    }


def recurring_counts(con: sqlite3.Connection) -> dict[str, int]:
    return {
        row["fingerprint"]: row["n"]
        for row in con.execute(
            """
            SELECT fingerprint, count(*) AS n
            FROM self_iteration_findings
            GROUP BY fingerprint
            """
        ).fetchall()
    }


def run_audit(record: bool) -> dict:
    started = now_iso()
    findings: list[dict] = []
    skill_findings, skills = audit_skills()
    capsule_findings, capsules = audit_capsules()
    memory_findings, memory = audit_memory()
    findings.extend(skill_findings)
    findings.extend(capsule_findings)
    findings.extend(memory_findings)

    result = {
        "started_at": started,
        "completed_at": now_iso(),
        "scope": {
            "skills_root": str(SKILLS_ROOT),
            "sophia_root": str(SOPHIA_ROOT),
            "database": str(DB_PATH),
        },
        "skills": skills,
        "capsules": capsules,
        "memory": memory,
        "findings": findings,
        "finding_count": len(findings),
    }

    if record:
        with connect() as con:
            prior = recurring_counts(con)
            cursor = con.execute(
                """
                INSERT INTO self_iteration_runs(started_at, completed_at, summary_json, finding_count)
                VALUES (?, ?, ?, ?)
                """,
                (
                    result["started_at"],
                    result["completed_at"],
                    json.dumps(result, ensure_ascii=False),
                    len(findings),
                ),
            )
            run_id = cursor.lastrowid
            for item in findings:
                con.execute(
                    """
                    INSERT INTO self_iteration_findings(
                      run_id, fingerprint, category, severity, subject, evidence, recommendation
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        run_id,
                        item["fingerprint"],
                        item["category"],
                        item["severity"],
                        item["subject"],
                        item["evidence"],
                        item["recommendation"],
                    ),
                )
                item["previous_occurrences"] = prior.get(item["fingerprint"], 0)
            result["recorded_run_id"] = run_id
    return result


def history(limit: int) -> list[dict]:
    with connect() as con:
        rows = con.execute(
            """
            SELECT id, started_at, completed_at, finding_count
            FROM self_iteration_runs ORDER BY id DESC LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]


def recurring(minimum: int) -> list[dict]:
    with connect() as con:
        rows = con.execute(
            """
            SELECT fingerprint, category, severity, subject,
                   count(*) AS occurrences, max(created_at) AS last_seen,
                   max(recommendation) AS recommendation
            FROM self_iteration_findings
            GROUP BY fingerprint, category, severity, subject
            HAVING count(*) >= ?
            ORDER BY occurrences DESC, last_seen DESC
            """,
            (minimum,),
        ).fetchall()
    return [dict(row) for row in rows]


def main() -> None:
    parser = argparse.ArgumentParser(description="Evidence-driven Sophia self-audit")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_audit = sub.add_parser("audit")
    p_audit.add_argument("--record", action="store_true")

    p_history = sub.add_parser("history")
    p_history.add_argument("--limit", type=int, default=8)

    p_recurring = sub.add_parser("recurring")
    p_recurring.add_argument("--minimum", type=int, default=2)

    args = parser.parse_args()
    if args.cmd == "audit":
        output = run_audit(args.record)
    elif args.cmd == "history":
        output = history(args.limit)
    else:
        output = recurring(args.minimum)
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
