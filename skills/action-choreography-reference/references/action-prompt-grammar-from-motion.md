# Action Prompt Grammar From Motion

Use this reference when turning a whitebox preview, mocap clip, game animation, single move, or combo fragment into AI video motion prompt language.

The goal is not to name the move. Preserve the move's force path, rhythm, inertia, peak, recovery, and connectable end state.

## Core Contract

Every action prompt must answer five questions:

1. Where does the force come from?
2. What route does the body or weapon travel?
3. Where is the peak impact, near miss, or visual climax?
4. How does inertia carry through after the peak?
5. What stable state does the character end in, and what can it connect to next?

If one answer is missing, the generated action often becomes slow, floaty, twitchy, or resets awkwardly.

## Motion Reading Checklist

For each source action, record:

- Intent: suppression, chase, launcher, guard break, dodge punish, finisher, reposition, or display beat.
- Start state: stance height, foot support, torso twist, weapon side, and stored tension.
- Preload: crouch, shoulder coil, hip turn, backstep, drag, guard lift, off-axis lean, or breath hold.
- Route: horizontal, diagonal, vertical, thrust, rising, falling, spiral, side cut, back turn, or crossing step.
- Speed curve: hold, sudden release, burst, impact beat, drag, rebound, brake, recovery.
- Weapon/body lag: whether the weapon trails behind the hips, pulls the torso, overshoots the body, or forces a recovery step.
- Peak: contact, near miss, slash arc, ground hit, body pass-by, pose silhouette, or camera-side crossing.
- Follow-through: where the hand, weapon, torso, and feet continue after the peak.
- Brake: planted foot, slide, spin-out, kneel, two-hand catch, blade drag, shoulder stop, or landing compression.
- End state: weapon front/back/high/low, body facing, weight foot, distance traveled, and what next move can start from it.
- Camera proof: what the camera must show so the motion reads clearly, usually full body for support and closer only at the peak.

## Single Action Prompt Template

```text
动作基底：角色执行一个[动作功能]，不是静态摆拍。
开场状态：角色已经处在[低/中/高]重心，[哪只脚/哪条腿]承重，身体向[方向]拧紧，武器/手臂停在[位置]，能看到蓄力。
起势：先由[脚/髋/肩/背/手腕]发力，[压缩/滑步/扭身/后撤/下沉]，把力量存到[身体部位/武器方向]。
释放：随后动作沿[路线]爆发，身体从[起点]冲到[终点]，武器/手臂滞后半拍后追上身体。
峰值：在[时间点/画面位置]出现最强剪影，[斩击/突刺/砸击/撞击/近失]明确改变空间关系。
跟随与刹车：峰值后不要立刻停住，惯性把[武器/手臂/衣摆/身体]继续带到[方向]，角色用[脚步/转身/拖刃/落地/下压]刹住。
结束状态：角色停在[可连接姿态]，武器位于[下一招可借力的位置]，重心稳定但还有余势。
镜头：镜头主要保持全身可见，峰值处短暂加强透视或贴近，但不能遮掉脚步、支撑和武器路线。
负面限制：不要慢动作拖满全程，不要站桩挥手，不要每招结束回正到中立姿势，不要用镜头抖动代替动作。
```

## Natural Prompt Pattern

Use this style when the final output should be paste-ready rather than analytical:

```text
开场就是动作中段。角色处在[压缩/滑步/回身/落地/拖刃]状态，[支撑脚/重心/武器位置]清楚可见。
动作先从[脚/髋/肩/背]发力，[身体路线]带动[武器/手臂]，但[武器/手臂/衣摆]滞后半拍后才追上。
峰值发生在[具体空间位置]，[接触/近失/斩线/砸地/穿过镜头前景]清楚改变画面关系。
峰值后不要切走，惯性继续把角色带向[方向]，他/她用[滑步/转身/拖刃/落地压缩/肩部下沉]刹住。
结尾停在[下一招可接状态]，而不是回到中立站姿。
```

## Combo Prompt Pattern

For combos, never write a list of unrelated named attacks. Each move's end state must become the next move's preload.

