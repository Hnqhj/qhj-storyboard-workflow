# Mechanism Vocabulary

Use this reference to translate mechanical transformation ideas into prompt-ready language.

## Core Principle

Mechanical transformation reads as believable when every size change has a visible source:

- folded parts unfold,
- nested parts telescope outward,
- panels slide on rails,
- linkages rotate around pivots,
- cables tighten,
- cams/pulleys rotate,
- locks click into place.

Avoid vague "liquid metal morphing" unless the object is explicitly supernatural.

## Mass Migration And Handling Change

Every transformation must declare where mass moves relative to the grip, body, mount, or vehicle.

```text
form A:
center of mass near [grip/core/mount]
low/moderate/high rotational inertia
support and braking rule

form B:
center of mass shifts [forward/outward/upward/asymmetrically]
rotational inertia increases/decreases
new grip, stance, brace, suspension, or counterweight rule
```

Visible transformation consequences:

- extending mass outward increases the visual demand for startup and braking;
- opening symmetrical limbs can preserve center balance while increasing rotational inertia;
- deploying one-sided blades or shields shifts the user's torso and stance;
- moving a counterweight toward the grip can make a large form redirect faster;
- cables, springs, dampers, gyros, powered joints, or ground anchors may assist but must be visible;
- the user must regrip, widen stance, shift hands, lower the pelvis, brace against terrain, or wait for a stabilizing lock before the next action.

Prompt pattern:

```text
As the outer segments extend, the weapon's center of mass moves away from the grip and the actor's arms drop slightly under the new leverage. The rear hand slides farther down the handle, the stance widens, and the hips counter-rotate. After the final latch closes, the frame shudders once, internal dampers settle the oscillation, and only then does the actor begin the heavier action rhythm.
```

Avoid:

```text
same one-handed grip before and after, unchanged swing speed, instant stop,
no body adjustment, no residual vibration, no final load-bearing lock
```

## Standalone Transformation Rule

If the user is generating clips separately, do not rely on prior clips. State the start and end form inside the current prompt.

Use:

```text
本段独立生成，开头就是[形态A]，结尾必须稳定成[形态B]。变形过程只通过可见铰链、伸缩轨道、剪式连杆、凸轮滑轮、缆索拉紧和锁扣完成，不依赖上一段历史。
```

For a clip that starts after transformation, state:

```text
本段开头已经是完全展开的巨型弓形态，不出现小弓，不出现变形过程。
```

Avoid:

```text
承接上一段、刚刚变大、之前的小弓、历史状态、看不见来源的体积增长。
```

## Mechanism Families

### Hinged Folding Limbs

Use for compact-to-large weapons, folding bows, scythes, wings, armor plates.

Prompt language:

```text
segmented bow limbs unfold from the central riser on visible hinge pivots, each black metal blade rotates outward in sequence, red light travels along the hinge seams, small locking teeth click into place
```

Good for:
large silhouette changes while keeping a clear core.

Avoid:
parts growing from nowhere, smooth rubber bending, random extra blades.

### Telescoping Rails / Nested Segments

Use for length extension: bow limbs, spear shafts, gun barrels, mechanical spine.

Prompt language:

```text
nested telescoping segments slide outward along internal rails, red guide lines illuminate each rail, the outer limb lengthens in two precise stages before locking with a metallic snap
```

Good for:
making a small weapon become physically longer.

Avoid:
stretching like elastic, inconsistent thickness, disappearing joints.

### Scissor Linkage / Pantograph Expansion

Use for expanding arcs, shields, mechanical wings, lattice weapons.

Prompt language:

```text
black scissor-link struts open like a pantograph, paired X-shaped linkages expand symmetrically, small pivots rotate in sync, the weapon's crescent arc grows wider without changing the central grip
```

Good for:
fast readable mechanical expansion.

Avoid:
unreadable mesh, linkages clipping through the body.

### Four-Bar Linkage / Synchronized Arm Motion

Use for paired limbs that must unfold in a controlled path.

Prompt language:

```text
a four-bar linkage drives the upper and lower bow arms outward together, pivot joints move in a constrained arc, the limb tips align precisely before the string tightens
```

Good for:
mechanical precision and believable path control.

Avoid:
free-floating limbs, unsynchronized parts.

### Cam And Pulley System

Use for compound bow feeling, heavy draw, tension, mechanical advantage.

Prompt language:

```text
red-lit cams rotate at both limb tips, cable loops pull through small pulleys, the bowstring tension increases visibly, the heavy limbs flex only slightly as the system stores energy
```

Good for:
large bows, heavy draw weight, assisted pull mechanics.

Avoid:
loose string, missing arrow, string passing through hands.

### Sliding Armor Plates

Use for mecha/weapon surface transformation.

