---
name: narrative-camera-groups
description: Downstream sole packaging owner selected by script-camera-group-router for every script-to-camera-group prompt. Convert an approved or fast-path fused shot plan into timed camera groups, a human-readable shot table, and one detailed six-part standalone prompt per group with explicit shot blocks. Preserve micro-beats in the structured plan; render them in the prompt only when the active profile is high. Do not perform a second director route, research pass, or platform rewrite.
---

# Narrative Camera Groups

Package generated footage as camera groups, never as a flat list of vague scenes or arbitrary short clips. Render visible delivery labels in Chinese unless the user requests another language.

## Scene-First Boundary Rule

`camera group` is a scene-continuity unit, not a plot-beat container. Determine
the scene envelope before counting groups. Consecutive shots belong to the same
camera group when they share the same location, time continuity, active
characters, blocking geography, lighting state, and uninterrupted action or
dialogue line. A single fixed-location scene that fits the duration limit must
produce exactly one camera group, even when it contains setup, reaction,
reveal, reversal, and dialogue turns. Those become internal 镜头01/镜头02
blocks in the group's shot table and event beats.

Open a new camera group only when there is a location change, meaningful time
jump, a deliberate closed state handoff for a later scene, or a verified model
limit/complexity constraint. A platform split creates generation segments under
the parent group; it never creates additional camera groups. If a proposed
boundary does not meet one of these conditions, merge the material back into
the current group and preserve the fixed-scene continuity locks.

## Ownership And Precedence

Own the final delivery format for plot/script-to-AI-video storyboard prompts. Other skills may supply content, but they must not replace this packaging contract.

Read `../director-workflow-70/references/liu-short-drama-contract.md` for Liu's canonical duration, audio, dialogue, framing, role-handle, and preflight rules. This skill owns group packaging and may add detail but must not contradict that contract.

When an `ExecutionPlan`, `CameraGroupPlan`, and `ShotLedger` are supplied,
consume them directly and do not reread the full orchestration contract. This
skill owns only group boundaries, the human-readable delivery, and the prompt
structure per group; it does not re-decide story facts, continuity, camera
grammar, platform syntax, or specialist physics.

## Runtime Prompt Profile

Immediately before packaging the first generation prompt, call
`skill_console_prompt_compilation_context` with the current `threadId` and the
approved state slice. Re-read it before each later generation call. The
returned `prompt_compilation_profile` is authoritative for this task. Apply it
while writing every group's six-part block: `low` keeps the six sections and
exact dialogue but uses simple shot wording without duration limits or `T=`
micro-beats; `medium` keeps duration limits with simple shot wording and no
`T=` lines; `high` keeps duration limits, `T=` lines, and complex shot wording.

This skill authors the canonical group package and hands the draft to the
selected platform compiler. It must not call `skill_console_compile_prompt`.
The selected platform compiler is the only owner of the single final compile
call and its `compilationReceipt`; a draft is not generation-ready until that
owner returns the compiled `promptText`. Keep `processing_depth` as backstage
routing metadata and keep `prompt_description_complexity` with the group's
generation settings.

Repeated script text is still a new route invocation and must read the current
task settings. When the user requests multiple versions of one group, preserve
the same approved story and shot facts, vary only the requested dimension, and
emit one `PlatformPromptSet` unit per explicit `variant_id` (`A`, `B`, or `C`).
Each variant goes through one compile call and stores its own receipt; never
silently merge variants or label an unrequested duplicate as a second version.

Execution-depth boundary:

- On `fast`, perform the compact fused planning pass described below, then
  package the resulting group.
- On `standard` or `full`, treat `ShotLedger` and `CameraGroupPlan` as approved
  planning evidence. Do not parse the script again, re-estimate duration,
  redesign shot purpose, or repeat continuity/readability review. Only verify
  that every approved field is represented in the table and the six-part group
  prompt, then hand the package to the selected compiler and preflight owner.
- If approved planning evidence is missing or contradictory, return a named
  `state_patch_request` to the planning owner. Do not silently rebuild the
  plan inside packaging.

Invoke this packaging route for every script-derived input, including complete
scripts, local fragments, dialogue blocks, and single continuation beats. A local
fragment uses the camera group belonging to its current scene envelope and still
receives the full six-part prompt package. Do not create a smaller group when
the fragment is merely another beat of the same continuous scene.

## State Handoff Contract

