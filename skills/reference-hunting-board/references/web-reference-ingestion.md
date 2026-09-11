# Web Reference Ingestion

Use this when the user gives web links, X/Twitter threads, GitHub repos, article pages, tool pages, or says “挨个去看 / 自己去看 / 拉网页 / 存参考”.

## Default capture order

1. Use public structured interfaces first:
   - X/Twitter: `api.fxtwitter.com`, `api.vxtwitter.com`, `publish.twitter.com/oembed`.
   - GitHub: repo page, README, releases, issues/PRs only when relevant.
   - Video/media links: `yt-dlp` or `gallery-dl` only when the user needs local media evidence.
2. Use static HTML extraction next:
   - `requests/httpx` + `trafilatura/readability` for article-like pages.
   - `BeautifulSoup/selectolax` for link lists and metadata.
3. Use headless rendering only when necessary:
   - `playwright` with its own headless Chromium.
   - Do not use or foreground the user’s interactive Chrome unless explicitly requested.
4. For large batches, limit scope before crawling:
   - source domains;
   - max URL count;
   - max depth;
   - output folder;
   - whether media should be downloaded.

## Project output

Save captured references under the current project, usually:

```text
02_research/web_references/
02_research/video_references/
02_research/github_references/
05_reviews/reference_breakdowns/
```

Each captured reference should preserve:

- source URL;
- capture time;
- extracted text;
- article or quote preview when available;
- media URLs when available;
- raw JSON/HTML evidence when practical;
- prompt-transfer note when the reference is creative.

## Local script

Use the bundled script for safe public page capture:

```powershell
python "<skills-root>\reference-hunting-board\scripts\capture_web_reference.py" `
  "https://x.com/gengdaJ/status/2069425112651272493" `
  --out-dir "<project-root>\02_research\web_references"
```

The script:

- does not use the user’s Chrome;
- does not log in;
- captures X/Twitter status text, article previews, quotes, media URLs, and raw JSON when public APIs expose them;
- captures ordinary webpages through static extraction;
- writes one Markdown file per URL.

## Creative extraction pass

After capture, do not stop at summarization. Extract:

```text
source -> mechanism -> usable workflow -> risk -> whether to install/adopt -> where to store it
```

For AI-video work, translate references into:

- reference role for Seedance/SD2;
- prompt-control wording;
- shot/motion/material mechanism;
- failure risk if copied blindly.

## Guardrails

- Do not bypass login, paywalls, private pages, platform restrictions, or robots scope.
- Do not scrape account-bound private content unless the user explicitly authorizes it.
- Do not download large videos/images unless the user asked or the reference cannot be assessed otherwise.
- Do not let a web reference overwrite the current project’s established style unless it solves a real repeated problem.
