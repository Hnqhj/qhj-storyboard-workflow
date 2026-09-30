---
name: full-prompt-delivery
description: 提示词可复制性校验或独立通用提示词重生成，用于剧本转镜头组流程之外。在镜头组工作中，仅在 narrative-camera-groups 之后被明确要求时作为完整性校验使用；绝不创作、重编译或重写已编译的镜头组提示词。 Validate copyability or regenerate generic standalone image/video prompts outside the script-camera-group pipeline. In camera-group work, use only as an explicitly requested completeness validator after narrative-camera-groups; never author, recompile, or rewrite an already compiled group prompt. Not part of fast, standard, or full camera-group ExecutionPlans.
---

# Full Prompt Delivery

For generic prompts outside camera-group production, deliver one complete prompt
that can be copied directly. For a camera-group `PlatformPromptSet`, validate
only and leave the existing prompt unchanged when it passes.

For substantial AI-video work, consume the route and state selected by
`$ai-video-production-governance`. This skill owns completeness and copyability;
it does not replace the director, storyboard, continuity, or platform compiler.

## Core Rule

- Outside camera-group production, treat a prompt request or revision as a full
  regenerated prompt.
- Merge the newest request with all still-valid constraints from the conversation: subject identity, reference-image roles, composition, camera, pose, direction, lighting, materials, motion, aspect ratio, text, and avoid rules.
- Never make the user splice a new paragraph into an older prompt. Do not return only a delta, replacement sentence, or "keep the rest unchanged" as the main deliverable.
- If a small generic-prompt change is requested, rewrite that prompt and change
  only the requested variable unless another constraint must be reconciled.
- When `narrative-camera-groups` has produced a camera-group prompt, do not
  rewrite it. Return pass/fail and a named field patch to the selected compiler.
  The selected compiler owns the only permitted final compile pass.

For Liu's真人短剧 Seedance work, read `../director-workflow-70/references/liu-short-drama-contract.md` before packaging. Its duration, audio, dialogue, framing, @handle, and standalone-group rules override generic prompt defaults.

## Reference Roles

When images are supplied, state their roles inside the prompt or immediately before it:

- layout/camera reference: controls framing, scale, axis, blocking, and spatial relation only;
- identity/appearance reference: controls face, hair, costume, prop, or material only;
- style reference: controls palette, medium, lighting, or finish only.

Prevent one reference from silently overriding another. Preserve the user's explicit instruction over inferred reference details.

## Platform Character Handles

When the user has uploaded five-view assets for the cast, write every distinct character mention inside each copy-ready prompt with its exact `@` handle, for example `@苏凌月`, `@苏建国`, `@刘大龙`, `@黑衣小弟甲`, or `@黑衣小弟乙`. Apply this consistently across identity locks, action beats, dialogue speaker labels, sound direction, and positive stability locks. Do not merge, invent, translate, or rename handles. Keep uploaded reference files in the exact `@图片名` / `@视频名` / `@音频名` format supplied by the user, with a parenthesized role on first mention; `@角色名` is a separate character asset call. `{{Image N}}` / `{{Video N}}` / `{{Audio N}}` may remain only as backend mapping outside the final prompt. Human-readable planning tables may use plain names, but model-facing prompt blocks must use exact `@` handles.

## Narrative Video Delivery Unit

For Liu's live-action short-drama complete-script + reference requests, follow
`../director-workflow-70/references/short-drama-director-stack.md` upstream: run
the reference-sufficiency check and three-concept gate before formal prompt
delivery unless direct execution is explicit. For a local fragment, inspect only
the fragment's active state, capacity, continuity, and required assets. This
skill checks completeness and copyability; it does not bypass the director brain
or replace the camera-group owner.

For Liu's default video audio, require character dialogue/voice-over and source-coupled dry foley/SFX in each prompt. Add music, score, BGM, ambience beds, or mood effects only when Liu or the authoritative script explicitly requires them.

For every script-derived input, deliver **narrative camera groups**, not one
standalone generation prompt for every individual shot. A complete script uses
global grouping. A local fragment or single continuation beat uses one or more
scoped local groups. Both routes require a human-readable shot table plus one
detailed six-part prompt per group.

Do not proactively create or offer storyboard reference images. Enter that
branch only when the user explicitly asks for storyboard images or an existing
project preference requires them.

When `$narrative-camera-groups` is active, it is the final packaging owner. This skill checks completeness only. Do not replace its flexible 14-28 second grouping, planning-table separation, per-shot timing, or prompt-per-group format with this skill's generic template.

A local-fragment route skips only unrelated whole-script planning. It still
uses `$narrative-camera-groups`, keeps planning notes outside the paste target,
and receives the complete camera-group package.

