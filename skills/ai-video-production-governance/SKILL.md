---
name: ai-video-production-governance
description: "正式 AI 视频与影视项目的治理：权限、项目状态、制作阶段、资产就绪度、容量、连续性交接与基于证据的修订。在剧本转镜头组工作流中仅完整档使用。用于正式项目跟踪、跨会话生产或非镜头组的治理。 Govern substantial AI-video and film projects through authority, project state, production phases, asset readiness, capacity, continuity handoffs, and evidence-based revision. In the script-camera-group workflow, use only when the received processing depth is full; fast and standard use their fused lightweight planners. Use directly for formal project tracking, cross-session production, or non-camera-group governance."
---

# AI Video Production Governance

Use this skill as a model-agnostic governance layer. It protects the current
script and project state while specialist skills design shots, visuals, action,
sound, platform wording, and delivery. It does not replace those specialists.

## When To Activate

Activate for any substantial moving-image task with one or more of these risks:

- a script, scene, dialogue block, or connected sequence;
- more than one shot, generation segment, or camera group;
- recurring characters, props, locations, or cross-clip continuity;
- supplied images, videos, audio, layouts, or prior accepted footage;
- capacity, timing, continuation, retake, or delivery questions.

Skip for a trivial standalone image or single-shot prompt when no project state,
asset binding, or continuation is needed.

## Ownership Boundary

This skill owns:

- authority and version status;
- project phase and current unfinished point;
- production scope and delivery contract;
- minimum state required before handoff;
- asset readiness and reference-role bookkeeping;
- capacity and natural-boundary decisions;
- continuity state between groups or segments;
- evidence classification after a result returns.

Do not own:

- final story structure or screenplay rewriting;
- shot design, camera grammar, or visual style;
- action choreography, VFX construction, performance, or sound design;
- platform-specific prompt syntax;
- final prompt packaging or media acceptance.

Return constraints and named state patches to the owning specialist. Do not write
a competing full prompt or silently change the authority source.

## Authority Rules

Maintain an explicit source order:

```text
user's latest adopted text
> inspected supplied references
> accepted project continuity state
> approved reusable rules
> provisional inference
```

Classify every text or reference as one of:

```text
authority | adopted revision | candidate | analysis only | reference only | rejected
```

Only `authority` and `adopted revision` may drive formal production. A suggested
rewrite remains outside the prompt until the user adopts it. Never change a
dialogue line, action, character fact, causal result, or ending merely to fit a
time limit or make a prompt sound cinematic.

Keep director, film, studio, photographer, or other named creative anchors in
backstage analysis by default. Translate their useful mechanisms into concrete
composition, lens, movement, light, material, performance, and edit behavior in
the final prompt. Include a name only when the user explicitly requests it and
the platform and safety contracts permit it.

When a contradiction could change the image, performance, continuity, or result,
report the smallest evidence set and mark the affected scope as blocked. Do not
silently select a convenient version.

## Minimal Project State

Keep a short state in conversation. Persist it to a project file only when the
task crosses sessions, scenes, or delivery boundaries:

```text
project_id:
current_phase: 1..7
authority_source: path/version/range
delivery_contract: liu_camera_group | generic_seedance_clip | storyboard_only | platform_specific
platform / generation_mode / aspect_ratio:
current_scope:
completed_endpoint:
next_start:
confirmed_decisions:
stage_outputs:
authorized_scope:
pending_decisions:
next_action:
duration_scope: project_default | scene_default | segment_override
continuity_locks:
asset_status:
open_questions:
```

Do not copy the full script or conversation into state. After a user revision,
update only changed fields. Remove expired working details while preserving the
authoritative source and accepted outputs.

## Seven Production Phases

Local asset organization is optional and on demand. Keep adopted master assets
in the shared library, copy only required versions into scene or episode
delivery folders, and keep work-in-progress, temporary renders, process logs,
and restore history outside the delivery layer. After an agreed asset batch is
adopted and visually checked, ask once whether the user wants a local project
folder organized; do not trigger this for skipped or unfinished asset work.

Use the smallest phase set that solves the request. Show the phase map only for a
new or ambiguous project; do not force a clear direct request through a tutorial.

1. **Lock authority** — identify the current script/version, scene, scope, and
   unfinished start point.
2. **Set production scope** — select platform, generation mode, aspect ratio,
   delivery contract, and whether the task is a standalone clip or sequence.
3. **Set creative baseline** — confirm or inherit medium, color/light, camera
   tendency, performance scale, and sound strategy when they affect the result.
