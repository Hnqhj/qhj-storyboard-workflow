---
name: creative-research-first
description: Front-load web research before substantial creative prompt work for AI images, videos, covers, characters, scenes, worlds, action, fashion, products, architecture, music, sound, scripts, ads, and model-specific generation. Proactively use when creating or substantially rewriting creative prompts, especially when quality depends on real references, current platform capabilities, domain vocabulary, historical/cultural accuracy, physical mechanisms, production techniques, or unfamiliar subject matter. Skip only for trivial transformations, fully specified user-provided material, explicit no-browse requests, or unavailable internet.
---

# Creative Research First

## Bottom-Layer Reasoning

Apply `sophia-mode` retrieval routing and `think-one-step-further`:

- Inspect supplied artifacts and local truth before browsing.
- Search only the unresolved knowledge gap.
- Prefer current primary and official sources for platforms, products, technical behavior, laws, and specifications.
- Translate sources into creative controls rather than copying reference language.
- Keep research proportional to the task.

## Core Intent

For substantive creative work, research before ideation and prompt writing:

```text
brief -> known assets -> knowledge gaps -> web research -> mechanism extraction -> creative synthesis -> prompt -> source note
```

Research is not a decorative bibliography. It must change the design, story, sound, camera, material, action, or generation strategy.

## Broad Reference Atlas Mode

When the user asks for "大批量通用参考", "不要只适用于这个", "动作库/审美库/转场库", or a reusable creative knowledge base, widen the research scope before narrowing to the current project.

- Build a reusable atlas across multiple lanes: action/martial/dance/stunt, camera/editing, aesthetics/lookdev, transitions/VFX, sound, material/light, production design/worldbuilding, character/weapon/vehicle/creature design.
- Include adjacent genres and media even when they are not immediately useful for the current prompt; label them as future-use routes.
- Extract every source as a mechanism and prompt control, not as a title list.
- After the atlas exists, select a small subset for the current project. Do not let the current project erase useful general references.

## Aesthetic Research Gate

For any non-trivial **base aesthetic / visual master / premium style / 画面质感 / 审美方向** decision, do not rely on memory, generic taste words, or a few familiar names. Run a focused but broad enough reference sweep before writing the visual master.

Minimum sweep:

- search 3-5 distinct reference lanes, such as film cinematography, animation surface treatment, production design, photography/editorial finish, VFX/compositing, game/CG lookdev, graphic design, or relevant niche artists/studios;
- inspect more than the first obvious result when taste is open or the user complains the result is cheap;
- compare at least 4-8 candidate anchors when the aesthetic is still unresolved;
- keep only the smallest compatible stack after research.

Extract aesthetic references as mechanisms, not as name lists:

```text
reference anchor -> what it controls -> visible mechanism
-> prompt language -> risk / what not to import
```

If a reference is useful only for one layer, scope it tightly:

```text
Fortiche / Arcane -> hand-painted 3D surface and character material hierarchy
John Wick 4 -> large-space hard light and practical color pools
The Raid -> readable action geography and contact proof
Spider-Verse -> sub-0.15s graphic impact frames only, not comic palette drift
```

Do not let a famous name override the project's existing style, story, action physics, continuity, or user's deliberate anchors.

## Cultural / Design Sedimentation Gate

For every substantial original character, world, faction, costume, weapon, creature, vehicle, ritual, profession, action system, or style-led image/video prompt, run a small web research pass before final prompt writing unless the user explicitly says not to browse or the task is a trivial wording edit.

Do this as a default universal step, not only when the user complains that one specific image "缺少文化". The goal is to add sedimentation: cultural memory, craft logic, material history, body technique, social use, symbolic consequence, and design lineage.

Minimum useful pass:

- search the relevant culture/craft/object/movement/profession/design tradition, preferably using museum, academic, practitioner, official, or high-quality reference sources;
- extract 3-6 usable mechanisms, not decorations: silhouette logic, material process, construction, ritual/social use, movement principle, color ownership, motif placement, wear/weathering, and forbidden cliché;
- translate findings into original design controls: costume structure, weapon function, scene rules, action rhythm, light/material response, and negative constraints;
- save or cite compact sources when browsing materially changes the result.

Avoid shallow cultural sticker work:

