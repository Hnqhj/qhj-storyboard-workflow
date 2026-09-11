#!/usr/bin/env python3
"""Lint a Liu short-drama camera-group JSON and optional prompt text.

The linter checks deterministic production constraints only. It does not judge
creative quality, acting truth, or whether a shot is artistically necessary.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FORBIDDEN_AUDIO = (
    "背景音乐", "配乐", "BGM", "music", "score", "氛围音", "情绪音效",
    "风铃", "紧张低频", "情绪音垫", "悬疑提示音",
)
FORBIDDEN_PACKAGING = ("紧凑版", "压缩版", "精简版", "compact prompt", "compressed prompt", "abbreviated prompt")
REQUIRED_HEADINGS = ("角色/资产锁定", "视觉材质总控", "镜头语言总控", "事件节拍", "声音", "正向稳定约束")
REQUIRED_SHOT_FIELDS = (
    "start", "end", "duration", "shot_size", "camera_position",
    "camera_height", "angle", "lens", "focus_dof", "lighting", "movement",
    "action", "performance", "dialogue", "cut_trigger", "handoff",
    "endpoint_state", "micro_beats",
)
REQUIRED_MICRO_BEAT_FIELDS = ("start", "end", "description")
FORBIDDEN_DETAIL_SHORTCUTS = (
    "同上", "沿用", "参考镜头表", "参照镜头表", "见镜头表", "保持不变",
    "same as above", "as above", "see shot table", "unchanged",
)
MIN_SECTION_CHARS = {
    "角色/资产锁定": 12,
    "视觉材质总控": 20,
    "镜头语言总控": 20,
    "事件节拍": 60,
    "声音": 12,
    "正向稳定约束": 12,
}
SOFT_BUDGETS = {"dialogue": (4, 8), "emotion": (3, 6), "action": (5, 10), "hybrid": (5, 9)}
DURATION_CONTRACTS = {
    "liu_camera_group": (14.0, 28.0),
    "generic_seedance_clip": (4.0, 15.0),
    "storyboard_only": (0.0, float("inf")),
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def lint(data: dict, prompt: str = "", complexity: str = "high") -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    total = data.get("group_duration")
    shots = data.get("shots")
    scene_type = data.get("scene_type", "hybrid")
    delivery_contract = data.get("delivery_contract", "liu_camera_group")
    output_format = data.get("output_format", "six_part")
    audio_authority = data.get("audio_authority", "default")
    if complexity not in ("low", "medium", "high"):
        fail("complexity must be low, medium, or high", errors)
        complexity = "high"

    if output_format != "six_part":
        fail("output_format must be six_part for every script-derived camera group", errors)
    if audio_authority not in ("default", "explicit_user", "authoritative_script"):
        fail(
            "audio_authority must be default, explicit_user, or authoritative_script",
            errors,
        )

    if delivery_contract not in DURATION_CONTRACTS:
        fail(
            "delivery_contract must be one of: "
            + ", ".join(DURATION_CONTRACTS),
            errors,
        )
    min_duration, max_duration = DURATION_CONTRACTS.get(
        delivery_contract, DURATION_CONTRACTS["liu_camera_group"]
    )

    if not isinstance(total, (int, float)):
        fail("group_duration must be a number", errors)
    elif total < min_duration or total > max_duration:
        if delivery_contract == "liu_camera_group":
            contract_label = "14-28s Liu camera-group contract"
        elif delivery_contract == "generic_seedance_clip":
            contract_label = "4-15s generic Seedance contract"
        elif delivery_contract == "storyboard_only":
            contract_label = "the selected storyboard-only contract"
        else:
            contract_label = "the fallback Liu 14-28s contract"
        fail(
            f"group_duration={total:g}s is outside {contract_label}",
            errors,
        )

    if delivery_contract == "liu_camera_group":
        required_group_state = (
            "opening_state",
            "ending_state",
            "one_action_spine",
            "first_frame_anchor",
            "handoff_state",
        )
        missing_group_state = [
            field for field in required_group_state if not str(data.get(field, "")).strip()
        ]
        if missing_group_state:
            warnings.append(
                "camera-group state is incomplete: "
                + ", ".join(missing_group_state)
            )

    if not isinstance(shots, list) or not shots:
        fail("shots must be a non-empty list", errors)
        return errors, warnings

    previous_end = 0.0
    summed = 0.0
    for index, shot in enumerate(shots, 1):
        if not isinstance(shot, dict):
            fail(f"shot {index} is not an object", errors)
            continue
        missing = [field for field in REQUIRED_SHOT_FIELDS if field not in shot]
        if missing:
            fail(f"shot {index} missing fields: {', '.join(missing)}", errors)
            continue
        empty = [field for field in REQUIRED_SHOT_FIELDS if not str(shot.get(field, "")).strip()]
        if empty:
            fail(f"shot {index} has empty required detail: {', '.join(empty)}", errors)
        try:
            start = float(shot["start"])
            end = float(shot["end"])
            duration = float(shot["duration"])
        except (TypeError, ValueError):
            fail(f"shot {index} has non-numeric start/end/duration", errors)
            continue
        if end <= start or duration <= 0:
            fail(f"shot {index} has invalid timing {start:g}-{end:g} ({duration:g}s)", errors)
        if abs((end - start) - duration) > 0.051:
            fail(f"shot {index} duration does not match start/end", errors)
        if abs(start - previous_end) > 0.051:
            fail(f"shot {index} has a gap/overlap before {start:g}s (expected {previous_end:g}s)", errors)
        if duration > 4.0:
            warnings.append(f"shot {index} lasts {duration:g}s; add a reason for a long take/dialogue hold")
        size = str(shot.get("shot_size", "")).lower()
        movement = str(shot.get("movement", "")).lower()
        if any(token in size for token in ("特写", "大特写", "ecu", "close-up", "close up")):
            if not shot.get("proof_task"):
                warnings.append(f"shot {index} uses a close-up without proof_task; confirm the strong-expression/action/detail reason")
        if any(token in movement for token in ("推脸", "推到脸", "push to face", "push-in to face")):
            fail(f"shot {index} pushes directly to a face; use upper-body, hands, prop, or relationship framing", errors)
        micro_beats = shot.get("micro_beats")
        if not isinstance(micro_beats, list) or not micro_beats:
            fail(f"shot {index} micro_beats must be a non-empty list", errors)
        else:
            micro_previous_end = start
            micro_sum = 0.0
            for micro_index, micro in enumerate(micro_beats, 1):
                if not isinstance(micro, dict):
                    fail(f"shot {index} micro beat {micro_index} is not an object", errors)
                    continue
                missing_micro = [field for field in REQUIRED_MICRO_BEAT_FIELDS if field not in micro]
                if missing_micro:
                    fail(f"shot {index} micro beat {micro_index} missing fields: {', '.join(missing_micro)}", errors)
                    continue
                try:
                    micro_start = float(micro["start"])
                    micro_end = float(micro["end"])
                except (TypeError, ValueError):
                    fail(f"shot {index} micro beat {micro_index} has non-numeric start/end", errors)
                    continue
                if micro_end <= micro_start:
                    fail(f"shot {index} micro beat {micro_index} has invalid timing", errors)
                if abs(micro_start - micro_previous_end) > 0.051:
                    fail(f"shot {index} micro beats have a gap/overlap before {micro_start:g}s (expected {micro_previous_end:g}s)", errors)
                if micro_start < start - 0.051 or micro_end > end + 0.051:
                    fail(f"shot {index} micro beat {micro_index} falls outside shot window {start:g}-{end:g}s", errors)
                if not str(micro.get("description", "")).strip():
                    fail(f"shot {index} micro beat {micro_index} has empty description", errors)
                micro_previous_end = micro_end
                micro_sum += micro_end - micro_start
            if abs(micro_sum - duration) > 0.051 or abs(micro_previous_end - end) > 0.051:
                fail(f"shot {index} micro beats must cover exactly {start:g}-{end:g}s", errors)
        previous_end = end
        summed += duration

    if abs(summed - float(total or 0)) > 0.051:
        fail(f"shot durations sum to {summed:g}s, not group_duration={total}", errors)
    if shots and abs(previous_end - float(total or 0)) > 0.051:
        fail(f"last shot ends at {previous_end:g}s, not group end {total}s", errors)

    low, high = SOFT_BUDGETS.get(scene_type, SOFT_BUDGETS["hybrid"])
    if not (low <= len(shots) <= high):
        warnings.append(
            f"{scene_type} group has {len(shots)} shots; soft review range is {low}-{high}, "
            "override only with a script-based reason"
        )

    if prompt:
        # The canonical Liu contract itself names prohibited layers. Remove
        # those negated phrases before looking for accidental positive audio.
        scan_text = prompt.replace("无任何音乐和情绪/氛围音效", "")
        scan_text = scan_text.replace("无任何音乐和情绪音效", "")
        scan_lines = [line for line in scan_text.splitlines() if not re.search(r"禁止|无音乐|不含音乐|no music|without music", line, re.I)]
        lowered = "\n".join(scan_lines).lower()
        found = [term for term in FORBIDDEN_AUDIO if term.lower() in lowered]
        if found and audio_authority == "default":
            fail("prompt contains forbidden audio terms: " + ", ".join(sorted(set(found))), errors)
        if "@" not in prompt:
            warnings.append("prompt contains no @character handle; verify whether uploaded five-view assets are in use")
        if audio_authority == "default" and ("仅人物台词" not in prompt or "纯拟声音效" not in prompt):
            warnings.append("prompt does not state the complete Liu audio contract explicitly")
        missing_headings = [heading for heading in REQUIRED_HEADINGS if heading not in prompt]
        event_text = ""
        if missing_headings:
            fail("prompt is missing complete-prompt headings: " + ", ".join(missing_headings), errors)
        else:
            heading_positions = [prompt.index(heading) for heading in REQUIRED_HEADINGS]
            if heading_positions != sorted(heading_positions):
                fail("six-part headings are not in the required order", errors)
            for idx, heading in enumerate(REQUIRED_HEADINGS):
                start = heading_positions[idx] + len(heading)
                end = heading_positions[idx + 1] if idx + 1 < len(REQUIRED_HEADINGS) else len(prompt)
                body = re.sub(r"^[】:\s：\-]+", "", prompt[start:end]).strip()
                compact_body = re.sub(r"\s+", "", body)
                if len(compact_body) < MIN_SECTION_CHARS[heading]:
                    fail(f"section {heading} is empty or under-detailed", errors)
            event_text = prompt[heading_positions[3]:heading_positions[4]]
            shot_lines = [line for line in event_text.splitlines() if re.search(r"(?:镜头\s*0*\d+|第\s*0*\d+\s*镜)", line)]
            if len(shot_lines) < len(shots):
                fail("事件节拍 must use one explicit shot block line per shot", errors)
        shortcuts = [term for term in FORBIDDEN_DETAIL_SHORTCUTS if term.lower() in prompt.lower()]
        if shortcuts:
            fail("prompt substitutes cross-references for detail: " + ", ".join(shortcuts), errors)
        for index, shot in enumerate(shots, 1):
            shot_marker = re.search(rf"(?:镜头\s*0*{index}|第\s*0*{index}\s*镜)", event_text)
            if not shot_marker:
                fail(f"事件节拍 is missing an explicit marker for shot {index}", errors)
            try:
                start_token = f"{float(shot['start']):g}"
                end_token = f"{float(shot['end']):g}"
            except (KeyError, TypeError, ValueError):
                continue
            if start_token not in event_text or end_token not in event_text:
                fail(f"事件节拍 shot {index} is missing its {start_token}-{end_token}s timecode", errors)
            if complexity == "high":
                for micro_index, micro in enumerate(shot.get("micro_beats", []), 1):
                    try:
                        micro_start = f"{float(micro['start']):g}"
                        micro_end = f"{float(micro['end']):g}"
                    except (KeyError, TypeError, ValueError):
                        continue
                    pattern = rf"T\s*=\s*{re.escape(micro_start)}\s*-\s*{re.escape(micro_end)}\s*s"
                    if not re.search(pattern, event_text, re.I):
                        fail(f"事件节拍 shot {index} is missing T={micro_start}-{micro_end}s micro beat {micro_index}", errors)
            elif re.search(r"(?:^|\n)\s*T\s*=", event_text, re.I):
                fail(f"{complexity} complexity prompt must omit visible T= micro-beats", errors)
        packaging = [term for term in FORBIDDEN_PACKAGING if term.lower() in prompt.lower()]
        if packaging:
            fail("prompt contains forbidden abbreviated-delivery terms: " + ", ".join(packaging), errors)
        if re.search(r"\{\{(?:Image|Video|Audio)\s+\d+\}\}", prompt):
            fail("prompt uses numbered {{Image/Video/Audio N}} as a primary reference; use the exact uploaded @name", errors)
        for reference in data.get("references", []) if isinstance(data.get("references"), list) else []:
            if not isinstance(reference, dict) or not str(reference.get("name", "")).strip():
                continue
            name = str(reference["name"]).strip()
            token = "@" + name
            if token not in prompt:
                fail(f"prompt is missing exact reference handle {token}", errors)

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path, help="camera-group JSON file")
    parser.add_argument("--prompt", type=Path, help="optional copy-ready prompt text")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    parser.add_argument("--complexity", choices=("low", "medium", "high"), default="high", help="active prompt description profile; default high preserves legacy T= checks")
    args = parser.parse_args()
    try:
        data = json.loads(args.json_file.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read JSON: {exc}", file=sys.stderr)
        return 2
    prompt = ""
    if args.prompt:
        try:
            prompt = args.prompt.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: cannot read prompt: {exc}", file=sys.stderr)
            return 2
    errors, warnings = lint(data, prompt, args.complexity)
    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if args.strict and warnings:
        errors.extend(f"strict: {warning}" for warning in warnings)
    if errors:
        return 1
    print(
        f"OK: {len(data['shots'])} shots, {data['group_duration']}s group "
        f"({data.get('delivery_contract', 'liu_camera_group')})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
