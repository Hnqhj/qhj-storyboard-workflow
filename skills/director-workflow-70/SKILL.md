---
name: director-workflow-70
description: Portable fallback orchestrator for explicitly requested director-workflow-70 use or installations that do not have script-camera-group-router. Coordinate film and AI-video specialists without private workspace systems. Do not implicitly invoke in the installed Liu script-to-camera-group workflow; its lightweight router and ExecutionPlan replace this duplicate dispatcher.
---

# Director Workflow 70

For Liu's recurring真人短剧 + Seedance workflow, read `references/liu-short-drama-contract.md` first, then `references/short-drama-director-stack.md`. The contract is the single source of truth for duration, audio, dialogue speed, framing, @handles, complete-prompt delivery, and preflight; the stack adds asset sufficiency, three-concept gating, leadership delegation, and specialist ownership.

Before loading conditional specialists, read
`references/adaptive-depth-routing.md` and automatically select `fast`,
`standard`, or `full`. This selection changes backstage depth only; it must not
change the required six-part camera-group delivery or ask the user to choose a
mode.

## Operating Contract

Act as the single front door for this bundle. Select the smallest complete specialist stack; do not load all skills by default.

For substantial AI-video or film work, route first through
`$ai-video-production-governance`. It owns authority, phase, scope, asset state,
capacity, continuity handoffs, and evidence status. This orchestrator remains
the dispatcher and conflict arbiter; it must not duplicate those facts in a
second private state format.

Classify source scope before packaging: every script, script fragment, dialogue
block, or continuation beat uses `$narrative-camera-groups` and the six-part
prompt contract. A complete script receives global grouping; a local fragment
receives a smaller local camera group. Only a non-script standalone idea may use
another prompt format.

This is a portable profile. Use only skills physically included beside this Skill. If a bundled specialist mentions an unavailable optional handoff, keep its local method and omit that handoff. Do not install missing tools, invoke private memory, or invent machine-specific paths.

Keep backstage analysis compact. Deliver the artifact the user needs: a plan, shot structure, copyable prompt, review, or targeted rewrite.

If the local `director_skill_console` MCP is available, use it as a non-blocking observability sink. Emit only explicit lifecycle events for the selected route and specialist handoffs; do not expose hidden reasoning or block production when telemetry is unavailable.

## Phase 0: Read the Directorial Job

Before routing, lock five facts:

1. **Narrative job** — what changes for the audience during this clip.
2. **Primary visual job** — the one result that must read immediately.
3. **Current state** — character form, location, held assets, relative scale, and accepted prior endpoint.
4. **Movement geometry** — where bodies, camera, force, and effects travel in space.
5. **Delivery surface** — still image, storyboard, 5–15 second clip, connected sequence, Seedance, or 即梦 SD2.

Keep one primary goal and at most one supporting goal. Ask only when a missing answer would change the whole route.

## Short-Drama Front Door

When the input is a complete script or connected multi-shot sequence plus
reference images, run these gates before formal shot breakdown:

1. Inspect and classify every reference by identity, costume/state, scene/layout, prop/weapon, motion, VFX, performance, continuity, or audio role.
2. Report `素材完整性检查` and list missing P0/P1/P2 evidence with its impact. Missing P0 identity, layout, or continuation evidence blocks a confident final breakdown; provide only provisional concepts until the evidence is supplied or the user explicitly says direct execution.
3. Present exactly three designed shot concepts and one recommendation. Wait for a choice unless the user says direct/按推荐/不要问 or has already locked a route.
4. After approval, dispatch only the needed leaders, merge their decisions through one state, and send the result through platform compilation and preflight.

This is a routing gate, not an additional visible prompt section. Keep leader task cards backstage unless the user asks to see the production-management view.

For a local fragment or single continuation beat, inspect only the active local
state, capacity, continuity and required assets, then create the minimum viable
local CameraGroupPlan. Do not show three global concepts or a full-script map,
but still provide a local shot table and a detailed six-part prompt.

