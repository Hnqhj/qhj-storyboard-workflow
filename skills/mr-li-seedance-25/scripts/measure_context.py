#!/usr/bin/env python3
"""Measure explicit UTF-8 rule bundles with a pinned reference tokenizer.

This measures text-rule loading, not account quota, billing, or whole-run usage.
No recursive routing is inferred: the reviewed JSON config lists every file.
"""

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys


SCHEMA_VERSION = 1
METHOD = "sum_of_per_file_encode_ordinary_token_counts"
SCOPE = "text_rule_loading_only_not_account_quota_or_whole_run_usage"


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def source_path(root, name):
    relative = Path(name)
    if not name or relative.is_absolute() or ".." in relative.parts:
        raise ValueError("File paths must be nonempty, relative, and without '..': " + name)
    resolved = (root / relative).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        raise ValueError("File escapes the chosen rule root: " + name)
    if not resolved.is_file():
        raise ValueError("Missing rule file: " + name)
    return resolved


def measure(root, config, config_sha256=None):
    import tiktoken

    if config.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Unsupported config schema_version")
    if config.get("status") != "ready":
        raise ValueError("Config is not ready; finish and review its explicit routes first")
    requested = config["tokenizer"]
    version = importlib.metadata.version("tiktoken")
    if requested.get("package") != "tiktoken" or requested.get("version") != version:
        raise ValueError("Install the config's exact tiktoken version before measuring")
    encoding = tiktoken.get_encoding(requested["encoding"])
    root = Path(root).resolve()
    records = {}
    scenarios = []
    scenario_ids = set()
    for scenario in config["scenarios"]:
        scenario_id = scenario["id"]
        if not scenario_id or scenario_id in scenario_ids:
            raise ValueError("Scenario IDs must be nonempty and unique")
        scenario_ids.add(scenario_id)
        names = scenario["files"]
        if not names or len(names) != len(set(names)):
            raise ValueError("Each scenario requires a nonempty, duplicate-free file list")
        resolved_names = set()
        for name in names:
            path = source_path(root, name)
            if path in resolved_names:
                raise ValueError("One physical file is listed twice in scenario " + scenario_id)
            resolved_names.add(path)
            if name not in records:
                raw = path.read_bytes()
                text = raw.decode("utf-8")
                records[name] = {
                    "path": name,
                    "sha256": hashlib.sha256(raw).hexdigest(),
                    "bytes": len(raw),
                    "unicode_codepoints": len(text),
                    "tokens": len(encoding.encode_ordinary(text)),
                }
        scenarios.append({
            "id": scenario_id,
            "label": scenario["label"],
            "basis": scenario["basis"],
            "assumptions": scenario.get("assumptions", []),
            "files": names,
            "file_count": len(names),
            "text_rule_tokens": sum(records[name]["tokens"] for name in names),
            "bytes": sum(records[name]["bytes"] for name in names),
        })
    if not scenarios:
        raise ValueError("At least one reviewed scenario is required")
    # Hash the actual reference vocabulary to detect tokenizer-data drift too.
    vocabulary_hash = hashlib.sha256()
    for token, rank in sorted(encoding._mergeable_ranks.items(), key=lambda item: item[1]):
        vocabulary_hash.update(rank.to_bytes(8, "big"))
        vocabulary_hash.update(len(token).to_bytes(8, "big"))
        vocabulary_hash.update(token)
    return {
        "schema_version": SCHEMA_VERSION,
        "label": config["label"],
        "scope": SCOPE,
        "root": str(root),
        "config_sha256": config_sha256,
        "method": METHOD,
        "tokenizer": {
            "package": "tiktoken", "version": version,
            "encoding": encoding.name,
            "mergeable_vocabulary_sha256": vocabulary_hash.hexdigest(),
            "encoding_note": "Reference encoding only; not a guarantee of this model's internal or billable tokenization.",
        },
        "python_version": platform.python_version(),
        "assumptions": config.get("assumptions", []),
        "exclusions": [
            "User messages, authority scripts, project state, and conversation history",
            "Output, image/video/audio processing, and reasoning usage",
            "Tool wrappers, message framing, retry overhead, cache discounts, and account quota conversion",
            "Unlisted files; no automatic transitive closure of Markdown links",
        ],
        "files": records,
        "scenarios": scenarios,
    }


