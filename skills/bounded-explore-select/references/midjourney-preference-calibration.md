# Midjourney Preference Calibration

Use this specialization for Personalization/Moodboard training and review. It retains the general bounded-exploration owner instead of creating a second candidate-selection Skill.

## Contract

1. Define the target preference distribution: color, light, material feel, emotional register and composition tendency.
2. Declare invariants and forbidden contamination directions.
3. Sample a small numbered batch within a preset budget.
4. Apply structure/readability hard gates before style or identity tendency scoring.
5. Select for closeness to the target distribution, not the single most spectacular image.
6. Feed back one observable gap per round.
7. Stop on stability, diminishing returns, budget, or overfitting risk; split assets when target distributions conflict.

## Hard boundaries

- More generations do not automatically improve taste. Learning requires comparison, attribution, a transferable rule and a new-example check.
- Fixed counts such as 2–3 selections, 3–5 rounds or a score of 500 are not universal thresholds.
- Personalization/Moodboards influence aesthetic tendency; they do not own identity, product geometry or physical camera matching.
- Current `--p`, profile, Moodboard and reference compatibility is owned by `midjourney-generation-adapter` and must be checked against current official documentation.

## Handoff

Output `target distribution / invariants / batch budget / gate / scoring / one feedback gap / STOP-CONTINUE-SPLIT`. The adapter then selects only the current compatible Midjourney controls; the ledger records the batch and result evidence.