For substantial tasks, create a minimal backstage Route Receipt before drafting. It records task class, active mandatory/conditional layers, one final owner per control surface, the exact instructions/references read, explicit skips with reasons, and `complete`/`incomplete` status. The receipt is internal bookkeeping; it is not pasted into the user's generation prompt.

Read `references/orchestration-contract.md` before dispatching specialists. It is
the shared source of truth for the state objects, task-card protocol, delivery
contracts, final owners, handoffs, and hard gates below. Do not restate or invent
a competing state schema in a downstream skill.

## Leadership Routing Contract

Use one brain and one owner per control surface:

- story/rhythm: `$video-structure-design` + `$screenwriting-story-craft` + `$shot-information-progression`;
- references/continuity: `$character-continuity-bible` and `$entity-continuity-system` when a durable registry is needed;
- world/aesthetic/material: `$production-design-worldbuilding` + one style owner + `$ai-material-realism`;
- camera/storyboard/delivery: `$cinematic-audiovisual-language` + `$professional-storyboard-director` + `$narrative-camera-groups`;
- action/VFX: `$action-choreography-reference` + `$action-rhythm-editing` + conditional Seedance fight/VFX skills;
- performance/sound: conditional performance/relationship skills +
  `$cinematic-music-sound-design` for dialogue/voice-over, physical foley and
  silence by default; add music or ambience only when the user or authoritative
  script explicitly requires it; `$seedance-audio` only for an explicitly
  requested timing reference;
- platform/QC: exactly one selected platform compiler
  (`$seedance-camera-group-compiler-fast` for fast Seedance,
  `$seedance-20` for standard/full Seedance, or `$jimeng-sd2-prompting` for
  即梦) plus the matching fast, standard, or full preflight profile.

Each dispatched leader returns `objective`, `inputs`, `decisions`, `state_patch_request`, and `uncertainty`. The brain arbitrates conflicts by explicit user instruction -> inspected references -> accepted continuity -> story/dialogue -> physical feasibility -> camera/aesthetic -> platform syntax -> decoration. No leader may silently rewrite another leader's domain.

Use the shared `TASK_CARD` shape from `references/orchestration-contract.md`.
Merge specialist results into one state. A specialist that returns a full
replacement storyboard, prompt, or continuity bible instead of a named patch is
not an additional owner; extract only its evidence and patch fields.

### Single-Owner Arbitration

Before drafting, record exactly one final owner for each active control surface: group boundaries and visible delivery=`$narrative-camera-groups`; shot design=`$professional-storyboard-director` when selected; camera grammar=`$cinematic-audiovisual-language`; acting foundation=`$live-action-performance-direction`; emotion or relationship modulation=`$emotional-performance-direction` or `$relationship-dialogue-direction` only when triggered; action physics=`$action-choreography-reference`, with `$seedance-fight-director` returning only an action patch inside an `ExecutionPlan`; VFX construction=`$cinematic-vfx-director`, with platform VFX helpers returning field patches only; sound=`$cinematic-music-sound-design` in foley-only mode; platform wording=the one compiler in `ExecutionPlan`; final audit=the matching preflight profile. All other skills return constraints or evidence only.

Governance is an orchestration layer rather than a competing final owner. Its
state and `RouteReceipt` must be complete before specialist drafting begins.

For Liu's short-drama route, the 14-28 second camera-group contract overrides generic platform examples mentioning 5, 8, 10, 13, or 15 seconds. Those durations remain valid only for an explicitly requested short test or a non-Liu task.

Select `delivery_contract` before estimating time:

- `liu_camera_group`: 14-28 seconds per group, never over 30;
- `generic_seedance_clip`: 4-15 seconds only when explicitly requested;
- `storyboard_only`: no forced generation duration;
- `platform_specific`: use the verified active-platform contract.

The selected contract is state, not a suggestion. Downstream skills may not
change it without an explicit user instruction or a preflight-blocking platform
constraint.

## Mandatory Baseline

For every substantial moving-image task, cover these owners:

- audiovisual and shot logic: `$cinematic-audiovisual-language`;
- shot design and coverage: `$professional-storyboard-director`;
- material, light, grounding, and texture behavior: `$ai-material-realism`;
- sound events and mix hierarchy: `$cinematic-music-sound-design`;
- platform packaging: use exactly one compiler selected by `ExecutionPlan`; the
  fast Seedance compiler, full Seedance compiler, and 即梦 compiler are never
  co-authors for the same prompt;
- final source-trace and prompt audit: use only the preflight profile selected
  for the current depth.

Add `$character-continuity-bible` when references, recurring characters, transformations, weapons, monsters, or multiple clips are involved.

## Routing Matrix

| Need | Route |
|---|---|
| Substantial script/video task | `$ai-video-production-governance` -> route below |
| Vague idea, story function, clip architecture | `$creative-anchor-director` -> `$video-structure-design` |
| Cultural grounding or unfamiliar reference | `$creative-research-first` -> `$reference-hunting-board` |
| Analyze a successful or failed reference clip | `$film-breakdown-distiller` |
| Story scene, dialogue, dramatic beat | `$screenwriting-story-craft` -> `$performance-scene-director` |
| Shot list, storyboard, camera coverage | `$shot-information-progression` -> `$master-shot-camera-planning` -> `$professional-storyboard-director` |
| Unconventional camera tension | `$cinema-language-atlas` -> `$high-tension-shot-design` |
| World, location, production design | `$production-design-worldbuilding` -> `$world-visual-development-director` -> `$mokeaigc-v9` when a world-image exploration layer is useful |
| Style, named anchors, medium grammar | `$visual-style-aesthetic-direction` -> `$visual-reference-vocabulary` -> `$aesthetic-style-intelligence` |
| Character/reference identity and sequence state | `$character-continuity-bible` -> `$entity-continuity-system` -> `$cross-shot-consistency-audit` |
| Explore variants without losing identity | `$invariant-exploration-director` -> `$bounded-explore-select` |
| Fight, weapon, pursuit, physical action | `$action-choreography-reference` -> `$action-rhythm-editing` -> `$seedance-fight-director` |
| Pure solo action showcase | add `$action-showcase-direction` |
| Transformation or mechanical reconfiguration | `$mechanical-transformation-design` |
| VFX, magic, impact, destruction, transformation FX | `$cinematic-vfx-director` -> `$vfx-effect-construction-engine` -> bundled `$seedance-vfx` for Seedance wording |
| Dialogue, foley, silence, physical rhythm sync | `$cinematic-music-sound-design` (foley-only mode); add bundled `$seedance-audio` only for an explicitly requested dry foley timing reference |
| Prompt compilation for 即梦 SD2 | `$jimeng-sd2-prompting` |
| Prompt compilation for Seedance | `$seedance-20` plus only the needed bundled subskills; do not also route through `$jimeng-sd2-prompting` unless 即梦 compatibility is explicitly requested |
| Review generated output | `$ai-video-output-review` -> `$ai-video-iteration-doctor` |
| Decide text vs image/video/constraint evidence | `$constraint-input-router` |
| Calibrate a visual direction before generation | `$minimum-visual-bible` -> `$visual-calibration-loop` |

## Core Pipelines

### A. Complete-Script Camera Groups

```text
Phase 0 intent -> continuity locks -> visual/material master -> camera master ->
event beats -> sound -> positive stability locks -> platform compiler -> preflight
```

For a new script/reference request, prepend:

```text
intake/reference sufficiency -> three concepts -> user choice/direct override ->
leader task cards -> arbitration -> the normal prompt pipeline
```

### A1. Local Fragment Camera Group

```text
local authority/state -> capacity check -> required asset roles -> local
ShotLedger -> local CameraGroupPlan -> selected platform compiler -> preflight
```

The local group may contain one or several shots, but its final prompt still uses
the six-part order and must be independently copyable.

### B. Action / Fight

```text
role and force asymmetry -> distance and line -> attack/defense response ->
position change -> rhythm escalation -> camera proof -> environment response ->
VFX support -> sound transient/tail -> platform compiler -> preflight
```

Do not let style, blur, or VFX hide missing contact or receiver response. Every exchange must alter posture, distance, support, weapon line, injury/state, or environment.

