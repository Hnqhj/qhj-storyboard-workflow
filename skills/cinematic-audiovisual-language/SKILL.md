---
name: cinematic-audiovisual-language
description: "Design formal audiovisual language for substantial film, AI-video, storyboard, shot-list, image-to-video, prompt-to-video, and generated-video diagnosis: shot function, framing, camera angle, axis, blocking, continuity, montage, rhythm, and sound-image relations. In the script-camera-group workflow, use as a separate Skill only on full depth; fast and standard use fused camera rules."
---

# Cinematic Audiovisual Language

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Purpose

Use this skill before adding visual spectacle. It turns an idea into a readable audiovisual sequence where every shot has a narrative function, a spatial logic, a camera choice, and a reason to cut.

If the sequence does not yet know what new information each shot contributes, why the next shot exists, or how visible behavior carries implied emotion, receive a shot-level information skeleton from `$shot-information-progression` first. That Skill owns viewer-knowledge delta and redundancy diagnosis; this Skill remains responsible for shot size, camera position/path, blocking, axis, continuity, sound-image grammar, and concrete cut mechanics.

If the scene already has a clear information skeleton but lacks a dominant key image or needs camera geography reverse-derived from an imagined frame, receive a master-shot blueprint from `$master-shot-camera-planning`. That Skill owns selection of the indispensable master images and their scene-level reverse derivation; this Skill validates and completes the general axis, continuity, camera-path, cut, and sound-image grammar.

This skill should run before more decorative prompt work such as high-tension effects, style polish, or material realism. If the user asks for "张力", combine this skill with `high-tension-shot-design` after the audiovisual structure is sound.

For a pure weapon, armor-function, movement-system, or character-ability showcase with no required opponent, hand the chapter architecture and showcase-specific shot progression to `$action-showcase-direction`; keep this skill responsible for shot function, geography, continuity, and cut logic.

## Reference Routing

Read only the reference needed for the task:

- `references/shot-function-grammar.md`: use for any storyboard, shot list, or video prompt. It defines how to make shots exist for a reason.
- `references/continuity-space-editing.md`: use for multi-shot action, chase, travel, dialogue, fight, or any sequence where screen direction and spatial clarity matter.
- `references/staging-mise-en-scene.md`: use when blocking, city scale, character placement, power relation, set design, color relation, or frame composition matters.
- `references/sound-rhythm.md`: use when timing, pacing, cut rhythm, sound design, music, impact beats, or J/L cuts matter.
- `references/ai-video-shot-planning.md`: use when packaging the final answer as an AI video prompt for Jimeng, Seedance, Kling, Runway, Sora, Veo, or similar tools.
- `references/source-map.md`: source links and research notes behind this skill.

## Reference 拉片 Protocol

When the task is to analyze a reference video, especially when the user says "拉片" or "整个都看", build a whole-clip shot grammar before writing a new prompt.

Track the whole reference across:

- first-frame hook and final-frame payoff;
- location geography, blocking, foreground/midground/background hierarchy, and screen direction;
- shot-size sequence, camera height, lens feel, movement family, and when the camera changes ownership;
- transition devices: action match, occlusion, whip, light, shape, impact frame, sound bridge, or motivated discontinuity;
- action-camera coupling: which body motion creates each camera opportunity, and which camera move proves a real action feature;
- rhythm density: orientation length, escalation compression, peak duration, release/aftermath hold;
- effects and sound as continuity tools, not decorative cover.

For each strong moment, record what the shot proves. Do not reduce a reference to "cool style" or "dynamic camera" if the useful lesson is actually blocking, cut reason, action vector, environmental reaction, or sound timing.

If the reference cannot be fully accessed, say exactly what was inspected and mark the rest as user-described evidence.

## Workflow

1. State the dramatic purpose in one sentence:
   - What should the viewer understand, feel, or anticipate by the end of the sequence?
2. Translate the temporal hinge if one exists:
   - turn "刚刚" into visible residue, "正在" into present action, "即将" into warning signs or anticipation, and "已经" into consequence.
3. Define the spatial path:
   - Where does the subject start, where does it move, what direction dominates the screen, and what changes at the end?
4. Build shots by function, not by vibe:
   - establish, orient, initiate, escalate, obstruct, reveal, impact, release, or transform.
   - when the brief requests special storyboard expression, design a contrasting multi-shot chain with large changes in scale, height, angle, depth, and viewpoint while preserving one continuous action phrase.
