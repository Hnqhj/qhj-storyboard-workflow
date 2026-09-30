# Director Skill Orchestration Contract

This is the shared contract for the director workflow, storyboard, camera-group,
platform-compiler, and preflight skills. It prevents each skill from inventing a
second workflow or silently taking ownership of another control surface.

## State Flow

Pass one structured state through the route. Each layer may add fields or submit
patches, but it may not silently replace another layer's decision.

```text
TaskEnvelope
  -> ExecutionPlan
  -> RouteReceipt
  -> ResearchReceipt (conditional)
  -> GovernanceState
  -> StoryContract
  -> ContinuityContract
  -> InformationLedger
  -> SpaceContract
  -> ShotLedger
  -> CameraGroupPlan
  -> GenerationSegmentPlan
  -> PlatformPromptSet
  -> QCReport
  -> OutputReview (when generated output is present)
  -> RetryPlan (when review is failed, partial, or blocked)
```

### Required state objects

`TaskEnvelope`:

```text
task_class, platform, generation_mode, delivery_contract,
aspect_ratio, target_duration, direct_execution, output_format, references,
processing_depth, depth_reasons
```

`processing_depth` is `fast`, `standard`, or `full`. It is **judged by the
decision layer (镜语) and received from the caller**, never selected here;
`depth_reasons` records where it came from
(`console` / `user` / `caller`), not script signals derived by the execution
layer. It controls backstage work only, never output completeness.

There is no genre axis and no genre field. A scene's genre arrives only as the
explicit signals the decision layer weighed (`fight`, `dialogue_intensive`,
`emotion_required`, `performance_required`, ...); they decide which conditional
specialists are eligible once depth is fixed, and they never change the depth.

`ExecutionPlan`:

```text
processing_depth, depth_reasons, prompt_owner,
platform_compiler, preflight_profile,
required_skills, forbidden_skills,
max_prompt_compile_count=1, research_owner, context_policy
```

The plan is the loading whitelist. Its skill lists must match the deterministic
router output; do not add a second director, platform compiler, delivery owner,
or preflight during execution.

`ExecutionPlan.context_policy` is the context budget for the route:

```text
source_of_truth=orchestration_state
handoff_mode=state_patch_only
reference_read_policy=read_once_reuse_receipt
transcript_replay=forbidden
review_mode=owner_only
```

Specialists receive only the state slice needed for their owned surface. They
reuse inspected references and `ResearchReceipt` rather than reopening the same
source or replaying the full upstream transcript. Review findings return named
field patches and do not trigger a second full review.

`RouteReceipt`:

```text
task_class
active_mandatory_layers
active_conditional_layers
skipped_layers_with_reasons
owner_by_control_surface
instructions_read
route_status: complete | incomplete
```

`ResearchReceipt` when `research_owner` is set:

```text
owner=creative-research-first, status=complete, run_count=1,
query_scope, source_ids, reused_by
```

Downstream owners reuse this receipt and do not launch another research pass.

`GovernanceState`:

```text
authority_source, authority_status, current_phase, current_scope,
stage_outputs, authorized_scope, pending_decisions, next_action, duration_scope,
completed_endpoint, next_start, confirmed_decisions, asset_status,
continuity_locks, open_questions
```

`StoryContract`:

```text
narrative_job, primary_visual_job, viewer_end_state,
major_beats, character_goals, obstacle, turn, consequence,
dialogue_constraints
```

`ContinuityContract`:

```text
character_ids, identity_locks, costume_state, prop_state,
location_lock, lighting_lock, axis, screen_direction,
accepted_previous_endpoint, allowed_changes, forbidden_changes
```

`InformationLedger`:

```text
shot_id, shot_function, primary_carrier, visible_behavior,
meaning, new_information, viewer_question_before,
viewer_state_after, handoff_to_next
```

`SpaceContract`:

```text
master_image, actor_positions, camera_zones, axis,
screen_direction, foreground_midground_background,
action_path, attention_path, reset_points
```

`ShotLedger`:

```text
shot_id, start, end, duration, function, shot_size,
camera_height, angle, lens, focus_dof, lighting, movement,
tracking_owner, cut_trigger, action, proof_task, sound_cue,
handoff, endpoint_state, micro_beats, generation_risk
```

