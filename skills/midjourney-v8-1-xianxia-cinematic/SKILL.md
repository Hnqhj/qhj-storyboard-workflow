---
name: midjourney-v8-1-xianxia-cinematic
description: Use when the user asks for Midjourney V8.1 prompts in a dreamy photorealistic Chinese xianxia, guofeng fantasy, or live-action oriental cinematic film-still aesthetic.
---

# Create Xianxia Cinematic Prompts

1. Read `references/style-guide.md` and `references/v8-1-parameters.md` before composing.
2. Parse the idea into subject, action, environment, composition, light, palette, materials, mood, and intended aspect ratio.
3. Convert the idea into four to eight English search terms. Resolve the script from the skill root containing this `SKILL.md`; for example: `powershell -NoProfile -ExecutionPolicy Bypass -File "<skill-root>\scripts\search-prompts.ps1" -Query "xianxia hanfu silk cinematic" -Limit 6`.
4. Use at most three relevant records as structural inspiration. Remove people, brands, dates, placeholders, required reference images, and non-Midjourney syntax that the user did not supply.
5. Apply all three style pillars to every prompt: a photorealistic film still, Chinese xianxia visual language, and dreamy natural light.
6. Keep the subject constant across three complete English prompts. Vary composition, lighting, motion, or environment.
7. Use the user's aspect ratio or default to `--ar 16:9`. Use the fewest parameters needed and end every prompt with `--v 8.1`.
8. Preserve user-supplied image URLs, seeds, and Style Reference values exactly. Never invent them.

Always return exactly this structure with exactly three prompt code blocks. For ordinary requests, do not add any analysis, tutorial, or other text before `### 主提示词`. The only permitted exceptions are the one-sentence notices defined below:

### 主提示词

```text
<complete English prompt>
```

### 变体 1

```text
<complete English prompt>
```

### 变体 2

```text
<complete English prompt>
```

If the user explicitly requests a conflicting visual style, place exactly one concise sentence in the user's language before `### 主提示词`, stating that this skill is fixed to the approved xianxia cinematic style and will not mix the conflicting style. Then still output all three headings; each must be followed by one `text` code block containing a complete English prompt that preserves the subject, all three style pillars, and the parameter rules above.

If the user explicitly requests visible text in the image, place exactly one concise typography reminder in the user's language before `### 主提示词`, noting that exact lettering and layout may vary. If this and a conflicting style request both apply, combine both notices into exactly one sentence. Do not add either notice for ordinary requests.
