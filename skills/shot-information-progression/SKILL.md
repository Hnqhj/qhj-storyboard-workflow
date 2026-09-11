---
name: shot-information-progression
description: Design and audit shot-to-shot information progression before camera, lighting, style, and effects polish. Use when a storyboard, AI-video prompt, short film, ad, or generated sequence looks cinematic but says little; has 没信息点, 主体不突出, 氛围大于叙事, 镜头重复, 同一情绪反复推近/换景别, 不知道下一个镜头拍什么, 运镜没有理由, 工具很多却拼成缝合怪, or needs to explain why each shot exists and what new knowledge, emotion, question, proof, or consequence it hands to the next. Separate visible behavior from implied emotional purpose, require an information delta for every cut, and build the narrative skeleton that hands off to storyboard and audiovisual-language Skills. Do not use as the owner for complete storyboard drawing, camera/axis design, lighting, performance direction, or macro video structure.
---

# Shot Information Progression

Make every shot earn its place. Build the sequence from viewer knowledge and emotional interpretation before choosing decorative camera, lighting, color, style, or effects.

## Ownership

Own:

- the primary information point of each shot;
- the difference between visible behavior and its emotional/attitudinal purpose;
- the information delta between adjacent shots;
- the question, answer, contradiction, proof, or consequence handed to the next shot;
- redundancy diagnosis and the minimum narrative skeleton.

Do not own:

- macro hook/turn/payoff duration design: receive from `$video-structure-design`;
- master-shot-led blocking, axis, camera-zone, view-height, and connector blueprint: hand to `$master-shot-camera-planning` when the scene should be constructed outward from key images;
- full storyboard tables or drawings: hand to `$professional-storyboard-director`;
- shot size, axis, blocking, lens, movement path, continuity, and cut mechanics: hand to `$cinematic-audiovisual-language`;
- actor micro-performance: hand to `$performance-scene-director`;
- lighting, palette, material, atmosphere, and visual polish: apply only after this gate through the relevant visual Skills.

## Core Model

Treat each shot as two coupled layers:

```text
visible layer: who/what is present, what happens, and what state changes
meaning layer: why this behavior matters, what attitude/emotion it implies,
               and what the viewer should now understand or anticipate
```

Behavior is observable. Emotion is the viewer's interpretation of behavior, context, timing, and consequence. Do not command “angry/sad/cinematic” without a visible carrier.

## Workflow

### 1. Define the sequence output

Write one sentence:

```text
By the end, the viewer should understand/feel/anticipate ______.
```

If this is unclear, do not start choosing shots.

### 2. Identify the information carriers

A shot may foreground one primary carrier:

- person: identity, action, decision, reaction, relationship, power;
- object: condition, evidence, threat, memory, function, change;
- scene: geography, route, constraint, social order, time, scale;
- atmosphere: emotional pressure carried by concrete light, sound, weather, absence, motion, or material traces.

“Atmosphere” alone is not an information point. For a people-free image, specify:

```text
target emotion -> visible environmental evidence -> what changed or may happen
```

Example: not “warm light through blinds,” but “two untouched bowls cooling beneath the last warm window light; one chair has been pushed back abruptly, implying a recent departure.”

### 3. Build an information card for every shot

Use this internal card:

```text
Shot function:
Primary carrier:
Visible behavior/state:
Context needed to read it:
Primary new information:
Implied attitude/emotion:
Viewer question before:
Viewer state after:
Handoff to next shot:
```

Keep one foregrounded information point. A shot may contain secondary detail, but it must not compete with the primary reading.

### 4. Run the Information Delta Gate

The next shot must do at least one job the previous shot did not:

- add new information;
- reveal cause or target;
- show consequence or reaction;
- reframe the meaning of known information;
- contradict an assumption;
- answer a viewer question;
- create a stronger question;
- change spatial, social, temporal, or emotional state;
- deliberately withhold information while increasing pressure.

If none applies, merge, remove, or redesign the shot.

Bad progression:

