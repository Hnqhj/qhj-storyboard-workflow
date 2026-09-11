# Allocation Model — decide where the prompt spends its budget

*The operational companion to `intent-vs-precision.md`: every generation has a finite fidelity budget, and a prompt that demands everything gets mediocrity everywhere. Decide where the budget goes before writing a word. Labels: [field] = practitioner-reported · [official] = current official guidance · [heuristic] = default to test. Craft guidance compiled 2026-06-11; official compactness/reference guidance rechecked 2026-07-10.*

## Master-first compression [official + heuristic]

BytePlus's official Seedance 2.0 guide recommends concise descriptions, avoiding redundancy and semantic conflicts, expressing spatial relationships through reference images first, and using ordered shot sequences for complex temporal events.

Apply that as a hierarchy:

1. **Global masters are higher-level, not longer.** Use one compact visual/material master and one compact camera master. They define the generation domain every later beat inherits.
2. **Event beats carry change over time.** After the masters are set, each beat adds only subject state change, action cause/result, camera proof, and endpoint. Do not repeat palette, rendering, material, and camera adjectives in every beat.
3. **One primary spend, one secondary spend.** Every specialist output competes for the same prompt budget; synthesis means selecting, not concatenating.
4. **References offload spatial fidelity.** In I2V/R2V, prompt mainly what the asset cannot show: motion, timing, camera path, sound, and the intended endpoint.
5. **Precision is not word count.** A high-density master can be more important than a paragraph of detail; additional detail is kept only when it changes a visible decision.

## The premise [field]

Identity fidelity, motion boldness, and scene density compete for the same generation budget. The known fragile areas — detail stability, multi-subject consistency, text rendering, facial micro-acting — are where overdrawn budgets fail first. A shot that needs a perfect face, a backflip, a crowded market, and a spoken line in one call will land none of them cleanly.

## The three spends

| Spend | What it buys | What it strains |
|---|---|---|
| Identity fidelity | stable faces, products, logos, costumes | motion range; every bold move risks drift |
| Motion boldness | committed action, physics, choreography | close-up identity detail, especially faces and hands |
| Scene density | crowds, layered environments, weather, props | per-subject stability; tiny background detail degrades |

## Allocation method [heuristic]

1. Name the primary spend — the one thing this shot is for. One per generation.
2. Pick one secondary; economize everything else on purpose.
3. Offload fidelity to references: identity carried by `[Image1]` is budget the text no longer spends, freeing prose for motion and timing.
4. Pay for the primary out of the others: bold motion buys down facial detail, so stage emotion in the body and ration close-ups; dense scenes buy down subject precision, so keep hero subjects large in frame and few in number.
5. Re-anchor across a series: chained generations drift, so respend on identity (original references, not outputs) every few clips.

## Worked allocations [field]

| Shot | Primary | Secondary | Economized |
|---|---|---|---|
| Product ad | product identity (ref-anchored) | one material motion beat | scene density, crowd, weather |
| Dance / action | motion boldness (donor `[Video1]`) | identity via `[Image1]` re-anchor | facial close-ups, set dressing |
| Establishing world shot | scene density and atmosphere | camera move | character identity (no close subjects) |
| Dialogue close-up | facial stability (locked camera) | the spoken line | motion, background activity |

## Trade table [field]

| If the shot needs | It pays with |
|---|---|
| Bold motion and a close-up face | choose one; put the emotion in posture and staging, or cut to a separate close-up shot |
| Many subjects | per-subject identity precision; pick one hero and let the rest read as shapes |
| Readable on-screen text | nothing — move text to post |
| A crowded frame and a tiny product detail | the detail; isolate the product beat in its own shot |

## Pre-write checklist [heuristic]

For sequence projects, allocate the current clip before allocating the full story. The full story owns objective and final outcome; the current clip owns one action, one endpoint, and the continuity locks needed for the next handoff. Future beats are not part of the current prompt budget.

1. What is this shot for — identity, motion, or world?
2. Which references carry fidelity so the text does not have to?
3. What is deliberately economized, and is that written as a constraint?
4. If the answer to 1 is "all three," which beats split into separate shots or generations?
