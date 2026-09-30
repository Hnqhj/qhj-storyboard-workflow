---
name: script-camera-group-router
description: 拆分镜、拆镜头组、剧本转分镜提示词、按镜头组生成 Seedance 提示词。按调用方给定的 fast/standard/full 深度执行，不自行判定；出执行方案等确认再加载下游。不用于纯分析、成片诊断、纯生图。 Lightweight first and only implicit entry for turning a complete script, script fragment, dialogue block, or continuation beat into AI-video camera-group prompts. Use when the user asks to 拆分镜、拆镜头组、剧本转分镜提示词、按镜头组生成 Seedance 提示词, or supplies script text and expects timed shot tables plus prompts. Read the fast/standard/full processing depth supplied by the caller; never decide it here. Do not use for analysis-only requests, generated-video diagnosis, image-only prompts, or storyboard-table-only delivery.
---

# Script Camera Group Router

Read the execution depth before loading any heavy director, storyboard, platform,
or preflight Skill. This is the single implicit front door for
script-to-camera-group prompt work.

**This router reads the depth; it does not decide it.** The judgement belongs to
the decision layer — **镜语**, the 镜头组架构师 expert run from `G:\工作\分镜` — and
reaches this layer through the console task-context (`prompt-context`); an
explicit user instruction overrides. It is recorded in `TaskEnvelope`:

```text
processing_depth = fast | standard | full -> how deep the backstage work goes (read from caller)
```

There is **no genre axis**. A scene's genre reaches this layer only as explicit
signals (`fight`, `dialogue_intensive`, `emotion_required`, `performance_required`,
...), which the decision layer already weighed when it judged the depth. This
layer never derives, records, or re-tiers a genre label of its own.

Never infer, judge, or re-tier the depth from the script. If a tier is absent,
use `standard`, label it an assumption in the execution proposal, and continue.
If the received tier cannot hold the material, stop and return a named blocker to
the caller instead of upgrading or downgrading.

## Invariants

### Route control

Users may explicitly select the top-level route with `路由：生图`、`路由：生视频`
or `路由：全流程` (also accept `图片`、`视频`). `生图` exits this router and
hands off to the image/world-development entry; `生视频` uses the camera-group
route; `全流程` enables governance and production-ledger tracking in addition
to the video route. When no route is stated, infer from the requested artifact
and show the selected route in the execution proposal.

Every depth returns the same visible deliverable:

```text
camera groups
-> human-readable shot table per group
-> one standalone detailed six-part prompt per group
-> explicit 镜头01/镜头02 blocks inside 事件节拍
-> contiguous micro-beats in the structured plan; visible T= lines only for high complexity
```

### Scene-First Grouping (Hard Rule)

Do not use dramatic beats, dialogue turns, shot count, or changes in camera
angle as camera-group boundaries. First identify the scene envelope: location,
time continuity, active characters, blocking geography, and uninterrupted action
line. If those remain continuous and the material fits within the platform's
duration limit, package the entire scene as **one camera group** and put all
coverage inside that group as 镜头01/镜头02/... .

Create multiple camera groups only for a scene/location change, a meaningful
time jump, a closed continuity handoff explicitly intended for a later clip, or
a verified platform/model limit that prevents the continuous scene from being
generated as one unit. Never split a single fixed-location dialogue or reveal
scene merely because it contains several dramatic turns. Generation segments
are submission units inside the same camera group and must not be relabeled as
new groups.

Read only these two short contracts before routing:

- `../director-workflow-70/references/liu-short-drama-contract.md`
- `../director-workflow-70/references/adaptive-depth-routing.md`

Do not read `ai-video-prompt-director`, `director-workflow-70`, the full
storyboard stack, or full preflight before the depth is read from the caller.

## Minimal Intake (Validation, Not Selection)

Capture only these facts about the material. They **validate** the received tier
and reveal which caller-eligible specialists apply — they never pick or move the
tier:

```text
input_scope, active_character_count, location_count,
platform, generation_mode, assets_sufficient,
fight/chase/weapon_contact/stunt,
vfx/transformation/destruction/simulation,
complex_blocking/cross_scene_continuity/reference_conflict/missing_p0,
research_required/output_retry/generated_output_present,
performance_required/emotion_required/relationship_scene/dialogue_intensive,
ip_or_likeness_risk/safety_required/commercial_claims/commercial_exhaustive
```

Unknown risk fields mean a received `fast` cannot be honored: return a named
blocker to the caller instead of silently promoting it to `standard`.

These signals are the only genre information that reaches this layer, and the
observed signal is the authority. With no fight, chase, weapon, or stunt in the
text, do not load the action specialists whatever anyone called the scene. A
signal never promotes the depth either: if the caller supplied `standard`, keep
`standard` and report the mismatch. When the user names a scene kind in Chinese
(`对话`、`打斗`), treat it as the matching signal and show it in the execution
proposal — never as a settings field.

