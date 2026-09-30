---
name: seedance-vfx
disable-model-invocation: true
description: "Compile an approved cinematic VFX design into concise Seedance 2.0 wording. Use for Seedance effects involving impact, particles, energy, magic, destruction, transformation, weather, explosions, smoke, fire, water, weapon trails, motion smears, debris, or environmental force response. General VFX concept, hierarchy, medium routing, and grading come from cinematic-vfx-director; this skill owns Seedance-ready compression and stability."
license: MIT
metadata:
  version: "7.0.0"
  updated: "2026-07-21"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050), locally extended for Liu"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# Seedance VFX Compiler

## Ownership

Use `$cinematic-vfx-director` first whenever the effect concept, medium, hierarchy, force path, destruction logic, or style is not already approved.

Use `$vfx-effect-construction-engine` between design and compilation whenever lifecycle selection, particle/energy/ritual grammar, or vocabulary still needs to be resolved. Inherit its source, formation, carrier, path, operation/contact, response, peak, and endpoint rather than replacing them.

This skill does not invent a second VFX design. It compresses the approved design into Seedance-readable visible events.

When an upstream `ExecutionPlan` selects `seedance-20` as the final
`platform_compiler`, use specialist mode: return one `TASK_CARD` with compact
VFX field patches for visual material, camera/effect coupling, event lifecycle,
foley, endpoint, and positive stability locks. Do not emit a separate complete
prompt or integrated six-part block. `seedance-20` applies the accepted patch
and performs the task's only final compilation. Use this Skill's standalone
prompt-section output only when no separate platform compiler is selected.

## Seedance Compilation Order

Compile each important effect as:

```text
source/owner -> formation or anticipation -> path/bulk motion ->
contact/collision -> receiver/environment/light response -> decay/residue
```

For a minor effect, keep only the 2–4 visible phases that matter. For the hero effect, preserve the full causal envelope.

## Effect Budget

- One dominant effect family per clip.
- One hero peak is the default for 10–15 seconds; allow one or two smaller supporting peaks when escalation needs them.
- One primary read per effect beat. Secondary debris/light/atmosphere supports it.
- Remove tertiary particles first when the frame becomes noisy.
- Effects cannot replace body mechanics, weapon contact, receiver response, or sound acknowledgment.

## Medium Lock

State the medium before compiling fast-motion effects:

- premium CG: shutter-aware blur, physical wake, refraction, material debris, local light spill;
- stylized CG / 2.5D: controlled geometry smear, pose echo, speed lines, 2D accents over stable 3D depth;
- pure 2D: drawn smear, contour break, shape rhythm, selective impact image, directional debris.

Do not collapse every medium into generic motion blur, glow, and particles.

## Prompt-Ready Effect Card

Backstage card:

```text
Function:
Medium:
Source/owner:
Primary read and shape:
Path/spatial layer:
Contact/collision:
Receiver/environment/light response:
Motion-effect family:
Intensity grade:
Decay/residue:
Sound sync:
```

Model-ready compression:

```text
[visible source] [forms/releases the effect]; it follows [clear path and depth],
contacts [target/surface], causes [receiver and environmental result],
briefly changes [nearby light/atmosphere], then [decays or leaves residue].
```

Do not include labels such as “Function”, “primary read”, “intensity grade”, “VFX card”, or workflow notes in the final prompt.

## Impact Compilation

For a principal hit, keep this order readable:

```text
pre-contact pressure -> exact visible contact -> short directional peak ->
receiver displacement/physiology -> delayed material/environment response -> decay
```

Use impact image, hitstop, exposure change, or camera impulse only at selected peaks. Contact must remain legible before the accent obscures it.

## Trails and Smears

- Anchor the trail to the actual moving edge, emitter, or body part.
- Match path, velocity, spatial layer, and cutoff to the source.
- Keep foreground/background occlusion correct.
- A stylized weapon may bend or elongate for a fleeting smear frame, while grip, handle count, striking/cutting side, and before/after identity stay stable.
- Distinguish presentation deformation from persistent weapon morphing.

## Destruction and Environment

Write material-specific response and causal emission:

- fracture begins at the contact or failed constraint;
- debris inherits local direction and speed;
- dust, water, sparks, fibers, shards, or chunks match the material;
- nearby objects, cloth, fog, foliage, and reflections respond only where the force reaches them;
- fragments collide, settle, cool, fade, or remain as residue.

## Light and Compositing

Emissive effects affect nearby surfaces according to distance, direction, color, and occlusion. Preserve exposure and body readability. Keep shared atmosphere, black level, depth, grain/noise character, and motion cadence so the effect belongs to the photographed/rendered scene.

## Liu Six-Part Prompt Integration

Do not create a separate generic VFX section in the copyable prompt.

- **视觉材质总控**: medium, effect color ownership, emissive behavior, material interaction, density hierarchy.
- **镜头语言总控**: camera/effect coupling, shake impulse, foreground wipe, effect reveal logic.
- **事件节拍**: source, path, collision, result, decay.
- **声音**: onset, peak, resonance, and tail.
- **正向稳定约束**: current-shot positive locks for effect ownership, weapon identity, contact visibility, and endpoint.

## Hard Failures

Recompile when the effect is decorative, detached, perpetual, medium-agnostic, hides contact, overgrades every hit, emits light without nearby illumination, creates debris before collision, gives every material the same fragments, or permanently mutates a weapon during a smear.

## Output Contract

Return:

1. one compact backstage effect card when useful;
2. one Seedance-ready positive phrase or integrated six-part prompt section;
3. one controlled retry variable if this is a failed-generation repair.
