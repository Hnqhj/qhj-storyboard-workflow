---
name: script-camera-group-router
description: Lightweight first and only implicit entry for turning a complete script, script fragment, dialogue block, or continuation beat into AI-video camera-group prompts. Use when the user asks to 拆分镜、拆镜头组、剧本转分镜提示词、按镜头组生成 Seedance 提示词, or supplies script text and expects timed shot tables plus prompts. Select fast, standard, or full processing depth before any heavy director Skill is loaded. Do not use for analysis-only requests, generated-video diagnosis, image-only prompts, or storyboard-table-only delivery.
---

# Script Camera Group Router

Select execution depth before loading any heavy director, storyboard, platform,
or preflight Skill. This is the single implicit front door for script-to-camera-
group prompt work.

## Invariants

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
storyboard stack, or full preflight before depth selection.

## Minimal Intake

Determine only:

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

Unknown risk fields do not qualify for `fast`; use `standard`.

## User Confirmation Gate (Mandatory)

When the user has selected a workflow completeness level and prompt
description complexity, and supplied a script or script fragment, stop after
the initial intake and routing decision. Before loading downstream skills or
writing generation prompts, show a concise execution proposal containing:

- the selected workflow depth and prompt complexity;
- the inferred risk/complexity reasons;
- every skill that will actually be loaded or called, including the platform
  compiler and preflight;
- the planned deliverables and any platform/tool compilation steps;
- skills explicitly excluded to avoid unnecessary compute.

Ask the user to confirm this proposal. Do not load downstream skills, call a
compiler, run preflight, or author the final camera-group prompts until the
user confirms. The visible skill activity must match the confirmed list: never
claim a skill was used unless it was actually loaded or called. If the user
changes completeness or prompt complexity, recalculate the proposal and ask
for confirmation again. This confirmation gate triggers on every new script or
script-fragment turn, including repeated or continuation input.

## Route

Create one `ExecutionPlan` before loading downstream instructions. Record the
selected depth and reasons, exact `required_skills`, exact `forbidden_skills`,
one `platform_compiler`, one matching `preflight_profile`,
`prompt_owner=narrative-camera-groups`, `max_prompt_compile_count=1`, and the
context policy `state_patch_only + read_once_reuse_receipt + no transcript
replay + owner_only review`. Treat that plan as the loading whitelist and
context budget for the current camera-group task.

### Generation Settings Gate

The task-bound workflow and prompt-description controls are runtime inputs, not
display-only metadata. Before any downstream skill writes a generation prompt,
call the MCP tool `skill_console_prompt_compilation_context` with the current
`threadId` and routing input. Use the returned `settings`,
`processing_depth`, `prompt_description_complexity`, and
`prompt_compilation_profile` as the only active settings for this task.

After `narrative-camera-groups` has produced the draft six-part prompt for a
group, the selected `platform_compiler` calls `skill_console_compile_prompt`
exactly once. Use its returned `promptText` as the only model-facing generation
text and record the returned `generationSettings` in orchestration state on the
matching `PlatformPromptSet` unit. Do not generate or hand off an uncompiled
copy. If the MCP compiler call fails, return a named state patch/block instead
of silently falling back to stale or inferred settings.

The selected workflow controls backstage processing depth (`none`, `fast`,
`standard`, `full`); it does not change the six-part delivery contract. The
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

### Fast

Use only when every fast condition in `adaptive-depth-routing.md` passes.
Load exactly:

```text
narrative-camera-groups
seedance-camera-group-compiler-fast
camera-group-preflight-fast
```

The router performs the minimal authority, capacity, asset-role, and continuity
check in the same pass. Do not load separate research, worldbuilding,
professional-storyboard, camera, material, sound, full platform, full-delivery,
or full-preflight Skills. If the target is not simple Seedance-compatible
T2V/I2V, escalate to `standard`.

### Standard

Use for ordinary complete scripts, multi-scene dialogue/emotion sequences, or any
task that is not proven low risk. Delegate to
`$camera-group-director-standard` for one fused story, continuity, information,
space, and shot-planning pass, then continue through `narrative-camera-groups`,
one platform compiler, and standard preflight. Do not load the full director,
governance, separate camera/material/sound, professional-storyboard, portable
orchestrator, or legacy short-drama Skill on this route.

### Full

Use when any full trigger in `adaptive-depth-routing.md` appears. Delegate to
`$ai-video-prompt-director` with `processing_depth=full` and only the triggered
action, VFX, continuity, research, performance, emotion, relationship, IP/safety,
or output-review specialists. A generated output, performance/emotion request,
relationship/dialogue-heavy scene, IP/likeness risk, safety requirement, or
commercial-claims check is independently sufficient to select `full`.

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

## Escalation

Escalate without discarding accepted work when timing overload, authority
conflict, unclear spatial causality, missing identity/layout evidence, reference
conflict, complex contact/VFX, or a P0/P1 preflight failure appears. Record the
new depth and reason. Never downgrade during the same task.