Prompt language:

```text
overlapping armor plates slide along hidden tracks, blade-like black panels fan outward, each plate reveals a red glowing inner spine, final plates clamp down to form a continuous armored arc
```

Good for:
gothic mechanical bow surfaces.

Avoid:
shimmering texture swap with no visible movement.

### Cable Tensioning / Winch Draw

Use when the weapon is too heavy for one hand, including big bow draw.

Prompt language:

```text
auxiliary red cables tighten like a winch system, chains pull taut, the archer braces the bow with one boot while both arms and body weight draw the string back
```

Good for:
making the big bow feel heavy.

Avoid:
effortless one-hand pull, no body weight, no strain.

### Over-Center Lock / Mechanical Latch

Use for final locked state.

Prompt language:

```text
over-center locking arms snap past their hinge point, side latches clamp shut, tiny red status lights stabilize, the whole frame shudders once and becomes rigid
```

Good for:
ending a transformation clearly.

Avoid:
never-ending unfolding, parts still wobbling after deployment.

## Bow Transformation Recipe

Use for small bow -> large gothic mechanical bow:

```text
compact black mechanical bow begins in one-hand agile form. The red core in the grip pulses; side latches release; nested upper and lower limb segments slide outward on rails; hinged blade plates rotate open in sequence; scissor-link struts widen the crescent silhouette; red-lit cams at both tips rotate and pull the cable system tight; dangling chains swing from inertia; dark red cloth strips whip outward; final over-center locks snap into place and the red bowstring becomes taut from tip to tip.
```

## Big Bow Draw Mechanics

Use when the expanded bow is too heavy for one hand:

```text
the archer plants one boot against the lower bow limb, braces the central grip with the left hand, hooks the red string with the right hand and shoulder line, then leans back with full body weight; cams rotate, cables tighten, chains pull taut, the heavy limbs flex only slightly before the arrow locks into firing position
```

Alternative big bow draw options:

- **Foot brace draw**: boot against lower limb, body leans back.
- **Ground anchor draw**: lower limb hooks into the floor, archer pulls upward.
- **Shoulder harness draw**: cable loops over shoulder/back, body rotation draws the string.
- **Two-hand staggered draw**: one hand stabilizes grip, the other draws, torso twists and steps back.
- **Spin-to-draw**: the bow swings around the body and inertia helps tension the string, then locks.
- **Inverted leg draw**: hands or bow core brace against the ground, both feet hook cable stirrups, core and leg extension draw the string.

Inverted hero draw prompt:

```text
the giant bow is too heavy to draw by hand; the archer flips into an inverted hero pose, one hand and the bow grip brace against the ground, both feet hook into red cable stirrups on the bowstring, legs open into a powerful V-shape and pull the string back through visible cams and pulleys; chains go taut, the bow frame shudders, air spirals toward the arrow core, then the lock reaches full draw with a red energy pulse
```

Stability constraints:

```text
保持巨弓尺寸稳定，脚套/缆索/弓弦连接清楚，腿部发力路径连续，禁止普通单手拉弓、无支点拉弓、脚穿过弓弦、髋膝反折、弓臂忽长忽短。
```

## Transformation Timing

5-second version:

```text
0-1秒：红色核心亮起，卡扣解锁。
1-2秒：上下弓臂第一段铰链展开。
2-3秒：伸缩轨道拉长，剪式连杆撑开弓体弧度。
3-4秒：凸轮和滑轮旋转，红色弓弦/缆索被拉紧。
4-5秒：锁止机构咔哒合拢，整把大弓震动一下进入稳定形态。
```

8-second version:

```text
0-2秒：特写核心与锁扣解锁。
2-4秒：中景展示弓臂铰链和甲片逐段展开。
4-6秒：全身镜头展示伸缩节和剪式结构把小弓扩成大弓。
6-8秒：凸轮拉紧弓弦，锁止完成，角色用身体重量稳住大弓。
```

## AI Video Negative Blocks

```text
禁止武器凭空变大、液体融化式变形、部件复制、弓弦消失、弓臂忽长忽短、武器变成镰刀/枪/剑、链条穿模、手指穿过握把、人物身体比例变化、镜头乱切、文字水印。
```

For transformation:

```text
每个新增长度都来自可见折叠段或伸缩段；每个旋转都有明确铰链；每个滑移沿轨道发生；最后必须有锁止状态。
```

## Reference Basis

Checked 2026-06-14:

- Compound bow mechanics use limbs, riser, cams/pulleys and cable systems for draw-force behavior.
- Linkage references: four-bar linkages, toggle/over-center locks, scissor/pantograph style expansion, telescoping/nested segments.
- Deployable structure references: origami/deployable engineering demonstrates compact-to-expanded staged motion and locking states.