Every packaged group must carry a structured `handoff_contract` in addition to
the human-readable handoff text:

```text
opening_state_id:
ending_state_id:
continuity_locks: { ... }
next_group_id: <next group id or null for the final group>
```

Adjacent groups must share the same state at the boundary, and the previous
group's `next_group_id` must point to the actual next group. When a platform
requires splitting one camera group into multiple generation segments, assign
contiguous `segment_index` values starting at 1, preserve each internal state
handoff, and make segment durations sum to the parent group duration. A split
is allowed only for a recorded model-limit, complexity, or continuity reason.

If generated footage is supplied for review, the route must receive an
`OutputReview`. A failed, partial, or blocked review is not repaired by rewriting
the whole prompt: return one `RetryPlan.single_retry_variable` to the owning
diagnostic skill for the next attempt.

When a context policy is supplied, consume only the approved
`ShotLedger + CameraGroupPlan + continuity/asset delta` slice. Do not reread the
full screenplay, upstream governance prose, or another group's prompt, and do
not run a second semantic or mechanical review owned by preflight.

Do not proactively create or offer storyboard reference images. Enter a
storyboard-reference branch only when the user explicitly requests those images
or an already approved project state requires them.

- Let the top-level video director choose the route and resolve creative intent.
- When the `ExecutionPlan` selects it, let the professional storyboard layer
  design story function, shot order, shot size, position, movement, timing, and
  continuity. On `fast`, perform that compact fused pass here instead.
- Use audiovisual, continuity, action, performance, material, VFX, and sound
  controls only when their owners appear in the current `required_skills`.
- Let the target-platform skill compile model-facing wording and reference handles.
- Let this skill alone decide camera-group boundaries, the human-readable table, prompt-per-group delivery, and the separation between planning and paste-ready text.
- Let preflight validate the result after packaging; preflight must not collapse several group prompts into one block.

When a specialist needs a correction, apply only its named `state_patch_request`
fields. Do not paste specialist full drafts into the group prompt. Preserve the
single-owner arbitration defined by the orchestration contract.

For deterministic checks, run `scripts/shot_group_linter.py` against a JSON shot plan; input fields are documented in `references/shot-group-json-schema.md`. It checks timing continuity, required fields, soft shot-count warnings, close-up proof tasks, direct face-push violations, @character presence, and forbidden positive audio terms. It is a mechanical gate, not a substitute for creative review.

For film-level camera and lighting wording, read `references/film-level-shot-spec.md`; use its field order and focal-length/lighting guidance when the user asks for影视级、电影级或摄影执行级分镜。

Upstream gate: for a new script plus references, accept a formal breakdown only after the director brain has completed `素材完整性检查` and the three-concept gate, or after the user explicitly requested direct execution. This skill does not invent missing reference facts or choose a competing concept.

When another skill proposes per-shot generation, an unstructured paragraph for
a script fragment, one prompt for the whole screenplay, one code block for all
groups, or a shot list without exact durations, this user-calibrated contract
wins. User presentation preferences may change language or labels, but every
script-derived camera group retains the detailed six-part structure.

## Core Contract

- Treat a **shot** as one distinct camera setup or continuous take. A shot may last 1, 2, 3, or 4 seconds; use a longer duration only when a deliberate dialogue delivery, one-take action, performance, or reveal needs it.
- Treat a **camera group** as consecutive shots inside one continuous scene envelope: shared location, continuous time, active characters, blocking geography, lighting state, and uninterrupted action/dialogue line. Use a flexible 14-28 second range as guidance, never exceed 30 seconds per generation segment, and choose the shortest duration that completes the scene material without padding. Dramatic beats do not define group boundaries.
- Treat a **generation segment** as the platform submission unit. Default to one
  generation segment per camera group. If a verified model limit or complexity
  constraint requires several segments, preserve the camera group's dramatic
  task and record each segment's opening state, ending state, and split reason;
  never delete dialogue or speed performance to avoid the split.
- Split a script at scene boundaries first: location change, meaningful time
  jump, deliberate closed handoff, or verified model limit. Completed
  micro-turns such as arrival/reveal or confrontation/reversal are internal
  shot beats by default and must not create a new camera group inside one
  continuous scene.
