# User-Calibrated AI Video Lessons

Use this reference when the user asks to summarize past AI video work, update the skill suite, build a new prompt from the user's recurring taste, or diagnose repeated failures across action, character PV, camera, style, material, or Seedance/Jimeng packaging.

These are generalized controls extracted from repeated user-reviewed generations. Keep them as mechanisms, not project history.

## 1. Prompt Output Contract

- For final generation prompts, provide one standalone positive-only copyable block in the fixed six-part order; translate current risks into `正向稳定约束`.
- Keep planning notes, review diagnosis, and preflight outside the copyable block.
- If the user says "directly give me all of it", deliver the full prompt, not a patch fragment.
- Do not include testing goals inside the prompt. The prompt should describe the film, not explain why the test exists.

## 1.1 Liu Local Asset Format And Whitebox Video Roles

Use Liu's exact name-based @reference format in final prompts:

```text
@角色立绘.png（角色身份、服装、脸、造型参考）：锁定身份与外观。
@动作预演.mp4（动作、节奏与运镜参考）：锁定动作节奏、身体重心、镜头远近与切镜逻辑。
```

Rules:

- Do not invent or shorten uploaded @names, use generic `参考图1`/`图1`, or output `@material[...]` and pseudo material-layer tags for Liu's paste-ready prompts.
- A whitebox / Blender / mocap video is evidence for movement, weight, camera distance, shot-scale changes, edit triggers, and action continuity; it is not an aesthetic, material, character, environment, or final-render reference.
- In the final copy block, use the fixed order `角色/资产锁定 -> 视觉材质总控 -> 镜头语言总控 -> 事件节拍 -> 声音 -> 正向稳定约束`; bind scoped exact `@图片名（...参考）` / `@视频名（...参考）` handles inside `角色/资产锁定` rather than adding a seventh `素材映射` section.
- Convert current risks into short positive present-state locks; keep exclusion, correction, and old-failure wording outside the paste target.

Hard enforcement:

- When a supplied reference is used, its first paste-ready mention must use the exact uploaded @name plus a parenthesized role scope: `@图片名（...参考）`, `@视频名（...参考）`, or `@音频名（...参考）`. Generic prose such as `参考图1` or `第一张图` is not an equivalent.
- For action-led video, put the complete default camera identity in `镜头语言总控`: named aesthetic anchors, perspective, lens family, distortion, movement energy, framing/edit rhythm, transition language, and reveal logic. Event beats inherit it. Only a genuine special-camera beat adds a local trigger and concrete visible result; repeating the master in every beat is unnecessary.

## 2. Visual Master Before Shot Detail

For this workflow, global visual style usually controls the result more strongly than detailed shot instructions. Put the visual master near the beginning:

```text
medium / aesthetic family / palette ownership / line and shape language
-> material-light system / render hierarchy / optical behavior
-> forbidden style drift
```

Only after that write action, camera, and local effects. Do not bury style rules after the shot list.

## 3. Clean-Slate Prompt Hygiene

When starting a new character, style, scene, or action test:

- do not carry old project-specific props, weapons, locations, monsters, colors, or negative examples into the new prompt;
- keep only reusable rules such as single-subject lock, no extra characters, no early terminal pose, readable contact, no weapon morph, no old motion mode;
- if an old failure must be blocked, express it as a universal behavior ban rather than naming the old concept.

This prevents prompt dependency, such as a new character inheriting a previous character's skating, rail, shadow, weapon, or scene logic.

## 4. Keyword Contamination And Visual Compensation

Use this lesson whenever a prompt failure looks irrational: the model disobeys a negation, over-amplifies an unintended association, flips an object toward the viewer, shows the wrong side of a subject, or turns an abstract camera/action instruction into a generic compensation image.

Principle:

```text
loaded word / denied word / abstract intent / camera label
-> model attention
-> associated stereotype, task prop, role costume, default environment, or compensation image
```

Do not store the source video's examples as a fixed blacklist. They are evidence of the mechanism, not the mechanism itself. For each new prompt, infer the current contamination source from the concept, medium, subject, action, camera request, negative constraints, and expected model association.

Common contamination families:

- denied nouns: the prompt says a thing should be absent, but the word itself still attracts its usual environment, costume, prop, activity, or genre;
- loaded task labels: a compact activity/profession/tool word brings default props and screen-facing proof that may violate the desired pose or angle;
- abstract relation verbs: intention, gaze, orientation, awareness, or interaction is not directly visible, so the model compensates with face, eyes, icons, labels, or unnatural object rotation;
- camera labels without proof: shot-size or angle names may be weaker than visible surfaces, occlusion, scale ratio, and frame occupancy;
- old-failure negatives: naming the previous wrong output can accidentally preserve it as a salient concept.

Repair pattern:

```text
1. Identify the current prompt's likely association cluster.
2. Remove the contaminating label when it is not essential.
3. Replace it with positive visible evidence of the desired frame.
4. Describe what is in frame, not what the character conceptually understands.
5. Keep negatives only for broad failure classes that are likely but not conceptually central.
```

General conversion recipes:

- activity label -> hand/body/object mechanics, visible prop side, interaction contact points, and the part of the action the camera should prove;
- profession/role label -> only the required visible garment/tool/material/setting traits, without importing the whole stereotype package;
- body-quality label -> silhouette, cloth tension, posture, proportion, muscle/fat distribution visible through clothing, and light/shadow proof;
- orientation/gaze/attention verb -> visible side surfaces, head/body axis, hidden/revealed facial features, target placement in frame, and gaze cue only if it is visible;
- shot-size/angle label -> subject frame occupancy, visible surfaces, foreground/background scale, occlusion, lens height, and shadow/edge proof.

Negative prompt and context-rewrite rule:

```text
Negative slot is not a memory of the old failure.
Context rewrite is not a contrast with the old context.
Both must be converted into the new visible target state.
```

- Before writing negatives, ask whether the forbidden noun is part of the target shot. If not, remove it unless it is a broad artifact class or a truly likely extra element.
- Do not use negative constraints to name a previous project-specific prop, creature, location, color, style, action mode, or failed image. Replace with a universal behavior ban or a positive lock.
- When retargeting a prompt to a new context, write it as a clean stateless shot: current subject, environment, prop state, action path, palette, camera relation, and visible constraints. Avoid "not like before", "no longer", "instead of", or old-context contrast language in the copyable prompt.
- If a negative repeats a salient unwanted concept more strongly than the positive side describes the desired concept, the negative is likely harmful.

Camera-control use:

- 拉近镜头：把提示词注意力分配给近景才看得清的小表面、局部结构、材质反光、缝线、手部/面部/道具细节。
- 拉远镜头：把注意力分配给主体占画面比例、地面足迹、周围环境、地平线、尺度关系和全身轮廓。
- 换角度：不要只写景别名；写该角度能看到的表面、遮挡、投影、轮廓、前后关系和被隐藏的部分。

## 5. Timing Confidence And Terminal Hold Audit

Exact timestamps are useful only when macro timing is known from a reviewed output, reference, animatic, edit map, music cue, or physical action budget.

Use exact chapter ranges, not exact internal cut timing, when confidence is high. Otherwise use causal order.

Always audit:

```text
Does each interval contain enough action?
Does the strongest peak arrive too early?
Does the final hero hold start before the last 1-1.5 seconds?
Is a simple gesture stretched into idle pose?
Does recovery disappear because the peak is too late?
```

For 15-second character/action clips, a final beauty hold longer than roughly 1 second is risky unless the user explicitly asks for a fashion/portrait ending.

## 6. Clip Mode: Character PV, Pure Showcase, Fight

Choose the mode before writing beats.

### Character PV

Primary job: sell identity, face, body type, attitude, color ownership, prop/weapon, expression, personal rhythm, and one iconic image.

Structure:

```text
entrance / identity reveal
-> expression or attitude turn
-> signature prop or motion proof
-> style-specific transition
-> short payoff icon
```

PV can include action, but not continuous fighting unless the prompt explicitly asks for action showcase.

### Pure Action Showcase

Primary job: prove a weapon, movement system, armor function, or ability. No opponent is required, but every peak must change state: route, support, weapon function, elevation, floor trace, environment, or final silhouette.

### Fight / Duel

Primary job: initiative and response. Every exchange needs entry, control point, receiver answer, contact/near-miss proof, cost, and changed state.

Do not let these modes collapse into each other. A PV that becomes only attacks loses character; a showcase that becomes only posing loses function; a fight that becomes only smooth movement is usually imagined.

## 7. Action Foundation

Action must be designed from state changes, not verbs.

For each major beat:

```text
preload or setup
-> commitment / burst
-> contact, near miss, or mechanism proof
-> receiver / prop / floor / air response
-> follow-through
-> braking or recovery
-> changed state
```

Avoid default openings where characters stand still before fighting. Use standstill only for ritual, dread, intimidation, or a deliberate stillness-before-burst beat.

## 8. Fantasy Escalation

Real movement reference is a base, not a ceiling. For fantasy clips, build:

```text
real support and weight
-> fantasy function
-> stylized camera / timing / impact exaggeration
```

If the action looks too realistic or ordinary, add one or two readable impossible functions, not a cloud of VFX. Examples: launched target, impossible axial attack, chain-saw ground bite, gravity snap, shadow misdirection, brush-stroke movement trail, naked-eye 3D foreground rupture.

## 9. Camera And Transition Proof Points

High-tension camera should prove something. Use 4-6 functional proof points rather than a long move list:

```text
identity proof
support / full-body proof
contact or mechanism close-up
vertical or route proof
extreme-wide consequence
short final icon
```

Action-led transitions should have:

```text
outgoing source -> frame coverage or matched vector
-> incoming shot inherits direction, contour, material, light, or sound
-> geography or changed state becomes readable
```

Avoid decorative orbiting, random rolls, repeated eye-level medium shots, and effects that replace contact.

## 10. Style And Material Quality

Advanced style comes from hierarchy and restraint, not more effects.

Always define:

- color ownership and forbidden palette drift;
- material surfaces and roughness response;
- key/rim/bounce light direction;
- AO/contact shadows at feet, seams, folds, contact points;
- highlight rolloff and shadow detail;
- what stays readable during motion blur.

For thick-painted / 2.5D / NPR looks, distinguish bold brushwork from dirty noise:

- use deliberate large brush planes, broken edge accents, visible directional strokes, clean value hierarchy;
- avoid random speckle, muddy backgrounds, full-frame grain, over-busy graffiti, and texture that destroys silhouette readability.

## 11. Reference And 拉片 Discipline

When reviewing a reference, inspect the whole work before extracting transferable parts:

- macro structure and retention;
- camera grammar;
- action grammar and speed curve;
- style and material finish;
- transitions/VFX;
- expression/performance;
- sound hierarchy;
- what not to transfer.

Do not transfer only a cool moment if the full clip's structure is doing the real work.

## 12. Video Review Discipline

When the user says "look at this", inspect the video before diagnosing.

For action/PV, always check:

- first-frame state;
- whether the required beat order happened;
- action density across the whole 15 seconds;
- whether final pose starts too early;
- whether the weapon/prop remains the same class;
- whether contact/mechanism is proven or only implied by light;
- whether the clip is the right mode: PV, showcase, or fight.

Report:

```text
what works and should be preserved
main failure
likely cause
next round changes only one main variable
what not to change
```
