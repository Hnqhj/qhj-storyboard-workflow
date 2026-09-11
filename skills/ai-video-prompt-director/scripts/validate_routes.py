#!/usr/bin/env python3
"""Validate that skill references in selected SKILL.md files resolve locally."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REFERENCE_PATTERN = re.compile(r"\$([a-z0-9-]+)")
DEFAULT_OPTIONAL = {
    "blender-mcp-previs",
    "commercial-video-strategy",
    "generation-asset-pipeline",
    "mocap-action-previs",
    "reference-track-mv-director",
}


def read_skill_name(skill_file: Path) -> str | None:
    for line in skill_file.read_text(encoding="utf-8").splitlines()[:12]:
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip('"')
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--skills-root", type=Path, default=Path.home() / ".codex" / "skills")
    parser.add_argument("--allow", action="append", default=[])
    args = parser.parse_args()

    available = {
        name
        for skill_file in args.skills_root.rglob("SKILL.md")
        if (name := read_skill_name(skill_file))
    }
    default_target = args.skills_root / "ai-video-prompt-director" / "SKILL.md"
    targets = args.paths or [default_target]
    references: set[str] = set()
    for target in targets:
        references.update(REFERENCE_PATTERN.findall(target.read_text(encoding="utf-8")))

    allowed = DEFAULT_OPTIONAL | set(args.allow)
    missing = sorted(references - available - allowed)
    optional = sorted(references & allowed - available)
    if optional:
        print("Optional capabilities using documented fallbacks:")
        print("\n".join(f"- {name}" for name in optional))
    if missing:
        print("Unresolved skill references:")
        print("\n".join(f"- {name}" for name in missing))
        return 1
    print("All required skill references resolve locally.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
