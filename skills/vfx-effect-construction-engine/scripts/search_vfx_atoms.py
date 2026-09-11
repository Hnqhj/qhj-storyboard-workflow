#!/usr/bin/env python3
"""Search the bundled bilingual VFX atom bank without loading it into prompt context."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BANK = Path(__file__).resolve().parents[1] / "references" / "vfx-atoms.json"

ALIASES = {
    "法阵": ["魔法阵", "召唤法阵", "结界", "符文", "领域"],
    "封印": ["结界", "吸附", "收缩", "空间恢复", "法阵熄灭"],
    "阴阳术": ["魔法", "符文", "法阵", "结界", "空间"],
    "修仙": ["能量", "法力", "元素", "领域", "神圣"],
    "妖刀": ["斩击", "光刃", "真空斩", "剑气", "能量尾迹"],
    "太刀": ["斩击", "弧形斩击", "纵向斩击", "横向斩击", "拖尾光迹"],
    "打击": ["命中", "冲击波", "火花", "碎片", "击退"],
    "变身": ["变身释放", "激活", "包裹", "凝固", "形态变化"],
    "拖影": ["粒子拖尾", "光束拖影", "残影", "运动模糊粒子"],
    "空间裂缝": ["空间撕裂", "空间裂缝", "维度裂开", "异空间裂缝"],
    "magic circle": ["Magic Circle", "Rune", "Barrier", "Domain"],
    "seal": ["Barrier", "Convergence", "Compression", "Space Restoration"],
    "weapon trail": ["Slash", "Particle Trails", "Light Trail", "Vacuum Slash"],
    "transformation": ["Transformation Cast", "Morph", "Activation", "Reassemble"],
}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def query_terms(query: str) -> list[tuple[str, int]]:
    q = normalize(query)
    if not q:
        return []
    terms: list[tuple[str, int]] = [(q, 10)]
    for token in re.split(r"[\s,，/]+", q):
        if token and token != q:
            terms.append((token, 5))
    for key, expansions in ALIASES.items():
        if normalize(key) in q:
            terms.extend((normalize(item), 2) for item in expansions)
    seen: dict[str, int] = {}
    for term, weight in terms:
        seen[term] = max(weight, seen.get(term, 0))
    return list(seen.items())


def score(atom: dict[str, str], terms: list[tuple[str, int]]) -> int:
    fields = {
        "zh": normalize(atom["zh"]),
        "en": normalize(atom["en"]),
        "category": normalize(atom["category"]),
        "role": normalize(atom["role"]),
        "family": normalize(atom["family"]),
    }
    total = 0
    for term, weight in terms:
        for field, value in fields.items():
            if term == value:
                total += weight * (5 if field in {"zh", "en"} else 3)
            elif term in value:
                total += weight * (3 if field in {"zh", "en"} else 1)
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description="Search bilingual VFX construction atoms.")
    parser.add_argument("query", nargs="?", default="", help="Chinese or English search phrase")
    parser.add_argument("--category", help="Exact category filter")
    parser.add_argument("--role", help="Exact construction-role filter")
    parser.add_argument("--family", help="Exact family filter")
    parser.add_argument("--limit", type=int, default=8, help="Maximum results (default: 8)")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    bank = json.loads(BANK.read_text(encoding="utf-8"))["atoms"]
    selected = []
    terms = query_terms(args.query)

    for atom in bank:
        if args.category and atom["category"] != args.category:
            continue
        if args.role and atom["role"] != args.role:
            continue
        if args.family and atom["family"] != args.family:
            continue
        rank = score(atom, terms) if terms else 1
        if rank > 0:
            selected.append((rank, atom))

    selected.sort(key=lambda item: (-item[0], int(item[1]["id"].rsplit("_", 1)[1])))
    results = [atom | {"score": rank} for rank, atom in selected[: max(1, args.limit)]]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    if not results:
        print("No matching VFX atoms.")
        return 1

    print("ID\tCategory\tRole\tFamily\tChinese\tEnglish\tScore")
    for atom in results:
        print(
            f"{atom['id']}\t{atom['category']}\t{atom['role']}\t{atom['family']}\t"
            f"{atom['zh']}\t{atom['en']}\t{atom['score']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
