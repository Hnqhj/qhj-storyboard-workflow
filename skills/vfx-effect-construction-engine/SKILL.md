---
name: vfx-effect-construction-engine
description: >-
  Construct and audit generative VFX systems from an effect intent or reference by choosing a dominant family, a visible source, material/shape, motion path, spatial depth, contact or operation, receiver/environment response, peak, decay, and endpoint. Use for 特效、VFX、粒子、能量、法阵、阴阳术、修仙、魔法、爆炸、冲击波、空间裂缝、武器轨迹、拖影、变身特效、环境破坏、光效，或特效廉价、乱飘、无起点终点、遮挡动作、与场景脱节的诊断与重写。This is the effect-construction and vocabulary specialist; cinematic-vfx-director remains the general VFX owner, action skills own body/contact, and seedance-vfx owns final Seedance compression.
---

# VFX Effect Construction Engine

## Mission

Turn an effect noun into a **visible causal system**. A usable effect must show who or what creates it, how it forms, where it travels, what it changes, and what remains.

Use the term bank as selectable atoms, never as a synonym pile.

## Ownership and Handoffs

- Receive the effect job, primary read, medium, and intensity from `$cinematic-vfx-director` when those decisions already exist.
- Own effect-family selection, lifecycle construction, vocabulary retrieval, source/path/interaction specificity, and effect-state continuity.
- Let `$action-choreography-reference` own body mechanics, weapon contact, receiver physiology, support, recoil, and recovery.
- Let `$ai-material-realism` own surface optics, grounding, exposure, reflections, and material-specific rendering.
- Let `$cinematic-audiovisual-language` own shot function, geography, axis, camera position, and cut reason.
- Let `$cinematic-music-sound-design` own the final sound and mix hierarchy.
- Hand the approved effect card to `$seedance-vfx` for Seedance wording. Do not invent a second effect concept during compilation.

For a standalone effect request, infer only the missing effect fields. Do not seize control of story, choreography, camera, or world design.

## Progressive Resources

- Read [effect-construction-grammar.md](references/effect-construction-grammar.md) for lifecycle templates and causal patterns.
- Read [effect-family-atlas.md](references/effect-family-atlas.md) when selecting between energy, ritual, elemental, technological, spatial, organic, destruction, atmosphere, or motion effects.
- Read [medium-integration.md](references/medium-integration.md) when the target is premium CG, stylized CG/2.5D, pure 2D, or a mixed pipeline.
- Read [vfx-atom-index.md](references/vfx-atom-index.md) only when choosing a category, role, or family filter for the term search.
- Retrieve vocabulary with `python scripts/search_vfx_atoms.py "<query>" --limit 8`. Add `--category`, `--role`, or `--json` when needed. Do not load the full 566-entry bank unless doing library maintenance.
- Read [source-provenance.md](references/source-provenance.md) only for auditing the distillation or source boundaries.

## Core Construction Grammar

For every important effect, resolve this chain:

```text
function -> owner/source -> trigger/formation -> material and primary shape ->
path and spatial layer -> operation/contact -> receiver and environment response ->
peak -> decay/residue -> readable endpoint
```

Add sound onset/peak/tail only after the visible chain is coherent.

### Required Effect Card

```text
Function:
Medium:
Owner/source anchor:
Trigger and formation:
Material/shape:
Path/spatial layer/speed curve:
Operation or contact:
Receiver/environment/light response:
Peak and intensity grade:
Decay/residue/endpoint:
Sound sync:
```

Keep the card backstage unless the user asks for analysis. Compile only visible and audible facts into the final prompt.

## Workflow

### 1. Classify the Deliverable

Choose one:

- still image / reference asset;
- short video effect;
- continuation effect;
- effect repair;
- vocabulary or design exploration.

For a still, freeze one decisive phase. Do not describe an entire timeline in one image prompt.

### 2. Lock the Effect Job and Primary Read

Write one sentence:

```text
The viewer must understand [force/state/ownership/transition/threat] at [beat]
without losing [contact/anatomy/geography/identity].
```

If the effect carries no indispensable information, reduce or remove it.

Choose one primary read per beat: source identity, travel path, contact direction, area/scale, transformation frontier, material destruction, or state transition.

### 3. Select the Family Before the Vocabulary

Choose one dominant family and at most one supporting family. Use [effect-family-atlas.md](references/effect-family-atlas.md).

For a 10–15 second clip, default to:

- one dominant family;
- one hero peak;
- one or two smaller supporting beats;
- one continuous spatial axis and causal chain.

Do not combine magic circle, lightning, fire, smoke, holograms, ribbons, and particles unless each solves a different required job.

### 4. Build Only the Visible Lifecycle

Select the useful phases rather than forcing every effect through a generic charge-and-explode template.

Use progressive state wording when continuity matters:

```text
即将形成 -> 开始生长/聚集 -> 正在沿路径推进 -> 接触并改变目标 ->
达到峰值 -> 逐步衰减 -> 留下稳定结果
```

The states must be causally linked. “正在” is not a substitute for geometry, force direction, or an endpoint.

### 5. Retrieve 4–8 Atoms and Give Each a Job

Use the bundled search script. Assign each selected atom to one slot:

