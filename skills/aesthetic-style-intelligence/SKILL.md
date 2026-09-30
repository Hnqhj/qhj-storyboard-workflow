---
name: aesthetic-style-intelligence
description: 审美风格情报：追踪、评估并蒸馏当前与历史上的审美风格信号，转成可复用的美术指导情报。触发：需要最新的视觉风格研究、跨媒介审美趋势侦察、风格锚点选择、高级而非通用的视觉方向。 Track, evaluate, and distill current and historical aesthetic style signals into reusable art-direction intelligence. Use when Codex needs up-to-date visual style research, cross-medium aesthetic trend scouting, style-anchor selection, premium/non-generic visual direction, or a companion layer for skills such as visual-style-aesthetic-direction, creative-anchor-director, visual-reference-vocabulary, production-design-worldbuilding, ai-material-realism, cinematic-audiovisual-language, and AI image/video prompt workflows.
---

# Aesthetic Style Intelligence

## Core Intent

Use this skill as a research and memory layer for aesthetic style, not as a final prompt writer.

Convert web research and inspected examples into compact, reusable controls:

```text
signal -> evidence -> visual rule -> useful companion skill -> prompt/control phrase -> boundary -> status
```

Favor transferable mechanisms over taste labels. A style signal is useful only if it changes a concrete art-direction decision: palette ownership, material response, framing, typography, motion language, lighting, surface texture, composition hierarchy, cultural/design lineage, or negative constraints.

## Companion Routing

Use this skill before or alongside:

- `visual-style-aesthetic-direction`: turn selected signals into a coherent style stack.
- `creative-anchor-director`: discover and assign high-density named references.
- `visual-reference-vocabulary`: expand missing visual vocabulary and reference anchors.
- `production-design-worldbuilding`: connect style to world rules, material culture, costumes, vehicles, props, and architecture.
- `ai-material-realism`: convert style into believable light, optics, texture, and render vocabulary.
- `cinematic-audiovisual-language`: bind style to shot grammar, blocking, editing, and sound-image rhythm.
- `jimeng-sd2-prompting` or platform-specific prompt skills: package the approved style controls into model-ready prompts.

Do not let this skill override domain skills. It supplies evidence-backed style intelligence; the companion skill decides final execution.

## Distilled Control Library

For normal use, read `references/current-style-controls.md` first. It contains the compact reusable style controls distilled from the daily ledger.

Use the chronological ledger only when you need evidence trails, status history, rejected signals, or promotion/deprecation decisions.

When applying a distilled control:

1. Select one primary control family.
2. Add at most 1-3 secondary controls from different layers.
3. Preserve the control's negative boundary.
4. Route execution to the listed companion skill.
5. Do not mix controls that claim the same layer unless the user explicitly asks for a hybrid.

## Research Workflow

1. Define the task lane: image, video, film, animation, 3D/CG, graphic design, fashion, product, architecture, UI, editorial, music video, game cinematic, or mixed media.
2. Browse current and historical sources when freshness matters. Compare multiple lanes instead of copying one viral example.
3. Record sources as evidence tiers:
   - primary: creator, studio, gallery, publisher, festival, platform, official process note, direct portfolio.
   - strong secondary: reputable criticism, interview, museum/editorial feature, trade publication.
   - weak secondary: social aggregation, unverified trend thread, moodboard repost.
4. Classify each signal:
   - `candidate`: interesting, single-source or untested.
   - `tracked`: repeated across credible sources or useful in one successful task.
   - `stable`: repeated, bounded, and portable across at least two contexts.
   - `deprecated`: overused, misleading, visually unstable, or no longer useful.
5. Translate retained signals into controls:
   - visible rule
   - layer controlled
   - companion skill to invoke
   - prompt phrase
   - negative boundary
   - misuse risk
6. Keep the final recommendation small: one primary style system plus at most 1-3 scoped secondary anchors.

## Reference Routing

Read `references/style-intelligence-ledger.md` when the user asks for current style research, wants a non-generic look, asks for aesthetic iteration, or when another skill needs style anchors.

Read `references/current-style-controls.md` before the ledger when the user needs an actionable style direction, prompt controls, or companion-skill handoff.

Update the ledger only when the research produces reusable knowledge. Do not add every source. Add entries that have a clear status, boundary, and companion-skill use.

## Update Format

When adding or revising ledger entries, use this shape:

```text
### YYYY-MM-DD - signal name
Status:
Lane:
Evidence:
Observed rule:
Controls:
Companion skills:
Prompt/control phrase:
Negative boundary:
Misuse risk:
Next validation:
```

## Quality Gate

Before using or promoting a style signal, check:

- Is the signal more specific than a generic adjective like premium, cinematic, edgy, dreamy, cyberpunk, or elegant?
- Does it name a visible rule, not just a vibe?
- Are palette, material, texture, light, composition, and motion responsibilities separated?
- Is there a clear boundary for what the reference must not control?
- Would this still help if the named reference were removed?
- Does the signal support the user's medium and model constraints?
- Is the output cleaner, more coherent, or more distinctive because of this signal?

## Output Shape

For research rounds:

```text
Route:
Sources checked:
Signals kept:
Signals rejected:
Ledger updates:
Companion skill handoff:
Next scan:
```

For a user-facing style recommendation:

```text
Style direction:
Primary system:
Scoped anchors:
Visible rules:
Companion skills:
Prompt-ready controls:
Negative boundaries:
```
