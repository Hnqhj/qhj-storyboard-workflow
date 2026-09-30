---
name: film-breakdown-distiller
description: 拉片与影片拆解：把电影、场景、片段、参考视频、镜头拆解与影评笔记蒸馏成可复用的电影语言机制、导演规则与 AI 视频提示词控制。触发：拉片、视频拆解、参考视频复刻与裂变、原创建构、shot craft。证据边界是强制的。 Discover, analyze, and distill films, scenes, clips, reference videos, shot breakdowns, and film-study notes into reusable film-language mechanisms, directing rules, and AI-video prompt controls. Use for 拉片、视频拆解、参考视频复刻/裂变、原创建构、shot craft lessons, mechanism-bank updates, or translating a reference's narrative/emotional/conversion functions into a new project while replacing its protected or signature expression. Evidence boundaries are mandatory.
---

# Film Breakdown Distiller

## Core Intent

Convert source-backed film observations into portable craft knowledge:

```text
source evidence -> scene problem -> craft observation -> mechanism -> controls -> misuse boundary -> review check
```

Use this skill for two modes:

- **New round:** find or choose one film/segment, verify sources, analyze one craft problem, and add a mechanism only when evidence is strong enough.
- **Distillation:** turn existing notes, shot tables, or completed breakdowns into reusable mechanisms and AI-video/directing controls.

## Required References

Load only what is needed:

- `references/mechanism-index.md`: compact map of all current mechanisms by craft axis. Read first when choosing a precedent or avoiding duplicates.
- `references/loop-playbook.md`: operating rules for the recurring film discovery and scene-breakdown learning loop.
- `references/mechanism-bank.md`: full mechanism entries. Read relevant sections after using the index, not the whole file by default.
- `references/reference-video-original-remake.md`: use when the task is to deconstruct a reference video and rebuild its functions as an original project rather than imitate its expression.

## Workflow

1. Define the unit of analysis:
   - one film, one scene, or one legally inspectable/verifiable segment;
   - exact craft axis: camera, blocking, editing, sound, performance, light/color, space, action rhythm, dialogue, evidence, testimony, or AI-video prompt transfer.
2. Separate evidence from inference:
   - mark source facts as `source-backed`;
   - mark generalized craft readings as `inferred from source-backed description`;
   - do not invent shot details when no legal clip, reliable breakdown, or source-backed description is available.
3. Check for duplicates:
   - read `mechanism-index.md`;
   - compare against nearby entries in `mechanism-bank.md`;
   - merge, refine, or add a validation pair instead of creating a near-duplicate.
4. Distill only portable craft:
   - keep what changes viewer knowledge, emotion, rhythm, space, attention, or ethical distance;
   - discard plot summary, generic praise, vague mood labels, and one-film-only symbolism.
5. Add or update a mechanism using the template below.
6. If the user wants an AI-video transfer, include positive controls, negative constraints, and review checks.

## Recurring Loop Rules

For the user's long-running film-discovery loop:

- Read the long-term `rolling-state.md` and `rollover-handoff.md` first.
- Analyze only one film or one verifiable segment per round.
- Keep chat reports under 1000 Chinese characters.
- Put detailed shot/timecode tables only in `work/shot-breakdowns/`.
- If no reliable source or legal inspectable segment is available, output a clean note and do not force a breakdown.
- Update `rolling-state.md` and then `mechanism-bank.md` when a mechanism passes the quality gate.

## Entry Template

```text
### Mechanism Name

Source example:
Source status:
Core observation:
Mechanism:
Works best when:
Concrete controls:
- Camera / framing:
- Blocking / performance:
- Editing / rhythm:
- Sound:
- Light / design:
Prompt transfer:
Review checks:
Misuse boundary:
Validation status:
```

## Quality Gate

Promote a lesson into the mechanism bank only when it has:

- credible source support or explicitly labeled inference;
- a concrete scene problem, not just a style label;
- at least one technical control;
- at least one use case where it helps;
- at least one misuse boundary;
- a review check that can be inspected later.

If any are missing, return a short `not ready to distill` note and state what evidence is needed.

## Output Contract

When updating the skill, report briefly:

```text
Updated:
Added mechanisms:
Merged/refined:
Not promoted:
Source confidence:
Next validation target:
```