5. For action involving meaningful mass or weapons, get the physical profile from `$action-choreography-reference`: support, center-of-mass path, weapon balance, contact response, braking, and recovery. The camera must reveal those mechanics rather than replace them.
6. For each shot, specify:
   - function, subject, action, shot size, camera height/angle, lens feel, camera movement, screen direction, duration, transition, and sound/visual beat.
7. Run a continuity pass:
   - preserve axis, screen direction, eyeline/action matches, identity, prop scale, environment geography, and lighting direction unless breaking them intentionally.
8. Run a rhythm pass:
   - vary shot length and shot scale. Use stillness before speed, a readable impact point, and a release beat after the peak.
   - verify action-camera coupling: each camera choice reveals or amplifies the performer's pose, route, acceleration, contact, reaction, or recovery.
   - shape a density curve rather than distributing cuts evenly: orient with longer readable shots, compress only around escalation or exchange, then widen or hold for consequence.
9. Package the prompt:
   - compile into Liu's six-part positive-only order: 角色/资产锁定 -> 视觉材质总控 -> 镜头语言总控 -> 事件节拍 -> 声音 -> 正向稳定约束. Put the complete camera style in `镜头语言总控`; ordinary event beats inherit it, and only a special-camera beat adds a local trigger plus visible result.

## Mass Readability Camera Rule

For heavy bodies, weapons, creatures, collisions, and throws:

- establish feet, support points, weapon length, and available braking space before the peak;
- use wide/full-body framing for startup, contact, and recovery;
- hold long enough to see receiver reaction and changed spacing;
- use inserts only for one grip shift, foot brace, cable tension, joint compression, or vibration detail;
- keep camera movement calmer than the body during heavy action;
- never use shake, speed lines, blur, or debris as the only evidence of force.

For substantial score, music, sound-design, AI music, orchestration, mix, or cue-sheet work, hand off to `$cinematic-music-sound-design`. This skill keeps sound-image grammar; the music skill supplies the deeper musical and acoustic system.

## Locomotion Camera Coupling

When a shot's credibility depends on visible walking, running, pursuit, stairs, slopes, or uneven terrain, couple the camera to the subject's route without mechanically locking it to each step:

- match average camera travel velocity to the subject while preserving slight inertial lag, catch-up, and settle;
- keep background parallax consistent with travel direction, distance, and lens perspective;
- frame the support/contact area when grounding is the proof task;
- use intentional relative drift only for a visible function: the subject outruns camera, a threat gains, a destination reveals, or braking becomes readable;
- coordinate motion blur with relative velocity: stable tracked layers stay more readable, foreground and background streak according to their screen-space speed.

Do not ask the body and camera to accelerate independently. Hand action support and gait phases to `$action-choreography-reference`; hand contact/material response to `$ai-material-realism`.

## Mandatory Camera Movement Grammar

For AI video prompts, do not confuse composition with cinematography. A good frame is not enough: each major beat must define how the camera moves through the action, what owns the camera at that moment, and why the movement happens.

Use this compact internal checklist before finalizing any substantial video prompt:

```text
name-style camera anchor: [director / cinematographer / film / studio / work]风格 + [concrete visible camera result]
camera tracking owner: subject / vehicle / weapon / threat / receiver / environment line / sound source
camera path: push / pull / side-track / chase / arc / descend / rise / whip / drift / recoil / handoff / motivated lock-off
movement motivation: acceleration, obstruction, scale reveal, contact, recoil, foreground wipe, danger, gaze shift, sound cue, or consequence
information proved: route, speed, friction, mass, contact, scale, spatial relation, state change, or emotional consequence
handoff/endpoint: next owner / consequence path / final camera state
```

Rules:

- Use locked-off shots only as deliberate pressure, ritual stillness, surveillance, tableau, or aftermath; otherwise add motivated movement.
- Avoid sequences that are merely `wide shot -> close-up -> overhead -> low angle`. Add the camera path between those positions.
- Let subject motion create camera opportunity: the car outruns the camera, a door forces a vertical rise, a body wipe hides a cut, a collision freezes the camera, a scale reveal pulls the camera back.
- In fast sequences, vary ownership: establish from environment, chase the subject, let the subject pass camera, hand off to consequence, then pull back for new spatial state.
- When writing final prompts, first invoke one selected anchor as `X风格 + visible camera result`, then include motion verbs such as 贴地追, 平行跟拍, 前方倒退, 垂直下降, 被甩到侧面, 半圈绕出, 猛拉远, 穿过前景遮挡, 跟随反冲. Technical verbs support the noun-style phrase and never stand alone.

