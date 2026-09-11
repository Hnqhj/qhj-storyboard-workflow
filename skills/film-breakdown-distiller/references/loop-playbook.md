# Film Discovery Loop Playbook

Use this for the user's recurring film discovery and scene-breakdown learning loop.

## Long-Term State

- Task root: `<project-root>/film-breakdown-loop`
- Read before each round:
  - `work/rollover-handoff.md`
  - `work/rolling-state.md`
- Write detailed tables only under:
  - `work/shot-breakdowns/`
- Distill mechanisms into:
  - `references/mechanism-bank.md`

## Round Shape

One round equals one film or one verifiable segment.

Chat report should stay under 1000 Chinese characters and include:

1. Today's selection
2. Why it is worth studying
3. Sources
4. Segment or scene problem
5. Breakdown
6. Reusable craft lesson
7. Misuse boundary
8. Next candidates

## Evidence Rules

- Browse when choosing new films, checking recent releases, or citing sources.
- Prefer official pages, restoration notes, practitioner interviews, reputable criticism, and legal clips.
- If a complete legal clip is unavailable, do a source-backed research breakdown.
- Do not invent camera movement, shot order, timecodes, blocking, or sound details that were not inspected or source-backed.
- Label inferred mechanisms as inferred from source-backed descriptions.

## State Update Rules

Update `rolling-state.md` with:

- round number;
- film / segment;
- core technique;
- source mode;
- notes about legal clip or no shot table.

Update `rollover-handoff.md` when:

- the analyzed count changes meaningfully;
- candidate list changes;
- context pressure is high;
- automation/thread handoff is needed.

Keep `rollover-handoff.md` under 20 lines.

## Candidate Discipline

- Avoid repeating analyzed films.
- Rotate craft axes: sound, routine, hand/action, space, dialogue, color, testimony, evidence, aftermath.
- Keep candidates fresh, but do not chase novelty when sources are weak.
- If no strong candidate is available, output a clean note instead of forcing a weak round.

## Mechanism Update Rules

Before adding a mechanism:

1. Read `mechanism-index.md`.
2. Search `mechanism-bank.md` for close mechanisms.
3. Add a new entry only if it solves a distinct craft problem.
4. Otherwise refine an existing mechanism or add a validation target.

Every mechanism needs:

- source example;
- source status;
- core observation;
- mechanism;
- concrete controls;
- prompt transfer;
- review checks;
- misuse boundary;
- validation status.