- formation;
- carrier/material;
- path or speed change;
- contact/operation;
- peak;
- decay/residue;
- light/color behavior.

Reject duplicates and empty intensifiers. Prefer one precise motion verb over three synonyms.

### 6. Bind the Effect to the Scene

Require at least three integrations for a hero effect:

1. **subject/prop** — hair, cloth, armor, weapon, body edge, active mechanism;
2. **world** — dust, water, fog, foliage, debris, architecture, nearby objects;
3. **image pipeline** — occlusion, depth, reflection, shadow, exposure, camera impulse;
4. **sound** — onset transient, peak impact, resonance, decay tail.

Emissive effects illuminate nearby surfaces according to distance, direction, color, and occlusion. Debris begins at the touched or failed material, inherits force direction, and settles or remains.

### 7. Preserve Action and Identity

Body action precedes effect release:

```text
body action -> visible contact/force direction -> effect release ->
receiver displacement/state change -> environment response -> residue
```

- Effects cannot replace contact, receiver acknowledgment, or recovery.
- Keep the contact point readable before flashes, wipes, or dense particles.
- Weapon trails originate on the moving edge and stop with it.
- A weapon may bend, stretch, or multiply only as a fleeting presentation smear. Grip, handle count, striking edge, mass direction, and before/after identity remain stable.

### 8. Route by Medium

- **Premium CG / photoreal**: physical wake, refraction, pressure distortion, material debris, restrained local light spill, shutter-aware blur, depth-correct compositing.
- **Stylized CG / 2.5D / NPR**: controlled geometry smear, pose echo, graphic speed lines, 2D accents over stable 3D depth and contact.
- **Pure 2D / hand-drawn**: shape rhythm, held keys, contour breaks, line-weight shifts, designed smear drawings, impact images, directional debris.
- **Mixed media**: assign which layer is drawn, simulated, or composited and unify occlusion, grain, black level, color, and cadence.

Do not translate every medium into generic bloom, particles, and motion blur.

### 9. Integrate into Liu's Six-Part Prompt

Do not create a separate generic VFX block in a final paste-ready prompt.

- **视觉材质总控**: medium, effect color ownership, emissive behavior, material interaction, density hierarchy.
- **镜头语言总控**: camera/effect coupling, effect reveal, brief impulse, foreground wipe.
- **事件节拍**: source, formation, path, contact/operation, result, decay.
- **声音**: onset, peak, resonance, tail.
- **正向稳定约束**: current-shot positive facts for ownership, contact visibility, weapon identity, endpoint.

### 10. Run the Gates

Rewrite before delivery if any answer is missing:

- What is the effect's owner and exact source?
- What material or shape carries it?
- What is its primary path, depth layer, and speed change?
- What does it touch or operate on?
- What visibly changes because of it?
- What is the selected peak rather than global spectacle?
- What remains or stabilizes at the end?
- Does the medium-specific treatment match the rest of the image?
- Is the subject/contact still readable?
- Does every chosen term perform a distinct job?

The workflow is complete only when the effect card resolves every applicable field, selected atoms have non-duplicated jobs, medium integration is explicit, and the final wording contains a readable source-to-endpoint chain without internal labels.

## Special Grammars

### Particles

```text
emitter/source -> distribution -> bulk motion -> speed change ->
interaction/occlusion -> lifetime -> disappearance or residue
```

Particles are evidence of a force or atmosphere, not default decoration.

### Magic, Ritual, Yin-Yang, or Cultivation

Resolve:

```text
power source -> activation protocol -> governing symbol/material ->
spatial operation -> resistance/cost -> result -> ritual residue
```

A formation, talisman, seal, sword aura, dharma image, or summoned entity must perform a specific operation: bind, redirect, reveal, divide, purify, exchange, suppress, summon, or seal.

### Transformation

Show an active frontier and material process:

```text
trigger -> advancing frontier -> partial changed state -> completed silhouette -> lock/settle
```

Avoid a uniform dissolve or instant costume swap unless that is the explicit concept.

### Impact and Destruction

```text
pre-contact pressure -> exact contact -> directional peak -> receiver displacement ->
material-specific delayed failure -> debris/wake -> settling residue
```

Use flash, hitstop, exposure inversion, or camera impulse only at selected peaks and only after contact is legible.

## Output Contract

When the user asks for a final prompt, return one complete copyable prompt with the effect integrated into the requested structure. Keep analysis, atom IDs, rejected options, and workflow labels out of it.

For effect design or repair, return:

1. one compact effect card when useful;
2. one model-ready integrated phrase or prompt section;
3. one controlled retry variable if diagnosing a failed generation.

## Hard Failures

- effect has no source, path, operation/contact, result, or endpoint;
- terms are stacked without jobs;
- light show appears before or instead of body action;
- particles or trails ignore depth, occlusion, or source motion;
- every beat is graded as a hero peak;
- effect color has no owner or contaminates the full palette;
- emissive energy produces no nearby light response;
- destruction emits the wrong material or starts before impact;
- a smear permanently mutates a character or weapon;
- density never falls after the peak;
- final wording exposes internal IDs, workflow notes, or generic claims such as “高级特效”.
