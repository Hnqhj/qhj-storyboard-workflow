#!/usr/bin/env python3
"""Render a mobile-reading long image from briefing JSON.

Uses Pillow only. Designed for Chinese AIGC daily briefings where the user
prefers reading a phone-friendly image instead of opening HTML.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


W = 1080
M = 74
CARD_W = W - M * 2
BG = "#f7f9fd"
WHITE = "#ffffff"
INK = "#1f2a3d"
MUTED = "#718096"
BLUE = "#3564f4"
INDIGO = "#6b58d9"
GREEN = "#22c78d"
LINE = "#dfe7f3"
SOFT_BLUE = "#eef4ff"
SOFT_CYAN = "#eafcff"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = "C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"
    return ImageFont.truetype(path, size)


F_TITLE = font(48, True)
F_SUB = font(25)
F_PILL = font(25, True)
F_H2 = font(34, True)
F_TAG = font(23, True)
F_META = font(23)
F_BODY = font(27)
F_BODY_BOLD = font(27, True)
F_SMALL = font(22)
F_FOOT = font(23)

_scratch = Image.new("RGB", (W, 100), BG)
_draw = ImageDraw.Draw(_scratch)


def text_w(text: str, fnt: ImageFont.FreeTypeFont) -> float:
    return _draw.textlength(str(text), font=fnt)


def line_height(fnt: ImageFont.FreeTypeFont, factor: float = 1.55) -> int:
    bbox = fnt.getbbox("国")
    return int((bbox[3] - bbox[1]) * factor)


def wrap(text: str, fnt: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    text = str(text or "").replace("\r", "").strip()
    lines: list[str] = []
    for para in text.split("\n"):
        para = para.strip()
        if not para:
            lines.append("")
            continue
        cur = ""
        for ch in para:
            test = cur + ch
            if text_w(test, fnt) <= max_w or not cur:
                cur = test
            else:
                lines.append(cur)
                cur = ch
        if cur:
            lines.append(cur)
    return lines


def source_parts(source: str) -> tuple[str, str]:
    parts = [p.strip() for p in str(source or "").replace("|", "｜").split("｜") if p.strip()]
    labels: list[str] = []
    url = ""
    for part in parts:
        if part.startswith("http://") or part.startswith("https://"):
            url = part
        else:
            labels.append(part)
    return "｜".join(labels) or "未标注来源", url


def card_height(item: dict) -> int:
    inner = CARD_W - 72
    source_label, _url = source_parts(item.get("source", ""))
    source_text = f"{source_label}｜{item.get('importance', '中')}"
    impact = item.get("impact") or item.get("interpretation") or "这条动态值得继续观察其对创作流程、成本和产出质量的实际影响。"

    h = 34 + 42 + 30
    h += len(wrap(item.get("title", ""), F_H2, inner)) * line_height(F_H2, 1.42) + 18
    h += len(wrap(source_text, F_SMALL, inner - 28)) * line_height(F_SMALL, 1.35) + 20
    h += 42 + len(wrap(item.get("summary", ""), F_BODY, inner)) * line_height(F_BODY, 1.5) + 22
    h += 62 + len(wrap(impact, F_BODY, inner - 38)) * line_height(F_BODY, 1.5) + 44
    return h


def draw_center(draw: ImageDraw.ImageDraw, text: str, y: int, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    draw.text(((W - text_w(text, fnt)) / 2, y), text, fill=fill, font=fnt)


def draw_card(draw: ImageDraw.ImageDraw, item: dict, y: int) -> int:
    card_h = card_height(item)
    x0, y0, x1, y1 = M, y, W - M, y + card_h

    draw.rounded_rectangle((x0 + 8, y0 + 10, x1 + 8, y1 + 10), radius=18, fill="#edf1f8")
    draw.rounded_rectangle((x0, y0, x1, y1), radius=18, fill=WHITE, outline="#e8eef8", width=2)
    draw.rounded_rectangle((x0, y0, x0 + 8, y1), radius=4, fill=BLUE)
    draw.line((x0 + 8, y0, x1 - 10, y0), fill=INDIGO, width=6)

    cx = x0 + 36
    cy = y0 + 34
    tag = str(item.get("category", "未分类"))
    tag_w = int(text_w(tag, F_TAG) + 38)
    draw.rounded_rectangle((cx, cy, cx + tag_w, cy + 42), radius=21, fill=SOFT_BLUE)
    draw.text((cx + 19, cy + 7), tag, fill=BLUE, font=F_TAG)

    date = str(item.get("date", ""))
    draw.text((x1 - 36 - text_w(date, F_META), cy + 7), date, fill=MUTED, font=F_META)
    cy += 72

    for line in wrap(item.get("title", ""), F_H2, CARD_W - 72):
        draw.text((cx, cy), line, fill=INK, font=F_H2)
        cy += line_height(F_H2, 1.42)
    cy += 12

    source_label, _url = source_parts(item.get("source", ""))
    source_text = f"{source_label}｜{item.get('importance', '中')}"
    draw.ellipse((cx, cy + 10, cx + 14, cy + 24), fill=GREEN)
    for line in wrap(source_text, F_SMALL, CARD_W - 100):
        draw.text((cx + 26, cy), line, fill=MUTED, font=F_SMALL)
        cy += line_height(F_SMALL, 1.35)
    cy += 16

    draw.text((cx, cy), "摘要", fill=INK, font=F_BODY_BOLD)
    cy += 42
    for line in wrap(item.get("summary", ""), F_BODY, CARD_W - 72):
        draw.text((cx, cy), line, fill="#3b4658", font=F_BODY)
        cy += line_height(F_BODY, 1.5)
    cy += 20

    impact = item.get("impact") or item.get("interpretation") or "这条动态值得继续观察其对创作流程、成本和产出质量的实际影响。"
    impact_lines = wrap(impact, F_BODY, CARD_W - 110)
    box_h = 62 + len(impact_lines) * line_height(F_BODY, 1.5) + 34
    draw.rounded_rectangle((cx, cy, x1 - 36, cy + box_h), radius=14, fill=SOFT_CYAN, outline="#d7f2f7", width=2)
    draw.text((cx + 24, cy + 18), "影响解读", fill=INK, font=F_BODY_BOLD)
    iy = cy + 62
    for line in impact_lines:
        draw.text((cx + 24, iy), line, fill="#3b4658", font=F_BODY)
        iy += line_height(F_BODY, 1.5)

    return y1 + 34


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--content_file", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--preview", default="")
    args = parser.parse_args()

    data = json.loads(Path(args.content_file).read_text(encoding="utf-8"))
    items = [item for item in data.get("items", []) if isinstance(item, dict)]

    header_h = 315
    cards_h = sum(card_height(item) + 34 for item in items)
    img = Image.new("RGB", (W, header_h + cards_h + 190), BG)
    draw = ImageDraw.Draw(img)

    y = 58
    draw_center(draw, "AIGC每日快报｜2026-06-01", y, F_TITLE, BLUE)
    y += 70
    draw_center(draw, "聚焦创作工具、前沿技术与可落地工作流", y, F_SUB, MUTED)
    y += 52
    pill = f"今日精选 · {len(items)}条动态"
    pill_w = int(text_w(pill, F_PILL) + 72)
    draw.rounded_rectangle(((W - pill_w) // 2, y, (W + pill_w) // 2, y + 54), radius=27, fill=BLUE)
    draw_center(draw, pill, y + 8, F_PILL, WHITE)
    y += 90
    draw.line((M, y, W - M, y), fill=LINE, width=2)
    y += 42

    for item in items:
        y = draw_card(draw, item, y)

    y += 10
    draw.line((M, y, W - M, y), fill=LINE, width=2)
    y += 30
    footer = "本快报由行业快报生成技能生成｜一级信源优先｜适合手机长图阅读"
    for line in wrap(footer, F_FOOT, W - M * 2):
        draw_center(draw, line, y, F_FOOT, MUTED)
        y += line_height(F_FOOT, 1.4)

    img = img.crop((0, 0, W, y + 40))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output)
    if args.preview:
        preview = Path(args.preview)
        img.crop((0, 0, W, min(2200, img.height))).save(preview)
    print(str(output.resolve()))


if __name__ == "__main__":
    main()
