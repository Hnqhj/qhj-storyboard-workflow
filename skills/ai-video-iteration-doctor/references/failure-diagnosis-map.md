# Failure Diagnosis Map

Use this map to choose the next retry change.

## Symptom Table

| Symptom | Likely cause | Next fix |
|---|---|---|
| Face changes | identity lock too late/weak; camera too aggressive | move identity lock to first sentence, reduce rotation, use reference role |
| Clothes change | costume not described as locked | add costume anchors and "全程保持不变" |
| Weapon morphs | prop shape/size not locked; action too complex | lock weapon silhouette, size, grip, and reduce movement |
| Action feels soft | no start/peak/follow-through; weak action verb | add action reference, impact pause, recoil, follow-through |
| Camera chaotic | too many camera moves | choose one move, add stable camera, remove extra motion |
| Background drifts | scene not locked; camera travel too large | lock spatial anchors, reduce camera distance |
| Material looks plastic | no roughness/reflection/imperfection | add physical material controls |
| Style looks cheap/generic | no medium domain, no aesthetic system, effects instead of hierarchy | add visual-style-aesthetic-direction block: medium, style family, color ownership, hierarchy, anti-cheapness |
| Render terms did nothing | AO/PBR/GI/anisotropy used as loose keywords | bind render terms to visible surfaces, seams, contact points, and light sources |
| Subject looks pasted into background | missing contact shadows, AO, shared light, bounce light | add contact shadows, ambient occlusion, shared key/rim light, global illumination bounce |
| Metal/fabric/hair looks flat | no roughness/anisotropy/topology | add roughness map, anisotropic highlights, normal/bump/displacement/topology controls |
| Clip flickers | overloaded details or duration too long | simplify scene, shorten clip, lock key elements |
| Motion too weak | verb too passive; no moving parts | strengthen action progression and cloth/hair/environment reaction |
| Motion too wild | too many actions; no constraints | limit to one beat and specify recovery |
| Bad hands/limbs | close hand action or complex contact | simplify contact, use wider framing, add anatomy constraints |
| No impact | missing contact beat and environmental reaction | add peak beat, recoil, debris/sparks/cloth reaction |
| Looks generic | no visual reference or material specifics | add 1-2 visual references and concrete details |
| Too much AI gloss | over-clean, global shine | add matte/gloss contrast, dirt, micro-scratches, wet/dry boundary |
| Text/watermark appears | no negative block | add no text/subtitle/logo/watermark |
| Action repeats | too few distinct verbs; long duration filled with repeated pose | add 5-6 timed peaks, different body levels, displacement, and weapon functions |
| Standing in place | prompt says showcase/display but not movement | add cross-frame travel, slide/dodge/jump/retreat, moving camera, no idle holds |
| Final pose starts too early | climax/closure placed too early; not enough mid-late state changes | move hero icon to final 1-1.5s; add one more action/mechanism/state-change beat before closure |
| Clip begins from the second action | first-frame/start-state instruction weak or contradicted by later cool shot | explicitly lock first action and second action order; forbid starting with the second action only when that failure occurred |
| Character PV becomes pure action | wrong clip mode; showcase structure used for a character-introduction task | switch to PV structure: identity reveal, expression, signature prop proof, short payoff |
| Action showcase becomes portrait posing | display contract lacks function ladder or action-density requirement | define 3-6 distinct function proofs and require displacement, route/support changes, or environment consequence |
| Shot feels flat | camera/composition lacks foreground depth and diagonal pressure | add low-angle ultra-wide, foreground weapon pass, triangular composition, controlled barrel distortion |
| Standalone clip uses wrong history | prompt relies on previous conversation or previous clip not provided | state "本段独立生成" and declare current form at frame 1 |
| New prompt inherits old concept | old project-specific negatives, props, motion modes, or scene terms remain in the prompt | do a clean-slate pass; remove old names and keep only universal constraints |
| Fantasy weapon feels ordinary | real reference used as ceiling instead of base | add 1-2 fantasy functions with visible support points and short impact peaks |
| Fantasy action looks too realistic | physical reference controls everything and no fantasy function changes state | keep real support/weight, add one impossible-but-readable function and one stylized camera/impact peak |
| Weapon feels weightless | mass distribution and braking missing | classify grip balance, add support, lag, follow-through, and delayed reset |
| Feet slide during force | base/traction missing | lock support foot, surface response, and corrective step |
| Heavy weapon stops instantly | inertia resolution missing | add continuation, pivot, circular brake, ground catch, or damper |
| Contact has sparks but no force | receiver/recoil missing | move both bodies/weapons and end at changed spacing |
| Superhuman action floats | strength treated as zero physics | push force into floor, air, target, prop vibration, and active damping |
| Martial arts all look the same | names not translated | define stance, range, force path, rhythm, defense, footwork, and recovery |
| Transformed weapon handles identically | new physical profile missing | add center-of-mass shift, regrip, stance change, and new timing |
| Mechanism trigger unclear | prompt names activation but not the visible switch/contact/source | show the hand/foot/lever/contact point, immediate mechanical response, and changed weapon/environment state |
| Character series bodies feel identical | style unity overrode silhouette diversity | keep style bible but vary body type, height impression, posture, expression, weapon scale, and movement rhythm |

## Retry Patch Template

```text
保留上一版中成功的[subject/composition/color/action].
本轮只强化[one target].
Add: [specific fix].
Reduce/remove: [conflicting instruction].
Negative: [failure-specific negative].
```

## Liu Short-Drama Primary Buckets

Use one primary bucket before writing the retry. If two buckets are plausible, choose the one whose change should create the clearest visible evidence.

