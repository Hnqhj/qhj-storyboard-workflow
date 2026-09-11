#!/usr/bin/env python3
"""
Capture web / X(Twitter) references into project-local Markdown files.

This script is intentionally conservative:
- It does not use the user's interactive browser.
- It does not log in, bypass paywalls, or scrape private pages.
- It saves raw API/html evidence next to the Markdown summary for traceability.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import textwrap
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

try:
    import trafilatura
except Exception:  # pragma: no cover
    trafilatura = None


USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
)


def slugify(text: str, fallback: str = "reference") -> str:
    text = re.sub(r"https?://", "", text.strip(), flags=re.I)
    text = re.sub(r"[^\w\u4e00-\u9fff.-]+", "-", text, flags=re.U)
    text = re.sub(r"-{2,}", "-", text).strip("-._")
    return (text[:80] or fallback)


def sha_short(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:10]


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def request_json(url: str) -> dict[str, Any]:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    return response.json()


def request_text(url: str) -> tuple[str, str]:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    content_type = response.headers.get("content-type", "")
    response.encoding = response.encoding or response.apparent_encoding or "utf-8"
    return response.text, content_type


def x_status_parts(url: str) -> tuple[str, str] | None:
    match = re.search(r"(?:x|twitter)\.com/([^/?#]+)/status/(\d+)", url)
    if not match:
        return None
    return match.group(1), match.group(2)


def normalize_tweet_from_fx(data: dict[str, Any]) -> dict[str, Any]:
    tweet = data.get("tweet", data)
    author = tweet.get("author") or {}
    article = tweet.get("article") or {}
    quote = tweet.get("quote") or {}
    media = tweet.get("media") or {}
    all_media = media.get("all") or []
    media_urls = []
    for item in all_media:
        for key in ("url", "thumbnail_url"):
            if item.get(key):
                media_urls.append(item[key])
    return {
        "source_kind": "x_status",
        "title": article.get("title") or (tweet.get("text") or "").splitlines()[0:1] or ["X status"],
        "text": tweet.get("text") or article.get("preview_text") or "",
        "article_title": article.get("title") or "",
        "article_preview": article.get("preview_text") or "",
        "author": author.get("name") or author.get("screen_name") or "",
        "screen_name": author.get("screen_name") or "",
        "created_at": tweet.get("created_at") or "",
        "likes": tweet.get("likes"),
        "bookmarks": tweet.get("bookmarks"),
        "views": tweet.get("views"),
        "quote_text": quote.get("text") or "",
        "quote_url": quote.get("url") or "",
        "media_urls": sorted(set(media_urls)),
        "raw": data,
    }


def normalize_tweet_from_vx(data: dict[str, Any]) -> dict[str, Any]:
    article = data.get("article") or {}
    qrt = data.get("qrt") or {}
    media_urls = list(data.get("mediaURLs") or [])
    for item in data.get("media_extended") or []:
        if item.get("url"):
            media_urls.append(item["url"])
        if item.get("thumbnail_url"):
            media_urls.append(item["thumbnail_url"])
    return {
        "source_kind": "x_status",
        "title": article.get("title") or (data.get("text") or "X status"),
        "text": data.get("text") or article.get("preview_text") or "",
        "article_title": article.get("title") or "",
        "article_preview": article.get("preview_text") or "",
        "author": data.get("user_name") or "",
        "screen_name": data.get("user_screen_name") or "",
        "created_at": data.get("date") or "",
        "likes": data.get("likes"),
        "bookmarks": None,
        "views": None,
        "quote_text": (qrt.get("text") if isinstance(qrt, dict) else "") or "",
        "quote_url": data.get("qrtURL") or (qrt.get("tweetURL") if isinstance(qrt, dict) else "") or "",
        "media_urls": sorted(set(media_urls)),
        "raw": data,
    }


def capture_x_status(url: str) -> dict[str, Any]:
    parts = x_status_parts(url)
    if not parts:
        raise ValueError("Not an X/Twitter status URL")
    user, status_id = parts
    errors: list[str] = []

    fx_url = f"https://api.fxtwitter.com/{user}/status/{status_id}"
    try:
        data = request_json(fx_url)
        item = normalize_tweet_from_fx(data)
        item["source_url"] = url
        item["api_url"] = fx_url
        return item
    except Exception as exc:
        errors.append(f"fxtwitter: {exc}")

    vx_url = f"https://api.vxtwitter.com/{user}/status/{status_id}"
    try:
        data = request_json(vx_url)
        item = normalize_tweet_from_vx(data)
        item["source_url"] = url
        item["api_url"] = vx_url
        item["errors"] = errors
        return item
    except Exception as exc:
        errors.append(f"vxtwitter: {exc}")
        raise RuntimeError("; ".join(errors))


def capture_regular_web(url: str) -> dict[str, Any]:
    body, content_type = request_text(url)
    extracted = ""
    if trafilatura is not None:
        try:
            extracted = trafilatura.extract(
                body,
                url=url,
                include_comments=False,
                include_tables=True,
                output_format="markdown",
            ) or ""
        except Exception:
            extracted = ""
    soup = BeautifulSoup(body, "html.parser")
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    if not extracted:
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        extracted = soup.get_text("\n", strip=True)
    links = []
    for a in soup.find_all("a", href=True):
        label = a.get_text(" ", strip=True)
        href = a["href"]
        if href and href.startswith(("http://", "https://")):
            links.append({"label": label[:120], "url": href})
    return {
        "source_kind": "web_page",
        "source_url": url,
        "title": title or url,
        "text": extracted,
        "content_type": content_type,
        "links": links[:200],
        "raw_html": body,
    }


def markdown_for_capture(item: dict[str, Any]) -> str:
    title = item.get("title")
    if isinstance(title, list):
        title = title[0] if title else "Reference"
    title = str(title or "Reference").strip()
    lines = [
        f"# {title}",
        "",
        "## Metadata",
        "",
        f"- Source URL: {item.get('source_url', '')}",
        f"- Source kind: {item.get('source_kind', '')}",
        f"- Captured at: {now_iso()}",
    ]
    for key, label in [
        ("api_url", "API URL"),
        ("author", "Author"),
        ("screen_name", "Screen name"),
        ("created_at", "Created at"),
        ("likes", "Likes"),
        ("bookmarks", "Bookmarks"),
        ("views", "Views"),
        ("content_type", "Content type"),
    ]:
        value = item.get(key)
        if value not in (None, ""):
            lines.append(f"- {label}: {value}")

    article_title = item.get("article_title")
    article_preview = item.get("article_preview")
    if article_title or article_preview:
        lines += ["", "## Article preview", ""]
        if article_title:
            lines.append(f"**{article_title}**")
            lines.append("")
        if article_preview:
            lines.append(str(article_preview).strip())

    text = str(item.get("text") or "").replace("\u200b", "").strip()
    if text:
        lines += ["", "## Extracted text", "", text]

    quote_text = str(item.get("quote_text") or "").replace("\u200b", "").strip()
    if quote_text:
        lines += ["", "## Quoted / referenced text", ""]
        if item.get("quote_url"):
            lines.append(f"Quote URL: {item.get('quote_url')}")
            lines.append("")
        lines.append(quote_text)

    media_urls = item.get("media_urls") or []
    if media_urls:
        lines += ["", "## Media URLs", ""]
        for u in media_urls:
            lines.append(f"- {u}")

    links = item.get("links") or []
    if links:
        lines += ["", "## Links", ""]
        for link in links[:80]:
            label = str(link.get("label") or "").replace("\n", " ").strip()
            href = link.get("url") or ""
            lines.append(f"- {label}: {href}" if label else f"- {href}")

    errors = item.get("errors") or []
    if errors:
        lines += ["", "## Capture notes", ""]
        for err in errors:
            lines.append(f"- {err}")

    return "\n".join(lines).rstrip() + "\n"


def save_capture(url: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    parsed = urlparse(url)
    source_slug = slugify(parsed.netloc + "-" + parsed.path.strip("/"), "reference")
    stem = f"{source_slug}-{sha_short(url)}"
    raw_path = out_dir / f"{stem}.raw.json"
    html_path = out_dir / f"{stem}.raw.html"
    md_path = out_dir / f"{stem}.md"

    if x_status_parts(url):
        item = capture_x_status(url)
        raw_payload = item.pop("raw", None)
        if raw_payload is not None:
            raw_path.write_text(json.dumps(raw_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        item = capture_regular_web(url)
        raw_html = item.pop("raw_html", "")
        if raw_html:
            html_path.write_text(raw_html, encoding="utf-8", errors="ignore")

    md_path.write_text(markdown_for_capture(item), encoding="utf-8")
    return md_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture public web references into Markdown.")
    parser.add_argument("urls", nargs="+", help="URLs to capture")
    parser.add_argument("--out-dir", required=True, help="Project-local output directory")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    paths: list[Path] = []
    for url in args.urls:
        try:
            path = save_capture(url, out_dir)
            paths.append(path)
            print(path)
        except Exception as exc:
            print(f"ERROR {url}: {exc}", file=sys.stderr)
    return 0 if len(paths) == len(args.urls) else 1


if __name__ == "__main__":
    raise SystemExit(main())