- Keep every group internally complete: repeat the opening state, identities, wardrobe or appearance facts provided by the user, location, spatial axis, action direction, key prop state, lighting, and its ending state.
- Do not use a single short clip merely to avoid shot planning. Do not force a 14-28 second group to be a single take or to fill unused time.
- Preserve the full script order. If one continuous scene exceeds the platform
  limit, split it into generation segments under one parent camera group when
  the workflow supports that; if separate deliverables are unavoidable, retain
  the same `scene_id` and explicit internal state handoffs. Never split a scene
  simply to create more prompt blocks.

## Platform Character Handles

- In every copy-ready generation prompt, prefix every named character with the exact platform handle supplied by the user: `@角色名`, with no space. Examples: `@苏凌月`, `@苏建国`, `@刘大龙`.
- Apply the handle consistently in `角色/资产锁定`, every `事件节拍`, dialogue speaker labels, `声音`, and `正向稳定约束`; do not alternate between a bare name and an `@` name inside the same prompt.
- Preserve the user's exact character spelling and handle. Every distinct character in the script, including role-labeled characters such as `黑衣小弟甲` and `黑衣小弟乙`, receives its own supplied platform handle (for example `@黑衣小弟甲`, `@黑衣小弟乙`); do not merge, translate, or rename handles.
- Keep reference-file handles separate and name-based: use the exact uploaded `@图片名`、`@视频名`、and `@音频名` for assets supplied with the script, always with a scoped role on first mention. `@角色名` calls the uploaded five-view character asset; it is a different handle type. `{{Image N}}`等编号只作后台映射，不进入最终提示词主引用。
- The human-readable shot table may use plain names for scanning, but every character mention inside the copy-ready prompt must use the `@角色名` form.

## Shot Design

For every shot, explicitly provide:

1. timecode and duration;
2. shot size: ECU/CU/MCU/MS/MLS/FS/WS/EWS or clear Chinese equivalent;
3. camera height, angle, and position when relevant;
4. camera movement with one owner and path, such as locked-off, push-in, pull-back, side-track, handheld follow, arc, pan, tilt, or crane;
5. lens/focal-length feel, aperture/depth-of-field, focus subject and focus transition when relevant;
6. lighting design: key/fill/rim or practical source, direction, hardness/softness, color temperature, shadow and reflection behavior;
7. on-screen action and dialogue carried by that shot;
8. a continuity handoff: action match, eyeline, sound bridge, foreground wipe, impact cut, or the changed spatial state.

Describe each shot with production-level specificity: opening pose and support, center-of-gravity direction, trigger, step-by-step motion path, contact and force feedback, breath/eyeline/dialogue beat, secondary motion in hair/cloth/props, lens and focus behavior, lighting direction and shadow response, deceleration and follow-through, and the exact end state. Detail must improve controllability, not create a frozen checklist.

Natural-performance lock: characters keep human timing and inertia. Preserve anticipation, weight transfer, acceleration, deceleration, recovery, breath, blinking, gaze shifts, and delayed listener reactions. For dialogue, coordinate lip movement with breath and small asymmetrical gestures that serve the words; for action, show preparation, force transfer, recoil and recovery. Never use mannequin-like stillness, instant pose changes, synchronized gestures, repeated nods, or simultaneous head turns without a story reason.

Close-up discipline: use wide/full, medium, and medium-close framing as the default for short-drama geography, dialogue, blocking, and movement. Reserve CU/ECU for a strong expression peak, decisive power/entrance beat, impact or force detail, critical eye/hand/prop evidence, or an otherwise unreadable story fact. When a character changes position, distance, level, or route, show the transition in wide or medium framing before any detail insert. Do not push directly into a face; push toward upper-body relation, hands, prop, or a two-person composition. A near shot should normally remain waist-up and retain shoulders, hands, eyeline, or the opposing relationship; avoid face-only close-ups and consecutive close-up chains.

Build the group as a readable progression rather than random coverage:

```text
orientation -> intention/reaction -> escalation -> contact or turn -> consequence/hold
```

Short-drama dialogue coverage rule: do not default to speaker-to-speaker alternation, but do not force a reaction cut for every line. Classify each beat by dialogue length, semantic completeness, conflict level, and available listeners. Very short replies, commands, interjections, or self-contained lines may finish in the same shot. Add a listener, witness, group, prop, or space reaction only when it adds information, changes relationship/power, reveals strategy, advances the next action, or creates a useful question. Medium lines or relationship turns usually need one reaction carrier; long lines, threats, insults, reversals, power declarations, and action commands may need one or two, unless the reaction adds no new information. As a default, let a speaker finish a full sentence or natural half-sentence before cutting; avoid cutting inside a single word. This is a continuity preference, not an absolute rule: an impact, interruption, danger, reaction snap, or reveal may motivate an earlier cut, but preserve the remaining speech as an audible bridge and keep the word intelligible. Cut on reaction landings, power shifts, gaze changes, interrupted movement, semantic pauses, or new information, not automatically at every sentence.