def compare(before, after, unchanged_other_units):
    for key in ("schema_version", "scope", "method", "tokenizer"):
        if before.get(key) != after.get(key):
            raise ValueError("Cannot compare results with different " + key)
    old = {item["id"]: item for item in before["scenarios"]}
    new = {item["id"]: item for item in after["scenarios"]}
    if old.keys() != new.keys():
        raise ValueError("Before and after scenario IDs must match exactly")
    if any(value < 0 for value in unchanged_other_units):
        raise ValueError("Unchanged-other units must be nonnegative")
    rows = []
    for scenario_id, previous in old.items():
        current = new[scenario_id]
        rb = previous["text_rule_tokens"]
        ra = current["text_rule_tokens"]
        delta = rb - ra
        rows.append({
            "id": scenario_id,
            "label": current["label"],
            "before_files": previous["files"],
            "after_files": current["files"],
            "before_text_rule_tokens": rb,
            "after_text_rule_tokens": ra,
            "text_rule_tokens_removed": delta,
            "text_rule_reduction_percent": round(100 * delta / rb, 4) if rb else None,
            "illustrative_sensitivity_not_measured_usage": [{
                "unchanged_other_token_units_X": value,
                "illustrative_total_reduction_percent": round(100 * delta / (rb + value), 4) if rb + value else None,
            } for value in unchanged_other_units],
        })
    return {
        "scope": SCOPE,
        "formula": "Rule reduction = (Rb - Ra) / Rb; illustrative whole-workload reduction = (Rb - Ra) / (Rb + X)",
        "variables": {
            "Rb": "Before text rules, loaded once per explicitly listed file",
            "Ra": "After text rules, loaded once per explicitly listed file",
            "X": "Unchanged input/history/state + output + images/media + reasoning, expressed only as assumed comparable token units",
        },
        "sensitivity_assumptions": [
            "X is hypothetical, not measured. Output, images/media, history, and reasoning are held unchanged.",
            "No claim that savings carry through to account limits, pricing, latency, or an actual run.",
            "Rule text is counted once without framing. Existing history, repeated tool reads, and cache behavior can change real usage.",
            "A negative reduction is an increase and is retained without clipping.",
        ],
        "scenarios": rows,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="Write complete JSON; otherwise print it")
    parser.add_argument("--compare", type=Path, help="An earlier result JSON, measured with the same method")
    parser.add_argument("--unchanged-other-units", type=int, nargs="+", default=[0, 4000, 16000, 64000])
    args = parser.parse_args(argv)
    try:
        config_raw = args.config.read_bytes()
        result = measure(args.root, json.loads(config_raw.decode("utf-8")), hashlib.sha256(config_raw).hexdigest())
        if args.compare:
            result["comparison"] = compare(read_json(args.compare), result, args.unchanged_other_units)
        serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            output_path = args.output.resolve()
            if output_path in {args.config.resolve(), args.compare.resolve() if args.compare else None}:
                raise ValueError("Output must not overwrite the config or prior result")
            if output_path in {source_path(args.root.resolve(), name) for name in result["files"]}:
                raise ValueError("Output must not overwrite a measured rule source")
            output_path.write_text(serialized, encoding="utf-8")
            print("Measured text rules only: " + str(output_path))
            for scenario in result["scenarios"]:
                print(f"{scenario['id']}: {scenario['text_rule_tokens']} tokens / {scenario['file_count']} files")
        else:
            print(serialized, end="")
    except (KeyError, ValueError, OSError, ImportError) as exc:
        print("MEASUREMENT ERROR: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
