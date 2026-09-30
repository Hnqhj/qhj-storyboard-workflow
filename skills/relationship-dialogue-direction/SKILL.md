---
name: relationship-dialogue-direction
description: "双人情绪戏导演：克制感情、亲密、告白、和解、分手、诀别、争吵、对峙与细腻正反打对白。触发：感情戏、正反打、对手戏、吵架戏、诀别、和解、暧昧、细腻表演、双人情绪戏。需保证双人表演、视线、走位与可入提示词的覆盖连贯。 Direct two-person emotional scenes for AI image and video: restrained romance, intimacy, confession, reconciliation, breakup, farewell, argument, confrontation, and delicate shot-reverse-shot dialogue. Use when the user asks for 感情戏, 正反打, 对手戏, 吵架戏, 诀别, 和解, 暧昧, 细腻表演, 双人情绪戏, or needs two-character performance, eyeline, blocking, and prompt-ready coverage to remain coherent."
---

# Relationship Dialogue Direction

## Role

Turn a relationship change into playable two-person behavior and a shootable coverage plan. Treat the scene as an exchange: one person acts, the other receives, then the balance changes. Do not write two independent emotional performances.

Read `references/relationship-coverage.md` for any full scene, multi-shot board, or prompt-ready package. For xianxia or Chinese historical drama, receive the canonical world, costume, prop, location, and power contract from `$ai-short-drama-storyboard` before planning the relationship coverage.

## Ownership And Handoff

- Use `$screenwriting-story-craft` first when desire, obstacle, subtext, or the relationship turn is missing.
- Use `$cinematic-audiovisual-language` for axis, staging, and cut grammar.
- This skill owns the relationship contract, performance asymmetry, reverse-shot coverage, and emotional handoff between shots.
- Let `$professional-storyboard-director` own the complete storyboard and shot count.
- Let `$ai-short-drama-storyboard` own character/location continuity and final `KEYFRAME_PROMPT`, `VIDEO_PROMPT`, `AUDIO_PLAN`, and `NEGATIVE_PROMPT` packaging.
- Use `$emotional-performance-direction` for a deep primary emotion pass, and `$performance-scene-director` when you need the emotion-profile library. Preserve the resulting emotion arc, but map it to both performers here.

## Workflow

1. State the relationship turn: what one person wants, what the other resists or protects, and what is different by the final frame.
2. Lock the two-person stage: screen side, body facing, eyeline, distance, shared prop or boundary, and the one stable master geography.
3. Assign unequal playable behavior. Specify the speaker's visible tactic and the listener's delayed response; do not mirror gestures, head turns, or breathing.
4. Build only the coverage the turn needs: establish the relationship, show pressure or avoidance, reveal the decisive reaction, then hold the changed distance or status.
5. Use an over-the-shoulder or reverse shot only when it proves gaze, power, withholding, or a shift in alliance. Keep the near shoulder, eyeline height, and axis consistent.
6. Package each generated clip with one main action, one dominant camera move, a start state, an end state, and one clear bridge to the next shot.

Short-drama reaction coverage is conditional, not quota-based: classify each beat by line length, semantic completeness, conflict level, and available listeners. Let very short replies, commands, interjections, or self-contained lines remain in the same shot. Add a listener/witness/group/prop reaction only when it contributes new information, changes power or distance, reveals a tactic, advances the next action, or creates a question. Medium lines or relationship turns usually need one reaction carrier; long lines, threats, insults, reversals, power declarations, or action commands may need one or two when justified, but never force a cut when the reaction adds no information. Prefer cutting after a complete sentence or natural half-sentence, not inside a word; treat this as a continuity preference rather than a rigid rule, allowing motivated interruption, impact, danger, or reaction cuts with an audible speech bridge. Cut when the reaction lands or the power/information state changes, not automatically when a sentence ends.

## Quiet-Scene Rule

For romance, grief, reconciliation, confession, and restrained arguments, performance readability outranks visual intensity. Prefer held medium-close framing, a motivated slow push, a single reaction insert, or a deliberate still frame. Escalate the scene through distance, eye contact, silence, and changed behavior before using aggressive movement or rapid cutting.

## Output

Return, at the density requested:

```text
Relationship contract:
- A wants / protects:
- B wants / protects:
- Power and distance at start -> end:
- Shared spatial anchor:
- Main emotional turn:

Performance relay:
1. A visible tactic -> B delayed reception
2. B visible counter-tactic -> A changed behavior

Coverage:
1. [function] [framing] [speaker/listener behavior] [cut trigger] [handoff]
2. ...

Generation locks:
- axis, screen sides, eyelines, wardrobe/prop state, and first/last-frame bridge
```

## Quality Gate

- Does each performer react to the other rather than perform in parallel?
- Does every reverse shot change power, information, distance, or emotional temperature?
- Is the listener given a readable delayed response?
- Does the scene establish geography before close coverage hides it?
- Are cuts motivated by an emotional turn, not merely alternating speakers?
- Does the final image show a changed relationship state?

## Avoid

- Do not use symmetrical alternating close-ups as a default.
- Do not make both characters emote at maximum intensity from the first beat.
- Do not let music, camera motion, tears, or visual effects substitute for a playable reaction.
- Do not change the camera side without an explicit bridge or geography reset.
