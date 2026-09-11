# Action Rhythm Map

Use this map to design action timing for AI video prompts.

## Basic Beat Anatomy

```text
Anticipation -> Acceleration -> Peak/Impact -> Follow-through -> Recovery
起势 -> 爆发 -> 峰值/接触 -> 延展 -> 收势
```

Why it works:

- Anticipation makes the action readable.
- Acceleration creates energy.
- Peak gives the viewer the "hit".
- Follow-through sells weight.
- Recovery prevents floating motion.

## Mass And Inertia Timing

Get the physical profile from `$action-choreography-reference` and its `weapon-body-dynamics.md` reference before timing a weight-sensitive beat.

```text
grip-biased/light:
0.15-0.35s preload -> short acceleration -> 0.05-0.12s peak
-> 0.2-0.5s brake/recover

balanced/medium:
0.3-0.7s preload -> committed acceleration -> 0.06-0.15s peak
-> 0.4-0.9s follow-through/recover

tip-heavy/head-heavy:
0.6-1.2s visible load -> sudden committed acceleration -> 0.08-0.18s peak
-> 0.8-1.8s follow-through, braking, and stance recovery

flexible-delayed:
handle initiation -> delayed weighted-end peak
-> returning tension wave -> orbit/slack recovery
```

These are cinematic timing ranges, not fixed biomechanics measurements. Compress or expand them to fit the actor, style, frame rate, and dramatic purpose while preserving the order.

Superhuman rule:

```text
compress startup only if increased force becomes visible in floor traction,
air displacement, prop vibration, receiver response, or active mechanical damping
```

For a two-person exchange, expand the peak into a causal micro-loop:

```text
attacker setup 0.15-0.3s
-> committed strike 0.2-0.4s
-> defense/contact 0.06-0.15s
-> receiver reaction 0.15-0.3s
-> shared recovery/reposition 0.2-0.5s
```

Do not spend the whole beat on the attacker. The defender's response and the changed spacing are part of the action, not optional aftermath.

## Rhythm Transfer Across Action Types

Keep the causal rhythm while changing the moving system:

```text
human strike:
weight shift -> strike -> contact -> receiver recoil -> stance recovery

weapon exchange:
support/wind-up -> arc or thrust -> bind/contact -> body and weapon deflection -> guard reset

animal charge:
gait compression -> explosive stride -> ground contact or near pass -> dust/body response -> next stride

vehicle collision or near miss:
approach -> steering/braking commitment -> closest point/contact -> suspension/debris response -> corrected path

creature impact:
mass preparation -> limb/body acceleration -> terrain receives force -> secondary reaction -> mass settles

pursuit:
route commitment -> acceleration -> obstacle/near miss -> lead relation changes -> route recovery
```

The transferable structure is force preparation -> committed motion -> peak relation -> consequence -> stabilized new state.

## Density By Readability

- Contact-heavy close combat: one clear exchange every 0.8-1.5 seconds.
- Heavy weapons or giant mass: one peak every 1.5-3 seconds.
- Pursuit and parkour: route or obstacle change every 1-2 seconds.
- Group fight: one primary interaction at a time; secondary threats enter during recovery.
- Mounted or vehicle action: preserve carrier motion continuously; overlay one upper-body or weapon peak per short beat.

If the result becomes mushy, reduce peak count before reducing response clarity.

## Duration Templates

The following numbers are cinematic planning ranges. Promote them into exact macro-segment prompt ranges when timing confidence is high from evidence or physical analysis. Otherwise preserve phase order and relative duration without false precision. Exact micro-shot timing remains exceptional.

### 3 Seconds

Best for one micro-action.

```text
0-0.5秒：起势，身体压低或武器后拉。
0.5-1.8秒：爆发，动作快速完成。
1.8-2.1秒：短暂impact pause，火花/衣料/水花响应。
2.1-3秒：收势，动作惯性结束。
```

### 5 Seconds

Best default for AI action.

```text
0-1秒：起势，角色进入清晰预备姿态。
1-3秒：爆发，完成主要动作路径。
3秒：峰值卡点，接触/闪光/冲击短暂停顿。
3-5秒：follow-through，衣摆、发丝、武器、环境反应延续，角色落回稳定姿态。
```

### 8 Seconds

Best for one action arc plus reveal.

```text
0-2秒：建立姿态和空间。
2-5秒：动作推进，镜头跟随。
5秒：峰值/反击/落点。
5-8秒：结果展示，慢推或轻微后拉。
```

### 15 Seconds

Use 3 macro phases as a default, not equal-duration micro-shots.

```text
0-4秒：进入与起势。
4-9秒：主动作或追逐段。
9-12秒：峰值冲突/卡点。
12-15秒：收势、反应或悬念。
```

Density rule:

```text
begin with enough duration to establish identity, direction, support, and threat
-> shorten only during the exchange or escalation
-> make the decisive peak brief and readable
-> restore duration for reaction, displacement, braking, or reveal
```

Do not force exact internal timestamps when the action topology is uncertain. Exact macro ranges are useful only when the physical phase budget, music cue, or inspected reference supports them.

### 15-Second Action Showcase

Use this only for intentionally dense weapon/body displays. Treat the windows below as a maximum-density planning example, not compulsory equal-length shot instructions.