Short-drama pace gate: each group opens with a visible hook or conflict pressure within the first 1-2 seconds, reaches an escalation/block/reversal or power shift by the middle, and ends on a concrete consequence or changed state. Remove neutral establishing shots, repeated emotional close-ups, and dialogue beats that do not alter information, relationship, distance, control, or next action.

Vary adjacent shots in at least two visible ways when a cut is needed: scale, height, angle, path, tracking owner, or viewpoint. Preserve action axis, screen direction, eyeline, subject count, and geography unless the script calls for a motivated reset.

## Timing Budget

- Begin with a 2-4 second orientation or pressure shot unless the first frame needs immediate impact.
- Use 1-3 second inserts only to prove a grip, eye reaction, object state, contact point, or incoming danger.
- Give dialogue enough duration for natural Chinese lip sync. Do not compress several full sentences into one 1-second shot.
- Estimate ordinary Mandarin dialogue at 2.8-3.2 Chinese characters per second, using 3 characters per second as the default average; restrained/emotional delivery remains 2-3 characters per second. Short urgent commands may briefly reach 3.5-4 characters per second, but never use that rate for continuous long sentences. Keep the edit fast through cuts, overlaps, action matches, and escalation; do not achieve pace by speeding up speech.
- Give action a visible start, force transfer, and result; reserve the last 2-4 seconds for the changed state, reaction, or dramatic hold.
- Check that all shot durations add up to the declared camera-group duration before delivery.

## Soft Coverage Budget

Use shot-count guidance as a review signal, not a rigid template. For a 14-28 second group, dialogue-led scenes usually need about 4-8 shots, emotion-led scenes 3-6, action-led scenes 5-10, and hybrid scenes 5-9. Increase or reduce only when line length, reaction value, action causality, or a deliberate one-take design justifies it. If a short group exceeds these ranges, run an overload review: merge shots that repeat the same information, keep the decisive reaction or contact readable, and preserve the stable end state.

Overload warning signs: more than one major event in a single shot, several simultaneous camera moves, more than two effect families at one peak, or a sequence that cannot give each dialogue/action beat its natural breath, reaction, and recovery. Split at a completed turn or simplify the coverage before compressing performance.

## Delivery Format

For each camera group, use this exact order. Repeat the entire order for every group:

```text
Camera Group XX | Total duration: about XX seconds | Story function:
Opening state:
Ending state:

Reference map:
- List every supplied `@图片名`、`@视频名`、or `@音频名` handle and its one primary role; keep backend `{{Image N}}` mapping outside the prompt.
- Write None when no external reference is supplied.

Human-readable shot table (planning aid only; never paste this table into the model prompt):
| Shot | Timecode/duration | Shot size | Position/angle/lens/focus | Lighting | Movement | Image, dialogue, reaction | Cut/continuity |

Copy-ready prompt:
[Character/assets and reference locks]
[Visual and material master]
[Camera-language master]
[Event beats]
[Sound]
[Positive stability locks]

Generation suggestion: state T2V, I2V, or R2V only when known; otherwise state the conservative assumption.
```

Keep the prompt self-contained. Use only supplied or clearly labeled assumptions; do not invent specific faces, costumes, locations, or era details that the script does not establish.

## Planning Layer Versus Generation Layer

Treat the shot table as a reader aid, not as prompt text.

- Keep the Markdown table outside every copy-ready code block.
- Do not paste table rows, pipe characters, column headings, production notes, or shorthand such as "see table" into the prompt.
- Do not omit shot detail from the prompt merely because the table already contains it.
- Re-express every shot inside `EVENT_BEATS` as a visibly separate shot block,
  never as one merged event paragraph. Use the stable shape `镜头01｜起始-结束s`
  followed by the complete model-facing shot setup. For `high`, add its
  indented/next-line `T=起始-结束s` micro-beats; `low` and `medium` omit T
  lines. Each shot block must state shot number, time
  window and duration, shot size, camera position/height/angle, focal-length or
  lens feel, aperture/depth-of-field and focus subject, lighting
  direction/quality/color temperature/shadow behavior, camera movement,
  concrete visible action, dialogue or performance, sound/cut trigger when
  relevant, ending state, and handoff.