## Coverage-Critical Cut Declaration

The camera master defines the film's default camera family; it does not by itself guarantee that a generator will create the required cuts. When a close-up, insert, wide proof shot, POV, or shot-scale jump is indispensable to the event, instantiate that coverage inside the relevant event beat.

Use a compact contract:

```text
cut trigger -> new shot size / height / angle / lens relation
-> one proof task -> continuity handoff
```

Rules:

- Use explicit `cut`, `瞬间插入镜头`, `切超远景`, or another concrete cut trigger when the shot change is output-critical.
- Change at least two visible camera attributes at a critical cut: scale, height, angle, lens relation, viewpoint, path, or tracking owner.
- Give the new shot one proof job: takeoff plane, gap width, contact point, receiver response, scale, route, or changed state.
- Preserve vector, axis, eye trace, and action phase across the cut; do not restate the whole camera master.
- If the sequence can succeed as one take, keep coverage flexible. If a cut is necessary to prove the event, master-layer language such as `穿插特写` or `多景别` is insufficient on its own.

## Action Camera Relay

For close combat, weapon exchanges, pursuit, and partner action, assign the camera a current tracking owner:

```text
X风格 + [visible pressure/contact result] -> follow the initiator during setup and acceleration
-> let the body or weapon outrun the camera and break the foreground
-> decelerate or briefly lock at contact
-> hand tracking ownership to the receiver's recoil, fall, slide, or redirected path
-> recover to a readable two-body or wide spatial state
```

Rules:

- Track one primary force event at a time; do not chase both performers independently.
- Keep camera speed slightly below the fastest body or weapon layer so movement remains visible inside the frame.
- Use a short 20-60 degree arc only when it reveals a contact plane, power shift, or new spacing.
- Let jump, fall, low sweep, or level change motivate camera elevation; avoid unmotivated vertical drift.
- At contact, show the bind, deflection, recoil, receiver response, and changed spacing before the camera accelerates again.
- Foreground weapon, cloth, limb, debris, or light may cover the frame only briefly; after the wipe, restore subject count, axis, and geography immediately.

## Temporal Hinge To Shot Grammar

Do not leave time words as literary explanation. Convert them into image and sound:

- **刚刚**: residue in costume, body, prop, environment, or expression; e.g. suitcase, wet hair, fading smile, half-finished drink, dust, fresh wound, screen still glowing.
- **正在**: playable present action; e.g. walking, checking a phone, wiping blood, laughing, hesitating before a door, starting an engine.
- **即将**: incoming pressure; e.g. unread notification, siren far away, shadow entering frame, phone vibration, door light changing, crowd pausing, engine tone rising.
- **已经**: consequence; e.g. smile gone, object dropped, route blocked, identity revealed, color state changed, sound cuts out.

Use cuts to reveal the time hinge: close-up of residue, medium shot of present action, insert or sound cue for incoming pressure, then reaction or consequence. This creates emotion without forcing the model to perform abstract psychology.

## Anti-Repetition Shot Ledger

For multi-shot or 10s+ prompts, create an internal shot ledger before finalizing:

```text
Beat / temporal cue / function / X风格 + visible camera result / tracking owner / shot size / camera height / lens feel / camera path / trigger / screen direction / subject action / proof/new information / handoff-endpoint
```

Revise the sequence if two adjacent beats repeat four or more columns without a deliberate reason. A strong sequence usually varies:

- shot size: extreme wide, wide, medium, close-up, insert, POV
- camera height: ground-level, waist-level, eye-level, overhead, worm's-eye
- camera path: locked, push, pull, side track, arc, vertical rise, snap pan
- subject action: wait, notice, launch, dodge, collide, choose, reveal, escape
- information: location, threat, route, identity, prop state, emotional change, consequence

For manga/comic-style cutting, preserve screen direction and axis while changing panel scale and silhouette. The cut should feel like a designed page turn, not a random camera teleport.

## Special Multi-Shot Expression

When the user asks for `特殊分镜表现手法 / 多分镜 / 多景别 / 多特殊角度`, do not merely increase shot count.

Build one connected action phrase:

```text
spatial anchor
-> intent/detail insert
-> full-body trajectory proof
-> special-angle acceleration or reversal
-> contact/reaction proof
-> wide consequence or new spatial state
```

Adjacent shots should strongly contrast in at least two dimensions—function, scale, height, angle, lens relation, depth, or viewpoint—but inherit:

- action direction and current action phase;
- target or eye-trace position;
- axis and scene geography;
- body/weapon trajectory;
- an outgoing visual or audible element when useful.

Treat body and camera as reciprocal choreography. The character's extreme pose or route creates the reason for the camera position; the camera then amplifies that same action through perspective, compression, pursuit, opposition, or reveal.

Use the information ladder when a complex action needs multiple views:

```text
intent detail
-> route or full-body trajectory proof
-> contact relationship
-> receiver/environment consequence
```

Give each shot one distinct information job while preserving the same vector, phase, eye trace, and target relation.

Prompt-ready line:

```text
X风格 + [具体可见动态运镜结果]；[动作/冲击/遮挡]触发镜头跟随[对象]沿[路径]移动，证明[威胁方向/尺度/接触/位移/状态变化]，并由[视觉或声音事件]交接下一镜。相邻镜头改变景别、机位高度、透视或主客观视点，同时继承同一动作矢量、动作阶段、眼动落点和空间轴线。
```

## Camera / Shot-Style Master Layer

For final AI-video prompts, especially action, monster, chase, transformation, character PV, or any prompt where Liu has complained that 镜头风格 was forgotten, add a compact camera / shot-style master before the timed shot list. Treat it as a required control layer, not decoration.

The layer should include:

- the intended shot language in one or two dense sentences;
- a compact compatible set of named director / cinematographer / studio / film / work anchors, each tied to one visible camera result;
- if Liu asks for 特殊分镜表现手法, replace the vague phrase with named anchors and role assignments first; do not rely on "特殊分镜、多分镜、多景别" alone as the main control;
- the shot-size range, including extreme close-up, over-shoulder, low angle, wide scale proof, or poster-like terminal frame as needed;
- the allowed movement family: handheld pressure, FPV chase, orbit, whip pan, push-pull, tilt, speed ramp, freeze / impact frame, etc.;
- for each movement family, the tracking owner and motivation: who/what the camera follows, why it moves, and what state or spatial information it proves;
- the transition logic: foreground wipe, body-block cut, smoke reveal, impact cut, reflection cut, hard smash cut, or delayed reveal;
- what each shot must prove: threat direction, scale, contact, friction, mass transfer, displacement, state change, or final dominance.

Treat the detailed owner/path/trigger/proof/handoff design above as backstage shot planning. For Liu's paste-ready prompt, `镜头语言总控` is the single owner of the default camera system: named aesthetic anchors, perspective, lens family, distortion, movement energy, framing/edit rhythm, transition language, and reveal logic. `事件节拍` inherits it and normally writes action, state change, contact, consequence, and handoff only. Add a local camera clause only for a genuine special device or exception, with its trigger and concrete visible result.

Default wording Liu has validated as useful:

```text
镜头风格母版：扳机社动画美学 + 极端透视与高能构图；金田透视法 + 近大远小的夸张纵深；FPV超广角 + 贴近动作路线的高速穿行；强桶形畸变 + 边缘外弯的速度压力。事件节拍默认继承；只有特殊镜头需求才局部补写“触发原因 + 特殊运镜 + 可见结果”。
```

If this layer is missing from a substantial copyable video prompt, the prompt is incomplete.

## Fixed-Scene Blocking Lock

When the whole clip happens in one location, lock the stage before writing timed beats. AI video models often rebuild the set after every cut, so define stable coordinates:

```text
固定横屏舞台：闸门/主背景 = 画面中后景；角色 = 画面左前景/中景；摩托/道具 = 角色右后方；红色面板 = 画面右侧背景；移动路径 = 从左前景到中景闸门识别区。
```

Rules:

- Use one master spatial relationship for the whole clip.
- Camera changes are allowed and often correct, but each change needs a continuity bridge: establishing wide shot, eyeline match, action match, insert close-up, foreground occlusion, whip/black-frame transition, or motivated reverse angle.
- Use wide shots to reveal position. Use close-ups, inserts, foreground obstruction, reflections, or body/prop details to hide small position changes.
- If a new camera side is used, state that subject positions are unchanged; only the camera has moved.
- Inserts and close-ups do not need to show full geography. They only need to preserve hand/prop/eyeline direction, then return to the established master geography.
- For one-scene SD2 prompts, avoid asking every shot to prove exact geography. Lock position in wide/master shots; let close-ups carry detail and conceal micro-drift.
- A blocking/layout reference image can control stage position better than text alone. Assign it explicitly as "layout/blocking reference only" and prevent it from overriding identity, style, or lighting.

