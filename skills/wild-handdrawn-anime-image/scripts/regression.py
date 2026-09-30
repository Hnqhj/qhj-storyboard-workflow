"""Offline manifest validation and descriptive reporting; no generation or image editing."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import statistics
import struct
import sys

IMAGE_KEYS = {"referenced_image_paths", "num_last_images_to_include", "image", "image_url", "input_image", "mask", "reference_images"}
PURPOSES = {"baseline", "revision", "repeat"}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resolve(base, value):
    p = Path(value)
    return p if p.is_absolute() else base / p


def has_image_header(path):
    b = Path(path).read_bytes()[:32]
    if b.startswith(b"\x89PNG\r\n\x1a\n") and len(b) >= 24:
        return all(struct.unpack(">II", b[16:24]))
    return b.startswith(b"\xff\xd8\xff") or b.startswith((b"GIF87a", b"GIF89a")) or (b.startswith(b"RIFF") and b[8:12] == b"WEBP")


def image_keys(value):
    if isinstance(value, dict):
        return (set(value) & IMAGE_KEYS) | set().union(*(image_keys(v) for v in value.values()), set())
    if isinstance(value, list):
        return set().union(*(image_keys(v) for v in value), set())
    return set()


def score(review, rubric):
    review = review or {}
    dims = rubric.get("dimensions", [])
    values = review.get("scores", {})
    if not dims or any(d["id"] not in values for d in dims):
        return None
    return sum(float(values[d["id"]]) / float(d["max_score"]) * float(d["weight"]) * 100 for d in dims)


def passes(review, rubric):
    review = review or {}
    total = score(review, rubric)
    if total is None or rubric.get("pass_score_100") is None:
        return False
    gates = review.get("hard_gates", {})
    lows = rubric.get("minimum_dimension_scores", {})
    return (review.get("verdict") == "accepted"
            and all(gates.get(g) is True for g in rubric.get("hard_gates", []))
            and all(review.get("scores", {}).get(k, -1) >= v for k, v in lows.items())
            and total >= rubric["pass_score_100"])


def assess(manifest, manifest_path, phase="draft"):
    errors, warnings = [], []
    base = Path(manifest_path).resolve().parent
    m = manifest
    def need(ok, message):
        if not ok:
            errors.append(message)
    need(m.get("schema_version") == 1, "schema_version must be 1")
    need(m.get("generation_mode") == "fresh_text_only", "generation_mode must be fresh_text_only")
    cases = m.get("cases", [])
    case_ids = [x.get("id") for x in cases]
    need(len(case_ids) == len(set(case_ids)), "duplicate case IDs")
    budget = m.get("budget", {})
    rubric = m.get("rubric", {})
    dims = rubric.get("dimensions", [])
    dim_ids = [d.get("id") for d in dims]
    if phase != "draft":
        need(bool(cases) and all(x.get("id") and x.get("label") and x.get("design_contract") for x in cases), "cases require id, label and design_contract")
        for k in ("batch_output_cap", "total_output_cap", "max_batches"):
            need(isinstance(budget.get(k), int) and not isinstance(budget.get(k), bool) and budget[k] > 0, f"positive integer budget.{k} required")
        need(bool(budget.get("authorized_scope")), "budget.authorized_scope required")
        need(bool(rubric.get("hard_gates")), "rubric hard_gates required before generation")
        need(bool(dims), "scoring dimensions required before generation")
        need(isinstance(rubric.get("pass_score_100"), (int, float)) and 0 <= rubric["pass_score_100"] <= 100, "pass_score_100 must be within 0..100")
        need(bool(rubric.get("tie_break")), "tie_break rule required")
        need(bool(m.get("plan_frozen_utc")), "plan_frozen_utc required")
        st = m.get("stability", {})
        for k in ("required_passing_batches", "plateau_comparisons"):
            need(isinstance(st.get(k), int) and st[k] >= 2, f"stability.{k} must be >=2")
        for k in ("max_batch_mean_delta", "max_case_score_delta", "minimum_gain"):
            need(isinstance(st.get(k), (int, float)) and st[k] >= 0, f"nonnegative stability.{k} required")
    if dims:
        need(len(dim_ids) == len(set(dim_ids)), "duplicate dimension IDs")
        need(all(isinstance(d.get("max_score"), (int, float)) and d["max_score"] > 0 for d in dims), "dimension max_score must be positive")
        need(all(isinstance(d.get("weight"), (int, float)) and d["weight"] >= 0 for d in dims), "dimension weight must be nonnegative")
        need(all(bool(d.get("observable")) for d in dims), "each dimension needs observable definition")
        if all(isinstance(d.get("weight"), (int, float)) for d in dims):
            need(abs(sum(d["weight"] for d in dims) - 1) < 1e-8, "dimension weights must sum to 1")
        need(set(rubric.get("minimum_dimension_scores", {})) <= set(dim_ids), "minimum score names unknown dimension")
    recipes = {r.get("id"): r for r in m.get("recipes", [])}
    need(len(recipes) == len(m.get("recipes", [])), "duplicate recipe IDs")
    if phase != "draft":
        need(recipes.get(m.get("active_recipe_id"), {}).get("status") == "approved", "active_recipe_id must bind an approved recipe")
        if isinstance(budget.get("batch_output_cap"), int):
            need(budget["batch_output_cap"] >= len(case_ids), "batch cap cannot cover all declared cases")
    for rid, r in recipes.items():
        p = resolve(base, r.get("path", ""))
        need(p.is_file(), f"recipe {rid}: file missing")
        if p.is_file():
            need(sha(p) == r.get("sha256"), f"recipe {rid}: SHA mismatch; version/freeze must change")
        if r.get("status") == "approved":
            need(bool(r.get("frozen_at_utc")), f"recipe {rid}: approved recipe needs frozen_at_utc")
    batches = sorted(m.get("batches", []), key=lambda b: b.get("index", -1))
    batch_ids = [b.get("id") for b in batches]
    need(len(batch_ids) == len(set(batch_ids)), "duplicate batch IDs")
    need(len({b.get("index") for b in batches}) == len(batches), "duplicate batch indexes")
    if isinstance(budget.get("max_batches"), int):
        need(len(batches) <= budget["max_batches"], "batch budget exceeded")
    attempts = m.get("attempts", [])
    need(len({a.get("id") for a in attempts}) == len(attempts), "duplicate attempt IDs")
    grouped = defaultdict(list)
    returned = []
    for a in attempts:
        aid = a.get("id", "<missing>")
        grouped[a.get("batch_id")].append(a)
        need(bool(a.get("invocation_id")), f"{aid}: invocation ID missing")
        need(a.get("batch_id") in batch_ids, f"{aid}: unknown batch")
        need(a.get("case_id") in case_ids, f"{aid}: unknown case")
        need(a.get("recipe_id") in recipes, f"{aid}: unknown recipe")
        need(a.get("status") in {"returned_image", "tool_failed"}, f"{aid}: invalid status")
        for k in ("model_version", "seed"):
            need(k in a, f"{aid}: {k} must be recorded (null means unavailable)")
        need(bool(a.get("tool")), f"{aid}: tool missing")
        need("created_utc" in a and (bool(a["created_utc"]) or bool(a.get("time_evidence"))), f"{aid}: record generation time or null plus available archive-time evidence")
        prompt_path = resolve(base, a.get("prompt_path", ""))
        request_path = resolve(base, a.get("request_path", ""))
        need(prompt_path.is_file(), f"{aid}: full prompt file missing")
        need(request_path.is_file(), f"{aid}: actual request record missing")
        if prompt_path.is_file():
            need(sha(prompt_path) == a.get("prompt_sha256"), f"{aid}: prompt SHA mismatch")
        if request_path.is_file():
            try:
                req = read_json(request_path)
                need(not image_keys(req), f"{aid}: image/edit input keys present: {sorted(image_keys(req))}")
                need(isinstance(req.get("prompt"), str) and bool(req["prompt"].strip()), f"{aid}: request prompt missing")
                if prompt_path.is_file():
                    need(req.get("prompt") == prompt_path.read_text(encoding="utf-8-sig"), f"{aid}: request and saved full prompt differ")
            except (ValueError, AttributeError) as exc:
                errors.append(f"{aid}: invalid request JSON: {exc}")
        if a.get("status") == "tool_failed":
            need(not a.get("output_path") and bool(a.get("error_evidence")), f"{aid}: tool_failed requires error evidence and no output")
            continue
        if a.get("status") != "returned_image":
            continue
        returned.append(a)
        output_path = resolve(base, a.get("output_path", ""))
        need(output_path.is_file(), f"{aid}: returned original missing")
        if output_path.is_file():
            need(sha(output_path) == a.get("output_sha256"), f"{aid}: original SHA mismatch")
            need(has_image_header(output_path), f"{aid}: unrecognized image header (header check is not full decoding)")
        r = a.get("review")
        if r is None:
            if phase == "complete":
                errors.append(f"{aid}: returned original unreviewed")
            continue
        need(bool(r.get("reviewer")) and r.get("inspected_original") is True, f"{aid}: original inspection/reviewer evidence missing")
        need(set(r.get("hard_gates", {})) == set(rubric.get("hard_gates", [])), f"{aid}: hard-gate keys incomplete")
        need(all(isinstance(v, bool) for v in r.get("hard_gates", {}).values()), f"{aid}: hard-gates must be booleans")
        need(set(r.get("scores", {})) == set(dim_ids), f"{aid}: score dimensions incomplete")
        for d in dims:
            v = r.get("scores", {}).get(d["id"])
            need(isinstance(v, (int, float)) and not isinstance(v, bool) and 0 <= v <= d["max_score"], f"{aid}: score {d['id']} outside range")
        need(bool(r.get("reason")), f"{aid}: reason missing")
        ev = r.get("evidence", [])
        need(bool(ev) and all(e.get("region") and e.get("observation") for e in ev), f"{aid}: locatable visual evidence missing")
        need(set(dim_ids) <= {e.get("dimension") for e in ev}, f"{aid}: every scored dimension needs its own locatable evidence")
        need(r.get("verdict") in {"accepted", "rejected"}, f"{aid}: invalid review verdict")
        if r.get("verdict") == "accepted" and dims and all(k in r.get("scores", {}) for k in dim_ids):
            try:
                need(passes(r, rubric), f"{aid}: accepted verdict contradicts gate/score threshold")
            except (ValueError, TypeError, ZeroDivisionError):
                errors.append(f"{aid}: invalid score types")
        if r.get("verdict") == "rejected":
            need(bool(r.get("rejection_codes")), f"{aid}: rejection reason codes missing")
    if isinstance(budget.get("total_output_cap"), int):
        need(len(returned) <= budget["total_output_cap"], "total returned-image budget exceeded (rejected images count)")
    need(len({str(resolve(base, a.get('output_path', ''))) for a in returned}) == len(returned), "returned originals reuse one output path; each original needs its own preserved file")
    prior_complete = True
    batch_stats = []
    for b in batches:
        bid = b.get("id")
        rows = [a for a in grouped[bid] if a.get("status") == "returned_image"]
        need(prior_complete, f"{bid}: opened before previous batch was fully reviewed")
        need(b.get("purpose") in PURPOSES and bool(b.get("hypothesis")), f"{bid}: purpose/hypothesis missing")
        recipe = recipes.get(b.get("recipe_id"), {})
        need(recipe.get("status") == "approved", f"{bid}: recipe not approved")
        need(all(a.get("recipe_id") == b.get("recipe_id") for a in grouped[bid]), f"{bid}: mixed recipe versions")
        if isinstance(budget.get("batch_output_cap"), int):
            need(len(rows) <= budget["batch_output_cap"], f"{bid}: batch output budget exceeded")
        counts = Counter(a.get("case_id") for a in rows)
        complete = set(counts) == set(case_ids) and all(n == 1 for n in counts.values()) and all(a.get("review") for a in rows)
        if b.get("status") == "complete" or phase == "complete":
            need(complete, f"{bid}: complete regression batch needs exactly one reviewed original per case")
        if b.get("status") == "complete":
            need(any(d.get("after_batch") == bid and d.get("decision") in {"STOP", "CONTINUE", "ESCALATE"} and d.get("reason") and d.get("evidence") for d in m.get("decisions", [])), f"{bid}: stop decision/evidence missing")
        prior_complete = complete
        totals = []
        for a in rows:
            try:
                s = score(a.get("review", {}), rubric)
            except (ValueError, TypeError, KeyError, ZeroDivisionError):
                s = None
            if s is not None:
                totals.append(s)
        passed = 0
        for a in rows:
            try:
                passed += bool(passes(a.get("review"), rubric))
            except (ValueError, TypeError, KeyError, ZeroDivisionError):
                pass
        batch_stats.append({"id": bid, "index": b.get("index"), "recipe_id": b.get("recipe_id"), "returned": len(rows), "reviewed": sum(bool(a.get("review")) for a in rows), "passed": passed, "complete": complete, "mean_score_100": round(statistics.mean(totals), 4) if totals else None})
    stability = {"satisfied": False, "batches": [], "reason": "insufficient complete identical-prompt repeats"}
    st = m.get("stability", {})
    n = st.get("required_passing_batches", 2)
    if not errors and len(batch_stats) >= n:
        recent = batch_stats[-n:]
        okay = all(b["complete"] and b["passed"] == len(case_ids) for b in recent) and len({b["recipe_id"] for b in recent}) == 1
        means = [b["mean_score_100"] for b in recent]
        if okay:
            okay = max(means) - min(means) <= st["max_batch_mean_delta"]
            for cid in case_ids:
                aa = [next(a for a in grouped[b["id"]] if a.get("status") == "returned_image" and a["case_id"] == cid) for b in recent]
                ss = [score(a["review"], rubric) for a in aa]
                okay = okay and len({a["prompt_sha256"] for a in aa}) == 1 and len({a["invocation_id"] for a in aa}) == n and max(ss) - min(ss) <= st["max_case_score_delta"]
        if okay:
            stability = {"satisfied": True, "batches": [b["id"] for b in recent], "reason": "observed complete same-recipe, identical-full-prompt repetitions satisfy the configured rule; not a probability claim"}
    stop_conditions = []
    if stability["satisfied"]:
        stop_conditions.append("configured_repeat_rule_satisfied")
    if isinstance(budget.get("total_output_cap"), int) and len(returned) >= budget["total_output_cap"]:
        stop_conditions.append("returned_output_budget_exhausted")
    if isinstance(budget.get("max_batches"), int) and len(batches) >= budget["max_batches"] and batches and batch_stats[-1]["complete"]:
        stop_conditions.append("batch_budget_exhausted")
    if m.get("decisions") and m["decisions"][-1].get("decision") == "CONTINUE" and stop_conditions:
        need(False, "CONTINUE contradicts mandatory stop condition: " + ", ".join(stop_conditions))
    if phase == "complete":
        need(bool(m.get("decisions")) and m["decisions"][-1].get("decision") in {"STOP", "ESCALATE"}, "complete delivery requires final STOP or ESCALATE decision")
    return {"valid": not errors, "phase": phase, "errors": errors, "warnings": warnings, "returned_originals": len(returned), "tool_failures": sum(a.get("status") == "tool_failed" for a in attempts), "batch_stats": batch_stats, "stability": stability, "stop_conditions": stop_conditions}


def report(m, result):
    lines = [f"# {m.get('name', 'Text-only style regression')}", "", f"Returned originals: **{result['returned_originals']}**; tool calls failing without an image: **{result['tool_failures']}**.", "", "These are observed counts in this task, not estimated future success probabilities. Rejected images remain in the denominator and original archive.", "", "| Batch | Recipe | Reviewed / returned | Passed | Mean / 100 |", "|---|---|---:|---:|---:|"]
    for b in result["batch_stats"]:
        lines.append(f"| {b['id']} | {b['recipe_id']} | {b['reviewed']} / {b['returned']} | {b['passed']} / {b['returned']} | {b['mean_score_100']} |")
    lines += ["", "Configured repeat rule: " + ("SATISFIED" if result["stability"]["satisfied"] else "NOT SATISFIED"), "", result["stability"]["reason"], "", "## Every returned sample", ""]
    for a in m.get("attempts", []):
        if a.get("status") != "returned_image":
            continue
        r = a.get("review") or {}
        lines += [f"- **{a['id']}** ({a['case_id']}, {a['recipe_id']}): {r.get('verdict', 'unreviewed')}; {r.get('reason', 'visual review pending')}", f"  Original: `{a.get('output_path')}`; full prompt: `{a.get('prompt_path')}`."]
        for e in r.get("evidence", []):
            lines.append(f"  {e.get('region')}: {e.get('observation')}")
    lines += ["", "## Decision", ""]
    for d in m.get("decisions", []):
        lines.append(f"- {d.get('after_batch')}: {d.get('decision')} — {d.get('reason')}; evidence: {d.get('evidence')}")
    if result["errors"]:
        lines += ["", "## Record validation issues", ""] + [f"- {e}" for e in result["errors"]]
    lines += ["", "Scope: file hashes, visible request records, budget, score completeness and configured repeat thresholds were checked. No script assessed the image's artistic quality, verified hidden service state, or inferred a success probability.", ""]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    q = sub.add_parser("init"); q.add_argument("manifest"); q.add_argument("--plan", required=True)
    q = sub.add_parser("validate"); q.add_argument("manifest"); q.add_argument("--phase", choices=["draft", "ready", "complete"], default="ready")
    q = sub.add_parser("report"); q.add_argument("manifest"); q.add_argument("--output", required=True)
    a = p.parse_args()
    target = Path(a.manifest)
    if a.command == "init":
        if target.exists():
            p.error("manifest exists; refusing to overwrite")
        m = {"schema_version": 1, "name": "wild-handdrawn-anime-image regression", "created_utc": datetime.now(timezone.utc).isoformat(), "plan_frozen_utc": None, "generation_mode": "fresh_text_only", **read_json(a.plan), "active_recipe_id": None, "recipes": [], "batches": [], "attempts": [], "decisions": []}
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"created": str(target), "status": "draft"})); return 0
    m = read_json(target)
    result = assess(m, target, a.phase if a.command == "validate" else "draft")
    if a.command == "report":
        out = Path(a.output); out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report(m, result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
