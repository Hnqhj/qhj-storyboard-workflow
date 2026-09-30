# Liu 真人短剧 Seedance 导演栈

This is the canonical user-calibrated overlay for Chinese live-action short-drama script + reference-image requests targeting Seedance 2.5 or 2.0. It supplements the portable workflow and fixes the gates, timing, and visible delivery. Routing is not decided here: the single entry point is `$script-camera-group-router`, which executes the fixed chain for the depth the decision layer supplied. Generic skill advice remains valid when it does not conflict with this file.

## Liu Audio And Duration Overrides

These project preferences override subordinate defaults:

- **Audio:** generated short-drama video defaults to clearly sourced character dialogue/voice-over and dry, physical foley/SFX. Allowed default sounds include footsteps, cloth movement, exertion breath, hand/prop handling, weapon movement, impacts, fractures, debris, body contact, and wall/floor response. Add background music, score, BGM, musical beds, emotional cues, or ambience only when the user or authoritative script explicitly requires them; then state their concrete narrative function and timing. In the copy-ready `声音` section, enumerate only sounds that are audibly present; enforce authorization backstage through this contract and preflight.
- **Duration:** camera groups use a flexible **14-28 second** range and never exceed 30 seconds. Choose the shortest duration that completes the story turn, natural dialogue, readable action causality, and stable handoff. Do not stretch a group to reach 20 seconds; split dense material or end earlier when the beat is complete.

## Director Brain

Use `$ai-video-prompt-director` as the full director brain when the received depth is `full`. It is not an entry point: `$script-camera-group-router` is the only entry, and `$director-workflow-70` is the portable methodology reference behind it, not a second front door. The brain owns intent, arbitration, delegation, integration, and final feedback. Specialist skills are leaders or executors, not competing authors.

Priority when decisions conflict:

```text
user's explicit instruction
-> inspected reference evidence
-> accepted continuity state
-> story function and dialogue
-> action/material feasibility
-> camera and aesthetic preference
-> platform syntax
-> decorative detail
```

Only the brain may resolve conflicts, choose the recommended concept, and approve the final prompt. Group boundaries, the human-only shot table, and the one-prompt-per-group packaging are owned by `$narrative-camera-groups`; the brain approves that packaging rather than re-deciding it. A specialist may propose a change but cannot silently overwrite another layer.

## Intake And Reference Sufficiency Gate

Run this gate every time the user supplies a new script, scene, dialogue block, or reference set. Inspect every supplied image before designing shots.

First classify:

- target: Seedance 2.5, Seedance 2.0, or conservative Seedance-compatible output when unspecified;
- mode: T2V, I2V, R2V, FLF2V, continuation, or unknown;
- scene signals actually present in the script: dialogue/story, fight/action, VFX/magic, emotion/performance, chase, transformation, or hybrid. Record only signals you can point to in the text; there is no genre axis and no genre label is assigned;
- requested deliverable: shot table, camera groups, complete copy-ready prompts, or diagnosis;
- expected number of groups from dialogue, action, locations, and stable handoffs.

Then audit references by function, not by file count:

| Function | Minimum evidence | Gate |
|---|---|---|
| character identity | face/5-view or approved identity image for every recurring named character | P0 for identity-sensitive work |
| costume/state | front or full-body view showing current costume, hair, accessories, damage/state | P0 when visible continuity matters |
| scene/layout | master environment view or layout/blocking board with left/right/depth relations | P0 for multi-person action or position-critical shots |
| prop/weapon | silhouette, scale, grip, material, current state | P0 when the prop changes action or plot |
| motion/action | stunt, previs, or clearly described physical basis | P1; P0 for complex fight or chase |
| VFX/magic | source, shape/material, color ownership, intensity or a clear permission to design | P1; P0 when the effect is the story turn |
| performance/relationship | face, pose, eye-line, relationship context, or prior endpoint | P1 for emotion/dialogue-led scenes |
| continuity source | accepted previous clip or tail frame for continuation | P0 for continuation |
| audio/timing | dialogue/foley requirements, supplied dry cue track, or permission to design physical sound | P1; P0 only when explicit beat-sync or supplied audio reference is required |

