#!/usr/bin/env python3
"""Structural, generated-source and reviewed-snapshot checks. NOT semantic validation."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from build_runtime import (MARKDOWN_LINK, SOURCES, TARGET, local_link_target,
                           render, source_body)

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = "review-snapshot.json"
TRACKED_SUFFIXES = {".md", ".py", ".json", ".yaml", ".txt"}


def tracked_files(root):
    return {p.relative_to(root).as_posix(): p for p in root.rglob("*")
            if p.is_file() and p.suffix in TRACKED_SUFFIXES
            and p.relative_to(root).as_posix() not in {SNAPSHOT, TARGET}
            and "__pycache__" not in p.parts}


def route_problems(root):
    """Check source existence and reachability, never infer rule meaning from words."""
    problems, links = [], {}
    if len(SOURCES) != len(set(SOURCES)):
        problems.append("duplicate runtime source")
    for name in SOURCES:
        if not (root / name).is_file():
            problems.append(f"missing runtime source: {name}")
            continue
        try:
            body = source_body(root, name)
        except ValueError as exc:
            problems.append(str(exc))
            continue
        links[name] = {local_link_target(name, match.group(2))
                       for match in MARKDOWN_LINK.finditer(body)} & set(SOURCES)
    reachable, pending = set(), ["SKILL.md"]
    while pending:
        name = pending.pop()
        if name in reachable:
            continue
        reachable.add(name)
        pending.extend(links.get(name, set()) - reachable)
    for name in sorted(set(SOURCES) - reachable):
        problems.append(f"runtime source is not reachable from entrypoint: {name}")
    return problems


def audit(root=ROOT, structural_only=False):
    root = Path(root)
    problems = []
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    version = re.search(r'(?m)^[ \t]*version: "(\d+\.\d+(?:\.\d+)?[A-Za-z]?)"$', text)
    name = re.search(r"(?m)^name: ([a-z0-9-]+)$", text)
    if not text.startswith("---\n") or not name or name.group(1) != "mr-li-seedance-25":
        problems.append("invalid skill identity/frontmatter")
    if not version or f"版本：{version.group(1)}" not in text:
        problems.append("missing or mismatched entrypoint version")
    else:
        for filename, prefix in [("USAGE_GUIDE.md", "适用版本："), ("CHANGELOG.md", "当前版本：")]:
            if prefix + version.group(1) not in (root / filename).read_text(encoding="utf-8"):
                problems.append(f"version mismatch: {filename}")
    problems.extend(route_problems(root))
    for name_, path in tracked_files(root).items():
        if path.suffix != ".md":
            continue
        data = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", data):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            resolved = (path.parent / target).resolve()
            if not resolved.exists() or (root.resolve() not in resolved.parents):
                problems.append(f"broken or nonportable reference: {name_}: {target}")
    try:
        if (root / TARGET).read_text(encoding="utf-8") != render(root):
            problems.append("single-file runtime differs from maintained sources")
    except (OSError, ValueError) as exc:
        problems.append(f"runtime unavailable: {exc}")

    if not structural_only:
        try:
            snapshot = json.loads((root / SNAPSHOT).read_text(encoding="utf-8"))
            expected = snapshot["sha256"]
            actual = {name_: hashlib.sha256(path.read_bytes()).hexdigest()
                      for name_, path in tracked_files(root).items()}
            if not isinstance(expected, dict) or not expected:
                problems.append("empty or invalid review snapshot")
            else:
                for name_ in sorted(set(expected) | set(actual)):
                    if expected.get(name_) != actual.get(name_):
                        problems.append(f"changed since recorded text review; review again: {name_}")
            if version and snapshot.get("version") != version.group(1):
                problems.append("review snapshot version mismatch")
            if snapshot.get("review_type") != "maintainer-text-review":
                problems.append("snapshot review_type must explicitly identify text-only review")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            problems.append(f"review snapshot unavailable: {exc}")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--structural-only", action="store_true")
    args = parser.parse_args()
    try:
        problems = audit(args.root, args.structural_only)
    except (OSError, ValueError) as exc:
        print(f"CHECK UNAVAILABLE: {exc}")
        return 2
    if problems:
        print("STATIC / REVIEW-SNAPSHOT CHECK FAILED")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("STATIC CHECK PASSED" if args.structural_only else "STATIC + REVIEW-SNAPSHOT CHECK PASSED")
    print("This does NOT prove semantic correctness, new-chat behavior or media quality.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