```text
0-2.5s: moving entry, first attack or shot while crossing the frame.
2.5-5s: direction change, slide/dodge/retreat, second distinct peak.
5-7.5s: transitional guard/parry/weapon-function change, third peak.
7.5-10s: jump, spin, vault, or strong body-level change, fourth peak.
10-12.5s: moving counterattack or moving shot, fifth peak.
12.5-15s: foreground 3D rush or hero finish, final peak and recovery.
```

Rules:

- Prefer 3-5 distinct action phrases. Use 5-6 peaks only when continuity is stable and each peak changes function, body level, route, or weapon behavior.
- Require visible displacement every beat: run, slide, retreat, jump, land, cross-frame, or Z-shaped footwork.
- If the user wants more shooting, specify that most shots happen while moving, not after standing and aiming.
- Use different action verbs across the six beats. Repeating "aim, draw, shoot" makes a 15-second clip feel empty.
- Change body level at least twice: standing -> crouch/slide -> jump/roll/inversion -> landing.
- Change spatial relation at least twice: toward camera, across frame, away from camera, foreground pass, side retreat.
- If the weapon has fantasy functions, assign a different function to different beats: shoot, slash, guard, hook, anchor, recoil burst, energy-string snap.
- Keep each peak short and sharp; impact frames should last about 0.08-0.12 seconds.
- Avoid long aim holds, repeated poses, standing rotations, and "showcase" language that lets the model idle.
- Preserve successful style from the previous iteration, then change only the action-density/spatial-displacement variable.

### 15-Second Anti-Idle Checklist

Before delivering a 13-15 second action prompt, verify:

- 3-5 distinct action phrases are named; extra peaks are justified by a new function.
- No single aiming, charging, posing, or slow-motion hold lasts longer than 2 seconds unless it is the final hero charge.
- Every beat has a body verb, a weapon verb, and a camera/framing intention.
- At least one beat crosses the frame and one beat uses depth toward/away from camera.
- The strongest peak is intentionally framed as the hero/impact/3D beat.
- Shot density rises toward the climax and releases afterward instead of remaining uniform.

Prompt shorthand:

```text
15秒内保持高动作密度：角色每2-3秒完成一个不同动作峰值，持续改变位置和身体高度，所有瞄准/蓄力都必须发生在移动、翻身、滑步或借力过程中，禁止原地长时间停顿。
```

## Rhythm Types

### Heavy Impact

Use for punches, hammers, heavy swords, monster hits.

```text
slow anticipation, sudden acceleration, brief impact pause, visible recoil, delayed debris and cloth movement, low-frequency sound hit
```

Mass-aware refinement:

```text
the weapon head lags during startup, overtakes through the peak, then pulls the arms and torso into a delayed brake; the feet or support surface resolve the remaining inertia before the next action
```

### Sharp Assassin

Use for knife, iaido, sniper-like precision, stealth.

```text
almost still anticipation, single explosive line, very short contact flash, clean follow-through, silence before and after the strike
```

### Graceful Flow

Use for wushu, staff, dance-like combat, magic action.

```text
continuous flowing motion, no hard stop until the final pose, fabric trails describe the arc, camera glides with the body
```

### Anime Impact

Use for exaggerated action.

```text
fast anticipation smear, one-frame high-contrast impact, brief freeze at the strongest silhouette, then explosive follow-through with debris arcs
```

### Chase Energy

Use for parkour or pursuit.

```text
steady running rhythm, obstacle beat every 1-2 seconds, camera stays low and close, landings recover immediately into forward motion
```

### Commercial Reveal

Use for product/action hybrid.

```text
slow setup, precise object movement, gliding camera, highlight sweeps across material on the beat, clean final hero frame
```

## Music Sync Language

Use when audio is involved:

```text
动作峰值卡在第二个鼓点。
拔刀瞬间对齐beat drop。
慢动作从音乐停顿处开始，重拍回来时完成斩击。
每次脚步落地对应低频鼓点。
```

English:

```text
the impact lands exactly on the second drum hit
the sword draw aligns with the beat drop
slow motion begins during the musical pause, full speed returns on the downbeat
```

## Camera Rhythm

Stable action:

```text
single low-angle tracking shot, no cuts, camera speed matches the subject
```

Heavy hit:

```text
camera holds during anticipation, micro shake only at impact, then stabilizes
```

Anime beat:

```text
brief impact frame, then return to motion, no long strobe
```

Chase:

```text
low handheld tracking, slight motion blur at edges, subject remains centered
```

## Prompt Block

```text
节奏：0-1秒起势，角色压低重心并拉开武器；1-3秒爆发，身体和武器沿一条清晰斜线加速；第3秒斩击峰值短暂停顿0.2秒，火花和衣摆在同一拍爆开；3-5秒完成follow-through，武器惯性下沉，角色稳定收势。镜头只做低机位稳定跟拍，冲击瞬间轻微震动。
```

## Negative Rhythm Blocks

```text
禁止动作无起势、无收势、持续乱挥、无限旋转、无重力漂浮、镜头乱切、节奏忽快忽慢、峰值不清。
```

For long action showcases:

```text
禁止原地站桩，禁止长时间瞄准，禁止重复同一个动作，禁止只在原地旋转，禁止动作拖成慢动作，禁止脚步没有位移，禁止峰值之间留空太长。
```

For music:

```text
禁止动作和鼓点错位，禁止多个峰值抢同一个beat，禁止画面闪烁代替动作。
```
