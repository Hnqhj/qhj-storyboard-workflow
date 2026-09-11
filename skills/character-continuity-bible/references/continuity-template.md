# Continuity Template

Use this reference to create reusable consistency blocks for AI video.

## Character Lock

```text
全程保持同一角色：相同五官比例、脸型、眼神、发型、发色、妆容、身材比例、年龄感和气质；不要换脸、不要年轻化/老化、不要改变种族或性别表达。
```

Detailed slots:

```text
Face: [face shape, eyes, brows, nose, lips, makeup, expression baseline]
Hair: [length, color, style, bangs, movement rules]
Body: [height impression, build, posture, silhouette]
Costume: [main garment, color, material, accessories, damage/wear]
Prop/weapon: [shape, size, color, material, grip, glowing parts]
World: [setting, era, tech level, weather, palette]
Lighting: [source direction, color temperature, contrast]
```

For likeness-sensitive work, record a **relationship signature**, not only isolated feature labels:

```text
Evidence status: observed / inferred / unknown
Face relationship signature: face width-to-length impression; cheekbone-to-jaw path;
eye spacing, tilt and asymmetry; brow-to-eye distance; nose-to-mouth and mouth-to-chin
proportions; hairline; age/skin baseline; stable mole, freckle, dimple or asymmetry.
Contaminating conditions: expression, beauty filter, focal-length distortion, hard shadow,
occlusion, makeup or low resolution.
```

Do not promote a relationship to a hard identity fact when the supplied view does not prove it.

## Physical Identity Lock

Use for recurring action characters and weapons:

```text
Actor physical class: [light/agile, human-matched, heavy/armored, superhuman, giant]
Strength versus weapon: [overpowered/matched/strained/mechanically assisted]
Dominant hand and grip: [left/right/ambidextrous; one/two/sliding/braced]
Default support: [narrow/mobile, shoulder-width, split/wide, grounded anchor]
Force signature: [linear, rotational, dropping, whipping, continuous]
Recovery signature: [snap back, flow through, rooted settle, delayed brake]
Weapon mass distribution: [grip-biased, balanced, tip-heavy, head-heavy, flexible-delayed]
```

Reusable lock:

```text
Across all shots, preserve the same actor-to-weapon strength relationship,
weapon balance, support logic, startup, follow-through, and braking behavior.
Do not let the weapon become weightless, change handedness, move its center of
mass, stop instantly, or use a different martial rhythm unless the story explicitly
changes form, injury, power state, or gravity.
```

## Costume Lock

```text
服装保持不变：黑色长皮衣、深红内衬、金属肩甲、腰带和腿部绑带位置固定；皮革有局部褶皱和反光，不能变成布料、盔甲或普通外套。
```

## Weapon / Prop Lock

```text
武器保持同一把：黑色弧形机械弓，红色发光弓弦，分段金属刃片，链条和暗红布条悬挂；弓的尺寸、弧度、握把位置、发光核心和箭的位置全程稳定，禁止变成镰刀、枪、剑或多把武器。
```

## Form-State Lock

Use this when the same weapon or character has multiple forms across separate clips. Lock the current form explicitly; do not assume the model remembers earlier states.

```text
本段形态锁定：视频开头已经是[小弓/巨弓/展开形态/损伤形态/蓄力形态]，全程保持这个形态逻辑；除非本段明确写变形，不出现其他形态。
```

Small bow example:

```text
小弓形态锁定：单手可持的紧凑黑红机械短弓，弓臂较短，红色能量弦细而利落，可作为近战双面刃使用；禁止变成巨弓，禁止体积突然扩大。
```

Giant bow example:

```text
巨弓形态锁定：完全展开的黑红巨型机械弓，尺寸高于人物，分段弓臂、凸轮滑轮、红色缆索、链条和暗红布条清晰可见；必须借助身体、地面、脚套或机械结构拉开，禁止普通单手拉弓，禁止出现小弓历史状态。
```

## Scene Lock

```text
场景保持同一空间：雨夜霓虹巷道，湿润柏油地面，远处招牌虚化，光源来自左后方红蓝霓虹；透视方向、地面积水位置和背景深度不漂移。
```

## Allowed Change Block

Use this to avoid over-locking:

```text
允许变化：发丝、衣摆、披风、雨水、水面波纹、金属高光、轻微呼吸和眼神变化。
禁止变化：脸、发型主体、服装结构、武器外形、人物身高比例、背景空间、镜头内人物数量。
```

## Multi-Shot Continuity

```text
全片锁定：同一角色、同一服装、同一武器、同一场景天气和色调。
镜头1：允许远景展示全身和环境。
镜头2：允许切到中景动作，但服装和武器细节保持一致。
镜头3：允许特写面部和武器反光，背景只做虚化，不重建空间。
转场：以上一镜头的结束姿态作为下一镜头起势。
```

## Reference Role Language

```text
@Image1 only locks character identity and costume.
@Image2 only locks weapon design and material.
@Image3 only locks environment color and lighting.
Do not merge backgrounds or copy unrelated poses from the references.
```

Chinese version:

```text
@Image1 仅用于锁定人物身份和服装。
@Image2 仅用于锁定武器造型和材质。
@Image3 仅用于锁定场景色调和光线。
不要混合参考图背景，不要复制无关姿势。
```

When a real-person identity image and a character/cosplay design image both contain faces, use a sovereignty firewall:

```text
真人身份图拥有：面部关系、年龄感、肤色基线和稳定自然不对称。
角色造型图只拥有：发型外轮廓、服装结构、配色、配件、角色身份和姿态倾向。
冲突时真人身份图优先；角色造型图不得提供替换面孔、骨相、年龄或族裔。
```

If the user explicitly wants identity transformation rather than preservation, write the allowed identity changes as the current state contract instead of silently applying this default.

Standalone role language:

```text
本段独立生成，@Image1就是本段唯一视觉现实；不要引用对话历史里的未上传形态，不要生成上一段里的旧武器或旧姿势。
```

## Negative Lock Blocks

Character:

```text
禁止换脸、五官漂移、发型变化、服装变色、配饰消失、身材比例变化、年龄变化、额外人物出现。
```

Prop:

```text
禁止武器忽大忽小、形态变化、凭空复制、握持错误、穿模、发光部件位置漂移、箭/弓弦消失。
```

Scene:

```text
禁止背景重建、空间透视变化、天气突变、光源方向改变、场景从室外变室内、无关道具出现。
```

## Continuity Bible Mini Format

```text
ID: [name/code]
Identity anchors:
Costume anchors:
Prop anchors:
Scene anchors:
Allowed motion:
Forbidden drift:
Reusable prompt block:
```