### C. VFX

```text
effect job -> source/owner -> trigger/formation -> material and shape ->
path/spatial layer -> contact/operation -> receiver/environment response ->
peak -> decay/residue -> sound sync -> platform compression
```

Use one dominant effect family per beat. Effects need a visible origin, route, result, and endpoint.

### D. Connected Sequence

```text
sequence objective -> ordered major beats -> accepted observed endpoint ->
current clip job -> current clip endpoint -> continuity audit -> next clip
```

Accepted footage overrides the plan. Do not replay completed beats or leak future beats early. When exact terminal frames differ, bridge with a new functional shot scale or motivated transition rather than pretending to reproduce the old frame.

### E. Review and Rewrite

```text
inspect actual output -> preserve successful layers -> identify the mechanism-level failure ->
change the smallest responsible layer -> rerun preflight
```

Do not convert one surface symptom into a universal blacklist.

### F. Structured Handoff

The orchestrator must hand downstream skills these objects in order:

```text
TaskEnvelope -> RouteReceipt -> GovernanceState -> StoryContract
-> ContinuityContract -> InformationLedger -> SpaceContract -> ShotLedger
-> CameraGroupPlan -> GenerationSegmentPlan -> PlatformPromptSet -> QCReport
```

Do not start final prompt drafting before `RouteReceipt.route_status` is
`complete`, and do not let platform compilation mutate story facts, timing,
continuity, or camera ownership.

## Prompt Delivery Contract

For every script-derived camera-group prompt, including a local fragment or
continuation beat, use this order unless the user explicitly requests another
format. Record the selected route as `TaskEnvelope.output_format = six_part`.

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

Rules:

- The copyable block contains only current positive facts: what exists, moves, sounds, and remains stable.
- Every concrete noun, style anchor, prop, ability, transition, sound, and camera routine must trace to current instructions, inspected references, accepted continuity, or an approved reusable rule.
- Put platform parameters outside the prompt when the user sets them in the interface.
- Use exact name-based `@图片名`、`@视频名`、`@音频名` in final prompts for references supplied with the script; retain `{{Image N}}`、`{{Video N}}`、`{{Audio N}}` only as backend mapping.
- Material and camera layers are mandatory but concise. Events inherit them instead of repeating them.
- Negative diagnostics, old failures, and backstage reasoning stay outside the paste-ready block.

## Quality Gates

Before delivery, verify:

1. current scene and movement path are not contaminated by an older template;
2. identity, form, weapon, scale, and reference roles are explicit enough for the task;
3. each shot adds information, proves contact, proves movement, reveals state, or hands off the next beat;
4. camera position, height, scale, path, and cut trigger are not merely style labels;
5. feet, support, center of mass, cloth drag, weapon mass, recoil, and braking match the action;
6. VFX has source, path, interaction, environment response, decay, and endpoint;
7. material language describes actual surface behavior, controlled highlights, AO/contact occlusion, and stable texture density;
8. sound identifies onset, transient, resonance, space, tail, and silence where relevant;
9. the final prompt has one primary goal and no mutually competing hero events;
10. The preflight profile selected by `ExecutionPlan` passes before delivery;
    `$ai-video-prompt-preflight` is full-depth only.
11. For new script/reference input, the asset completeness report and three-concept gate were completed or an explicit direct-execution override was present.
12. For short-drama output, groups use 14-28 seconds (never over 30), individual shots are usually 1-4 seconds, and dialogue has natural speaking time; choose the shortest complete group rather than padding duration.
13. The final response contains one complete prompt per group plus a separate human-only timed shot table; every shot detail is restated inside its group prompt.
14. Inside `事件节拍`, every shot window is subdivided into contiguous `T=起始-结束s` micro-beats. Each T range contains one observable action, performance, camera change, sound-linked event, or state result; T ranges cover the shot exactly without gaps or overlaps.

## Stop Rule

Stop when the requested production artifact is complete and audited. Do not expand into generation, browser operation, local archive automation, Blender, mocap, editing, or long-term memory unless the host system provides those abilities and the user explicitly asks for them.