## Translating Abstract Blocking Boards

If the user supplies or needs a CAD/color-board layout reference, treat it as stage geography, not final imagery:

- Convert color blocks into screen-space relationships: foreground, midground, background, left/right, near/far, overlap, and action path.
- Preserve front/back hierarchy. If one block crosses in front of another on the board, the shot plan must state which subject visually occludes or leads the other.
- Preserve long-axis direction for elongated objects. Vehicles, long props, tables, doors, platforms, bridges, screens, and weapons need a screen direction or nose/end direction, not just a location.
- Preserve subject orientation separately from location: standing point, body facing, gaze/attention direction, and movement path are different locks.
- Use the board to set master geography, then allow close-ups/inserts to hide small drift. Do not require every insert to reproduce the whole board.
- When switching camera angle, restate that the physical layout from the board stays fixed and only the camera moved.
- If the final shot is not top-down, do not ask the model to generate a top-down diagram. Translate the board into normal cinematic camera language.

Generic blocking prompt phrase:

```text
Use @ImageX only as an abstract stage map: preserve object footprints, front/back layer, long-axis orientation, facing/gaze direction, action path, and left/right relationship. Final shots use cinematic camera angles; do not reproduce the diagram, labels, arrows, grid, or color blocks.
```

## Output Shapes

For diagnosis:

```text
问题诊断：
- 镜头功能：
- 空间连续性：
- 节奏：
- 需要重写的点：
```

For a storyboard:

```text
视听目标：
时间铰链：
空间路径：
镜头名词风格母版：[compact compatible X风格 + visible camera result anchor set]
分镜：
1. [时长] 功能 / 动作 / X风格 + 可见动态运镜结果 / 跟随对象 / 路径 / 动作或冲击触发 / 证明任务 / 交接或终点 / 剪辑或声音
2. ...
连续性锁定：
正向稳定约束：
```

For a direct AI video prompt:

```text
【角色/资产锁定】...
【视觉材质总控】...
【镜头语言总控】[complete camera style: aesthetic anchors + perspective + lens family + distortion + movement energy + framing/edit rhythm + reveal logic]
【事件节拍】[action/state/contact/consequence beats; local camera clause only for a genuine special-camera need]
【声音】...
【正向稳定约束】...
```

## Quality Gate

Before finalizing, check:

- Can the viewer tell where the subject is before the shot becomes stylish?
- Does each shot change information, emotion, power, space, or speed?
- If time words drive emotion, are they visible as residue, present action, warning sign, or consequence?
- Does the cut have a reason: action match, viewpoint reveal, impact, contrast, time compression, or rhythm?
- Is the screen direction stable enough that action does not feel like teleportation?
- Is there one dominant camera move per shot?
- Does `镜头语言总控` contain the complete camera style, while ordinary event beats avoid repeating it and special-camera beats alone state trigger + visible result?
- Are locked-off shots deliberate tension choices rather than missing运镜?
- Are shot sizes varied instead of repeating the same cool angle?
- If special multi-shot expression is requested, do the shots strongly contrast while still reading as one continuous physical phrase?
- If the storyboard is based on a reference, was the whole reference grammar considered before extracting a few attractive shots?
- Does the performer create the camera opportunity, and does the camera reveal or amplify a real action feature?
- Is there a clear camera tracking owner, and does ownership change only when initiative or force transfer changes?
- Does shot density form a deliberate curve instead of equal-duration coverage?
- If an effect or foreground object hides a cut, does the subject and geography become readable immediately afterward?
- For weighted action, can the viewer see support, center shift, contact response, and inertia resolution?
- Does the last shot resolve or invert the first shot?

## Avoid

- Do not write a list of "cool camera moves" without shot functions.
- Do not write only fixed shot descriptions when the medium is video; if the camera does not move, explain why stillness is the pressure.
- Do not use low angle, drone shot, slow motion, whip pan, orbit, and crash zoom in the same short shot.
- Do not cut every 1-2 seconds unless the sequence has a clear rhythm map and readable anchors.
- Do not make every shot the same energy level. Contrast creates tension.
- Do not rely on "cinematic, dynamic, high tension" as a substitute for spatial and editing logic.
- Do not crop out feet and recovery when weapon weight or balance is the point.
- Do not cut at contact before recoil, receiver response, or the new spatial state is visible.
- Do not break the axis or screen direction accidentally. Break it only when the intent is confusion, shock, or disorientation.