- do not paste random symbols, patterns, sacred objects, scripts, or national clichés onto a generic pretty character;
- do not make every character ancient, mythic, religious, or ornate just because culture was researched;
- do not let researched references overwrite the user's chosen style or current character direction;
- when the user wants modern, cute, sexy, sci-fi, street, PV, or action-showcase work, still research the relevant design lineage and material/lifestyle logic, then express it lightly.

## When Research Is Required

Browse before final prompt creation when:

- the user asks for a new creative concept, scene, character, cover, world, fight, vehicle, script, score, or sound plan;
- the task references a profession, historical period, culture, real object, physical mechanism, musical tradition, production process, or unfamiliar aesthetic;
- the task is an original character/weapon/costume/worldbuilding prompt and would otherwise risk being merely "pretty" without cultural, craft, material, or social depth;
- current AI model/platform controls matter;
- the user asks for high quality, authenticity, advanced aesthetics, professional terminology, or broad generality;
- the user asks for or critiques base aesthetics, 画面质感, 审美, 高级感, style bible, visual master, non-generic style, or says the result feels cheap;
- previous attempts failed and external references can clarify the mechanism.

Skip or minimize browsing when:

- the user asks for a tiny wording change;
- the task is a direct transformation of complete supplied material;
- current local files are the authoritative source;
- the user explicitly says not to browse;
- research would expose private material or add no decision value.

## Research Lanes

Use the smallest necessary combination:

1. **Domain truth**: how the real object, craft, profession, culture, music, movement, or system works.
2. **Reference mechanics**: examples that solve composition, motion, sound, structure, lighting, material, editing, or emotional problems.
3. **Platform truth**: current official model capabilities, modes, limits, reference syntax, duration, aspect ratio, audio, and controls.
4. **Audience/context**: platform conventions, genre expectations, accessibility, or use case when relevant.

## Workflow

1. Inventory:
   - user references;
   - current project files;
   - active capsules;
   - known constraints.
2. Write 2-5 research questions that would materially change the output.
   - When the user knows only part of the relevant vocabulary, include an anchor-gap question: which director, studio, film, animator, cinematographer, martial art, dance, stunt, weapon system, or sound reference best names the missing function?
   - For aesthetic work, include at least one baseline taste question: what reference systems solve the desired finish, lighting, texture, color hierarchy, and anti-cheapness better than the current prompt?
3. Search:
   - use official/primary sources for current technical facts;
   - use credible educational, institutional, museum, studio, or practitioner sources for craft;
   - compare multiple examples for taste and aesthetics.
4. Extract each useful finding as:

```text
source fact/reference -> mechanism -> visible/audible control -> prompt language -> risk/boundary
```

5. Synthesize:
   - combine mechanics into an original direction;
   - do not imitate one living artist or copy one copyrighted scene.
6. Write the prompt only after the research brief is coherent.
7. Cite a compact source list when browsing was used.

Read `references/research-playbook.md` for query and extraction templates.

## Output Discipline

For normal final delivery, keep the research compact:

```text
研究提炼：
- ...

参考机制：
- ...

完整提示词：
...

来源：
- link
```

Do not bury the prompt under a long research report unless the user asks for one.

## Coordination

- Use `$creative-workbench-toolkit` when research is about open-source tools, GitHub projects, assistant infrastructure, long-term workflow stacks, reference libraries, prompt evaluation, automation, or whether something should be installed/adopted.
- Use `$reference-hunting-board` for visual, motion, film, photography, action, and material reference boards.
- Use `$cinematic-music-sound-design` for music and sound research.
- Use official model documentation before `$jimeng-sd2-prompting` or other platform-specific packaging.
- Use `$visual-style-aesthetic-direction`, `$production-design-worldbuilding`, `$screenwriting-story-craft`, or `$cinematic-audiovisual-language` after research establishes the relevant mechanics.
- Use `$capsule-engine` only after a researched mechanism is validated in real work or explicitly adopted as architecture policy.

## Guardrails

- Do not browse broadly without research questions.
- Do not treat search ranking as authority.
- Do not use outdated model tutorials when current official documentation exists.
- Do not copy prompts, lyrics, scripts, visual layouts, or proprietary workflows verbatim.
- Use named references as high-density creative anchors when they genuinely fit. Verify their relevance, preserve the selected name, and add mechanics only as clarification or guardrails.
- Do not force research findings into the prompt when they conflict with the user's brief.
- Do not claim a source proves an aesthetic judgment; distinguish evidence, precedent, and taste.