## User Confirmation Gate (Mandatory)

When the depth has been read from the caller and a script or script fragment is
in hand, stop after the initial intake and validation pass. Before loading downstream skills or
writing generation prompts, show a concise execution proposal containing:

- the received workflow depth and prompt complexity,
  **each with its source** (console / user / caller, or `assumed`);
- the validation findings that confirm or contradict those received tiers;
- every skill that will actually be loaded or called, including the platform
  compiler and preflight;
- the planned deliverables and any platform/tool compilation steps;
- skills explicitly excluded to avoid unnecessary compute.

Ask the user to confirm this proposal. Do not load downstream skills, call a
compiler, run preflight, or author the final camera-group prompts until the
user confirms. The visible skill activity must match the confirmed list: never
claim a skill was used unless it was actually loaded or called. If the user
changes depth or prompt complexity, recalculate the proposal and ask
for confirmation again. This confirmation gate triggers on every new script
or script-fragment turn, including repeated or continuation input.

## Route

Create one `ExecutionPlan` before loading downstream instructions. Record the
received depth and its source, exact
`required_skills`, exact `forbidden_skills`,
one `platform_compiler`, one matching `preflight_profile`,
`prompt_owner=narrative-camera-groups`, `max_prompt_compile_count=1`, and the
context policy `state_patch_only + read_once_reuse_receipt + no transcript
replay + owner_only review`. Treat that plan as the loading whitelist and
context budget for the current camera-group task.

### Generation Settings Gate

The task-bound workflow and prompt-description controls are runtime inputs, not
display-only metadata.

**Console access (MCP removed 2026-09-23).** The `skill_console_*` MCP tools no
longer exist. Reach the same logic through the console CLI. Console root =
`G:\工作\vibecoding\director-skill-console` (or `$SKILL_CONSOLE_ROOT` if set).
Invoke as `node "$CONSOLE/src/cli.js" <subcommand> ...`.

| was (MCP tool) | now (CLI subcommand) |
|---|---|
| `skill_console_prompt_compilation_context` | `prompt-context --thread <id> [--input <json>]` |
| `skill_console_prompt_preflight` | `prompt-preflight --thread <id> --prompt-file <path\|->` |
| `skill_console_prompt_compilation_status` | `prompt-status --thread <id> [--compiler <c>]` |
| `skill_console_compile_prompt` | `prompt-compile --thread <id> --compiler <c> --prompt-file <path\|->` |

All four print the same JSON the MCP tool returned and exit non-zero on failure.
Pass prompts via a file or `-` (stdin), never inline — they routinely exceed
10k characters.

Before any downstream skill writes a generation prompt, run `prompt-context`
with the current `threadId` and routing input. Use the returned `settings`,
`processing_depth`, `prompt_description_complexity`, and
`prompt_compilation_profile` as the only active settings for this task.

After `narrative-camera-groups` has produced the draft six-part prompt for a
group, the selected `platform_compiler` runs `prompt-compile` exactly once. Use
its returned `promptText` as the only model-facing generation text and record
the returned `generationSettings` in orchestration state on the matching
`PlatformPromptSet` unit. Do not generate or hand off an uncompiled copy. If the
compiler call fails, return a named state patch/block instead of silently
falling back to stale or inferred settings.

The selected workflow controls backstage processing depth (`none`, `fast`,
`standard`, `full`); it does not change the six-part delivery contract. Which
conditional specialists are eligible follows the observed signals: a fight
signal pulls the action/choreography chain, dialogue/emotion/performance signals
pull the relationship/emotion/performance chain. The received depth and prompt
complexity are part of the compilation receipt: changing either makes an
existing receipt stale, so the platform compiler must be called again for the
affected groups. The
selected description profile controls the generated shot wording: `low` keeps
the six parts and exact dialogue with simple shot descriptions, no duration
limit, and no `T=` micro-beats; `medium` keeps duration limits with simple shot
descriptions and no `T=` lines; `high` keeps duration limits, `T=` micro-beats,
and complex shot descriptions. Read the task settings again for every new
generation call; never cache them across groups or retries.

Every new script or script-fragment turn re-enters this route and reads the
current task settings again, even when the text is identical to an earlier
turn. Do not deduplicate repeated user input. If the user explicitly asks for
two or more prompt versions for the same camera group, set
`prompt_variant_count` to that requested count (maximum 3), assign each unit a
distinct `variant_id` such as `A` and `B`, and compile each variant exactly once
with its own receipt. Repeated or duplicate `variant_id` values remain an error.

### Received `fast`

Load this chain only when the caller supplied `fast` **and** every fast condition
in `adaptive-depth-routing.md` passes. Load exactly:

```text
narrative-camera-groups
seedance-camera-group-compiler-fast
camera-group-preflight-fast
```

The router performs the minimal authority, capacity, asset-role, and continuity
check in the same pass. Do not load separate research, worldbuilding,
professional-storyboard, camera, material, sound, full platform, full-delivery,
or full-preflight Skills. If the target is not simple Seedance-compatible
T2V/I2V, return a named blocker to the caller; do not promote the tier yourself.

