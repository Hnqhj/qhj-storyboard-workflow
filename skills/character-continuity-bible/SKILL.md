---
name: character-continuity-bible
description: "为反复出现的角色、服装、武器、道具、场景建立连续性锁。身份或状态连续性脆弱、跨场跨集、参考职责冲突、或完整档 ExecutionPlan 选中时使用。快速与标准档不要单独调用。 Build and maintain continuity locks for recurring characters, costumes, weapons, props, locations, multi-shot sequences, and reference-driven AI image/video generation. Use when identity or state continuity is fragile, cross-scene or cross-episode, reference roles conflict, or a full-depth ExecutionPlan selects it. Do not invoke separately on script-camera-group fast or standard routes; their fused planners handle straightforward local continuity."
---

# Character Continuity Bible

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this skill to create a compact continuity bible that can be reused across AI-video prompts. The goal is to keep identity, costume, props, world rules, spatial logic, and shot-to-shot details stable.

This skill is especially important before generating series clips, action scenes, character reels, short dramas, or any image-to-video sequence where the same person/weapon/location must persist.

## Liu Default: Face-First Character Reference

For Liu's character setting/reference sheets, identity utility outranks atmosphere. Make a large, clearly lit face close-up the dominant panel; do not spend the primary area on an environmental hero image.

Use this default hierarchy unless Liu specifies another board type:

```text
large face identity close-up
-> front/back full-body proportion and costume views
-> expression or profile evidence
-> weapon/prop transformation and material details
-> small action silhouette when useful
```

The face close-up should normally occupy about 40-55% of the board and remain large enough to preserve bone structure, eye shape, eyelids, nose, lips, jaw, hairline, skin texture, age, and asymmetry. Use neutral or softly modeled light that keeps both facial structure and skin material readable. Atmosphere may unify palette and mood, but it must not hide, miniaturize, backlight, or stylize away the identity reference.

Do not use the atmosphere-first world-board ratio for a production character reference. If a project also needs an atmospheric character hero image, generate it as a separate asset or keep it as a small secondary panel.

## Persistent Entity Handoff

Use `$entity-continuity-system` before this Skill when the project needs a durable cross-shot, cross-episode, or cross-model registry with entity IDs, state IDs, approved views, versions, source/licensing fields, and write-back rules. This Skill remains the prompt-facing compiler: select the current approved entity/state version and turn it into compact identity, costume, prop, scene, spatial, and negative locks for the present generation. Do not maintain two competing sources of truth.

Use `$invariant-exploration-director` when the same task must deliberately separate hard continuity locks from bounded or open exploration variables. It defines variable ownership; this Skill writes the continuity-relevant hard locks.

## Workflow

1. Extract stable anchors: face, hair, body type, costume, colors, weapon, props, material, world, scene, lighting.
2. For action characters, extract the physical identity: body mass/strength class, dominant hand, base stance, weapon length, grip, mass distribution, and whether the character stops, redirects, or absorbs force.
   - When the character recurs across fights and must remain recognizable through movement, read `references/character-combat-identity.md`. Compile the approved combat role, primary basis, preferred range, force/rhythm/recovery signature, small function-tagged move pool, and drift boundary; keep per-scene choreography flexible.
3. When a user supplies preferred body proportions, lock them as adult character proportion rules and keep them subordinate to identity, action readability, costume design, and safety boundaries.
4. Separate flexible traits from locked traits.
5. Write a reusable continuity block.
6. Write negative locks for common drift.
7. For multi-shot work, add per-shot allowed changes and forbidden changes.
8. If prompt packaging is needed, combine with `$jimeng-sd2-prompting`.

## Narrative-Function Continuity for Props

Track a recurring prop by both appearance and dramatic function. Record what it opens, remembers, proves, motivates, transforms, and must still accomplish later. Before adding a new relic, token, weapon accessory, key, bell, photograph, letter, or talisman, compare its proposed function with every approved story-critical prop.

