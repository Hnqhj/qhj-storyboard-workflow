---
name: high-tension-shot-design
description: Add strong visual tension to AI image and video prompts through cinematic shot size, camera angle, composition, storyboard beats, camera movement, speed sensation, editing rhythm, lens/framing choices, motion effects, and prompt-ready shot language. Use when the user asks for 张力, 压迫感, 高级镜头, 分镜, 景别, 构图, 运镜, 镜头感, 速度感, 节奏, 剪辑节奏, 电影感, 动态镜头, 生图参考, 视频参考, shot design, shot size, camera movement, storyboard, cinematic tension, anime impact, action rhythm, or wants a still/video prompt made more powerful, dramatic, fast, oppressive, epic, lonely, unstable, or memorable.
---

# High Tension Shot Design

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Purpose

Turn a flat image/video idea into a high-tension visual plan. Choose a precise composition, camera angle, camera motion, shot rhythm, and effect vocabulary that makes the scene feel stronger without becoming cluttered or incoherent.

For video prompts, this skill strengthens an existing audiovisual plan; it does not replace one. Establish shot function, spatial path, axis/screen direction, blocking, and cut reason with `$cinematic-audiovisual-language` before adding high-tension mechanisms.

## Model-Executable Tension Layer

Do not output only "more tension", "more cinematic", "more oppressive", "faster", "more epic", or "stronger composition". Translate tension into a visible pressure mechanism.

For every high-tension beat, specify:

```text
Tension source:
Eye anchor:
Pressure device:
Frame geometry:
Camera behavior:
What changes by the end:
What must stay readable:
```

Translation rules:

- **Pressure** = distance closing, blocked exit, scale mismatch, edge trapping, foreground obstruction, countdown, weather, crowd, weapon, or sound threat.
- **Speed** = stable subject anchor + fast foreground pass + background parallax + route obstacle + consequence frame.
- **Danger** = visible proximity to harm + escape cost + consequence, not random shake.
- **Epic / awe** = scale proof + delayed reveal + small human/object comparison + readable hierarchy.
- **Instability** = one motivated destabilizer: tilt, handheld, roll, subjective POV, or occlusion; not all at once.

Bad:

```text
镜头更有张力，更压迫，更电影感。
```

Good:

```text
Eye anchor is the character's left hand gripping the door frame. The corridor walls converge behind him, the monster shadow enters from the right foreground, and the only exit is blocked by a swinging red warning light. Camera makes a slow 30cm push-in; face, hand, exit line, and shadow edge stay readable.
```

For a pure action, weapon, transformation, or ability showcase, use `$action-showcase-direction` first to define the display contract, chapter contrasts, shot-function ladder, sourced transitions, and final icon. Add only one dominant tension device per beat afterward.

For a whole-film high-energy action look—large-format realism plus animation exaggeration, aggressive POV, unconventional framing, extreme shot-scale contrast, or a bounded free-camera envelope—use `$kinetic-action-visual-master` first. This skill then chooses the dominant tension device for each individual beat.

This skill is for both:

- AI image prompts: one decisive frame with strong composition and visual pressure.
- AI video prompts: one shootable movement or short storyboard beat with controlled camera motion.

## Reference Routing

Read only the file needed for the task:

- `references/composition-tension.md`: framing, power dynamics, negative space, scale, diagonals, foreground obstruction, depth.
- `references/shot-size-angle.md`: 景别, camera height, angle, lens feel, and when to use wide/medium/close-up/extreme close-up.
- `references/camera-motion.md`: push-in, pull-out, tracking, arc, roll, whip pan, dolly zoom, handheld, locked camera.
- `references/speed-sensation.md`: visual speed, acceleration, fast/slow contrast, motion blur, parallax, speed ramp, chase and vehicle energy.
- `references/storyboard-rhythm.md`: 3s/5s/8s beat design, reveal/impact/reaction structures, action and emotional pacing.
- `references/editing-rhythm-cuts.md`: cut rhythm, shot duration, match cut, jump cut, smash cut, invisible cut, eye trace, and AI-video equivalents.
- `references/storyboard-shotlist-library.md`: reusable shot-list patterns for action, reveal, chase, emotional rupture, product/vehicle, and character entrance scenes.
- `references/effect-vocabulary.md`: impact frames, motion blur, parallax, speed ramp, lens compression, silhouette, smoke/rain/sparks, anime impact.
- `references/ai-prompt-packaging.md`: how to package tension language for image generation and image-to-video/text-to-video tools.
- `references/source-map.md`: source links used to build this skill.