Report this outside the prompt:

```text
素材完整性检查：完整 / 部分完整 / 关键缺失
已确认：...
缺失或不足：...
补充素材优先级：P0 / P1 / P2
缺失影响：会改变身份、站位、动作、特效、节奏或仅影响装饰
当前可用假设：...
```

If a P0 item is missing, ask the user to add it before formal shot breakdown. You may still show provisional concepts, clearly marked as provisional; do not present final shot tables or generation prompts as if the missing evidence were settled. If the user says “直接生成 / 按推荐 / 不要问”, use a conservative assumption, state it briefly outside the prompt, and continue unless the missing item makes the requested identity or geography impossible.

## Three-Concept Gate

For every new script or materially new scene, before formal storyboard delivery, present exactly three designed concepts unless the user explicitly requests direct execution or has already selected a concept.

Each concept must contain:

```text
概念名称：
镜头结构：hook -> build -> turn -> payoff
摄影策略：camera family, shot-scale range, axis, movement ownership
节奏策略：dialogue treatment, cut density, peak and release
动作/VFX/表演重点：the one visual proof the concept prioritizes
生成风险：the main Seedance risk and mitigation
适用场景：why this route fits the supplied script and references
```

End with:

```text
导演推荐：概念 X
推荐理由：...
选择后将锁定：...
```

Do not output the final shot table or copy-ready group prompts in the same response while waiting for a concept choice, unless the user explicitly says to execute directly. A partial reply uses the recommended concept for any unanswered option.

## Leadership Map And Task Cards

After concept approval, dispatch only the needed leaders. Every leader receives the current state and returns decisions, not a second full prompt.

### Story and Short-Drama Rhythm Leader

Owner: `$video-structure-design`, `$screenwriting-story-craft`, `$shot-information-progression`.

Must return: one segment objective, hook/build/turn/payoff, viewer-information delta per beat, dialogue budget, emotional or action turn, and group split points.

### Reference and Continuity Leader

Owner: `$character-continuity-bible`, `$entity-continuity-system` when a durable registry is needed.

Must return: character handles and identity locks, costume/state, prop/weapon state, scene layout, axis, screen sides, current first frame, accepted endpoint, and allowed changes.

### World, Aesthetic, and Material Leader

Owner: `$production-design-worldbuilding`, `$visual-style-aesthetic-direction`, `$creative-anchor-director` when named anchors or unfamiliar references matter, `$ai-material-realism` for surface/light/render behavior.

Must return: medium, color ownership, architecture/production-design invariants, light direction, material response, and a compact anti-cheapness rule. Do not let this leader write shot timing.

### Camera and Storyboard Leader

Owner: `$cinematic-audiovisual-language`, `$professional-storyboard-director`, `$narrative-camera-groups`.

Must return: shot functions, exact shot durations, shot sizes, camera height/angle, one primary movement, tracking owner, cut reason, axis/screen direction, and handoff endpoint. `$narrative-camera-groups` alone decides group boundaries, human-only tables, and one prompt per group.

### Action and VFX Leader

Owner when conditional: `$action-choreography-reference`, `$action-rhythm-editing`, `$seedance-fight-director`, `$cinematic-vfx-director`, `$vfx-effect-construction-engine`, `$seedance-vfx`.

Must return: stance/support, center-of-mass path, weapon load and grip, force/contact/reaction/braking, action peaks, and for each hero effect source -> formation -> path -> collision -> receiver/environment response -> decay. The platform compiler may compress wording but cannot invent a new effect or action.

### Performance and Sound Leader

Owner when conditional: `$live-action-performance-direction` for visible behavior and physical execution, `$emotional-performance-direction` for the emotion arc and intensity, `$performance-scene-director` for the emotion-profile library and the single-character short form, `$relationship-dialogue-direction` for asymmetric two-person exchange, and `$cinematic-music-sound-design` for dialogue/voice-over, physical sound and silence by default, and for explicitly authorized music/ambience when required; `$seedance-audio` only when an explicit timing reference is requested.

