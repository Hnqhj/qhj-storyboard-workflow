# Project Prompt Inheritance

Use this reference for recurring, multi-shot, or high-continuity AI-video projects and when an external production case exposes a stable style prefix, constraints, reusable asset sheets, and shot-specific prompts.

## Build three layers

### P0 — Project invariants

Keep only approved project-wide facts:

- smallest relevant story/scene evidence;
- canonical character, costume, prop, creature, and location states;
- compact visual/material master;
- temporal-style laws when the medium requires them;
- generation-stage audio policy;
- backstage risk list and review checks.

The whole screenplay or bible remains context, not paste-ready text.

### P1 — Shot binding

Bind the current shot to exact entities and references:

- active entity/state IDs;
- each reference's one primary role;
- allowed local variation;
- required first visible state and handoff/end state.

Do not let a style, motion, or layout reference silently override identity.

### P2 — Shot delta

Write only what changes for this shot:

- one main event and visible state change;
- blocking/geography and camera proof;
- local performance/action rhythm;
- local light or atmosphere change;
- sound cue and end-state handoff.

## Compile for Liu's prompt contract

Merge P0, P1, and P2 into the current six-part order:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

Translate imported negative constraints into positive present-state locks. Keep exclusions, old-failure language, source commentary, and workflow notes backstage. Repeat only fragile invariants; do not paste P0 in full for every shot.

## Priority and contamination rule

Use this priority:

```text
current explicit shot instruction
> approved episode/scene state
> approved project invariants
> external case or reusable template
```

If an inherited clause conflicts with the current scene, movement, or handoff state, remove it at the source. A later stability line cannot repair a wrong positive association.

## Completion checks

- Every model-ready sentence traces to P0, P1, P2, a supplied reference, or an approved reusable rule.
- The shot delta contains no unrelated project lore.
- Entity/reference roles remain explicit.
- The prompt carries one shot objective, one coherent visual system, and one audio policy.
- Exact prompt, settings, references, output, and retry lineage are handed to `$creative-production-ledger`; actual generation additionally triggers `$generation-asset-pipeline`.

## Boundaries

- This reference compiles context; it does not own the screenplay, visual bible, entity source of truth, camera grammar, platform syntax, or review.
- Do not treat a published project's prompt length or negative syntax as a universal standard.
- Do not infer that an invariant caused the result when the source also used heavy iteration, hand correction, or post-production.

