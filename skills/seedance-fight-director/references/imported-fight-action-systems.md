# Imported Fight / Action Systems

Use this reference for high-control fight, weapon, chase, action, anime battle, Wuxia, superpower, mecha combat, Seedance/Higgsfield action prompting, or when an output needs hit timing, start/end pose anchors, reference-material mapping, and failure diagnosis.

This distills the imported `武戏.zip` material:

- `角色打斗导演.md`
- `动作分解文档.docx`
- `武戏设计.zip` / `专业SD-05 打斗场景.zip`
- `战斗提示词工程-0628.pdf` examples

Do not override the main `seedance-fight-director` workflow. Use this as an extra precision layer.

## Liu Final Compilation Override

All imported `@material[...]`, legacy section order, negative slots, and HEAVY/RUSH/CHASE camera mechanics are backstage concepts only. Liu's final paste-ready prompt always uses the six-part positive-only order and exact scoped handles such as `{{Image 1}}（角色身份、外观、服装与武器参考）`. Compile the complete default camera identity into `镜头语言总控`; event beats inherit it. Only a genuine special-camera beat adds a local trigger and visible result.

## 1. Action anchoring taxonomy: A/B/C/D

Before writing a prompt, classify every important action.

### A. Start-pose required

Use a start-pose / 起始态 anchor when the action has:

- preparation, coiling, weight shift, muscle pre-tension;
- explosive acceleration;
- large center-of-mass change;
- weapon draw, swing, thrust, slash, block, kick, leap, throw;
- emotional escalation into physical action.

Examples:

- straight punch, hook, uppercut;
- whip kick, high kick, tornado kick, flying knee, sweep;
- sword draw, slash, thrust, parry, heavy overhead strike;
- spear/staff thrust or sweep;
- leap attack, charge, magic charge, power wave;
- dodge into counter, knockback, fall, thrown body.

Output requirement:

```text
start-frame prompt: feet, support base, knee bend, hip/shoulder coil, weapon line, eyes, breathing, target relation, pre-impact tension.
video prompt: from exact starting pose -> weight shift -> acceleration -> peak action -> recoil/recovery.
```

### B. In-motion only

Use a simple in-motion prompt when the action is continuous, low-force, looping, or naturally interpolated:

- normal walk, slow run, swimming, gliding, flying;
- waving, nodding, turning head;
- normal door open/close;
- picking up a light object;
- idle breathing, clothes moving, repeated dance groove.

Output requirement:

```text
the character smoothly [continuous action], steady speed, no sudden change, maintain exact appearance.
```

### C. Borderline: upgrade by drama

Default to in-motion, but upgrade to start-pose when emotion, plot importance, speed change, or slow motion matters.

Examples:

- normal turn -> in-motion; alert turn + draw weapon -> start-pose;
- ordinary open door -> in-motion; angry kick door -> start-pose;
- casual sit/stand -> in-motion; wounded rise or rage stand -> start-pose;
- pick up cup -> in-motion; pick up sword/key relic -> start-pose.

### D. Start + end pose / dual anchor

Use dual anchor when the final pose must connect to the next shot, or when the motion has clear preparation -> explosion -> follow-through.

Use for:

- draw + strike + finishing pose;
- jump: takeoff + aerial action + landing recovery;
- throw/fire: launch + arm follow-through;
- fall/knockback ending posture;
- magic charge + release + exhaustion;
- heavy push/breakthrough;
- ritual/emotional action with exact end state.

Output requirement:

```text
reference image 1: exact start pose
reference image 2: exact termination pose
video prompt: continuously performs the full action and arrives at the termination pose with natural recoil and balance recovery.
```

## 2. Dual-axis fight mode

When the user does not specify the fight rhythm, choose if obvious; if the rhythm changes the result materially, offer the three modes quickly.

### Visual style axis

| Code | Style | Use when |
|---|---|---|
| SCI | sci-fi / mecha | armor, cyber, exosuit, robot, energy weapon, space, engine thrust |
| WUX | wuxia / xianxia | sword, saber, qi, robe, lightness skill, Jianghu, ancient fantasy |
| MOD | modern realistic | MMA, boxing, street fight, tactical chase, urban brawl |
| FAN | fantasy dark | magic, knight, monster, elemental duel, cursed armor |

### Rhythm axis

| Code | Rhythm | Fight feel |
|---|---|---|
| HEAVY | heavy impact | 4-5 hit marks in 15s, slow tension, long hit-stop, massive recoil |
| RUSH | rapid combo | 10-15 hit marks in 15s, micro hit-stop, handheld/whip/cut rhythm |
| CHASE | pursuit/evade | 2-3 scarce impacts, lots of route change, one hit becomes a climax |

Use the rhythm to set timing, not just adjectives.

## 3. Hit-marking rules

Every real impact needs three visible proof layers:

1. **impact frame / hit-stop**: the motion briefly locks at contact.
2. **screen/environment reaction**: camera shake, ground slide, wall crack, water spray, robe snap, sparks, dust.
3. **directional particle/effect ejection**: material-specific, traveling along the force path.

Rhythm parameters:

```text
HEAVY: 80-150ms hit-stop, shake level 3-5, large particles, slow motion 0.2x-0.3x, 0.3-0.5s breathing gaps.
RUSH: 20-50ms micro hit-stop, shake level 1-2, small dense particles, one terminal heavy hit, minimal breathing gap.
CHASE: no shake during travel; on hit use 100-150ms hit-stop, shake level 4-5, speed drops from fast travel to 0.3x impact.
```

RUSH cluster format:

```text
Hit cluster @X.Xs-X.Xs (N hits):
#1 @X.Xs - [target/limb] | micro hold Xms | shake 1 | [small particles]
#2 @X.Xs - [target/limb] | micro hold Xms | shake 1 | [small particles]
terminal #N @X.Xs - [target/limb] | hit-stop Xms | shake X | [large burst]
```

## 4. Style-specific wording

Keep terminology within the chosen style.

SCI:

- arms/legs -> structural modules, actuator arms, support struts;
- hit -> impact face, striking module, kinetic contact;
- injury -> structural damage, surface delamination, energy leak;
- particles -> metal fragments, electric sparks, plasma arc, energy pulse.

WUX:

- arms/legs -> sword arm, palm line, footwork, body method;
- force -> qi infusion, inner-power rotation, waist-step coordination;
- reaction -> qi-channel disturbance, robe snap, body-line collapse;
- particles -> sword-qi arc, leaf/water/petal burst, robe fragments.

MOD:

- force -> hip drive, shoulder rotation, ground reaction, weight transfer;
- reaction -> stagger, slip, guard break, short freeze, clothing deformation;
- particles -> sweat spray, rain splash, dust, glass/wood/concrete debris.

FAN:

- force -> rune activation, elemental condensation, cursed-energy surge;
- reaction -> armor crack, magic shield fracture, elemental backlash;
- particles -> embers, ice shards, shadow fragments, rune collapse, soul afterimage.

## 5. Camera contract

The camera proves the action. It must not compete with it.

Core choices:

- HEAVY backstage mechanics: low angle, slow push, orbit, dolly zoom, close impact insert, aftermath stillness. Compile the default mass/pressure grammar into `镜头语言总控`.
- RUSH backstage mechanics: handheld follow, jump cut every 1-2 hits, whip pan along strike, frame skip, pivot spin around hit point. Compile the default speed/contact grammar into `镜头语言总控`.
- CHASE backstage mechanics: one-take tracking, Z-axis push, parkour POV, top-down route reveal, scarce impact speed-ramp. Compile the default pursuit/geography grammar into `镜头语言总控`; write a local beat clause only for a special exception.

Action camera checks:

```text
support point visible?
force path readable?
distance change visible?
defense/reaction visible?
endpoint state visible?
one dominant camera motion only?
```

## 6. Reference material mapping

For Seedance/Higgsfield, if the user provides images/video references, explicitly map them.

Higgsfield-style maximum planning assumption:

```text
up to 9 images + 3 videos can be used as references, if the actual surface supports it.
```

Use Liu's exact scoped handles in the prompt body, not only in a note.

Template:

```text
【角色/资产锁定】
{{Image 1}}（角色A身份、服装与武器参考）：锁定角色A。
{{Image 2}}（角色B身份、轮廓与尺度参考）：锁定角色B。
{{Image 3}}（环境空间、地面材质与光线参考）：锁定战斗场地。
{{Video 1}}（动作节奏、重心、路线与运镜参考）：迁移动作与镜头证据。
{{Image 4}}（色彩与渲染质感参考）：迁移视觉材质结果。
```

If the user gives a reference but not its role, ask one compact question: character, scene, style, action, composition, material, or endpoint?

## 7. Paste-ready action prompt shape

Use this when the user asks for final prompt:

```text
【角色/资产锁定】
{{Image N}}（...参考）：...  # replace N with the real supplied number
【视觉材质总控】
[arena geometry / surface / light / visible material response]
【镜头语言总控】
[complete camera style: named aesthetic anchors + perspective + lens family + distortion + movement energy + framing/edit rhythm + reveal logic]
【事件节拍】
[action/state/contact/consequence beats; local trigger + visible camera result only for a genuine special-camera need]
【声音】
[impact / movement / ambience / silence]
【正向稳定约束】
[identity / weapon / geography / camera-anchor / contact / material / endpoint locks]
```

For English prompts, keep action verbs concrete and timed:

```text
From the exact starting preparation pose, the character shifts weight through the rear foot, coils the hip and shoulder, accelerates into [action], reaches a clear impact frame at [time], then recoils into [ending state] with balance recovery.
```

## 8. Common failure fixes

- **No weight / floaty action**: add support foot, center-of-mass route, recoil, landing or braking.
- **Instant teleport**: add entry path, distance change, and one continuous camera relation.
- **Fake fight**: add control point: weapon line, guard, wrist, shoulder, centerline, angle, or route.
- **Weak impact**: add hit-stop timing, reaction cost, environment proof, directional particles.
- **Overbusy prompt**: reduce to one exchange, one route, one camera move, one endpoint.
- **Face/identity drift**: map identity refs explicitly and keep action reference role limited.
- **Cannot continue next clip**: produce a stable final pose and turn it into the next clip's start state.
