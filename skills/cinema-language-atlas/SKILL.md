---
name: cinema-language-atlas
description: Research, organize, and apply reusable film-language knowledge for shot breakdowns, cinematography, lighting/color, composition, editing, storytelling, VFX, genre/style vocabulary, sound-image rhythm, film-stock intention profiles, and AI image/video prompt controls. Use when Codex needs to explain or select a cinematic term, gate a request as single-frame vs temporal vs multi-shot, translate film/director/equipment/film-stock anchors into observable mechanisms, design cinematic shots, improve prompts, or update cinema references. Do not use it to answer current film-product availability or platform-parameter questions without live primary-source research.
---

# Cinema Language Atlas

## Core Intent

Use this skill to turn credible film craft sources and inspected film examples into reusable controls:

```text
source / film example -> observation -> mechanism -> executable camera/editing/staging control -> use case -> misuse boundary -> validation status
```

When the task involves AI image/video or future reusable research, prioritize prompt-writing transfer: convert each mechanism into concrete prompt wording, timing locks, negative constraints, and output-review checks.

Prefer specific mechanisms over taste labels. Do not treat one film, director, or scene as a universal rule.

## Workflow

1. Start with 2-5 research questions that could change the analysis or prompt design.
2. Check the relevant reference file before browsing or writing.
3. Browse current sources when the request needs external evidence, source freshness, or new examples.
4. Separate technical description from shot function:
   - technical description: shot scale, angle, movement, duration, lens/focus, transition, match, sound, blocking;
   - shot function: what the shot makes the viewer know, feel, compare, anticipate, or reconstruct.
5. Translate validated mechanisms into prompt-writing controls when useful:
   - positive control: what to ask for in concrete film language;
   - timing / spatial lock: when and where the cue happens;
   - negative constraint: what the model should not add, reveal, flatten, or overdo;
   - review check: what visible or audible output proves the prompt worked.
6. Save only reusable, bounded knowledge in references. Mark single-source ideas as candidates.
7. Use capsule-engine only after a mechanism has inspectable evidence, boundaries, and successful application in more than one context, or after explicit user policy approval.

## Reference Map

- `references/shot-breakdown-method.md`: read for shot-by-shot workflow, shot function taxonomy, timecode table fields, and prompt-control translation.
- `references/shot-language.md`: read for shot scale, framing, angle, lens, movement, screen direction, blocking, offscreen space, and reveal/occlusion.
- `references/lighting-color.md`: read for hard/soft light, motivated light, color temperature, contrast, color pools, rim light, material response.
- `references/dialogue-scenes.md`: read for subtext, resistance, reaction shots, silence, eyeline staging, table/car/corridor scene constraints.
- `references/action-scenes.md`: read for action geography, contact proof, weapon weight, fight rhythm, group combat hierarchy, danger cues.
- `references/sound-editing-rhythm.md`: read for sound bridges, listening point, Foley, silence, impact timing, J/L cuts, montage rhythm, and sound-image transitions.
- `references/short-form-retention-editing.md`: read for modern trailer, ad, Shorts/Reels/TikTok, hook, retention curve, information release, loop, CTA, and platform-informed video structure.
- `references/prompt-writing-techniques.md`: read first when the task asks for AI image/video prompts, prompt rewrites, negative constraints, timing/spatial locks, output review checks, or platform-informed prompt structure.
- `references/cinematic-prompt-vocabulary.md`: read when selecting or explaining cinematography, lighting, composition, editing, storytelling, VFX, genre/style, or film-stock vocabulary; it compiles labels into observable mechanisms, gates single-frame vs temporal vs multi-shot requirements, and prevents equipment/director/film-stock names from masquerading as physical proof or professional method. Use `references/cinematic-vocabulary-index.json` only as a 350-entry lookup index, not as current product truth.
- `references/iteration-synthesis.md`: read when resuming the paused cinema self-iteration loop or when needing the latest compact R1-R95 state, current route coverage, validation commands, and non-promoted/capsule boundaries.
- `references/style-anchors.md`: read for directors, cinematographers, editors, action directors, films, animation, ads, MV, or game-cinematic anchors.
- `references/applied-breakdowns.md`: read for inspected or source-backed sample breakdowns that test whether the atlas methods work on actual sequences.
- `references/source-map.md`: read for source quality notes, search scope, source freshness, and what each source is allowed to support.
- `references/case-cards.md`: read for inspected applications, failures, prompt deltas, and mechanisms not yet ready for capsules.

## Output Discipline

For research/update rounds, report:

```text
Round route:
Sources:
Extracted mechanisms:
Prompt-writing techniques:
Updated:
Not promoted:
Next round:
```

For scene analysis or prompt design, return the usable analysis first, then cite compact sources or reference files.
