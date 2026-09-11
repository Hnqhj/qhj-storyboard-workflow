# Motion Trail and FX Grammar

Use this reference when action speed, impact, magic, weapon arcs, camera movement, or character PV energy depends on motion trails or effects. The goal is not "more blur"; the goal is a trace language that belongs to the visual style and still proves the action.

## Core Rule

Every action trace must answer:

```text
effect type -> source anchor -> spatial layer/depth -> direction/path -> duration -> what stays sharp -> what it proves -> decay -> forbidden misuse
```

If a prompt cannot answer those fields, remove the effect or simplify it.

## Main Trace Types

| Type | Best for | Prompt control | Avoid |
|---|---|---|---|
| Photographic motion blur | live-action, realistic CG, vehicles, handheld camera, chase | layer-based blur by motion vector; subject/contact point remains readable; background or foreground streaks according to camera relation | global blur, smeared faces, melted weapon silhouettes |
| Animation smear frame | 2D animation, anime, cartoon, stylized 3D with drawn timing | 1-2 frame stretched/deformed inbetween on the moving limb, weapon, hair, cloth, or prop; returns immediately to clean pose | constant deformation, every frame smeared, anatomy staying broken |
| Afterimage / pose echo | superhuman anime, comic action, game PV, teleport-like speed | stepped silhouettes or repeated limb/weapon positions behind the main body; main body is crisp and clearly primary | clone confusion, extra characters, equal-opacity duplicates |
| Graphic speed/focus lines | manga, comic, Spider-Verse-like graphics, posterized action | background speed lines prove direction/urgency; near-body motion lines prove the moving object; focus lines point attention to impact | random UI lines, lines covering face/contact, lines contradicting movement |
| Impact frame / exposure inversion | anime, comic, stylized action punctuation | ultra-brief black-white or high-contrast frame at contact; immediately returns to scene lighting | long strobe, repeated flashing, hiding the hit |
| Physical debris / particles | realistic impacts, heavy weapons, ground contact, water/wet floors | particles originate from contact point; scale, direction, gravity, bounce, occlusion, and settling match material | decorative particle storm, sparks without metal, dust without broken surface |
| Energy / ink / brush trail | fantasy powers, calligraphy, ink wash, painterly 2D, magic weapons | trail is anchored to hand/weapon/body/impact; obeys palette, brush texture, occlusion, and fast decay | full-screen glow, neon soup, trail replacing body mechanics |
| Foreground wipe blur | high-tension camera cuts and near-lens passes | cloth, weapon, wall, debris, or body passes close to lens and triggers the cut | decorative camera shake without a physical occluder |

## Style Bias Matrix

- **Live-action / IMAX / grounded 3D:** prefer photographic motion blur, shutter-like streaks, dust, water, debris, lens/foreground wipe. Use graphic effects only as very short accents.
- **Anime / Trigger / 大张克己-style action:** prefer pose contrast, smear frames, impact frames, stylized speed lines, hard silhouette holds. Keep key poses readable.
- **Spider-Verse / comic print:** avoid traditional soft motion blur; use stepped timing, pose echoes, speed/motion lines, halftone, hatching, panel-like holds, and graphic impact punctuation.
- **Fortiche / Arcane-like painterly 3D:** keep character/contact readable; add hand-drawn 2D FX, painterly scratches, restrained smoke, small graphic accents, and expression/body-pose clarity. Do not flood the frame with generic particles.
- **Ink wash / xuan paper / oil-paint hybrid:** use brush-smear, dry-brush wakes, ink bloom, negative-space wake, and painterly displacement. Keep face, hands, weapon edge, and contact point clean. Avoid photographic global blur and random dirty splatter.
- **Woodcut / engraving / print:** use hard carved streaks, negative slashes, hatching density changes, and posterized impact shapes. Avoid soft volumetric glow.
- **Cutout / stop-motion / puppet:** use layer parallax, shadow smears, held poses, foreground wipe, and slight handmade jitter. Avoid fluid CG trails that break the medium.
- **Neon cyber / music PV:** use controlled light trails and graphic afterimages, but each trail needs an emitter, palette ownership, and decay. Avoid turning all motion into full-frame glow.

## Prompt Compression Pattern

Use one compact sentence per important beat:

```text
拖影/特效规则：不写泛泛的运动模糊。每个拖影必须来自手、武器、脚底、衣摆、镜头前景或碰撞点；有明确方向、空间层级、持续时间和消散方式。脸、主武器轮廓、脚底支撑和接触点保持可读。
```

For one beat:

```text
她的肘击只留下 1-2 帧暗色笔刷 smear，来源是前臂护甲，沿斜下攻击线拖出，主脸和肘部接触点保持清晰，命中后拖影立刻断成碎墨消散。
```

## AI Video Guardrails

- Do not stack every trace type in one beat. Pick 1 physical proof + 1 style trace at most.
- Do not let effects replace action causality. The body must still show approach, contact, receiver response, and new state.
- Do not write "motion blur" when the desired look is actually smear, pose echo, speed lines, or ink trail.
- For character PVs, preserve face and costume readability; put trace effects around prop, hair, cloth edge, feet, or background rather than across the face.
- For fight scenes, keep contact points visible. Effects should frame the hit, not cover it.
- For 2D/painterly video, prefer clean graphic traces over photorealistic blur unless the style explicitly borrows live-action optics.
