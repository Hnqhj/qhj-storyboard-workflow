---
name: seedance-prompt
disable-model-invocation: true
description: "This skill should be used when the user asks to write, improve, translate, compress, or debug a Seedance 2.0 video prompt; mentions T2V, I2V, V2V, R2V, camera direction, prompt quality, or provides reference assets for a production-ready prompt."
license: MIT
metadata:
  version: "6.1.0"
  updated: "2026-06-22"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-prompt

For Liu's live-action short-drama script workflow, follow `../../director-workflow-70/references/short-drama-director-stack.md` upstream. Preserve the selected concept, reference-sufficiency result, 14-28 second group boundary, exact per-shot timing, no-music audio contract, and six-part prompt order; this skill compiles Seedance wording and does not redesign the storyboard. When named five-view character assets are supplied, use the exact `@角色名` handle for every model-facing character mention and keep file references in `{{Image N}}` / `{{Video N}}` / `{{Audio N}}` form.

In that no-music contract, compile only character dialogue and source-coupled dry foley/SFX; do not add music, score, BGM, ambience beds, wind chimes, tension sounds, emotional drones, suspense stingers, or mood-only effects.

Build production-ready Seedance prompts from clear concepts or supplied reference assets. Treat the prompt as a short shooting brief: it must say what changes on screen, what the camera does, what the light and sound contribute, and what must stay stable. Keep final prompts under the platform prompt budget and remove filler before delivery.

Load `[ref:quick-ref]` for the checklist, `[ref:reference-workflow]` for multimodal references, `[ref:i2v-guide]` for image-to-video, `[ref:first-last-frame-guide]` for first/last-frame work, `[ref:examples-by-mode]` when examples are useful, `[ref:shot-list-continuity]` for multi-shot professional plans, `[ref:multishot-grammar]` for shot-label grammar, the shots-times-seconds budget, and cut placement inside one generation, and `[ref:multilingual-community-examples]` for Chinese/Russian/Japanese/Korean/Spanish or mixed-language prompts. When sequence state is present, load `[ref:prompt-compiler]` and compile only the current clip contract.

## Intent

This is the translator between a scene that exists in someone's head and one that exists on screen. The user has already imagined it; the job is to lose as little as possible in transit. Success is a first generation close enough that they can react instead of explain. Each revision inherits everything the story has already decided and changes only what the reaction asked for - a draft is a conversation, not a restart.

## Director Formula

Before filling slots, decide the one thing the shot is doing. Load `[ref:directing-engine]`, read the scene, name a single intention, and let that intention choose the camera, lighting, blocking, performance, and sound together so they reinforce instead of compete. The formula below is the container for a coherent setup, not a checklist of independent decorations; if a project voice is already set, keep this shot inside it.

Use `Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints`. Put the subject and primary action first because early clauses set the shot hierarchy. Do not force every slot if a reference asset already shows the information; for I2V, describe only the motion, camera, timing, transformation, audio, and preservation constraints that the still image cannot show.

| Slot | Use for | Prompt-ready pattern |
|---|---|---|
| Subject | The anchor the model must track. | `Original ceramic perfume bottle on black acrylic, label preserved exactly` |
| Action | The visible change. | `condensation beads form and slide down the glass over five seconds` |
| Scene | Only what is not already in references. | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | One primary move with endpoint. | `slow dolly-in from medium product shot to macro label detail` |
| Light and style | Physical light plus safe visual language. | `warm practical key from frame left, cool blue rim, clean commercial realism` |
| Audio | Ambient bed, SFX, dialogue, or silence. | `Sound: low room tone, soft glass chime on final frame` |
| Stability locks | Preservation and positive state anchors. | `logo, shape, label, and cap geometry remain unchanged` |

## Mode Gate

Choose the mode before drafting. **T2V** needs subject, action, scene, camera, light, style, and constraints because nothing is visible yet. **I2V** starts from `[Image1]` and adds only motion, time, camera, lighting transition, audio, and preservation. **V2V** should map `[Video1]` to source clip, camera move, action rhythm, blocking, edit target, or extension anchor rather than accidentally transferring identity. **R2V** must list every reference role and state which role each reference transfers. **FLF2V** uses `[Image1]` as first frame and `[Image2]` as last frame, then describes only the continuous transition.

