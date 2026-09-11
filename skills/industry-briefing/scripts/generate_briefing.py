#!/usr/bin/env python3
"""Generate HTML or Markdown industry briefings from structured JSON content.

This Codex-compatible fallback replaces the original encrypted Linux-only
binary entrypoint. It intentionally uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_HTML = ROOT / "assets" / "template.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate an industry briefing")
    parser.add_argument("--industry", required=True, help="Industry name")
    parser.add_argument("--theme", default="[]", help="JSON array of themes")
    parser.add_argument("--start_date", required=True, help="Start date YYYY-MM-DD")
    parser.add_argument("--end_date", required=True, help="End date YYYY-MM-DD")
    parser.add_argument("--item_count", type=int, default=10, help="Expected item count")
    parser.add_argument("--format", choices=["html", "markdown", "md"], default="html")
    parser.add_argument("--content", default="", help="Briefing content JSON")
    parser.add_argument("--content_file", default="", help="UTF-8 JSON file with briefing content")
    parser.add_argument("--output", default="", help="Optional output path")
    return parser.parse_args()


def load_content(raw: str) -> dict:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid --content JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit("--content must be a JSON object")
    items = data.get("items", [])
    if not isinstance(items, list):
        raise SystemExit("--content.items must be a list")
    return data


def load_content_arg(args: argparse.Namespace) -> dict:
    if args.content_file:
        raw = Path(args.content_file).read_text(encoding="utf-8")
        return load_content(raw)
    if args.content:
        return load_content(args.content)
    raise SystemExit("Either --content or --content_file is required")


def safe_filename(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|]+", "_", text.strip())
    return text or "industry"


def importance_class(value: str) -> str:
    value = value.strip()
    if value in {"高", "high", "High"}:
        return "importance-high"
    if value in {"中", "medium", "Medium"}:
        return "importance-medium"
    return "importance-low"


def item_value(item: dict, key: str, default: str = "") -> str:
    value = item.get(key, default)
    return "" if value is None else str(value)


def source_parts(source: str) -> tuple[str, str]:
    if "｜" in source:
        parts = [part.strip() for part in source.split("｜") if part.strip()]
    else:
        parts = [part.strip() for part in source.split("|") if part.strip()]
    label_parts: list[str] = []
    url = ""
    for part in parts:
        if part.startswith("http://") or part.startswith("https://"):
            url = part
        else:
            label_parts.append(part)
    return "｜".join(label_parts) or "未标注来源", url


def grouped_items(items: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        if isinstance(item, dict):
            groups[item_value(item, "category", "未分类") or "未分类"].append(item)
    return dict(groups)


def render_html(data: dict, industry: str, date_range: str, output_path: Path) -> None:
    template = TEMPLATE_HTML.read_text(encoding="utf-8")
    items = [item for item in data.get("items", []) if isinstance(item, dict)]
    groups = grouped_items(items)
    cards: list[str] = []

    for item in items:
        category = item_value(item, "category", "未分类")
        importance = item_value(item, "importance", "中")
        source_label, source_url = source_parts(item_value(item, "source", "未标注来源"))
        source_html = html.escape(source_label)
        if source_url:
            source_html += f'｜<a href="{html.escape(source_url)}" target="_blank" rel="noreferrer">{html.escape(source_url)}</a>'
        impact = item_value(item, "impact") or item_value(item, "interpretation") or "这条动态值得继续观察其对创作流程、成本和产出质量的实际影响。"
        cards.append(
            f"""
            <article class="brief-card">
                <div class="card-top">
                    <span class="tag">{html.escape(category)}</span>
                    <span class="date">{html.escape(item_value(item, "date"))}</span>
                </div>
                <h2>{html.escape(item_value(item, "title", "未命名动态"))}</h2>
                <div class="source-row">
                    <span>{source_html}<span class="importance">{html.escape(importance)}</span></span>
                </div>
                <div class="section-label">摘要</div>
                <p class="summary">{html.escape(item_value(item, "summary"))}</p>
                <div class="impact-box">
                    <div class="section-label">影响解读</div>
                    <p class="impact">{html.escape(impact)}</p>
                </div>
            </article>
            """
        )

    high_count = sum(1 for item in items if item_value(item, "importance") == "高")
    sources = sorted({item_value(item, "source") for item in items if item_value(item, "source")})
    rendered = (
        template.replace("{{INDUSTRY}}", html.escape(industry))
        .replace("{{DATE_RANGE}}", html.escape(date_range))
        .replace("{{END_DATE}}", html.escape(data.get("end_date") or date_range.split("至")[-1].strip()))
        .replace("{{TOTAL_COUNT}}", str(len(items)))
        .replace("{{GENERATE_TIME}}", datetime.now().strftime("%Y-%m-%d %H:%M"))
        .replace("{{CATEGORY_COUNT}}", str(len(groups)))
        .replace("{{HIGH_IMPORTANCE}}", str(high_count))
        .replace("{{CONTENT}}", "\n".join(cards))
        .replace("{{SOURCES}}", html.escape("、".join(source_parts(source)[0] for source in sources) if sources else "未标注"))
    )
    output_path.write_text(rendered, encoding="utf-8")


def render_markdown(data: dict, industry: str, date_range: str, output_path: Path) -> None:
    items = [item for item in data.get("items", []) if isinstance(item, dict)]
    groups = grouped_items(items)
    high_count = sum(1 for item in items if item_value(item, "importance") == "高")
    lines = [
        f"# {industry}行业快报",
        "",
        f"- 时间范围：{date_range}",
        f"- 总条数：{len(items)}",
        f"- 覆盖领域：{len(groups)}",
        f"- 重要动态：{high_count}",
        f"- 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]
    for category, category_items in groups.items():
        lines.extend([f"## {category}", ""])
        for item in category_items:
            lines.extend(
                [
                    f"### {item_value(item, 'title', '未命名动态')}",
                    "",
                    f"- 日期：{item_value(item, 'date')}",
                    f"- 重要性：{item_value(item, 'importance', '中')}",
                    f"- 来源：{item_value(item, 'source', '未标注来源')}",
                    f"- 摘要：{item_value(item, 'summary')}",
                    "",
                ]
            )
    output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    data = load_content_arg(args)
    industry = args.industry or data.get("industry", "行业")
    date_range = data.get("date_range") or f"{args.start_date} 至 {args.end_date}"
    fmt = "md" if args.format in {"markdown", "md"} else "html"
    output_path = Path(args.output) if args.output else Path.cwd() / f"{safe_filename(industry)}_快报_{args.end_date}.{fmt}"

    if fmt == "html":
        render_html(data, industry, date_range, output_path)
    else:
        render_markdown(data, industry, date_range, output_path)

    print(str(output_path.resolve()))


if __name__ == "__main__":
    main()
