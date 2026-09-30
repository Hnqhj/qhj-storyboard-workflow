---
name: mechanical-transformation-design
description: "可信的机械与生物机械变身设计：机甲变形分镜、载具变机器人、展开、装甲装配、表面替换、折叠、伸缩、锁定、武器变形，含可见变形前沿、机构与材质来源、质量迁移、重心变化、重新握持、支撑、惯性、稳定与新的操作行为。 Design believable mechanical and biomechanical transformation, mecha transformation storyboards, vehicle-to-robot restructuring, deployment, armor assembly, surface replacement, folding, telescoping, locking, and weapon morphs with a visible transformation frontier, mechanism or material source, mass migration, center-of-mass change, regripping, support, inertia, settling, and new handling behavior. Proactively use for mechanical transformation, biomechanical armor, progressive material replacement, transforming weapons, deployable armor, mecha combat, TF-style transformation, folding bows, hinges, rails, linkages, cables, latches, locks, or when a transformation feels like a flash-cut skin swap, magical growth, or unchanged weight."
---

# Mechanical Transformation Design

## Bottom-Layer Reasoning

Apply `think-one-step-further`:

- Give every new length, volume, and mass a visible source.
- Make the user or carrier adapt to the new form.
- End in a locked and dynamically stable state.
- Add one guardrail for the next likely morph or inertia failure.

## Core Intent

Make transformation feel engineered rather than magical. Parts unfold, telescope, slide, rotate, tension, align, lock, transfer load, and settle.

The transformation is incomplete until the new form has a new mass profile and handling rule.

## Reference Routing

Read only what the task needs:

- `references/mechanism-vocabulary.md`: use for engineered hinges, rails, locks, linkages, telescoping, folding, and deployment vocabulary.
- `references/transformation-frontier.md`: use for biomechanical armor, progressive material replacement, and visible transformation-boundary design.
- `references/tf-mecha-storyboard-import.md`: use for vehicle-to-robot, TF-style mecha transformation, mecha fight storyboards, 9-grid transformation boards, and transformation-as-combat-function.

## Workflow

1. Define form A and form B, including silhouettes, dimensions, and invariant identity anchors.
2. Define each form's physical profile:
   - total-mass impression;
   - grip-relative center of mass;
   - moment-of-inertia class;
   - grip/support requirements;
   - movement and braking signature.
3. Choose the transformation domain:
   - engineered mechanism: choose 2-4 mechanism families from `references/mechanism-vocabulary.md`;
   - biomechanical armor or material replacement: use `references/transformation-frontier.md`.
4. Stage the transformation:
   - physical or behavioral trigger;
   - release/unlock;
   - pre-crack, seam activation, or old-surface withdrawal;
   - primary deployment or active transformation frontier;
   - internal structure reveal when relevant;
   - secondary extension;
   - mass migration and alignment;
   - regrip/rebrace;
   - final tension/lock;
   - shudder, damping, and stable proof.
5. Describe sound, material response, camera framing, and body/carrier adaptation.
   Keep old state, active boundary, and completed new state visible together whenever the transformation domain permits it.
6. Add stability constraints: no magic growth, duplicated parts, unrelated weapon, unchanged handling, or immediate action before settling.
7. For action use, combine with `$action-choreography-reference`, `$action-rhythm-editing`, `$character-continuity-bible`, and `$jimeng-sd2-prompting`.

## Output Shape

```text
Invariant core:
Form A physical profile:
Form B physical profile:
Mechanism stages:
Mass migration:
Regrip/support change:
Lock and settling:
Proof of new function:
Paste-ready prompt:
Negative constraints:
```

## Guardrails

- Do not write only “becomes bigger”; name the source of every added length.
- Keep silhouette continuity through a stable grip, core, color, material, or structural spine.
- State how the center of mass and rotational inertia change.
- Require a regrip, stance change, brace, carrier adjustment, or mechanical support when the new load demands it.
- Do not let compact and expanded forms accelerate, stop, and recover identically.
- Use staged deployment; keep one mechanism readable per close-up.
- Do not transform the whole body or object simultaneously. Move one readable frontier through named regions.
- Bind each material to a distinct behavior: old surface exits, inner structure appears, new surface grows/slides/locks, and energy remains confined to its source or seams.
- Use a short flash, smoke, spark, body turn, or foreground wipe only to bridge the hardest boundary; restore continuous structure immediately afterward.
- Keep the camera relatively stable and follow the active frontier rather than competing with the transformation.
- Delay horns, wings, shoulder masses, or other silhouette-defining structures until the final completion phase.
- End with an explicit lock, residual vibration, damping, and stable form.
- For bows, separate decorative armor from functional limbs, cams, pulleys, string/cable tension, and support.
