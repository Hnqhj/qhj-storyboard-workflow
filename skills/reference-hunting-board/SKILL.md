---
name: reference-hunting-board
description: "参考搜索板：为 AI 视频与图像创作搭建参考检索板。触发：参考、找参考、参考板、moodboard、灵感板、搜图、搜视频、镜头参考、动作参考、武器参考、电影参考、广告参考、摄影参考、美术参考、分析参考图、提炼参考、reference hunting。 Build reference-search boards for AI video/image creation. Proactively use when the user needs visual references, motion references, film/frame references, martial arts examples, weapon-use examples, moodboards, search keywords, reference directions, source-hunting plans, or says they lack examples to look at. Trigger on 参考, 找参考, 参考板, moodboard, 灵感板, 搜图, 搜视频, 镜头参考, 动作参考, 武器参考, 电影参考, 广告参考, 摄影参考, 美术参考, 分析参考图, 提炼参考, reference hunting, visual research."
---

# Reference Hunting Board

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this skill to turn a vague visual goal into a practical reference board plan. The output should help the user know what to search, what to compare, what to extract, and how to translate references into AI-video prompt language.

If the user asks to actually search the web or find current references, browse and cite sources. If they only need directions, provide search terms and extraction criteria without browsing.

When `$creative-research-first` is active, this skill supplies the visual/motion/reference lane. Return mechanisms and prompt translations, not a standalone inspiration dump.

For video work, references must solve shot problems, not just provide taste. Classify each reference by the problem it answers: shot function, spatial path, scale, screen direction, speed sensation, blocking, cut rhythm, material/light behavior, or world design.

## Universal Reference Atlas Mode

When the user asks for broad, reusable, general-purpose, or "大批量通用" references, do not narrow the search to the current project. Build a reference atlas first, then derive project-specific subsets later.

Cover multiple lanes by default:

- action and movement systems: martial arts, dance, stunt, sport, parkour, weapon systems, creature/vehicle motion;
- shot and camera grammar: staging, lens/height/scale, axis, action-camera coupling, coverage, geography, editing;
- aesthetic systems: cinema, animation, CG/lookdev, illustration, graphic design, photography, fashion/product/architecture, experimental media;
- transitions and VFX: action match, occlusion, whip, graphic match, impact frame, light wipe, reflection, sound bridge, speed ramp, practical debris, compositing style;
- material and light: surface hierarchy, palette ownership, contrast, roughness/specular behavior, smoke/water/glass/metal/skin/fabric;
- sound and music: foley source, impact transient, resonance, silence, rhythm, cue function, mix hierarchy;
- design/world lanes: character silhouettes, costumes, weapons, vehicles, monsters, architecture, props, UI/typography if relevant.

For each lane, collect anchors as:

```text
anchor -> usable mechanism -> prompt control -> failure risk -> good for / avoid for
```

The atlas should include adjacent directions that may not fit the current project. Mark them as future-use lanes instead of discarding them.

For action tension, fight choreography, weapon/camera references, manga-style impact, AI action-video 拉片, or broad “动作/审美/转场参考”, read `references/action-tension-reference-atlas.md` first, then browse only to fill gaps or refresh specific examples. Use the atlas categories to avoid overfitting references to one current prompt.

For web/X/GitHub/article/tool links, or when the user says "挨个去看", "自己去看", "把这些链接都看了", or "常用开源工具都整", read `references/web-reference-ingestion.md`. Prefer background capture through public APIs, static extraction, and headless Playwright; do not foreground or disturb the user's interactive browser unless explicitly requested. Use `scripts/capture_web_reference.py` for safe public URL capture into the current project.

## Full Reference Breakdown / 拉片 Rule

When the user provides external video links, local videos, screenshots, or says "拉片", "整个都看", "先看这个", or "这几个之前做得不错", treat the reference as a whole work before mining it for the current prompt.

- If the whole reference is accessible, inspect the complete piece or enough sampled intervals to cover beginning, escalation, peak, release, and ending. If it is not accessible, state the access limit and use any available user notes, screenshots, local files, or visible segments without pretending to have watched it.
- Classify the reference across the full grammar, not only the immediately transferable piece: aesthetic system, production design, character/prop design, camera grammar, action grammar, editing rhythm, transition devices, effects language, sound-image relation, prompt structure, and failure risks.
- Extract mechanisms, not fan labels: what the frame does, how the cut works, how bodies create camera opportunities, how effects inherit action vectors, how the environment proves force, and what prompt wording likely produced it.
- Preserve the user's successful personal references as reusable cases. A reference from the user's own work should be treated as project evidence, not as a random inspiration clip.
- Only after the whole-work breakdown should you decide what belongs in the current project, what belongs in a shared skill/case card, and what should be avoided for this specific attempt.

Output shape for a full 拉片:

```text
Reference identity / source:
Whole-piece impression:
Beat map:
Aesthetic system:
Camera and shot grammar:
Action or motion grammar:
Transitions / VFX / sound:
Prompt-transfer mechanisms:
Non-transferable traits:
Risks if copied blindly:
Reusable skill/case lesson:
```

## Workflow

1. Inventory the user's supplied images/videos, current project files, and already-known references. Extract what they solve before searching externally.
2. Identify the unresolved reference need: camera, action, weapon, character, costume, material, lighting, editing, worldbuilding, product, or mood.
3. If the user supplied URLs, ingest the sources first: capture text, media links, raw evidence, and source metadata into the current project before summarizing.
4. Generate multilingual search terms: Chinese, English, and field-specific terms.
5. Split references into buckets:
   - shot grammar reference
   - must-have reference
   - style reference
   - motion reference
   - material/detail reference
   - avoid reference
6. Explain what to extract from each bucket, not just what to collect.
7. Translate the extracted reference traits into prompt-ready language: function, framing, camera height, lens feel, motion vector, screen direction, cut reason, material/light cue, and failure risk.
8. If the output will feed an AI-video prompt, hand off to `$ai-video-prompt-director` or `$jimeng-sd2-prompting`.

Read `references/hunting-playbook.md` for detailed query patterns and board templates.

## Output Shape

```text
参考目标：

参考板分区：
1. 镜头语法参考：
   搜索词：
   解决什么镜头问题：
   看什么：
   提炼成提示词：

2. 必找参考：
   搜索词：
   看什么：
   提炼成提示词：

3. 动作/运动参考：
...

避免参考：
...

最终可用提示词素材：
...
```

## Guardrails

- Do not dump a generic list of famous films or artists. Tie every reference to a specific shot problem.
- Do not browse for a replacement when the user's supplied artifact or local project state already answers the question.
- Do not build a board that only says "style/mood". Include at least one shot-grammar or motion reference when the deliverable is a video prompt.
- Do not only extract current-project-relevant fragments when the user asks to watch or break down the whole reference. Cover the whole-work grammar first, then transfer selectively.
- When using named creators or films, extract visual mechanics rather than asking for direct imitation.
- For actual web searches, prefer primary/credible pages and provide links. Do not claim references were checked if they were only inferred.
- Do not depend on references that require exact copyrighted characters or scenes unless the user explicitly asks and has a legitimate context.