| Mode | Drafting priority | Common mistake | Repair |
|---|---|---|---|
| T2V | Build the whole shot in compact layers. | Too many events in one clip. | Keep one visible beat and one endpoint. |
| I2V | Preserve visible identity; add motion. | Re-describing the image until the product or face drifts. | Say `preserve [Image1] exactly`; add only dynamic changes. |
| V2V | Transfer motion, camera, or timing. | Copying unauthorized likeness or scene details. | Use owned/licensed/authorized references and restrict transfer role. |
| R2V | Assign separate roles to each asset. | One reference asked to control identity, pose, scene, and style. | Split roles or prioritize the most important role. |
| FLF2V | Move from first frame to last frame. | Treating the last frame as vague mood instead of endpoint. | State `[Image2]` is the final visual target. |
| Edit | Preserve the source clip while changing one layer. | Rewriting the whole scene and losing continuity. | Say `[Video1] is the source clip; change only...` |
| Extend | Continue from accepted source footage only. | Starting from a planned ending or inventing the clip state. | Route to `[skill:seedance-continuation]` and use the observed end state. |

## Sequence Boundary

The generic prompt skill must not independently invent continuation state. If the user asks to continue, extend, make part two, or use a previous clip, route to `[skill:seedance-continuation]` unless the accepted clip/final frame and observed end state are already present in the sequence state.

For sequence prompts, preserve `project_id`, `clip_id`, `parent_clip_id`, continuity locks, exact reference tags, the actual opening state, completed beat exclusions, and reserved future beats. The final prompt remains natural language and covers only the current clip.

## Prompt Build Process

First, identify the single visible beat: reveal, arrival, decision, transformation, contact, pursuit, or disappearance, and name the one intention it serves. Next, assign reference roles before adding adjectives. Then write a compact first draft in the director formula order, keeping camera, light, performance, and sound aimed at that intention. Finally, run a self-check and the directing coherence test from `[ref:directing-engine]`: one main subject, one main action, one motivated main camera move, physically motivated lighting, performance written as a visible gesture rather than an emotion word, assigned character tags, sound intent, and no hollow boosters.

## Compression Rules

When the prompt is too long, cut in this order: duplicate style adjectives, generic quality words, background details visible in references, secondary camera moves, secondary actions, and speculative emotional labels. Keep preservation constraints, action timing, and role maps. If a user requests a bilingual or mixed-language prompt, use language mixing only for clarity: reference roles, dialogue language, technical camera terms, and safe production constraints. Do not use another language to hide unsafe intent.


## Liu copyable-prompt hard gate

When the output is for Liu and is meant to be pasted into AI-video / SD2 / Seedance generation, do not use a loose natural-language paragraph. The final paste-ready prompt must follow this order unless Liu explicitly requests another format:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

Paste-ready prompt policy: the model-ready code block is positive-only. It states only what is present, visible, audible, active, and locked in the current shot. Exclusion, absence, correction, comparison to old attempts, and previous-failure wording stay outside the copyable block. If a risk must be controlled, translate it into a positive present-state lock before delivery. Named-anchor gate: Name-style anchors mean director, cinematographer, photographer, production designer, animation director, manga artist, studio, film title, game title, or art/design reference names. `镜头语言总控` uses name-style anchors or bounded camera grammar for substantial camera-sensitive prompts; these anchors own composition, blocking, lens feeling, camera motion, edit rhythm, shot scale, and reveal logic. `视觉材质总控` always carries concrete material/light/color/render controls, while its name-style anchors are conditional. Use visual-material name anchors when material, light, color, render finish, production-design surface, or atmosphere is a decisive creative variable, the source lacks clear material identity, or Liu requests named aesthetic references. When the material direction is already clear, neutral, reference-driven, prompt-budget constrained, or contamination-prone, write direct visible material behavior without a visual-material name anchor. Use 2-4 compatible anchors total when anchors are useful. In the paste-ready prompt, write each used anchor as `[Name/Work/Studio]风格 + [concrete positive visible material/camera result]`; keep role-assignment wording backstage and do not use duty verbs such as `负责` inside the copyable block. Technical camera/material terms support the style-result phrase.

Before finalizing, source-trace every concrete phrase. If a noun, prop, place, palette, camera routine, transition, enemy, power, sound cue, or stability lock comes from an old project, default template, or previous failure rather than the current request, supplied/inspected asset, active global bible/continuity lock, or user-approved reusable rule, remove it and rewrite the prompt before delivery.

## Output Contract

Return:

1. Mode: T2V, I2V, V2V, R2V, FLF2V, edit, or extend.
2. Reference role map, if any.
3. Final prompt under the verified active-surface prompt budget.
4. Optional Chinese compressed version when useful.
5. Shot-list or delivery note when the prompt belongs to a professional sequence.
6. Safety or copyright note when relevant.

Before finalizing, run an anti-slop pass and remove vague quality boosters.
