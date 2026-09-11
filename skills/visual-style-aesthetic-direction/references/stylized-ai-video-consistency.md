# Stylized AI Video Consistency

Use this for multi-shot AI video prompts, style drift diagnosis, and graphic effects such as red lines, energy strings, ribbons, ink slashes, brush trails, wires, chains, and UI traces.

## Style Bible Fields

Before writing timed shots, lock:

```text
Base medium:
Rendering hierarchy:
Palette ownership:
Linework:
Shape language:
Texture system:
Lighting logic:
Camera/editing style:
Motion language:
Graphic effects grammar:
Forbidden drift:
```

Example:

```text
Base medium: black-white ink wash with woodcut-like hard edges.
Rendering hierarchy: characters use sharp silhouettes and simple cel planes; environment uses paper texture and ink bleed; red line uses flat graphic ink but obeys depth and occlusion.
Palette ownership: world = black/white/gray; protagonist action line = vermilion red only; no other saturated colors.
Motion language: held poses, short smear frames, match-on-action cuts, no random camera spin.
```

## Rendering Hierarchy

Define how different layers are rendered:

- character: linework, shading, proportion, face detail
- environment: depth, texture, perspective, material realism
- effects: flat graphic, volumetric, particle, ink, light, thread, liquid, smoke
- camera: 3D physical camera, manga panel cuts, poster-like holds, stop-motion layers

Without hierarchy, AI may reset the style every cut.

## Graphic Element Anchor Rule

For every line/ribbon/thread/energy trail, specify:

```text
source anchor:
target anchor:
height/layer:
tension:
contact:
occlusion:
reflection/shadow:
motion path:
forbidden state:
```

Example for a red thread:

```text
The vermilion thread is physically anchored to the protagonist's left wrist and wrapped around the opponent's sword handle. It floats taut through midair at waist height, occasionally occluding the foreground body, casting a faint red reflection on wet surfaces only when passing near water. It must not become a painted stripe on the floor.
```

## Common Failure: Meaningful Line Becomes Floor Stripe

Symptom:
- red line, energy string, leash, cable, or slash mark lies flat on the ground for no reason.

Likely cause:
- prompt says "line across the scene" or "red line on bridge" without height, anchor, or layer.

Fix:
- define it as a suspended object or motion trace:

```text
The red line is not painted on the ground. It is a taut suspended thread from wrist to weapon, crossing through midair in front of the torso. It only touches the floor at a named anchor point if specified.
```

## Multi-Shot Consistency Locks

For 10-15 second stylized videos:

- keep the same base medium across all beats
- keep the same color ownership
- keep the same line thickness and shadow behavior
- keep effects obeying the same physical/graphic rule
- change camera distance and angle, not rendering style
- re-establish space after inserts or abstract impact frames
- use one designated impact-frame style, not a different effect every peak

## Allowed Variation

Allow:
- shot size changes
- camera angle changes
- pose and action changes
- cloth/hair/particles moving
- paper grain shifting subtly
- red accent changing shape as a motion trace

Forbid:
- palette expansion
- new art medium mid-shot
- character becoming more cartoon or more real without intent
- effects changing from ink to neon to fire
- graphic elements losing anchors
- background architecture rebuilding after each cut

## Prompt Patch For Style Drift

```text
Preserve the successful style: [specific successful look]. This round only strengthens consistency. Across all shots, keep the same base medium, same black/white/gray palette, same vermilion accent ownership, same paper/ink texture, same character rendering level, and same hard-edge shadow rule. Camera angles may change, but the rendering style must not reset between shots.
```

## Cross-Platform Stylization Booster

Use this when identical or near-identical prompts produce a consistently stronger stylized look on another platform. Infer the **visible control layer**, not the platform's unknowable hidden wording.

### Inference procedure

Compare at least two matched outputs and mark only transformations that repeat across unrelated subjects or styles:

```text
medium priority: realism-first or art-direction-first
graphic abstraction: silhouette, contour, shape simplification, color blocking
shading: continuous PBR gradients or two/three-step designed shadow planes
surface: realistic microtexture or hand-painted/matte/selective detail
motion: ordinary blur or pose exaggeration/smear/impact-frame treatment
composition/editing: conventional coverage or panel-like graphic inserts
palette: broad natural color or compressed owned colors
persistence: whether the same treatment survives every cut
```

If the same transformations recur across multiple aesthetic families, classify the cause as a probable platform-side stack: prompt rewrite, style adapter/model routing, and/or post-processing. Do not claim the exact hidden prompt was recovered.

### Packaging rule

Keep the base visual master authoritative. Add the inferred layer as an optional module with a named intensity. The module may control:

- artistic interpretation over photographic literalism;
- coherent 2D/2.5D/NPR medium translation;
- bold readable silhouettes and expressive contour behavior;
- simplified large forms and controlled flat color blocks;
- two- or three-step designed shadow planes;
- matte or hand-painted surfaces with reduced unowned microtexture;
- dynamic foreshortening, readable key poses, brief smears, and one designated impact-frame language;
- consistent art direction across every shot.

It must not silently change identity, costume, weapon category, world geography, action causality, contact point, or end state.

### Controlled expressive deformation

For stylized action, separate **structural frames** from **expressive motion frames**:

```text
anticipation/contact/recovery frames: correct anatomy, weapon identity, edge alignment, contact, and mass
high-speed in-between frames: brief directional bending, stretching, foreshortening, smear, or arc exaggeration
after the speed peak: restore the stable structure immediately
```

This preserves tension without freezing the weapon into a rigid product render or allowing permanent morphing.

### Paste-ready booster

```text
【可开关风格化增强层】
强风格化非写实剧场动画，艺术解释优先于摄影写实；将角色、武器、环境和特效统一转译为同一种二维／二点五维视觉语言。手绘厚涂表面，清晰有力的外轮廓，简化而准确的大形体，雕塑化明暗色块，两至三档受控阴影，有限而明确的主色关系，哑光材质，降低无意义微纹理与真实PBR反光。每一帧都像完成度很高的动态插画，而不是普通游戏CG。

动作采用夸张但可读的动画关键姿势、强透视缩短、短促smear frame、速度峰值的受控形变与统一的图形化impact frame。武器和肢体只在高速运动帧中瞬时弯曲、拉伸和透视夸张；起势、接触、受力结果与收势帧恢复正确结构。攻击方向、碰撞位置、质量关系和人物空间关系保持清楚。

通过大色块、剪影、装饰几何、线条方向与短促图形插入镜头强化节奏；风格元素参与构图和动作，而不是只贴在材质表面。全片保持同一美术语言。避免摄影写实、普通PBR游戏渲染、塑料高光、杂乱微纹理、灰脏颜色、平均化光影，以及写实材质与卡通线条无规则混用。
```

### Strength selection

- **Light**: preserve cinematic CG materials; add silhouette, palette, and impact-frame discipline only.
- **Medium**: default for stylized action; use graphic shading, selective hand-painted surfaces, and controlled expressive deformation.
- **Strong**: use for character PV, graphic fantasy, comic, painterly, or decorative worlds; allow the entire frame to read as illustration, but retain structural frames and action proof.

Do not enable Strong by default for contact-critical choreography. If action already suffers from fake contact, slow movement, or unstable weapons, repair choreography first and use Light or Medium.

## Prompt Patch For Graphic Element Drift

```text
The graphic element must keep a clear spatial role: [source anchor] to [target anchor], [height/layer], [tension state], [interaction]. It is not a decorative floor stripe, not a random speed line, not a UI overlay, and not a new object detached from the character.
```

## Preflight Questions

Before finalizing a stylized video prompt, ask:

- What is the base medium?
- What changes by shot, and what never changes?
- Which color belongs to whom?
- Do graphic effects have anchors and layers?
- Does the impact frame return to the same world after the hit?
- Can the viewer still understand space after the most abstract shot?
- Is the final frame a consequence of the action, not only a pretty still?
