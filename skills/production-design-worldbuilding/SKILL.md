---
name: production-design-worldbuilding
description: "一致的生产设计与世界观构建：视觉世界规则、美术方向、地点、建筑、道具、服装逻辑、载具与武器设计语言、色彩归属、材质系统、环境叙事、文化技术规则与视觉圣经交接。触发：世界观、美术设定、场景设定、视觉系统、道具设计、场景统一、颜色体系。 Create coherent production design and worldbuilding for AI images/videos: visual world rules, art direction, locations, architecture, props, costume logic, vehicle/weapon design language, color ownership, material systems, environmental storytelling, culture/technology rules, and visual bible handoff. Use when the user asks for 世界观, 美术设定, 场景设定, 视觉系统, 美术风格, 生产设计, 道具设计, 城市设计, 场景统一, 颜色体系, 反差背景, production design, art direction, world bible, environment design, concept art bible, or complains that a scene feels random, pasted together, inconsistent, generic, or not like a real world."
---

# Production Design Worldbuilding

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Purpose

Use this skill to make a video world feel designed rather than assembled from cool fragments. It defines the rules behind locations, colors, materials, props, costumes, vehicles, symbols, technology, weather, signage, and scale.

Use this before shot design when the world itself is important. Use it with `character-continuity-bible` when the user needs consistency across clips.

## Model-Executable Worldbuilding Layer

Do not output only abstract labels such as "coherent world", "visual logic", "color ownership", "story pressure", "culture depth", or "not generic". Convert every world rule into visible evidence.

For each major world element, fill this compact schema:

```text
Who made/uses it:
Why it exists:
Material/process:
Visible wear or adaptation:
Color/motif owner:
Behavior/ergonomics:
Scene proof:
Forbidden generic drift:
```

Translate abstract terms this way:

- **World rule** = a visible repeated constraint across architecture, costume, prop, vehicle, signage, or ritual.
- **Culture depth** = material process + use behavior + social meaning + wear/residue.
- **Color ownership** = which group/object/function owns the color, where it appears, and where it must not appear.
- **Location pressure** = how the place forces an action: narrow path, height, weather, surveillance, ritual order, resource scarcity, crowd flow, heat, cold, noise, or danger.
- **Coherent design** = at least 3 shared signals across categories: shape language, material family, joint/fastener logic, repair style, symbol placement, scale, or light behavior.

Bad:

```text
这个世界很有文化沉淀，建筑和服装统一，有高级感。
```

Good:

```text
所有公共建筑使用同一种黑色烧陶砖和铜铆钉，居民外衣边缘也缝着铜片；铜片不是装饰，而是身份登记牌和风铃式警报器，行走时会发出细碎声。禁止随机霓虹、通用赛博管线、无功能符号。
```

## Reference Routing

Read only the file needed for the task:

- `references/world-rules.md`: use for fictional world rules, social logic, technology level, environment, city systems, and visual causality.
- `references/art-direction-system.md`: use for palette, shape language, material families, contrast logic, lighting, and visual motifs.
- `references/location-prop-costume.md`: use for locations, props, vehicles, weapons, costumes, signage, objects, and environmental storytelling.
- `references/ai-worldbuilding-packaging.md`: use when turning the world bible into image/video prompts.

## Workflow

1. Use `$creative-anchor-director` to supplement missing architecture, production-design, fashion, craft, cultural, or design-movement names when useful. Use `$creative-research-first` for substantive worlds, cultures, technologies, architecture, vehicles, professions, historical settings, or unfamiliar materials.
   - Universal culture/depth rule: for every substantial original character, faction, costume, weapon, creature, vehicle, location, ritual, or worldbuilding prompt, run at least a small web research pass before final writing. This is required even when the concept already looks good, because "pretty" is not enough if the design lacks sedimentation.
   - Research must extract mechanisms rather than stickers: who made it, what material/process formed it, what social/ritual/professional use it has, what body movement or ergonomics it implies, what motifs belong where, what colors/materials are meaningful, and what cliché to avoid.
   - Express the research through structure, material, silhouette, prop function, space rules, and negative constraints; do not simply paste cultural symbols onto a generic design.
2. Define the world promise:
   - What should the viewer understand about this world within one image or shot?
3. Set three rules:
   - social rule, technological rule, visual/material rule.
4. Assign color ownership:
   - which colors belong to the world, character, danger, authority, memory, luxury, decay, or rebellion?
5. Choose shape language:
   - curves vs blades, grids vs organic forms, vertical pressure vs horizontal speed, handmade vs machine-clean.
6. Build locations as story machines:
   - each place should pressure, reveal, hide, trap, tempt, or transform the character.
7. Bind props and costumes to the world:
   - objects should look designed by the same culture, economy, technology, and material logic.
8. Write a reusable world bible:
   - concise locks plus allowed variations and forbidden drift.

## Output Shape

```text
世界承诺：
核心规则：
颜色归属：
形状语言：
材料体系：
地点设计：
道具/载具/服装逻辑：
环境叙事细节：
可变范围：
禁止漂移：
可直接进提示词的世界设定：
```

## Quality Gate

- Can the viewer tell what kind of society made this place?
- Can the viewer tell what culture, craft, profession, material process, or social use shaped the character/weapon/costume/location?
- Do character, costume, vehicle, and architecture share a design logic?
- Are colors assigned by meaning rather than random beauty?
- Are props functional inside the world, not just decorative?
- Does the location create story pressure?
- Is there a clear forbidden list to prevent generic cyberpunk/fantasy drift?

## Avoid

- Do not list aesthetic adjectives without rules.
- Do not mix every cool genre reference.
- Do not wait for the user to know the relevant architect, production designer, fashion, craft, or design-movement vocabulary; propose a small compatible set when it materially sharpens the world.
- Do not make all surfaces the same material or color.
- Do not create lore that cannot appear visually.
- Do not over-explain history when a prop, sign, ritual, or architectural rule can show it.