```text
push into angry face -> cut to another angle of the same angry face
```

Better options:

```text
angry face -> reveal what he sees
angry face -> show the person receiving his anger
angry face -> show the damaged object/evidence that caused it
angry face -> show a restrained action that contradicts the anger
angry face -> show the consequence of his decision
```

Changing shot size is not automatically new information.

### 5. Order shots by causality and viewer state

Use compact chains such as:

```text
context -> behavior -> target/cause -> interpretation -> consequence
question -> partial answer -> contradiction -> decision -> changed state
residue -> present action -> incoming pressure -> reaction -> consequence
```

Choose the chain that fits the dramatic job. Do not use a generic sequence as a fixed formula.

### 6. Add camera only as proof

After the information chain is stable, state what the camera must prove:

- geography needs a wide spatial relation;
- decision needs readable face/body/prop relation;
- hidden cause needs a reveal or point-of-view handoff;
- material evidence needs an insert;
- power change needs changed blocking, height, distance, or frame ownership;
- consequence needs enough duration and space to register.

Then hand the chain to `$cinematic-audiovisual-language`. Do not choose push-in, close-up, orbit, dutch angle, or lens flare merely to create “film feeling.”

### 7. Add atmosphere as multiplication, not rescue

Lighting, color, haze, texture, music, and effects may intensify an established meaning. They cannot repair a missing subject, cause, relationship, or consequence.

Use this order:

```text
meaning -> information carrier -> causal sequence -> camera proof
-> performance -> light/color/material/sound polish
```

## Shot Ledger

For any multi-shot sequence, return or maintain:

```text
Shot / primary information / visible behavior / implied meaning
/ information delta / why now / question answered or created
/ handoff endpoint / camera proof requirement
```

Reject adjacent shots that repeat the same carrier, visible state, implied meaning, and viewer knowledge unless repetition is a deliberate pressure device. If deliberate, name what intensifies: duration, distance, obstruction, contradiction, or expected consequence.

## Storyboard And Reverse-Engineering Boundary

A storyboard is the first structural pillar of visual narration, not a guaranteed image of the finished edit. Production changes, performance, coverage, accidents, and editing alter the result.

When studying a finished film:

- infer shot function and information flow;
- do not pretend the final edit reveals the exact original storyboard or design process;
- transfer the mechanism, not the literal shot order;
- verify whether the new scene has the same dramatic condition before reusing a camera choice.

## Tool-Abundance Guardrail

More available methods create more possible combinations, not more meaning. Before using any tool, effect, camera move, transition, style preset, or AI reference, complete:

```text
I use [method] here because it reveals/changes/proves ______.
Without it, the viewer would miss/misread ______.
```

If neither blank can be filled, remove the method. Do not build a collage of individually attractive but causally unrelated techniques.

## Output Shape

```text
最终观众状态：
当前核心问题：
冗余诊断：

【镜头信息递进表】
镜头1：
- 可见行为/状态：
- 主信息点：
- 隐含情绪/态度：
- 相比前镜新增：
- 交给下一镜的问题/状态：
- 镜头需要证明：

镜头2：
...

删改建议：
交给分镜与视听语言的骨架：
之后才添加的表现层：表演 / 灯光 / 色彩 / 材质 / 音乐 / 特效
```

## Quality Gate

- Can the sequence's final viewer state be stated in one sentence?
- Does every shot have one primary information carrier?
- Is emotion attached to observable behavior, context, or consequence?
- Does every adjacent shot create an information delta?
- Does a close-up reveal something, or merely repeat the same face?
- Does camera movement prove information rather than advertise technique?
- Can a people-free atmosphere frame identify its emotional target and evidence carrier?
- Are lighting and style amplifying meaning rather than replacing it?
- Is the storyboard treated as a production base rather than a deterministic final edit?
- Can every tool choice complete the “because it proves…” sentence?

Read `references/information-delta-grammar.md` for the diagnostic matrix and `references/source-case.md` for the source conversation distilled into this method.
