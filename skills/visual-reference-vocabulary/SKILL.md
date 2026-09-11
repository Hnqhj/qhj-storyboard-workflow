---
name: visual-reference-vocabulary
description: "Proactively discover, suggest, preserve, and minimally clarify high-density visual reference anchors for AI image/video prompting, including directors, films, studios, cinematographers, photographers, animators, composition, camera, lighting, and editing terms. Use when the user knows only part of the relevant visual vocabulary or wants better camera movement, tension, anime impact, cinematic feeling, commercial polish, or visual name anchors. Trigger on 运镜, 构图, 镜头感, 张力, 压迫感, 史诗感, 高级感, 电影感, 动画感, 视觉参考词, 导演镜头, 摄影术语, Spielberg shot, Kubrick, Hitchcock, Obari pose, 大张正己, 大张一刀."
---

# Visual Reference Vocabulary

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this skill as the visual-language specialist under `$creative-anchor-director`. The user may know only some useful visual names. Preserve those anchors, identify which visual functions remain unnamed, research or retrieve suitable candidates, and add the smallest compatible set.

Default to practical AI-video use: terms must help a model generate a stronger shot, not just sound educated.

This skill provides vocabulary, not the whole directing plan. For video prompts, combine with `$cinematic-audiovisual-language` before final output so references become shot function, spatial path, axis/screen direction, and cut logic instead of a list of cool names.

## Workflow

1. Inventory the user's existing anchors and state what each already controls.
2. Run a visual anchor-gap audit. Check only relevant lanes:
   - medium/material/optical finish;
   - production design, palette, and composition;
   - camera and action coverage;
   - animation timing, posing, effects, and editing;
   Hand movement, weapon, partner, music, and sound gaps back to `$creative-anchor-director` for specialist routing.
3. Proactively find candidates for material gaps:
   - use internal reference maps for established terms;
   - use `$creative-research-first` when the domain is unfamiliar, a claim is uncertain, or a better real-world practitioner/reference may exist;
   - verify what the name actually contributes before recommending it.
4. Select the smallest compatible anchor set:
   - usually 2-4 major style anchors for the whole clip;
   - movement/weapon bases are counted separately when they belong to specific performers;
   - do not add a name when the user's existing anchor already covers that function.
5. For each selected term, give:
   - **Name**: Chinese + English if useful.
   - **Role**: the one layer it controls.
   - **Why it fits**: a short connection to the current brief.
   - **Prompt form**: preserve the name, optionally followed by one short disambiguator.
   - **Avoid**: likely AI failure mode.
6. End with a merged anchor line or prompt block that can be inserted directly.
7. If the user is making a video prompt, combine with `$cinematic-audiovisual-language` before final packaging. If they are using 即梦 SD2 / Seedance, combine with `$jimeng-sd2-prompting`. If material realism matters, combine with `$ai-material-realism`.

For cross-domain anchor auditing and compatibility, use `$creative-anchor-director`. Read `references/visual-reference-map.md` when selecting specific visual vocabulary.

When the user asks for director, camera, montage, or shot-style anchors, or mentions names such as Hitchcock, Zack Snyder, Hideaki Anno, Kubrick, Kurosawa, Obari, Trigger, or 大张, read `references/camera-director-anchor-atlas.md`. Preserve useful names in anchor-first form (`Name 式 + function`) and assign each anchor a clear job such as suspense geometry, heroic speed-ramp, graphic montage, impact pose, subjective POV, or readable body-contact proof.

## Output Shape

Use this compact format:

```text
你要的感觉：

你已有的锚点：
我补充的锚点：
1. 名词 / English
   负责：
   为什么适合：
   提示词写法：
   避坑：

可直接粘贴：
...
```

For prompt rewrites, output:

```text
视觉参考选择：
...

改写后的提示词：
...

负面限制：
...
```

## Guardrails

- Keep useful named references in the final prompt. Do not automatically replace a director, studio, film, photographer, animation school, or shot name with a long descriptive substitute.
- Use anchor-first syntax: `name + one short purpose or disambiguation`. Expand further only when anchors conflict or a known model failure requires it.
- Do not wait for the user to supply every useful name. Proactively supplement missing anchor lanes when a well-matched term would compress the prompt or improve creative direction.
- Do not force one named reference into every lane. An anchor is valuable only if it changes a decision.
- Do not let named references replace audiovisual grammar. A reference term must solve a shot problem: function, scale, pressure, route, rhythm, or information reveal.
- Prefer 2-4 strong references over a long name salad.
- If a named reference is a living artist/director/photographer, use it as optional shorthand and provide descriptive alternatives. Do not depend on exact imitation.
- Avoid copyrighted characters, exact franchise scenes, or living-person likeness unless the user explicitly provides a legitimate context.
- If uncertain about a niche term, mark it with `?` and offer a safer descriptive phrase.