`micro_beats` 是镜头内 T 节拍数组。每项记录 `start`、`end`、`description`；
它们使用镜头组绝对时间轴，连续覆盖该镜头窗口，并在最终 `事件节拍` 中
以 `T=起始-结束s` 逐项展开。

`CameraGroupPlan`:

```text
group_id, duration, opening_state, ending_state, source_shots,
one_action_spine, dominant_camera_behavior, first_frame_anchor,
handoff_state, timing_confidence
```

`GenerationSegmentPlan`:

```text
segment_id, group_id, segment_index, duration, platform,
opening_state, ending_state, split_basis, split_reason
```

`QCReport`:

```text
status, hard_failures, warnings, missing_locks,
timing_errors, owner_conflicts, prompt_trace_errors,
single_retry_variable
```

## Task Card Protocol

Every dispatched specialist returns a patch, not a competing full draft:

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

The orchestrator merges patches in this priority order:

```text
explicit user instruction
> inspected reference truth
> accepted continuity state
> story/dialogue contract
> physical feasibility
> camera/aesthetic choice
> platform syntax
> decoration
```

## Final Owners

Assign exactly one final owner to each active control surface:

```text
macro structure              = video-structure-design
story unit                   = screenwriting-story-craft
shot information delta       = shot-information-progression
continuity facts             = character-continuity-bible
durable entity registry      = entity-continuity-system (when needed)
master spatial blueprint     = master-shot-camera-planning (when needed)
camera grammar               = cinematic-audiovisual-language
complete shot table          = professional-storyboard-director
group boundaries and delivery= narrative-camera-groups
project authority/state       = ai-video-production-governance
performance foundation      = live-action-performance-direction
emotion/relationship patch   = triggered specialist only
action physics               = action-choreography-reference
VFX lifecycle                = cinematic-vfx-director
material/light realism       = ai-material-realism
sound and foley              = cinematic-music-sound-design
platform wording             = one selected platform compiler, one compile
final audit                  = preflight matching fast / standard / full
```

All non-owners return constraints, evidence, or patches only.

## Delivery Contracts

Select one `delivery_contract` before timing:

```text
liu_camera_group       = 14-28 seconds per group, never over 30
generic_seedance_clip  = 4-15 seconds when explicitly requested
storyboard_only        = no forced generation duration
platform_specific      = follow the verified platform contract
```

`narrative-camera-groups` owns the Liu camera-group contract. Generic platform
examples must not override it.

## Input-Scope Compiler Route

```text
complete script / multi-shot sequence
  -> global breakdown + CameraGroupPlan
  -> six-part standalone prompt per camera group

local fragment / one continuation beat
  -> local state and capacity check + local ShotLedger / CameraGroupPlan
  -> detailed six-part standalone prompt per local camera group
```

For script-derived inputs, record `TaskEnvelope.output_format = six_part`.
Complete and local routes differ only in planning scope, not final prompt shape.

## Handoff Rules

- Structure hands off completed beats and dialogue constraints.
- Information progression hands off one primary information job per shot.
- Space planning hands off axis, positions, paths, and reset points.
- Storyboard design hands off the complete `ShotLedger`.
- Specialist layers may add only named patch fields.
- Camera groups split only at a completed turn, location/state change, or stable
  endpoint; every split has an opening anchor and handoff state.
- `CameraGroup` is a director planning unit; `GenerationSegment` is a platform
  submission unit. Default to 1:1. Split a group into several segments only for
  a verified model limit, complexity, or continuity need, and record the reason
  plus every segment's opening and ending state.
- The platform compiler changes syntax, not story facts, timing, continuity, or
  camera ownership.
- Preflight may block or request a patch, but may not redesign the concept.

## Hard Gates

Block delivery when any of these is true:

1. An active control surface has no owner or competing final owners.
2. A required state object is missing for the selected output mode.
3. Group timing is outside its selected delivery contract.
4. Shot timecodes have gaps, overlaps, or do not sum to the group duration.
5. A group has no stable opening or ending state.
6. A plot-critical reference role or identity lock is missing.
7. A final prompt is not standalone for its generation unit.
8. A specialist block contradicts the merged state instead of submitting a patch.

Warnings may cover justified long takes, sparse coverage, or optional aesthetic
detail, but warnings must name the evidence and the owner responsible for the
decision.