```text
这是一套连续连招，不是几个单招硬切。每一招的结束姿态都成为下一招的起势来源。

第一段：[起势来源] -> [路线] -> [峰值] -> [结束时武器/身体位置]。
第二段：借第一段的[回弹/拖刃/转身/落地/侧移]继续发力，改走[新路线]，在[新高度/新方向]制造第二个峰值。
第三段：角色不回到中立，直接从[上一段末端姿态]转入[追击/上挑/回旋/下砸/突刺]，速度曲线为[短停顿/反弹/二次爆发]。
终结段：用[更大位移/更低重心/更高跃起/更重刹车]完成收束，最后停在清晰的强剪影。
```

Continuity bridge formula:

```text
上一招结束状态 -> 可借用的惯性/姿态 -> 下一招起势来源
```

Example:

```text
第一刀拖到身后低位，不回正；后脚滑步追上重心，借剑身回弹把身体带成反向转髋，第二刀从背后低位斜上挑出。
```

## Good Versus Bad Wording

Bad:

```text
角色快速挥剑，很有力量。
```

Good:

```text
后脚蹬地，髋部先转，重剑拖在身后半拍后横扫追上身体，斩线穿过镜头前景；余势把剑带到背后，角色用前脚滑步刹住。
```

Bad:

```text
角色跳起来砍一刀。
```

Good:

```text
上一段回旋的反弹把身体带离地面，双膝先收紧，重剑从低位绕到头顶；角色在下落瞬间斜劈，落地时肩和剑一起下沉，地面承受冲击。
```

Bad:

```text
连续三连击。
```

Good:

```text
第一刀从右低位斜上挑，把身体打开；剑落到左肩后不回正，角色顺势转髋做第二刀横扫；横扫拖到身后时后脚追上重心，直接改成短距离突刺，最后用剑尖下压刹住。
```

## Weapon Notes

### Greatsword / Heavy Sword

- Show weight through lag, overshoot, recovery cost, and braking.
- The sword often moves after the hips; hands do not make all the power.
- Good transitions come from drag, rebound, shoulder catch, blade resting behind the body, or planted-foot rotation.
- Avoid endless fast wrist cuts.

Prompt cue:

```text
双手握重剑，剑身明显滞后身体半拍；每次变向都由脚步和髋部先改线，剑的重量把肩膀继续拖过峰值，角色必须滑步、转身或拖刃才能刹住。
```

### One-Hand Sword / Katana

- Use sharper guard changes and cleaner directional cuts than greatsword.
- Feet still need support; do not let the upper body perform alone.
- Good transitions come from guard return, sheathing-line recoil, side cut, passing step, or wrist-led redirection after the body has already set the line.

### Spear / Polearm

- Emphasize reach, hand sliding, shaft alignment, and distance control.
- Good transitions come from thrust recoil, staff spin, butt-end counter, step-through, or planted shaft braking.

### Unarmed

- Show contact logic through hip, shoulder, elbow, knee, or foot chain.
- Avoid pure upper-body flailing.
- Each strike should change distance, angle, balance, guard state, or initiative.

## Camera Rules

- Use full-body framing when judging or generating action clarity.
- Camera motion can orbit, push, whip, or dip only to reveal the action route, not to hide missing motion.
- Peak frames may use low angle, near-weapon foreground crossing, or slight speed ramp.
- Show feet during preload, support, landing, and braking.
- For AI video prompts, specify 30 fps output when needed while preserving smooth in-between motion and clear body mechanics.

## Rejection Rules

Reject or rewrite a motion prompt when it contains:

- action names without force-path description;
- "fast, cool, powerful" without support, route, peak, and recovery;
- hard reset to neutral between moves;
- full-time slow motion;
- floating jumps without takeoff or landing compression;
- weapon acceleration after the body has already stopped, unless explained as rebound or secondary swing;
- camera cuts that hide the body during the actual transition.

## Catalog Fields

When storing validated action assets, add these prompt-facing notes:

- `prompt_intent`
- `start_state`
- `motion_route`
- `speed_curve`
- `peak_frame_note`
- `follow_through`
- `end_state`
- `connects_well_to`
- `prompt_seed_sentence`