## Workflow

1. Identify the target tension:
   - pressure, speed, danger, isolation, intimacy, awe, instability, power, chaos, ritual, luxury, violence, silence, or emotional rupture.
2. Confirm the audiovisual base:
   - shot function, spatial path, screen direction, subject/action relationship, and cut reason are clear.
3. Pick one dominant visual mechanism:
   - composition, angle, lens, motion, edit rhythm, effect, or blocking.
4. For action sequences, design the tension across a shot chain:
   - use multiple shot functions, shot sizes, camera heights, special angles, foreground relations, and viewpoints;
   - preserve one continuous action vector, action phase, eye trace, and spatial relation;
   - make performer pose/path and camera response amplify each other.
   - assign camera tracking ownership and transfer it only when initiative, impact, or receiver motion changes.
5. Keep the shot readable:
   - one main subject, one main action, one camera movement, one emotional result.
6. Translate into prompt language:
   - describe what the viewer sees, how the camera behaves, what moves, what stays locked, and what must not happen.
7. For AI video:
   - keep one main action per 5-second clip.
   - make camera motion specific and limited.
   - avoid piling multiple camera moves into one short shot.

## Tension Mechanism Menu

Pick one dominant mechanism per beat, then rotate mechanisms across the sequence:

- **Scale isolation**: extreme wide city frame, subject is a tiny異色 mark crossing a huge ordered environment.
- **Worm's-eye launch**: camera below the subject/vehicle, sky or building canyon behind, subject cuts upward through frame.
- **Foreground rupture**: wheel, weapon, hand, debris, or light trail tears past the camera for a brief screen-breaking peak.
- **Telephoto compression**: far obstacles stack tightly, making speed feel dangerous and space feel narrow.
- **Overhead map turn**: top-down or high oblique angle reveals route, trap, gate, crowd flow, or changing city geometry.
- **Reflection pass**: action appears in glass, wet ground, visor, metal panel, or screen before the real subject crosses frame.
- **Negative-space pressure**: the subject is trapped near an edge of the frame while empty space or architecture dominates.
- **Stillness-before-burst**: hold a clean composition, then break it with one sudden action or cut.
- **Contact-lock relay**: follow the attacker into the exchange, let the weapon or body outrun the lens, briefly stabilize at contact, then continue along the receiver's recoil or redirected path.
- **Transformation frontier**: keep old surface, active changing edge, and completed new material visible in the same frame; follow the frontier instead of flooding the whole subject with effects.

For vehicle/action clips, do not use only side tracking. Combine scale, height, foreground, route reveal, and impact peaks while keeping screen direction readable.

## Action-Led Camera Constraints

- Keep camera speed slightly lower than the fastest performer or weapon.
- Use foreground rupture as a brief peak, not sustained screen coverage.
- Let body level changes motivate camera height changes.
- Use short arcs to reveal contact geometry; do not orbit merely to create motion.
- Reduce camera motion at impact, then release into recoil, displacement, or a wider consequence view.
- Alternate wide trajectory proof with close intention/contact views; do not hide every footstep and recovery in close-up.

## Output Shape

For quick enhancement:

```text
张力方向：
建议镜头：
构图：
运镜：
效果：

可直接粘贴：
...

负面限制：
...
```

For storyboard:

```text
分镜结构：
镜头1：
镜头2：
镜头3：

统一视觉锁定：
负面限制：
```

## Guardrails

- Do not produce a list of famous names without translating them into visible shot mechanics.
- Do not use tension devices as a substitute for audiovisual grammar. If the shot function, blocking, axis, or screen direction is unclear, fix that first.
- Do not confuse a whole-film kinetic envelope with a per-shot move list. Let `$kinetic-action-visual-master` define the permitted family; this skill selects one dominant mechanism for the current beat.
- Do not interpret “multiple shots, scales, and special angles” as disconnected coverage. Each change must continue the action, reveal new information, or alter the power/space relation.
- Do not combine too many tension devices. One strong mechanism usually beats six weak ones.
- Do not make every beat equally fast. Concentrate short shots and aggressive reframing around the escalation peak, then restore a readable result.
- Do not let an effect, blade, cloth wipe, smoke, or flash conceal the subject for more than the transition instant or replace the required contact/consequence view.
- Do not use fast motion when the intended tension is silence, dread, loneliness, or psychological pressure.
- For image-to-video, respect the input image composition and describe motion rather than re-describing static appearance.
- Avoid camera instructions that fight each other, such as locked-off camera plus handheld shake plus orbit plus crash zoom in one 5-second shot.