Must return: visible micro-performance, eye-line/listener relay, dialogue pace, voice priority, dry foley, impact/transient, physical sound bridges, and purposeful silence. Dialogue must remain intelligible; speed comes from image rhythm and escalation, not rushed speech. Music, score, ambience beds, and emotional sound cues appear only when the user or authoritative script explicitly requires them.

### Platform Compiler and Profiled QC Leader

Owner: exactly one compiler selected by `ExecutionPlan`:
`$seedance-camera-group-compiler-fast`, `$seedance-20`, or
`$jimeng-sd2-prompting`. Load only Seedance subskills named by the plan; action
and VFX subskills return field patches and do not author another full prompt.
Run the preflight that matches the received depth:
`$camera-group-preflight-fast` for `fast`, `$camera-group-preflight-standard` for
`standard`, and `$ai-video-prompt-preflight` for `full`. The depth is an input from the
decision layer (镜语) and is never chosen or re-tiered here. `$creative-production-ledger`
records an actual generation attempt only when generation is performed.

Must return: mode assumptions, platform-compatible prompt wording,
reference-token preservation, `compiled_by`, `compile_count=1`, risk notes, and
a pass/repair decision. A preflight returns findings or named field patches,
never a rewritten full prompt. Do not claim a model feature without current
source or inspected evidence.

Task-card interface:

```text
TASK_CARD
owner:
objective:
inputs:
must decide:
deliver:
state_patch_request:
uncertainty:
```

The brain merges cards into one state. `state_patch_request` may change only named fields; unresolved conflicts are surfaced to the user or resolved by the priority order above.

## Timing And Short-Drama Rhythm Contract

- A camera group is a set of consecutive shots, not one shot. Target 14-28 seconds, normally choose the shortest complete duration, and never exceed 30 seconds.
- Individual shots are normally 1-4 seconds. Allow longer shots only for a complete dialogue delivery, emotional hold, one-take action, or reveal that needs the time.
- Shot descriptions must be detailed enough to control generation while preserving human flow: state the opening support and weight, trigger, continuous path, contact/force transfer, breath and eyeline, secondary cloth/hair/prop motion, deceleration, recovery, and handoff state. Require anticipation, inertia, delayed reactions, natural blinking and asymmetrical micro-actions; prohibit mannequin stillness, instant pose changes, repetitive gestures, synchronized head turns, and mechanical speech timing.
- Estimate ordinary Mandarin dialogue at 2.8-3.2 Chinese characters per second, using 3 characters per second as the default average; restrained or emotional delivery at 2-3. Short urgent commands may briefly reach 3.5-4 characters per second, but never use that rate for continuous long sentences. Preserve pauses, breath, listener reaction, and usable lip-sync time.
- Keep the overall pace fast through shot density, motivated cuts, J/L cuts, action matches, escalation, and compressed transitions. Do not speed-read dialogue.
- Short-drama conflict gate: open each group with a visible hook or pressure within 1-2 seconds when the material supports it, reach an escalation, interruption, reversal, or power shift by the midpoint when the beat requires one, and end with a concrete consequence or changed state. Remove neutral setup, repeated face coverage, and any line/shot that does not change information, relationship, distance, control, or next action; do not manufacture conflict or reaction cuts when the script is intentionally quiet or a line is too short to need coverage.
- A group usually follows orientation or immediate hook -> intention/reaction -> escalation -> contact/turn -> consequence/hold. Peak around the latter half; reserve the final 2-4 seconds for consequence, changed status, or a stable handoff.
- Use a soft shot-count budget for review, not as a template: dialogue groups about 4-8 shots, emotion groups 3-6, action groups 5-10, hybrid groups 5-9 within 14-28 seconds. Override when line length, action causality, reaction value, or a deliberate one-take design requires it; otherwise merge repeated information or split at a completed turn.
- Every shot has one primary visible change and one dominant camera movement. Every action peak shows preparation, contact or near-contact, receiver/environment response, and recovery when physically relevant.
- For dialogue, cuts are driven by gaze, power shift, prop movement, interruption, semantic pause, or a physical source sound. Prefer letting a speaker finish a sentence or natural half-sentence before cutting and avoid splitting a word; this is a soft continuity preference, not a law. Motivated impact, danger, interruption, reaction snap, or reveal cuts may occur earlier if the remaining speech continues as an audible bridge and stays intelligible. Do not cut once per sentence by habit.
- Close-up policy: default to wide/full, medium, and medium-close framing for ordinary dialogue, geography, blocking, and movement. Reserve CU/ECU for strong action or power peaks, decisive gaze, force/contact detail, or critical prop evidence. Show position or staging changes in wide/medium first. Do not push directly into a face; push toward upper-body relation, hands, props, or two-person composition. Keep near shots waist-up or wider with shoulders, hands, eyeline, or relationship context; avoid face-only and consecutive close-up chains.
- For action/VFX, use one dominant effect family per beat, keep contact visible, and let camera ownership pass from initiator to receiver/consequence after force transfer.