4. **Prepare assets (optional)** — classify identity, structure, layout, prop,
   motion, style, lighting, timing, and audio references; prepare only the
   minimum missing evidence.
5. **Break down and compile** — hand story and information work to the relevant
   owners, then receive the ShotLedger and platform prompt package.
6. **Review and repair** — use actual output evidence; preserve passed layers and
   change one responsible variable per retry.
7. **Close delivery** — verify adopted scope, files, references, continuity,
   media evidence, and the accurate next start point.

Natural commands may jump phases: `继续`, `做 1-1`, `跳过资产`, `只改站位`,
`返回基调`, `结束并审阅`. Do not repeat questions that are already confirmed.

## Delivery Contracts

Select one contract before timing:

```text
liu_camera_group:
  camera group = one continuous scene-continuity planning unit; normally 14-28s, never over 30s
  generation segment = model submission unit; normally 1:1 with the group
  split groups only at scene/location or meaningful time boundaries; split into
  generation segments when a model limit or generation complexity requires it

generic_seedance_clip:
  use the verified active-surface limit, normally 4-15s

storyboard_only:
  design shots without forcing a generation duration

platform_specific:
  use the currently verified platform contract
```

Do not confuse a camera group with a generation segment. Preserve the group’s
dramatic task and handoff when a platform split is required.

Scene-first invariant: same location + same time continuity + same active
characters + continuous blocking/action line = one camera group by default.
Shot changes, dialogue turns, reveals, reactions, and camera-angle changes are
internal coverage, not group boundaries. A new group requires a scene change,
meaningful time jump, deliberate closed handoff, or verified platform limit.

## Input-Scope Compilation Route

Classify the user's source before choosing prompt packaging:

```text
complete_script_or_multi_shot_sequence
  -> global story/information breakdown
  -> ShotLedger and CameraGroupPlan
  -> six-part prompt packaging

local_fragment_or_single_continuation_beat
  -> current-state and local-capacity check
  -> local CameraGroupPlan with the needed shots
  -> one detailed six-part prompt block per local camera group
```

For every script-derived input, record
`TaskEnvelope.output_format = six_part`. User instructions may change language,
platform wording, or visible presentation details, but do not downgrade the
camera-group prompt to an unstructured format. A local fragment may still need
continuity, action, performance, or platform specialists; the route is shorter,
not exempt from feasibility checks.

## Received Processing Depth

Read `../director-workflow-70/references/adaptive-depth-routing.md` before
dispatching optional specialists. `processing_depth` and `depth_reasons` are
**judged by the decision layer (镜语) and supplied by the caller** through the
console task-context, or overridden by an explicit user instruction: record them
verbatim and never derive them. If no depth is
supplied, default to `standard` and label it an assumption. Check the received
depth against that document's low-risk/high-risk lists — a mismatch is a routing
blocker to report back, not a licence to change the tier.
Depth changes backstage work only. Preserve the same camera groups, six-part
prompt, explicit shot blocks, T micro-beats, dialogue authority, and standalone
copyability at every depth.

There is no genre field to record. Which conditional specialists are eligible
follows the explicit signals on record (`fight`, `dialogue_intensive`,
`emotion_required`, `performance_required`, ...), and they never select or lower
the depth. Verify every recorded signal against the evidence — a signal with no
support in the script is a routing defect, not a licence to load specialists.

## Capacity Gate

Before formal prompt writing, estimate:

```text
dialogue speaking time
+ required pauses and listener reaction
+ sequential actions
+ spatial setup and movement
+ prop recognition and contact
+ cut/transition time
+ required endpoint hold
```

Use ordinary Mandarin delivery as an evidence-based estimate, not a compression
target. When content does not fit, split at a complete dialogue, action,
discovery, emotional landing, or genre boundary. Do not delete, rewrite, speed
read, add artificial stutters, or insert empty reaction shots to hit a nominal
limit. Record timing confidence as `high`, `medium`, or `low` and name its basis.

## Asset And Reference Gate

Give every supplied asset one primary role:

```text
identity | costume/state | environment/layout | prop | first frame | last frame
motion | camera | timing | audio | style | lighting | continuity evidence
```

P0 evidence normally includes plot-critical identity, layout, continuation state,
or a prop whose geometry changes the action. P1 evidence improves performance,
motion, VFX, or sound control. P2 evidence is optional polish.