- Let the camera master define the shared camera family once, while each shot line specifies the concrete local setup and movement needed for that shot. Do not reduce a shot line to only "close-up" or "push in".
- Never write "same as the previous group", "continue above", or "use the table". Repeat all identity, reference, scene, visual, camera, audio, and stability facts required to generate that group independently.

Inside each copy-ready prompt, use this complete six-part order:

```text
ROLE_ASSET_LOCK
VISUAL_MATERIAL_MASTER
CAMERA_STYLE_MASTER
EVENT_BEATS
SOUND
POSITIVE_STABILITY_LOCKS
```

The platform compiler may render the canonical headings in Chinese. Put all supplied reference handles and role limits inside `ROLE_ASSET_LOCK`. Put dialogue, voice, source-coupled foley, physical sound synchronization, and intentional silence inside `SOUND`. Keep the paste-ready block positive and generation-facing; enumerate only sounds that are present. Music, ambience, or mood effects require an explicit user or authoritative-script instruction; that authorization is enforced backstage and in preflight, not as negative wording inside the copy block.

## End-To-End Workflow

For `fast`, parse the local script, estimate timing, build the compact shot
sequence, split at natural handoffs, and lock opening/ending states before
packaging. For `standard` and `full`, begin at the approved `ShotLedger` and
`CameraGroupPlan` and perform only these packaging steps:

1. Confirm the approved group boundary and opening/ending handoff.
2. Show the human-readable shot table for the current group.
3. Write one complete, self-contained paste-ready prompt for that group,
   restating every approved shot in concrete prose.
4. Repeat for every remaining group.
5. Return packaging completeness findings to the selected preflight owner.

The selected preflight owner performs the authoritative timing, continuity,
semantic, and mechanical checks according to `review_budget`; this skill does
not run a second full quality review.

At the start of this workflow, assert `delivery_contract`. Use the Liu
14-28-second range only for `liu_camera_group`; honor 4-15 seconds only for an
explicit `generic_seedance_clip` request. Record `timing_confidence` and the
evidence for any exact range.

## Packaging Completeness Gate

Before handing off, verify only packaging-owned conditions:

- Every approved group appears once, in script order, with its approved opening,
  ending, action spine, first-frame anchor, and handoff state.
- The shot table is outside the copy-ready prompt and is clearly only a planning aid.
- Every table row has a corresponding full prose shot description inside the group's prompt.
- Every group has its own complete reference, visual, camera, event, sound, and stability sections.
- All six sections contain substantive current-group controls; empty headings,
  filler summaries, and one-line placeholders fail delivery.
- Every `事件节拍` shot includes shot number, timecode/duration, shot size,
  camera position/height/angle, focal length or perspective, depth of field and
  focus subject, lighting direction/quality/color temperature/shadow behavior,
  camera movement/path, action/performance, verbatim authoritative dialogue,
  cut trigger, ending state, and handoff.
- No section uses `同上`, `沿用`, `参考镜头表`, `保持不变`, or equivalent
  cross-reference wording instead of complete current-group detail.
- The approved structured plan must always retain contiguous in-shot
  `micro_beats` on the camera-group time axis. Render those beats as visible
  `T=起始-结束s` lines only when `prompt_description_complexity=high`; for
  `low`/`medium`, keep the shot window and concrete event prose while omitting
  T lines from the copy-ready block. In either case each stored range contains
  one observable action, performance, camera change, sound-linked event, or
  state result and covers the shot exactly with no gaps or overlaps.
- The final `事件节拍` must visibly repeat the shot-block boundary for every
  shot (`镜头01`, `镜头02`, ...). A single unlabelled paragraph containing
  several shots fails even when its facts are technically present.
- No group prompt depends on the table, another prompt block, or conversation context.
- Every shot block is represented without merging, omission, or cross-group
  references. High-complexity prompts additionally represent each stored
  `micro_beats` range as a visible `T=` line.
- Every supplied handle and every approved specialist `state_patch_request` is
  copied into the correct six-part section.

Do not repeat duration, shot-purpose, continuity, readability, physical-action,
or audio policy review here. Those checks have one owner in the selected
preflight profile. If one of them appears wrong, return the named field to that
owner instead of re-running the review locally.