On resume, interpret `继续`, `跳过`, and `返回` against persisted phase state.
`继续` advances only from the current completed phase; `跳过` records an
optional phase as skipped; `返回` reopens the named phase while preserving
unrelated confirmed decisions and asset indexes. Resolve any temporary
duration override before routing a bare `继续`.

### Received `standard`

Load this chain for ordinary complete scripts, multi-scene dialogue/emotion
sequences, or any task that is not proven low risk. Delegate to
`$camera-group-director-standard` for one fused story, continuity, information,
space, and shot-planning pass, then continue through `narrative-camera-groups`,
one platform compiler, and standard preflight. Do not load the full director,
governance, separate camera/material/sound, professional-storyboard, portable
orchestrator, or legacy short-drama Skill on this route.

### Received `full`

Load this chain when the caller supplied `full` **and** at least one full trigger
in `adaptive-depth-routing.md` is present. Delegate to
`$ai-video-prompt-director` with `processing_depth=full` and only the triggered
action, VFX, continuity, research, performance, emotion, relationship, IP/safety,
or output-review specialists. A generated output, performance/emotion request,
relationship/dialogue-heavy scene, IP/likeness risk, safety requirement, or
commercial-claims check is independently sufficient to justify `full` — report
the mismatch rather than promoting a lower received depth. An action or
dialogue/emotion signal pre-triggers its own specialist chain, but the script
signal is still the authority: keep a specialist only when the text actually
supports it.

### Caller-Named Capabilities

Some skills have no signal row and no depth of their own. They load only when the
caller names them or the task plainly matches their single lane, and they never
change the received depth. A named capability sits **inside** the chain step it
serves: it never replaces a chain owner and never authors a second full prompt.

| capability | skill | lane |
|---|---|---|
| shot tension / framing / movement | `high-tension-shot-design` | camera design |
| film-language terms and mechanisms | `cinema-language-atlas` | research |
| reference breakdown (拉片) | `film-breakdown-distiller` | research |
| candidate explore-and-select | `bounded-explore-select` | concept gate |
| non-text input routing (mask / depth / layout / mocap) | `constraint-input-router` | intake |
| cross-shot drift audit | `cross-shot-consistency-audit` | review |
| visual progression / color script | `visual-calibration-loop` | cross-group scheduling |
| minimum visual contract | `minimum-visual-bible` | project setup |
| pure-action showcase, no opponent | `action-showcase-direction` | action lane — named only |
| whole-film kinetic visual master | `kinetic-action-visual-master` | action lane — named only |
| live-action fantasy VFX (xianxia) | `cinematic-fantasy-vfx-director` | VFX lane — named only |
| CG xianxia effect system | `cg-xianxia-vfx-design` | VFX lane — named only |

The four "named only" rows have implicit invocation switched off in `SKILL.md` and
`agents/openai.yaml`. Full load conditions: `adaptive-depth-routing.md`.

## Single-Pass Rules

- `narrative-camera-groups` is the only prompt-structure and group-packaging
  owner.
- Exactly one platform compiler may convert the approved structured plan.
- A compiler receives `ShotLedger + CameraGroupPlan + continuity/asset delta`,
  not the entire upstream prose history.
- `full-prompt-delivery` is not part of camera-group authoring; it may validate
  copyability only when explicitly requested.
- Preflight returns findings or named field patches. It never authors a second
  prompt.
- Compile each final camera-group prompt once after plan validation.
- Do not report a script-derived camera-group task as ready until the state
  passes its JSON Schema, every group has one final `PlatformPromptSet` unit,
  and the selected preflight has written a passing `QCReport`.
- Every camera group must carry a structured `handoff_contract` with opening
  and ending state IDs, continuity locks, and a correct `next_group_id`.
- Split generation segments must use contiguous `segment_index` values, retain
  internal state handoffs, and sum to the parent camera-group duration.
- When generated footage is supplied, require `OutputReview`; failed, partial,
  or blocked output requires one named `RetryPlan.single_retry_variable`.
- Research has one owner and one receipt; downstream layers reuse it.
- When research runs, write one `ResearchReceipt` with owner, scope, source IDs,
  `run_count=1`, and downstream consumers. A second browse/research pass is a
  routing failure.

## Blockers Instead of Escalation

When timing overload, authority conflict, unclear spatial causality, missing
identity/layout evidence, reference conflict, complex contact/VFX, or a P0/P1
preflight failure appears, **do not re-tier**. Stop, keep all accepted work, and
return a named blocker to the caller: the received depth, the blocker, and the
smallest depth that would hold it. The caller decides the new depth; this router
only records the decision it receives. Never downgrade on its own. A depth change
also arrives from the caller and must still be re-shown in the confirmation
gate; it invalidates any compilation receipt written under the previous depth.