Bind only assets actually visible, used, or required for continuity in the current
generation unit. Keep stable master assets separate from shot-specific storyboard
references. Do not invent file handles, renumber adopted assets, or let a layout
reference override identity, style, or lighting.

Asset state must be explicit:

```text
missing | available | in_progress | pending_review | adopted | replaced | rejected
```

Keep internal identity separate from platform syntax:

```text
asset_id | asset_type | asset_status | role | source_path | platform_handle
```

`asset_id` and `role` are stable facts. The selected platform compiler may
render `@角色名`, exact `@文件名`, or backend `{{Image N}}` syntax, but it may not
rename the asset, change its role, or use a temporary number when a formal ID is
already available.

Missing P0 evidence blocks a confident formal handoff. A direct-execution user
override may permit a conservative provisional route, but the missing evidence
and its impact must remain visible outside the prompt.

## Handoff Contract

Pass the following objects through the route instead of prose-only memory:

```text
TaskEnvelope
RouteReceipt
StoryContract
ContinuityContract
InformationLedger
SpaceContract
ShotLedger
CameraGroupPlan
GenerationSegmentPlan
PlatformPromptSet
QCReport
OutputReview
RetryPlan
```

Each specialist receives a task card and returns only a patch:

```text
TASK_CARD
owner:
objective:
inputs:
decisions:
state_patch_request:
uncertainty:
blocking: yes | no
```

The route's `context_policy` is mandatory: use the shared orchestration state as
the source of truth, reuse one reference/research receipt, pass only named
state-field deltas, prohibit transcript or mega-prompt replay, and assign one
review owner per surface. A revision reopens only the owner of the failed field.

The orchestrator resolves conflicts in this order:

```text
explicit user instruction
> inspected reference truth
> accepted continuity
> story/dialogue
> physical feasibility
> camera/aesthetic
> platform syntax
> decoration
```

## Prompt And Storyboard Boundary

For a complete script, let the storyboard and camera-group owners produce the
human-readable ShotLedger and group boundaries. The selected platform compiler
then translates the approved state into its syntax. The compiler may change
formatting and handles, but not story facts, timing, continuity, or ownership.

For a local fragment, the package may be smaller than a complete script, but its
final delivery is still a CameraGroup with a detailed six-part prompt. Use the
minimum shots needed to express the local beat, while retaining opening state,
ending state, continuity, timing, and platform feasibility.

Storyboard reference images are optional outputs. Enter that branch only when the
user explicitly requests storyboard images or has already set a project-level
preference. Their creation must not rewrite the script or become video prompt
bindings.

## Review And Repair

When an output exists, classify the failure before changing instructions:

```text
prompt/workflow | missing asset | continuity | performance | action/physics
camera/edit | material/light | audio | platform/interface | model randomness | unknown
```

Record:

```text
passed layers to preserve
one primary failure mechanism
one responsible owner
one variable to change
evidence and confidence
next endpoint to re-check
```

Do not turn a single failure into a universal blacklist. Do not advance the
completed point until the revised result has been inspected or the user accepts
the provisional status.

## Completion Gate

Before reporting completion, verify:

- the authority source and scope are explicit;
- the selected delivery contract is respected;
- every active control surface has one owner;
- the orchestration state passes the declared JSON Schema and the route-specific
  business checks;
- required P0 evidence is available or the provisional status is explicit;
- timing and natural boundaries were checked before writing;
- the current endpoint and next start point are recorded;
- every camera group has exactly one standalone `PlatformPromptSet` unit with
  `compile_count=1` and the selected compiler;
- every group carries a structured handoff contract: opening state, ending
  state, continuity locks, and the next-group pointer form one chain;
- generation segments are indexed contiguously, preserve state handoffs, and
  reconcile to the parent camera-group duration;
- `QCReport` exists and is `pass` before a script-derived camera-group task is
  reported as ready;
- when generated output is present, `OutputReview` is mandatory; failed,
  partial, or blocked output requires a single-variable `RetryPlan`;
- platform compilation and final preflight have run when applicable;
- file/media claims match actual inspection evidence.

Use `ready`, `ready_with_caveat`, `needs_one_more_pass`, or `blocked`; do not use
“complete” merely because a prompt was drafted.

## References

- Shared state and ownership schema: `../director-workflow-70/references/orchestration-contract.md`
- Fusion compiler details and acceptance matrix: `references/mr-li-fusion-contract.md`
- Use the active storyboard, continuity, platform, and preflight skills for
  their owned decisions; this skill only governs their handoffs and state.
