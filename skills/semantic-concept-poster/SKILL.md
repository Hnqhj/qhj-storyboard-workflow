---
name: semantic-concept-poster
description: 高概念封面与海报提示词：从词、短语、短句、字母组、角色图、物件图、风格参考或版式参考出发，把含义与参考转成极简语义视觉隐喻。触发：封面、概念海报、文字海报、字效海报、词语海报、语义隐喻、高级封面、小红书封面、角色封面、杂志封面。 Create high-concept cover/poster prompts from a word, phrase, short sentence, letter group, character image, object image, style reference, or layout reference by turning meaning and references into a minimal semantic visual metaphor. Use when the user asks for 封面, 概念海报, 文字海报, 字效海报, 词语海报, 语义隐喻, 高级封面, 小红书封面, 角色封面, 动漫时尚封面, 杂志封面, 参考图封面, 视觉隐喻, poster prompt, typography poster, fashion magazine cover, or wants text plus images transformed into a strong graphic art cover instead of a literal illustration.
---

# Semantic Concept Poster

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Purpose

Turn a word, character, phrase, short sentence, letter group, or reference image into a high-concept cover/poster prompt where the text remains the central visual subject and the image becomes a semantic or editorial carrier.

The result must not be a normal illustration or a simple enlarged word pasted onto a background. It must feel like a complete visual sentence: text + image + layout all express the meaning together.

## Reference Routing

Read the smallest useful reference set:

- `references/poster-principles.md`: always read for text-first semantic concept posters.
- `references/reference-image-mode.md`: read when the user provides or mentions a character, object, scene, style, or layout reference image.
- `references/magazine-character-cover.md`: read when the user wants a character cover, anime fashion cover, luxury editorial cover, futuristic magazine cover, or the "NEO VANGUARD" style.

## Input Handling

Accept compact user input such as:

```text
核心文字 / 单词 / 词组 / 字母：失重
文字语言：中文
可选补充语境：亲密关系里的不安全感
可选情绪倾向：孤独、悬浮、冷
可选禁用元素：不要宇航员
```

For image-assisted covers, accept:

```text
核心文字：
参考图类型：角色 / 物体 / 风格 / 版式 / 场景
需要保留：
可改变：
情绪倾向：
禁用元素：
```

If the user gives only one word, infer language, context, and emotion. Ask at most one clarifying question only when the word is ambiguous enough that the cover direction would change materially.

## Workflow

1. For a substantive new concept, use `$creative-research-first` to research relevant cultural symbolism, editorial/print references, object behavior, current platform constraints, or unfamiliar subject matter before choosing the metaphor. Skip for tiny rewrites or when the supplied references fully define the task.

2. Understand the text first:
   - literal meaning
   - emotional temperature
   - symbolic/cultural associations
   - hidden tension, contrast, paradox, or social/psychological depth
   - best visual logic: object relation, human relation, spatial relation, scale contrast, conflict, order, absurdity, poetry, etc.

3. Choose one strong visual metaphor:
   - Prefer one precise, memorable image over many decorative elements.
   - Use concrete carriers for abstract ideas.
   - For concrete words, avoid literal depiction; add relationship, scale, contrast, absence, tension, or atmosphere.

4. Build the poster:
   - Make the user text the main title and visual skeleton.
   - Let image elements interact with the letterforms/characters: standing before them, embedded in them, cutting them, hiding behind them, using their negative space, or creating narrative around them.
   - Keep the design minimal, clean, strong, and poster-like.
   - Add a compact material/print finish layer: paper stock, ink behavior, grain, screenprint/lithograph texture, controlled wear, light direction, contact shadows, and surface response. Keep it clean and editorial, not dirty or noisy.

5. Output copy-ready prompt:
   - Brief semantic judgment.
   - One concept direction.
   - Full image-generation prompt.
   - Material/print finish embedded in the prompt.
   - Negative prompt.
   - Optional small caption if useful.

6. When references are provided:
   - Inspect or infer what the reference contributes.
   - Preserve only what the user asks to preserve.
   - Make the reference serve the title/meaning, not replace it.
   - Avoid poster designs where the image is merely pasted behind text.

## Reference Role Rules

When the user provides images, assign each one a role before writing the prompt:

- **identity reference**: preserve face, hair, outfit, silhouette, or character design.
- **style reference**: preserve rendering, texture, lighting, color mood, or editorial finish.
- **layout reference**: preserve hierarchy, typography density, cover grid, margins, or magazine language.
- **object/prop reference**: preserve shape, material, mechanism, brandless design details.
- **scene reference**: preserve environment logic, palette, depth, or atmosphere.

Do not let a layout reference overwrite identity, and do not let an identity reference force the same background. If a reference contains text, treat it as layout/style unless the user explicitly asks to reproduce the text.

For character covers, make the character and title form one editorial idea: title interacts with silhouette, pose, clothing, prop, negative space, panel, or graphic system.

For final cover prompts, include physical print/design realism by default. Avoid flat pasted typography, plastic skin, generic glossy render, fake magazine text clutter, or a background image that ignores the title.

## Output Rules

Default output in Chinese. Use English only when the target platform or user asks for it.

Do not over-explain. Keep the semantic analysis short and useful. The final image prompt is the main deliverable.

If the user explicitly asks to generate the image, use the final prompt as the image generation prompt after applying this skill.