If an approved prop already carries the same function, reuse that prop and advance its state rather than inventing a substitute. A same-function substitution is continuity drift even when the new object looks compatible. New props are permitted only when their function is distinct, their relationship to existing props is explicit, and they do not steal a later payoff.

For each story-critical prop, lock:

```text
entity and approved visual state
current owner and on-body/storage position
narrative functions already established
what event may change its state or ownership
what later payoff requires it to survive, remain recoverable, or remain recognizable
whether dream copies, projections, or replicas may appear, and how they are distinguished from the one physical original
```

## Ontology and Agency Lock

Continuity includes what an entity is capable of wanting, knowing, feeling, choosing, and remembering. For every recurring nonhuman entity, record its ontology and control source before writing behavior:

```text
ontology: sentient / instinctive / possessed / memory echo / illusion / automated defense / environmental mechanism
control source: self / summoner / world system / relic / parasite / recorded memory
available agency: choice, planning, emotion, recognition, self-preservation, sacrifice
behavior grammar: trigger-response, imitation, hunting instinct, command execution, learned tactics, or free decision
```

Do not use human emotion as a shortcut for readable motivation when the entity lacks agency. Show priority and causality through target selection, interrupted commands, synchronized reset, stimulus response, resource routing, structural reconfiguration, or environmental control.

## Adult Character Proportion Preference

Use this only for adult characters, especially adult female or feminine-coded character design. Do not apply it to childlike, minor, or school-age characters.

Preferred proportion lock when aligned with the user's brief:

```text
Adult stylized heroic/fashion-action proportions: nine-head-tall body ratio;
legs occupy about two thirds of total height; navel sits near the body's golden-ratio
division; hourglass body line with approximately 0.7 waist-to-hip ratio; tight inward
waistline; rounded lifted hips; naturally upright chest line; toned thighs without
bulk; long slender calves; fine bony ankles; clean flowing arm lines.
Keep the design elegant, athletic, and action-capable; no pornographic framing,
no childish body/face combination, and no anatomy that breaks movement credibility.
```

Compact Chinese prompt block:

```text
成年角色比例锁定：九头身，腿长约占身高三分之二，肚脐位于全身黄金分割附近；沙漏型身材，腰臀比约 0.7，腰线紧致内收，臀部浑圆上翘，胸部线条自然挺拔；大腿紧致、小腿纤细修长、脚踝纤细骨感、手臂线条流畅利落。整体为高级时装/动作角色比例，保持运动可信度，不低俗化，不幼态化。
```

## Action Physics Continuity Lock

Use this when the same character or weapon appears across action clips:

```text
Physical identity remains constant: [actor] keeps the same mass/strength class,
dominant hand, stance logic, acceleration signature, recoil tolerance, and recovery
speed. [Weapon] keeps the same length, grip, mass distribution, center-of-mass
relation, flexibility, and braking demand. Camera changes may alter appearance,
but must not turn a heavy head-loaded weapon into a wrist-light prop or make a
light character directly stop giant mass without a brace, redirection, or powered assist.
```

Lock current transformed forms separately. When the weapon form changes intentionally, declare the new physical profile and handling behavior rather than inheriting the old form's timing.

For recurring fighters, physical identity is necessary but not sufficient. Use `references/character-combat-identity.md` to preserve how the character claims range, answers pressure, changes initiative, and recovers. Send approved profile versions to `$entity-continuity-system`, and let `$action-choreography-reference` solve the current opponent and scene inside those bounds.

## Series Silhouette Diversity Lock

Use this for teams, color-coded series characters, recurring casts, or any set where style unity must not make every character feel like the same body template.

Keep shared series traits:

```text
same medium/style family, same render finish, related costume construction,
coherent palette system, shared world/brand logic, compatible weapon design language
```

Vary each member deliberately:

```text
height impression, limb length, torso/hip/shoulder balance, posture, facial attitude,
hair volume, expression rhythm, weapon scale, stance width, movement tempo,
silhouette outline, amount of exposed skin, jacket/skirt/pants shape, shoe mass
```