| Bucket | Typical evidence | Keep unchanged |
|---|---|---|
| 表演/聆听 | 木偶式说话、无换气、听者无反应、同步手势 | 台词原文、身份、站位 |
| 台词/口型 | 抢读、词中切断、口型与声音错位 | 景别、动作顺序、音频禁用项 |
| 景别/切镜 | 纯脸特写、调度看不清、切镜无语义落点 | 表演节拍、动作因果 |
| 动作/物理 | 站桩、脚滑、无重心、无回弹/收势 | 角色和场景锁定 |
| 特效/合成 | 发光贴图、无来源、遮动作、无环境受光 | 接触点和动作路线 |
| 连续性/资产 | 换脸、换装、道具/位置漂移 | 已验证的镜头节奏 |
| 声音协议 | 出现音乐、情绪音垫或无来源音效 | 画面与台词 |
| 模型/平台 | 其他层已通过仍持续失败 | 已验证的最小提示词 |

Chinese:

```text
保留上一版的[成功部分]。
本轮只调整[一个目标]：[具体修正]。
减少/删除：[冲突项]。
负面限制：[对应失败项]。
```

## Failure-Specific Patches

Identity drift:

```text
以@Image1锁定同一人物身份。第一优先级保持相同五官、发型、妆容、脸型、身材比例和服装。镜头只做轻微前推，不做大角度环绕。禁止换脸、换发型、换装、年龄变化。
```

Weapon morph:

```text
武器保持同一把：长度、弧度、握把、刀刃/弓弦/链条位置固定。动作只允许武器按原形产生清晰弧线，不允许变形、复制、消失或穿过身体。
```

Weak action:

```text
动作改为一个清晰节拍：起势0-1秒，爆发1-3秒，接触峰值3秒短暂停顿，3-5秒完成follow-through和回收。加入身体重心转移、衣料甩动、冲击反应。
```

Chaotic camera:

```text
只保留一个镜头运动：低机位稳定跟拍/慢推/轻微环绕15度。禁止快速旋转、随机变焦、跳切、镜头抖动。
```

Fake material:

```text
加入材质物理：局部粗糙度、微划痕、指纹油污、冷色刃口高光、湿地严格干湿边界。禁止全局发亮、塑料反光、白糊高光。
```

Weak aesthetic system:

```text
保留上一版成功的主体和动作，本轮只修审美系统：明确媒介域为[photography/cinema/2.5D/NPR/graphic design等]，主风格为[one aesthetic family]，颜色归属为[who owns which colors]，画面层级为[primary/secondary/tertiary]，材质和线条遵守同一规则。删除无关风格名、随机特效和过多装饰。
```

Render vocabulary not taking effect:

```text
本轮只修渲染词绑定：AO只出现在脚底、衣料重叠、装甲缝隙和物体接触处；PBR roughness map区分哑光面与磨亮边缘；anisotropic highlights只用于刷纹金属/发丝/缎面；global illumination bounce来自明确地面或墙面；禁止把AO/PBR/SSS当作孤立关键词堆叠。
```

Pasted subject:

```text
主体和背景使用同一光源方向：脚下有精确contact shadows，衣摆和地面接触处有ambient occlusion，环境色产生轻微bounce light，背景反射或雾气按距离衰减。禁止角色像贴纸一样漂在场景上。
```

Repetitive 15-second action:

```text
保留上一版成功的角色、服装、黑红色调、机械细节和镜头风格。本轮只强化动作密度与位移：15秒拆成6个不同峰值，每2-3秒更换一次动作，加入冲刺、滑步、侧身射击、近战刃扫、跳跃转身、前景破屏收势。删除长时间原地瞄准和重复拉弓。
```

Flat action camera:

```text
本轮只强化镜头张力：低机位FPV超广角跟拍，前景武器多次切过镜头，人物和武器形成强三角构图与斜线压迫，峰值瞬间短促桶形畸变和impact frame；禁止平视中景、远距离旁观、持续静态构图。
```

Standalone history mismatch:

```text
本段独立生成，以@Image1为唯一视觉基准。视频开头已经是[当前形态]，不出现上一段、不出现小弓/旧形态/历史变形过程。全程只保持本段指定的人物、服装、武器和场景。
```

## One-Variable Rule

Weightless-weapon retry patch:

```text
Preserve identity, scene, and action intention. Change only physical handling:
define the weapon as [grip-biased/balanced/tip-heavy/head-heavy/flexible-delayed]
relative to the actor; show [support stance] before acceleration, visible lag or
tension during startup, both-body/weapon recoil at the peak, and a delayed
[step/pivot/circular brake/damper] before the final stable guard. No instant stop,
sliding feet, camera-shake-only impact, or unchanged handling after transformation.
```

Use this priority:

1. If identity/prop broke: fix continuity first.
2. If action unreadable: simplify action second.
3. If camera bad: simplify camera third.
4. If aesthetic system is cheap/generic: fix medium/style/color/hierarchy fourth.
5. If texture/rendering fake: add material/render physics fifth.
6. If rhythm weak: add timing/impact sixth.

Only after the clip is stable should you add more style.

## Preserve-And-Transpose Rule

When the user says a retry "works" but needs a new emphasis, preserve the successful layer and transpose the weak layer.

Examples:

- Style works, action stands still -> keep style, change only movement density and displacement.
- Character works, weapon wrong -> keep identity/camera, change only prop lock.
- Big idea works, standalone history wrong -> keep action plan, rewrite the first sentence as a standalone current-state declaration.
- Hero pose works, not enough force -> keep pose, add leverage, support points, recoil, airflow, debris response.