## Mode Profiles

Select one primary profile before dispatch:

| Profile | Primary proof | Typical coverage |
|---|---|---|
| story/dialogue | information and power shift | 35-85mm, eye-level/over-shoulder, restrained pushes and reverses |
| fight/action | force, route, contact, changed spacing | 24-50mm, full-body proof, low/side tracking, short inserts only for contact |
| VFX/magic | source, operation, scale, consequence | establish geography, source insert, propagation, receiver/environment response, decay |
| emotion/beauty | micro-expression and relationship change | held medium/close shots, eye-line, breath, distance, soft motivated movement |
| hybrid | one dominant profile plus one support | keep the support subordinate; split if both demand equal peak complexity |

## Required Visible Delivery

When formal delivery is approved, output in this order:

1. 制作假设与目标模式。
2. 素材完整性检查与补充清单。
3. 剧情/视听目标与连续性锁定。
4. 每个镜头组的总时长（14-28秒）、功能、开场状态、结束状态和参考素材职责。
5. 每组一张仅供人理解的镜头表，逐镜标明时间、时长、景别、机位/视高/角度、焦段/镜头感、对焦景深、布光方向/光质/色温/阴影、运镜、说话者/听者/旁观者、动作/台词、反应载体、转场承接。
6. 每组一个独立完整可复制提示词，固定六段顺序：`角色/资产锁定 -> 视觉材质总控 -> 镜头语言总控 -> 事件节拍 -> 声音 -> 正向稳定约束`。
7. 生成前预检：通过/需修改、最大风险、缺失锁定、建议拆段、下一轮只调一个变量。

The human shot table never enters the prompt block. Every prompt block restates every shot in natural language with exact time window, duration, shot size, camera setup/movement, speaker/listener/witness coverage, visible reaction, action, dialogue, sound cue, and handoff. Use `@角色名` for every uploaded platform character handle and exact name-based `@图片名` / `@视频名` / `@音频名` for references supplied with the script; numbered `{{Image N}}` / `{{Video N}}` / `{{Audio N}}` tokens remain backend mapping only.

## Platform Adapter

- If the user names Seedance 2.5 or 2.0, load `$seedance-20` and the necessary current references before making platform claims.
- If the version is unspecified, write natural-language prompts compatible with both versions, keep the six-part structure, and place unverified interface parameters outside the copy-ready block.
- Preserve character `@` handles exactly as supplied. Preserve file/reference handles exactly as the current Liu format requires.
- Treat each camera group as one standalone generation unit. State its visible first frame and stable endpoint; use accepted prior footage only when it is actually supplied.

## Final Arbitration Checklist

Before delivery, the brain confirms:

- reference roles are explicit and missing P0 evidence is surfaced;
- exactly three concepts were offered at the concept gate or a direct-execution override was explicit;
- one leader owns each control surface;
- timing totals add up and dialogue has natural speaking time;
- groups are 14-28 seconds and never over 30 seconds;
- camera grammar, action physics, VFX lifecycle, performance, sound, and material behavior serve the same event;
- every prompt is standalone, positive, reference-scoped, and Seedance-compatible;
- preflight has a concrete risk and a single next variable when a retry is likely.
