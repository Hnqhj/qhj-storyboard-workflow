#!/usr/bin/env python3
"""Append-only production ledger for creative generation projects."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


SCHEMA_VERSION = 1
LEDGER_DIR = "production-ledger"
LEDGER_FILE = "ledger.yaml"


def now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def project_root(value: str) -> Path:
    return Path(value).expanduser().resolve()


def ledger_path(root: Path) -> Path:
    return root / LEDGER_DIR / LEDGER_FILE


def load_ledger(root: Path) -> dict[str, Any]:
    path = ledger_path(root)
    if not path.exists():
        raise SystemExit(f"Ledger not found: {path}. Run init first.")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != SCHEMA_VERSION:
        raise SystemExit(f"Unsupported or invalid ledger: {path}")
    return data


def save_ledger(root: Path, data: dict[str, Any]) -> None:
    path = ledger_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    data["project"]["updated_at"] = now()
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_directory(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    for child in sorted(item for item in path.rglob("*") if item.is_file()):
        relative = child.relative_to(path).as_posix()
        file_hash = sha256_file(child)
        file_size = child.stat().st_size
        size += file_size
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_hash.encode("ascii"))
        digest.update(b"\0")
    return digest.hexdigest(), size


def display_path(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def asset(root: Path, value: str, kind: str, role: str | None = None) -> dict[str, Any]:
    raw = Path(value).expanduser()
    path = raw.resolve() if raw.is_absolute() else (root / raw).resolve()
    if not path.exists():
        raise SystemExit(f"Asset not found: {path}")
    if path.is_dir():
        digest, size = sha256_directory(path)
        asset_kind = f"{kind}-directory"
    else:
        digest, size = sha256_file(path), path.stat().st_size
        asset_kind = kind
    record: dict[str, Any] = {
        "path": display_path(root, path),
        "kind": asset_kind,
        "exists": True,
        "size_bytes": size,
        "sha256": digest,
    }
    if role:
        record["role"] = role
    return record


def parse_pairs(values: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise SystemExit(f"Expected key=value, got: {value}")
        key, item = value.split("=", 1)
        key = key.strip()
        if not key:
            raise SystemExit(f"Empty key in: {value}")
        result[key] = item.strip()
    return result


def parse_references(root: Path, values: list[str]) -> list[dict[str, Any]]:
    records = []
    for value in values:
        if "=" not in value:
            raise SystemExit(f"Reference must declare role=path, got: {value}")
        role, path = value.split("=", 1)
        records.append(asset(root, path.strip(), "reference", role.strip()))
    return records


def next_id(items: list[dict[str, Any]], prefix: str) -> str:
    highest = 0
    for item in items:
        value = str(item.get("id", ""))
        if value.startswith(prefix) and value[len(prefix) :].isdigit():
            highest = max(highest, int(value[len(prefix) :]))
    return f"{prefix}{highest + 1:03d}"


def command_init(args: argparse.Namespace) -> None:
    root = project_root(args.project)
    root.mkdir(parents=True, exist_ok=True)
    path = ledger_path(root)
    if path.exists() and not args.force:
        raise SystemExit(f"Ledger already exists: {path}")
    created = now()
    data = {
        "schema_version": SCHEMA_VERSION,
        "project": {
            "id": args.project_id or root.name,
            "title": args.title or root.name,
            "created_at": created,
            "updated_at": created,
        },
        "attempts": [],
        "reviews": [],
    }
    save_ledger(root, data)
    print(json.dumps({"ledger": str(path), "project": data["project"]}, ensure_ascii=False, indent=2))


def build_attempt(
    root: Path,
    data: dict[str, Any],
    args: argparse.Namespace,
    parent: str | None = None,
) -> dict[str, Any]:
    if parent and not any(item["id"] == parent for item in data["attempts"]):
        raise SystemExit(f"Parent attempt not found: {parent}")
    prompt = asset(root, args.prompt, "prompt")
    outputs = [asset(root, value, "output") for value in args.output]
    return {
        "id": next_id(data["attempts"], "A"),
        "created_at": now(),
        "status": args.status,
        "parent_attempt": parent,
        "prompt": prompt,
        "references": parse_references(root, args.reference),
        "model": args.model,
        "mode": args.mode,
        "settings": parse_pairs(args.setting),
        "outputs": outputs,
        "changes": list(args.change),
        "notes": list(args.note),
    }


def command_attempt(args: argparse.Namespace) -> None:
    root = project_root(args.project)
    data = load_ledger(root)
    record = build_attempt(root, data, args)
    data["attempts"].append(record)
    save_ledger(root, data)
    print(json.dumps(record, ensure_ascii=False, indent=2))


def command_retry(args: argparse.Namespace) -> None:
    root = project_root(args.project)
    data = load_ledger(root)
    if not args.change:
        raise SystemExit("Retry requires at least one --change delta.")
    parent = next(item for item in data["attempts"] if item["id"] == args.parent)
    if not args.model:
        args.model = parent.get("model")
    if not args.mode:
        args.mode = parent.get("mode")
    if not args.reference:
        args.reference = [
            f"{item['role']}={item['path']}"
            for item in parent.get("references", [])
            if item.get("role")
        ]
    if not args.setting:
        args.setting = [
            f"{key}={value}" for key, value in (parent.get("settings") or {}).items()
        ]
    record = build_attempt(root, data, args, parent=args.parent)
    data["attempts"].append(record)
    save_ledger(root, data)
    print(json.dumps(record, ensure_ascii=False, indent=2))


def command_review(args: argparse.Namespace) -> None:
    root = project_root(args.project)
    data = load_ledger(root)
    if not any(item["id"] == args.attempt for item in data["attempts"]):
        raise SystemExit(f"Attempt not found: {args.attempt}")
    record = {
        "id": next_id(data["reviews"], "R"),
        "attempt_id": args.attempt,
        "created_at": now(),
        "verdict": args.verdict,
        "evidence": [asset(root, value, "review-evidence") for value in args.evidence],
        "issues": list(args.issue),
        "notes": list(args.note),
    }
    data["reviews"].append(record)
    for attempt in data["attempts"]:
        if attempt["id"] == args.attempt:
            attempt["status"] = "accepted" if args.verdict == "accept" else "reviewed"
    save_ledger(root, data)
    print(json.dumps(record, ensure_ascii=False, indent=2))


def command_summary(args: argparse.Namespace) -> None:
    root = project_root(args.project)
    data = load_ledger(root)
    reviews_by_attempt: dict[str, list[dict[str, Any]]] = {}
    for review in data["reviews"]:
        reviews_by_attempt.setdefault(review["attempt_id"], []).append(review)
    summary = {
        "project": data["project"],
        "attempt_count": len(data["attempts"]),
        "review_count": len(data["reviews"]),
        "attempts": [
            {
                "id": attempt["id"],
                "parent_attempt": attempt.get("parent_attempt"),
                "status": attempt.get("status"),
                "model": attempt.get("model"),
                "mode": attempt.get("mode"),
                "changes": attempt.get("changes", []),
                "outputs": [item["path"] for item in attempt.get("outputs", [])],
                "verdicts": [
                    review["verdict"] for review in reviews_by_attempt.get(attempt["id"], [])
                ],
            }
            for attempt in data["attempts"]
        ],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def iter_assets(data: dict[str, Any]):
    for attempt in data["attempts"]:
        yield f"{attempt['id']}.prompt", attempt.get("prompt")
        for index, item in enumerate(attempt.get("references", []), start=1):
            yield f"{attempt['id']}.reference[{index}]", item
        for index, item in enumerate(attempt.get("outputs", []), start=1):
            yield f"{attempt['id']}.output[{index}]", item
    for review in data["reviews"]:
        for index, item in enumerate(review.get("evidence", []), start=1):
            yield f"{review['id']}.evidence[{index}]", item


def command_verify(args: argparse.Namespace) -> None:
    root = project_root(args.project)
    data = load_ledger(root)
    checks = []
    for label, record in iter_assets(data):
        if not record:
            continue
        raw = Path(record["path"])
        path = raw if raw.is_absolute() else root / raw
        item = {"asset": label, "path": record["path"], "status": "ok"}
        if not path.exists():
            item.update({"status": "missing", "expected_sha256": record.get("sha256")})
        else:
            actual, size = (
                sha256_directory(path) if path.is_dir() else (sha256_file(path), path.stat().st_size)
            )
            if actual != record.get("sha256") or size != record.get("size_bytes"):
                item.update(
                    {
                        "status": "changed",
                        "expected_sha256": record.get("sha256"),
                        "actual_sha256": actual,
                        "expected_size_bytes": record.get("size_bytes"),
                        "actual_size_bytes": size,
                    }
                )
        checks.append(item)
    failures = [item for item in checks if item["status"] != "ok"]
    result = {
        "ledger": str(ledger_path(root)),
        "status": "fail" if failures else "pass",
        "checked_assets": len(checks),
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(2)


def add_attempt_args(parser: argparse.ArgumentParser, retry: bool = False) -> None:
    parser.add_argument("project")
    if retry:
        parser.add_argument("--from", dest="parent", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--reference", action="append", default=[], help="role=path")
    parser.add_argument("--model")
    parser.add_argument("--mode")
    parser.add_argument("--setting", action="append", default=[], help="key=value")
    parser.add_argument("--output", action="append", default=[], required=True)
    parser.add_argument("--change", action="append", default=[])
    parser.add_argument("--note", action="append", default=[])
    parser.add_argument(
        "--status",
        choices=["planned", "generated", "reviewed", "accepted", "failed"],
        default="generated",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("project")
    init.add_argument("--title")
    init.add_argument("--project-id")
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=command_init)
    attempt = sub.add_parser("attempt")
    add_attempt_args(attempt)
    attempt.set_defaults(func=command_attempt)
    retry = sub.add_parser("retry")
    add_attempt_args(retry, retry=True)
    retry.set_defaults(func=command_retry)
    review = sub.add_parser("review")
    review.add_argument("project")
    review.add_argument("--attempt", required=True)
    review.add_argument("--evidence", action="append", default=[], required=True)
    review.add_argument("--verdict", choices=["accept", "conditional", "retry", "reject"], required=True)
    review.add_argument("--issue", action="append", default=[])
    review.add_argument("--note", action="append", default=[])
    review.set_defaults(func=command_review)
    summary = sub.add_parser("summary")
    summary.add_argument("project")
    summary.set_defaults(func=command_summary)
    verify = sub.add_parser("verify")
    verify.add_argument("project")
    verify.set_defaults(func=command_verify)
    return parser


if __name__ == "__main__":
    parsed = build_parser().parse_args()
    try:
        parsed.func(parsed)
    except StopIteration:
        raise SystemExit("Referenced attempt was not found.") from None
    except KeyboardInterrupt:
        sys.exit(130)