Prompt rule: state "same team visual language, different silhouette and personality." Do not copy the same adult proportion block blindly across a team unless uniformity is the point.

## Spatial Continuity Lock

For one-scene clips, lock spatial relationships as part of continuity, not only identity:

```text
空间锁定：同一横屏场景，同一闸门，同一摩托，同一角色站位关系。闸门固定在画面中后景，角色固定在画面左前景到中景之间，摩托固定在角色右后方，红色控制面板固定在画面右侧背景。只允许角色手部、头部和一步以内的位置变化，不允许人物、摩托、闸门互换位置。
```

Use this whenever the user says 站位变了, 背景漂移, 一会儿左一会儿右, 同一场景控制不了位置, or the clip has close-ups inside one location.

Reference rule:

- If a layout/blocking reference exists, declare it separately from identity/style references.
- Use it to lock relative positions, camera framing, object scale, left/right relationships, and action path.
- Do not require close-up shots to prove the full stage; use close-ups to preserve hand direction, eyeline, prop position, and action continuity.

## Abstract Layout / Color-Board References

When a user needs stronger position control, prefer an abstract layout/color-board reference over a pretty scene reference. The board should encode spatial logic, not character design:

- Use simple color blocks, circles, rectangles, arrows, paths, and optional grid lines.
- Create a clean machine-facing board without text whenever it will be uploaded as a reference.
- Create a separate labeled board or legend only for human checking.
- Assign each color/shape in the prompt: character, vehicle, prop, set piece, door, panel, obstacle, target point, action path, camera direction.
- State that the board controls only relative position, front/back layer, orientation, scale, left/right relationship, and action path.
- Forbid copying blocks, arrows, labels, grids, diagram style, simplified shapes, and color marks into the final video.

Object footprint rules:

- Do not mark large objects as points. Use their footprint: rectangle, oval, strip, circle, or zone.
- For any elongated object, encode its long axis and nose/front/end direction with a block shape plus arrow. This applies to vehicles, long props, tables, doors, platforms, bridges, signs, screens, weapons, and any object whose direction matters.
- If an elongated object crosses in front of or behind a subject, place the block in the correct layer on the board. Do not merely put it beside the subject.
- For a character or moving subject, encode at minimum: standing area, body facing direction, gaze/attention direction if relevant, and movement path if the shot includes displacement.
- For set pieces, encode fixed location and interaction target points separately. Example: the gate area and the checkpoint/scan point are not the same lock.
- For occlusion, encode foreground/midground/background explicitly in the prompt. The model must know whether one object blocks another or sits behind it.

Reusable prompt role:

```text
@ImageX: abstract color-board layout/blocking reference only. It controls only relative positions, front/back layer, object footprint, long-axis orientation, facing direction, action path, left/right relationship, and scale. Do not copy color blocks, arrows, labels, grid, diagram style, or simplified shapes into the final video.
```

Read `references/continuity-template.md` for field templates and lock language.

## Output Shape

```text
连续性圣经：
身份锁定：
服装/道具锁定：
世界/场景锁定：
可变化范围：
禁止变化：

可直接粘贴：
...
```

For multi-shot:

```text
全片锁定：
镜头1允许变化：
镜头2允许变化：
转场连续性：
负面限制：
```

## Guardrails

- Do not lock every detail. Lock what matters for recognition and continuity.
- Put identity and prop locks early in the prompt when they are critical.
- If a reference image exists, name its role: identity, costume, prop, scene, lighting, or pose.
- When a computable pose guide would reduce ambiguity, use `$creative-production-ledger` to extract a lightweight skeleton and declare it `pose/blocking reference only`; never let it override identity, costume, materials, lighting, or world style.
- For action scenes, lock weapon length, grip, color, and silhouette.
- Also lock actor strength class, weapon mass distribution, handedness, support logic, and recovery signature when weight is story-relevant.
- For video, add persistence language: "全程保持", "不随镜头变化", "不变形", "不漂移".
