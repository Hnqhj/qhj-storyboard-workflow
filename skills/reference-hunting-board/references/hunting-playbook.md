# Reference Hunting Playbook

Use this to build compact, useful reference boards for AI video work.

## Reference Board Buckets

Use 3-5 buckets, not a giant pile:

```text
1. Core shot reference: framing and camera language.
2. Motion reference: body/action/mechanical movement.
3. Material reference: texture, light, reflection, damage.
4. Mood/color reference: palette and atmosphere.
5. Avoid reference: what the result should not resemble.
```

## Search Query Formula

Use:

```text
[subject/action] + [camera/motion/material] + [format/source type] + [style/era]
```

Examples:

```text
low angle sword draw rain night cinematic shot
iaido draw cut slow motion reference
bo staff figure eight motion reference
neon wet asphalt specular reflection cinematography
black leather cyberpunk costume material closeup
Spielberg push in reaction shot example
Obari pose mecha sword diagonal composition
parkour kong vault side view slow motion
```

Chinese variants:

```text
低机位 拔刀 雨夜 电影镜头
居合 抽刀 动作参考
长棍 八字舞花 动作参考
霓虹 雨夜 积水 反光 摄影参考
黑色皮革 服装 材质 特写
大张正己 构图 武器 斜线 姿势
跑酷 猩猩跳 慢动作 侧面
```

## What To Extract

For camera references:

```text
framing, lens feeling, camera height, camera movement, subject position, background depth, cut timing
```

For action references:

```text
start pose, line of force, body rotation, weapon/limb path, peak impact, follow-through, recovery
```

For material references:

```text
roughness, reflection boundary, dirt placement, scratches, fabric weave, wet/dry contrast, skin translucency
```

For mood references:

```text
color contrast, light source, exposure, fog/smoke/rain density, time of day, emotional temperature
```

## Prompt Translation Template

```text
Reference trait:
The shot uses [camera/action/material trait].

Prompt translation:
[Subject] in [scene], [camera/framing], [action path], [material/lighting], [consistency lock], [negative].
```

## Board Output Template

```text
参考板：

A. 核心镜头参考
- 搜索词：
- 判断标准：
- 提炼词：

B. 动作参考
- 搜索词：
- 判断标准：
- 提炼词：

C. 材质/环境参考
- 搜索词：
- 判断标准：
- 提炼词：

D. 避免方向
- 不要找：
- 原因：
```

## Good Reference Rules

- Prefer references with clear silhouettes and readable motion.
- For AI video, side-view or three-quarter-view action references are more useful than chaotic close-ups.
- For weapons, find references where the full arc is visible.
- For clothing and props, find close-ups and full-body shots separately.
- For mood, choose references with a clear light source.
- Avoid references that are too iconic if the final work should feel original.

## When To Browse

Browse when:

- the user explicitly asks to search/find references;
- the reference needs current examples, a real person, a current brand, a current trend, or a specific film/video;
- the user needs links, citations, or a source list.

Do not browse when:

- the user only asks for search terms or a board structure;
- enough domain vocabulary is already known and no source claim is needed.
