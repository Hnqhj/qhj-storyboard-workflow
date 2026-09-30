---
name: seedance-prompt-short
disable-model-invocation: true
description: "This skill should be used when the user asks for a compact Seedance 2.0 prompt, short Chinese prompt, prompt compression, 30-100 word output, or removal of unnecessary prompt language."
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

# seedance-prompt-short

For Liu's live-action short-drama workflow, use this skill only when he explicitly requests compression. Preserve the upstream selected concept, current group boundary, and essential timing/continuity; when five-view character assets are supplied, retain exact `@角色名` handles for every named character and do not compress them into bare names.

When compressing Liu's prompt, retain the 14-28 second group boundary when a group is requested and retain the no-music audio rule: named dialogue plus source-coupled dry foley only.

Compress Seedance prompts without losing the production signal. A short prompt still needs mode, subject, action, camera, light, sound when useful, and constraints. Remove filler before removing physical details.

When sequence state is present, compression must preserve continuity locks, exact reference tags, actual opening state, current clip action, endpoint, completed beat exclusions, and reserved future beats. Do not compress away the words that keep a continuation from replaying completed action or leaking future action.

## Intent

Compression is an act of judgment about what the user loves most. What survives the cut is the soul of their shot; everything else goes first. If the user would mourn a deleted word, it was never filler.

## Compression Priority

Preserve in this order:

1. Reference tags and their role.
2. Subject or product identity.
3. Action verb and visible endpoint.
4. One camera move.
5. Physical light source or atmosphere.
6. Audio cue or silence instruction.
7. Safety, IP, or continuity constraint.
8. Sequence state clauses: actual opening state, continuity locks, completed beats, and reserved beats.

Delete generic adjectives, duplicate style labels, obvious background details, secondary camera moves, and secondary actions before deleting preservation constraints.

For bilingual or mixed-language compression, load `[ref:multilingual-community-examples]`. Keep only the language mix that clarifies reference roles, dialogue, camera terms, or safe production constraints.

## Compact Templates

| Need | Template |
|---|---|
| T2V | `[Subject] [action and endpoint] in [scene]. Camera: [one move]. Light/style: [physical source]. Sound: [cue]. Constraint: [risk/continuity].` |
| I2V | `[Image1] preserved; only [motion/light/camera] changes. Camera: [one move]. Sound: [cue]. Constraint: [what must not change].` |
| V2V | `[Video1] controls [motion/camera/timing] only; new subject [anchor]. [Action]. Do not transfer [identity/scene/logo].` |
| Chinese | `[Image1]为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。声音：[提示]。` |

## Output Contract

Return one compact prompt, ideally 30-100 English words or an equivalent Chinese prompt when the user asks for Chinese or maximum compression. Include a one-line note only if something important was removed.
