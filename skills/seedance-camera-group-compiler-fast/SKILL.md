---
name: seedance-camera-group-compiler-fast
description: 快速档 Seedance 编译器，仅在调用方给定 fast 档时使用。把已批准的 ShotLedger 与 CameraGroupPlan 转成一份六段式中文提示词，含显式镜头块。不用于续写、FLF2V、V2V/R2V、全参考、打斗、VFX、变身、重试。 Lightweight Seedance-compatible compiler used only when the received processing depth is fast, for a low-risk T2V or simple I2V camera group. Convert an approved ShotLedger and CameraGroupPlan into one detailed six-part Chinese prompt with explicit shot blocks; render T micro-beats only for the high profile. Do not use for continuation, FLF2V, V2V/R2V, all-reference workflows, API/provider questions, fights, VFX, transformations, retries, or uncertain platform capabilities.
---

# Seedance Camera Group Compiler Fast

Compile one approved low-risk camera group. Do not redesign story, shot order,
timing, continuity, performance, or asset roles.

## Mandatory Runtime Compile

**Console access (MCP removed 2026-09-23).** The `skill_console_*` MCP tools are
gone; use the console CLI instead. Console root =
`G:\工作\vibecoding\director-skill-console` (or `$SKILL_CONSOLE_ROOT` if set);
invoke as `node "$CONSOLE/src/cli.js" <subcommand> ...`. Pass prompts via a file
or `-` (stdin), never inline.

Immediately before writing the final block, run
`prompt-context --thread <threadId> --input '<routing-json>'` with the approved
inputs. Use its current `prompt_compilation_profile` for every shot. Then run
`prompt-compile --thread <threadId> --compiler seedance-camera-group-compiler-fast
--prompt-file <path|-> --input '<routing-json>'` exactly once with the completed
six-part block. Use the returned `promptText` verbatim as the generation prompt
and retain its `generationSettings` and `compilationReceipt` (persist it on the
matching `PlatformPromptSet` unit). Do not use a cached profile or emit the draft
if either runtime call fails.

Profile rules are strict: `low` means simple shot descriptions with no duration
limit and no `T=` lines; `medium` means simple shot descriptions with duration
limits and no `T=` lines; `high` means complex shot descriptions with duration
limits and contiguous `T=` micro-beats. All profiles retain the six sections,
complete structure, and exact dialogue.

An identical script fragment in a later user turn still starts a fresh compile
and rereads settings. If the user explicitly requests multiple versions, use
the same approved group data with distinct `variant_id` values and compile each
requested version once; do not treat the second requested variant as an
accidental duplicate.

## Inputs

Use only:

```text
CameraGroupPlan
ShotLedger rows belonging to that group
current identity/location/prop locks
exact platform handles
audio authority
```

Do not consume the whole screenplay, all upstream analysis, or specialist prose
once these structured inputs exist.

## Output

Emit one standalone Chinese block in this order:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
  镜头01｜起始-结束s｜完整局部镜头设置
  T=起始-结束s：单一可观察变化（仅 high profile 输出）
声音
正向稳定约束
```

Repeat each shot's concrete position, height, angle, lens/perspective,
focus/depth of field, light behavior, movement path, action/performance,
verbatim dialogue, cut trigger, endpoint, and handoff. Preserve exact `@`
handles. Use only dialogue/voice-over and source-coupled dry foley unless the
active authority explicitly permits other audio.

## Boundaries

- Support simple T2V and simple I2V natural-language compilation only.
- Escalate to `seedance-20` for continuation, first/last frame, V2V/R2V,
  all-reference, provider/API/capability claims, safety/IP repair, or retry.
- Do not browse, research, inspect provider documentation, or load Seedance
  subskills.
- Do not create compact, abbreviated, alternate, or second prompt versions.
- Return a field-level error instead of silently changing an approved plan.
