# Midjourney V8.1 compatibility boundary

Verified against official Midjourney documentation on 2026-08-10.

Midjourney's current default is V8.2, so every prompt produced by this V8.1-specific skill must end with `--v 8.1`.

## Safe controls for this skill

| Control | V8.1 guidance |
| --- | --- |
| `--v 8.1` | Always include it and place it at the end of the parameter block. |
| `--ar W:H` | Supported. Default is `1:1`; V8.1 supports up to 14:1 in SD and 4:1 in HD. Use integer ratios. |
| `--raw` | Supported. Use for more literal prompt following, realistic photography, or direct stylistic control. The syntax is `--raw`, never `--style raw`. |
| `--s N` | Supported. Range 0–1000; default is 100. Lower follows the prompt more literally, higher adds artistic interpretation. |
| `--c N` | Supported. Range 0–100; default is 0. Higher values increase variation and reduce predictability. |
| `--no terms` | Supported. Use a short list of concrete unwanted elements. |
| `--seed N` | Supported. Add only when the user provides or requests a seed. |
| `--sref URL_OR_CODE` | Style Reference is supported. Preserve user-provided URLs or codes exactly. |
| `--sw N` | Style Reference weight is supported. Use only together with `--sref`. |
| leading image URL + `--iw N` | Image prompts and image weight are supported. Never invent a URL. |
| `--tile` | Supported for seamless repeating patterns. |
| `--weird N` | Supported, but use only when the user asks for unconventional exploration. |
| `--profile CODE` | Personalization is supported. Add only when the user supplies a profile or moodboard code. |
| `--hd` / `--sd` | V8.1 supports native 2048px HD and 1024px SD. HD costs more GPU time and limits aspect ratio to 4:1. |

Parameters must come after the prompt text, separated by spaces, with no punctuation appended to parameter values.

## Do not emit for V8.1

- `--q`: the official version comparison lists the Quality parameter as unavailable for V8.1/V8.2.
- `--oref`: Omni Reference belongs to V7 and is unavailable in V8.1.
- `--cref` or `--cw`: Character Reference and Character Weight are unavailable in V8.1.
- `::` multi-prompts or prompt weights: official compatibility currently stops at V6.1 and Niji 6.
- `--draft`: the dedicated Draft documentation says V8.1/V8.2 Draft is available only on midjourney.com and unavailable in Discord. Do not add it by default; preserve or use it only when the user explicitly requests website Draft. The Version compatibility table currently conflicts by marking Draft unavailable.
- `--turbo`: unavailable in V8.1.
- `--niji`: a different model family, not V8.1.

## Official sources

- Version and compatibility: https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version
- Draft and Conversational Modes: https://docs.midjourney.com/hc/en-us/articles/35577175650957-Draft-Conversational-Modes
- Parameter list and placement: https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List
- Raw: https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw
- Stylize: https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize
- Chaos: https://docs.midjourney.com/hc/en-us/articles/32099348346765-Chaos-Variety
- Aspect ratio: https://docs.midjourney.com/hc/en-us/articles/31894244298125-Aspect-Ratio
- Multi-prompts: https://docs.midjourney.com/hc/en-us/articles/32658968492557-Multi-Prompts-Weights
