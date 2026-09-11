#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

REQUIRED_LABELS = ["confirmed", "volatile", "field-observed", "unverified", "internal"]
REQUIRED_OFFICIAL_MARKERS = ["seed.bytedance.com", "volcengine.com", "arxiv.org", "runwayml.com"]


def parse_date(text: str) -> date | None:
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    registry = root / "references" / "source-registry.md"
    if not registry.exists():
        errors.append("missing references/source-registry.md")
    else:
        text = registry.read_text(encoding="utf-8")
        match = re.search(r"^last_verified:\s*(\d{4}-\d{2}-\d{2})$", text, re.M)
        if not match:
            errors.append("source-registry.md missing last_verified: YYYY-MM-DD")
        else:
            verified = parse_date(match.group(1))
            if verified:
                age = (date.today() - verified).days
                if age > 30:
                    errors.append(f"source-registry.md last_verified is {age} days old")
                elif age > 14:
                    warnings.append(f"source-registry.md last_verified is {age} days old")

        for label in REQUIRED_LABELS:
            if f"`{label}`" not in text:
                errors.append(f"source-registry.md missing evidence label `{label}`")

        for marker in REQUIRED_OFFICIAL_MARKERS:
            if marker not in text:
                errors.append(f"source-registry.md missing official source marker `{marker}`")

        for line in text.splitlines():
            if "|" not in line or line.lstrip().startswith("|---"):
                continue
            if "volatile" in line and "Recheck" not in line and "recheck" not in line:
                errors.append("volatile source row must include recheck wording")
            if any(word in line.lower() for word in ["reddit", "community", "corpus", "forum"]) and not any(
                label in line for label in ["field-observed", "unverified", "internal"]
            ):
                errors.append("community source row must be field-observed, unverified, or internal")

        if "Seedance 2.0 Pro" in text and "ambiguous" not in text.lower():
            errors.append("Seedance 2.0 Pro appears without an ambiguity correction")

    data_path = root / "data" / "sources.seedance-2026-05-30.json"
    if not data_path.exists():
        errors.append("missing data/sources.seedance-2026-05-30.json")
    else:
        try:
            data = json.loads(data_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"source data JSON parse error: {exc}")
        else:
            sources = data.get("sources")
            if not isinstance(sources, list) or len(sources) < 20:
                errors.append("source data must contain at least twenty source records")
            else:
                for i, source in enumerate(sources):
                    for key in ["id", "title", "url", "language", "source_type", "retrieved_at", "confidence", "claims"]:
                        if key not in source:
                            errors.append(f"source record {i} missing `{key}`")
                    if source.get("source_type", "").startswith("community") and source.get("confidence") == "high":
                        warnings.append(f"community source `{source.get('id')}` should rarely be high confidence")

    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if errors:
        print("Source registry errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Source registry check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