- A camera group may contain several consecutive shots, cuts, or transitions that form one coherent dramatic unit.
- For Liu's short-drama workflow, use a flexible 14-28 second range and never exceed 30 seconds. Choose the shortest complete group that preserves natural dialogue, readable action causality, and a stable handoff; split at a natural story turn, completed action, location change, or stable end state.
- Do not pad a group to reach a target duration. Do not split a continuous dialogue line or one necessary cause-effect action; split dense material at the nearest natural handoff.
- Each group must be independently usable: repeat all relevant identity, wardrobe, location, lighting, prop, blocking, and ending-state anchors. Never require the user to splice together earlier prompt fragments.
- Give a timed shot table for human understanding only, outside the copy-ready prompt. Then provide one complete generation prompt for the whole group. Inside that prompt, restate every shot as concrete model-facing prose with its time window, shot size, local camera setup/movement, visible action/dialogue, and continuity handoff. Do not paste the Markdown table or refer the model to it.
- For every reference image, state its role in that specific group: identity/appearance, setting/layout, action/motion, camera/composition, or style/material. State `None` when no reference image is used.

Use this fixed Chinese delivery shape for every narrative camera group:

```text
镜头组 01｜总时长：约 XX 秒｜剧情功能：……
开场状态：……
结束状态：……

参考素材与职责：
- @图片名/@视频名/@音频名：具体职责；没有外部参考时写“无”（编号映射仅后台记录）

理解用镜头表（仅供人查看，不进入提示词）：
| 镜头 | 时间码/时长 | 景别 | 机位与运动 | 画面与台词 | 转场/连续性 |

完整可复制提示词（独立代码块）：
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍：逐镜以完整自然语言重写时长、景别、机位、运动、画面、台词与承接
声音
正向稳定约束
```

Keep the headings and field order stable. Repeat the reference map, planning table, and complete self-contained prompt for every group. Do not replace the complete prompt with a template, a partial revision, a table reference, or instructions to retain text from a previous response.

Apply the same six-part structure to local-fragment groups. Do not permit empty
headings or terse placeholders. Each section must contain current-group control
information, and `事件节拍` must restate every shot with shot number, timecode
and duration, shot size, camera position/height/angle, focal length or
perspective, depth of field and focus, lighting direction/quality/color
temperature/shadows, camera path, action/performance, verbatim authoritative
dialogue, cut trigger, ending state, and handoff. Reject `同上`, `沿用`,
`参考镜头表`, `保持不变`, or equivalent references in place of details.

## Complete Prompt Checklist

Include the fields that matter to the task in this order:

1. target tool or use case when relevant;
2. subject identity, count, pose, action, and state;
3. setting and spatial relationship;
4. camera position, shot size, orientation, screen direction, and composition;
5. lighting, palette, atmosphere, and material response;
6. motion, speed, blur, or temporal behavior when relevant;
7. output format, aspect ratio, transparency, or exact text when requested;
8. a compact targeted avoid block.

Do not add unsupported facts just to fill the checklist. Keep unknown or unproved details open.

## Text And Transparency

- For exact text, quote every required string verbatim and require no extra text. Warn briefly that generated typography may need post-layout when accuracy matters.
- For transparent assets, state the desired alpha output. If the selected tool lacks native transparency, give the tool-appropriate chroma-key fallback as a short delivery note rather than pretending the prompt guarantees alpha.

## Output Format

Use this default structure:

```text
完整提示词：
[one complete copy-ready prompt]

避免：
[short targeted avoid block]
```

For multiple variants, provide a complete prompt for each variant. For narrative
video, treat chronological splits as camera groups rather than variants. For
Liu's short-drama camera-group workflow, compact, compressed, abbreviated, or
partial prompt modes are not allowed: repeat every required field in every group
so each block is independently copyable and generatable. A local fragment may
have fewer groups because its scope is smaller, but its six-part prompt may not
be abbreviated or omit required controls. A short note about what changed may follow
the prompts, but never replaces them.

`事件节拍`必须重写每个镜头的全部执行字段，并在每个镜头窗口下嵌套
连续的 `T=起始-结束s` 微节拍。T 使用镜头组时间轴，完整覆盖该镜头；
每个 T 段只描述一个有明确边界的动作、表演、运镜、声音同步点或状态
变化。不能用“持续”“保持”或无时间范围的长句替代 T 节拍。
镜头之间必须用明确的 `镜头01`、`镜头02` 等边界分块；不能把多个镜头
压成一段没有镜头编号的连续事件文字。

## Quality Gate

Before responding, verify that:

- the prompt works without the user consulting an earlier message;
- no approved constraint was dropped or contradicted;
- reference images have explicit ownership;
  - every script-derived input uses complete camera-group prompts in Liu's 14-28 second range and never longer than 30 seconds unless an explicit contract overrides it, with a reference map, a human-only timed shot table, and one detailed six-part prompt per group that restates every shot in prose, dialogue, pure foley, and targeted stability constraints;
- the main subject and composition are not buried under style adjectives;
- motion blur and effects have a direction and readability target;
- negative constraints are concise and do not reintroduce unrelated old concepts.
