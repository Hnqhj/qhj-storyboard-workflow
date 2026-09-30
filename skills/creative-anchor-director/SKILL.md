---
name: creative-anchor-director
description: 创作锚点导演：主动发现、研究、选择并组合高密度语义参考锚点，涵盖导演、影片、工作室、动画师、摄影师、艺术家、设计师、建筑、时尚、类型、剪辑流派、武术、舞蹈、特技、武器体系、作曲与音乐传统。触发：补足名称锚点、举一反三、探索新风格。 Proactively discover, research, select, and combine high-density semantic reference anchors across creative work, including directors, films, studios, animators, cinematographers, photographers, artists, designers, architecture, fashion, genres, editing schools, martial arts, dance, stunt disciplines, weapon systems, composers, music traditions, and sound aesthetics. Use when the user knows only some names, asks Codex to补足名称锚点/举一反三, explores a new style or action language, or needs different projects to receive distinct compatible reference stacks without doing the reference research themselves.
---

# Creative Anchor Director

## Purpose

Own the reference-vocabulary burden for the user. Preserve names they already know, discover the missing ones, assign each anchor one clear job, and compress the result into a small compatible stack that improves creative decisions and prompt generation.

This is an orchestrator. Domain skills verify the substance:

- `$visual-reference-vocabulary`: camera, composition, photography, animation, and visual language.
- `$visual-style-aesthetic-direction`: medium and aesthetic system.
- `$production-design-worldbuilding`: architecture, culture, costume, prop, vehicle, and world design.
- `$action-choreography-reference`: martial art, dance, sport, stunt, partner movement, and weapon handling.
- `$cinematic-music-sound-design`: composers, music traditions, instrumentation, recording, sound design, and mix aesthetics.
- `$cinematic-audiovisual-language`: shot function, staging, spatial logic, editing, and sound-image relation.

## Reference Routing

Read `references/creative-anchor-framework.md` when auditing a brief, researching missing names, resolving anchor conflicts, or creating multiple reference routes.

## Workflow

1. Parse the creative job:
   - medium, format, duration, audience, emotion, world, action, and target model;
   - identify which parts need strong identity rather than generic competence.
2. Inventory known anchors:
   - preserve every deliberate user-provided name;
   - state internally what each one controls;
   - treat names as starting evidence, not a complete vocabulary.
3. Run a relevance-based gap audit:
   - check only lanes that matter to this project;
   - do not fill every lane mechanically.
4. Route to specialists:
   - ask the relevant domain skill to propose and verify candidate names;
   - use `$creative-research-first` when the domain is unfamiliar, the association is uncertain, the reference is niche, or current model/platform recognition matters.
5. Select the smallest useful stack:
   - prefer one primary anchor per function;
   - use secondary anchors only when they control a distinct layer;
   - separate global anchors from character-, object-, sequence-, or sound-specific anchors.
6. Assign division of labor:
   - state what each name controls and what it must not override;
   - resolve conflicts before prompt writing.
7. Compress:
   - preserve names verbatim;
   - add one short role or disambiguator only when needed;
   - avoid replacing a useful term with a paragraph.
8. Learn from output:
   - after generation, use `$creative-casebook` to identify which anchors visibly helped or conflicted;
   - promote validated, scoped lessons through `$capsule-engine`;
   - do not turn one project's choices into universal defaults.

## Anchor Lanes

Choose only relevant lanes:

- medium, capture, and finish;
- visual style and art direction;
- production design, architecture, costume, and props;
- cinematography, framing, and camera movement;
- animation posing, timing, effects, and editing;
- story tone, genre, and performance mode;
- body movement, martial art, dance, sport, or stunt;
- weapon, vehicle, creature, or mechanical movement;
- partner interaction and ensemble movement;
- music, instrumentation, rhythm, recording, and sound design.

## Selection Test

Every proposed anchor must pass:

- **Fit**: does it solve a real need in this brief?
- **Distinct role**: does it add something the existing anchors do not?
- **Compatibility**: can its role coexist with the primary direction?
- **Compression**: is the name more useful than a generic paragraph?
- **Recognition**: is the term established enough for the user/model, or does it need a short fallback?
- **Evidence**: is the attribution known, researched, or marked tentative?

Do not use fake numerical scores. Explain only the decision-changing distinction.

## Operating Modes

### Silent Director

Default during final prompt creation. Perform the audit internally and output only the selected anchors inside the finished prompt.

### Compact Recommendation

Use when the user asks what references to use. Return existing anchors, 2-5 supplements, each role, and one paste-ready line.

### Route Exploration

Use when taste is genuinely open. Offer 2-3 coherent routes with different anchor stacks and consequences. Do not combine all routes.

## Output Contract

```text
已有锚点：
- [name] -> [role]

建议补充：
- [name] -> [distinct missing role]

分工与兼容：
- ...

可直接粘贴：
[compact anchor-first prompt line]
```

Omit the audit in normal final prompts unless it helps the user choose.

## Guardrails

- Do not make the user provide complete reference vocabulary.
- Do not add a famous name merely to sound sophisticated.
- Do not force a named anchor into every lane.
- Do not stack several names that all control the same function.
- Do not silently delete the user's deliberate anchors.
- Do not assume a name's style from memory when uncertain; research it.
- Do not let named references replace shot logic, action physics, material behavior, or story causality.
- Do not generalize any project-specific anchor stack into defaults for unrelated future work.
- Do not over-explain. Keep the name; add the minimum clarification.
