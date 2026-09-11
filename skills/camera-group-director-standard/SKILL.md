---
name: camera-group-director-standard
description: Lightweight one-pass director and shot planner used only when script-camera-group-router selects standard depth for an ordinary complete script, multi-scene dialogue or emotion sequence, or a local scene that is not proven fast. Produce the approved story, continuity, information, space, shot, and scene-first camera-group state without loading the full director, governance, cinematography, material, sound, or professional-storyboard Skills. Escalate fights, VFX, transformations, difficult continuity/reference conflicts, research, commercial exhaustive work, and generated-output retries to full.
---

# Camera Group Director Standard

Build one production-ready structured plan for an ordinary script-derived task.
Do not write the final platform prompt and do not invoke other Skills.

## Authority

Read only `../director-workflow-70/references/liu-short-drama-contract.md` in
addition to the supplied `TaskEnvelope`, script, assets, and accepted project
locks. Treat script dialogue, character facts, event order, causality, and
outcome as authoritative unless the user explicitly approves a change.

## Inputs

Require or conservatively infer:

```text
TaskEnvelope and ExecutionPlan
complete script or local fragment
current character/location/prop locks
asset_id -> exact platform handle -> one role mappings
accepted previous endpoint when continuation applies
audio authority
```

Missing identity, layout, endpoint, or conflicting reference evidence that can
change the result is not a default assumption; escalate to `full`.

## One-Pass Plan

1. State the narrative job, viewer end state, ordered major beats, and immutable
   dialogue/fact constraints in `StoryContract`.
2. For a complete script, map the full sequence before grouping. For a local
   fragment, plan only that local unit while preserving any accepted incoming
   state.
3. Build `ContinuityContract` and `SpaceContract`: identity, wardrobe, prop and
   location state; actor positions; axis; screen direction; action/attention
   path; opening and endpoint locks.
4. Build one `InformationLedger` entry per shot. Give each shot one primary job:
   orient, prove action, reveal information, carry dialogue, show a meaningful
   reaction, turn power, or hand off the next beat.
5. Build `ShotLedger` in natural screen time. Preserve full dialogue and budget
   breath, pauses, listener reactions, action preparation, force/result,
   recovery, and the final hold. Do not create pace by accelerating speech.
6. Form camera groups from scene continuity before considering duration. Shots
   sharing one location, continuous time, stable blocking geography, active
   characters, lighting state, and uninterrupted action/dialogue line belong to
   one camera group. Setup, reveal, reaction, reversal, dialogue turns, and
   changes of shot size or angle remain internal shots. Open another group only
   for a location change, meaningful time jump, deliberate closed scene handoff,
   or verified platform limit. Use 14-28 seconds as a preferred generation
   duration, never as a reason to split an otherwise continuous scene. When a
   platform limit forces division, create ordered generation segments under the
   same scene/group ID with explicit opening and ending states. Do not pad.

## Shot Detail Floor

Every shot must include:

```text
group_id, shot_id, start, end, duration, function
shot_size, camera_position, camera_height, angle, lens
focus_dof, lighting, movement, tracking_owner, cut_trigger
action, performance, verbatim dialogue, sound_cue
proof_task, handoff, endpoint_state, micro_beats
```

Use concrete, motivated camera choices. State the visible camera position,
height, angle, perspective/lens feel, focus subject and depth of field, light
source direction/quality/color temperature/shadow behavior, movement owner and
path, and cut trigger. Keep materials grounded through stable texture,
reflection/roughness behavior, contact shadows, and coherent nearby light.

Performance includes objective, gaze, breath, weight transfer, preparation,
inertia, reaction delay, recovery, and only story-serving hand/cloth/prop
motion. Sound contains authoritative dialogue/voice-over and source-coupled dry
foley unless audio authority explicitly adds something else.

Inside every shot, use contiguous group-absolute `T=start-end` micro-beats that
cover the shot exactly. Each micro-beat carries one observable action,
performance change, camera change, sound synchronization point, or state result.

## Output

Return one `TASK_CARD`, not prose alternatives:

```text
owner: camera-group-director-standard
objective
StoryContract
ContinuityContract
InformationLedger
SpaceContract
ShotLedger
CameraGroupPlan
assumptions
uncertainty
state_patch_request
blocking: yes | no
```

`narrative-camera-groups` packages the accepted plan, the selected platform
compiler renders it once, and `camera-group-preflight-standard` validates it.
None of those downstream stages may reopen this plan without a named field
patch.

## Escalation

Escalate to `full` without discarding accepted fields when the task reveals
fight/chase/weapon contact/stunts, VFX/transformation/destruction/simulation,
complex crowd or cross-scene continuity, reference conflict, missing P0
evidence, current platform research, generated-output retry, commercial
exhaustive delivery, timing overload, or a preflight P0/P1 failure.
