# Character Combat Identity

Read this reference when a recurring character must remain recognizable through **how they fight**, not only through face, costume, weapon, or color. It owns the compact prompt-facing combat identity card. Durable IDs, versions, approvals, and cross-shot state history remain with `$entity-continuity-system`; per-scene choreography remains with `$action-choreography-reference`.

## 1. Separate Identity From Deployment

Use two layers:

```text
durable combat identity: what should remain recognizable across fights
scene deployment: which parts of that identity solve the current opponent, space, objective, and duration
```

A character does not need to repeat the same move to remain consistent. Preserve the movement grammar, tactical preference, silhouette, force path, and recovery signature while allowing the scene to choose a different action.

## 2. Combat Identity Card

Record only fields that visibly change performance:

```text
entity ID / combat-profile version:
dramatic combat role: pressure-owner / intercept-counter / control-convert / evade-reenter / protect-delay / other
primary movement or martial basis:
optional secondary basis and its single job:
preferred range and entry method:
stance, support, body level, and silhouette motif:
dominant force path and attack geometry:
rhythm and recovery signature:
preferred defensive answer:
signature transition or reversal source:
weapon/equipment/fantasy function:
function-tagged move pool:
approved phase variants and visible transition proof:
forbidden drift:
approved visual evidence / last verified case:
```

### Functional Tags

Use a small move pool organized by what an action accomplishes:

| Tag | Function |
| --- | --- |
| `ENTRY` | enter range or claim a line |
| `PROBE` | test guard, distance, or timing |
| `INTERCEPT` | interrupt an incoming route |
| `CONTROL` | pin a line, grip, angle, balance point, or objective access |
| `BREAK` | create a visible opening or remove support |
| `PRESSURE` | keep the opponent answering under cost |
| `REVERSAL` | convert a prior disadvantage into initiative |
| `EXIT_RECOVER` | brake, disengage, regrip, regain support, or reset distance visibly |
| `FINISH` | resolve the objective or deliver the decisive consequence |

The pool is not a syllabus. Three to five verified signature actions or transitions are usually more useful than dozens of names. Each entry should contain:

```text
name or descriptive anchor:
function tag:
visible mechanics:
required range/support/contact:
natural predecessor:
end state / next source:
known generation failure:
```

If a martial or movement name is unfamiliar, uncertain, or historically specific, verify it before promoting it to the durable card. A descriptive movement alternative should remain available.

## 3. Primary And Secondary Basis

Use one primary basis to establish identity. Add at most one secondary basis in a short beat, and assign it one missing function such as entry, range control, weapon handling, ground recovery, or fantasy amplification.

The secondary basis must not replace the primary stance, rhythm, or recovery without a visible transition and an approved profile update. Percentages such as “70% style A / 20% style B” are optional planning notes, not reliable prompt controls.

## 4. Anti-Drift Rules

Write positive identity behavior first, then one or two failure-specific boundaries:

- preserve the preferred range, force path, rhythm, and recovery signature;
- preserve the role contrast: pressure, interception, conversion, evasion, protection, or control;
- preserve one recurring support or silhouette motif;
- let different opponents change tactics without erasing the character's grammar;
- keep temporary scene tactics local unless the user approves them as a new combat-profile version.

Do not enforce zero move reuse. Reuse is valid when opponent, purpose, range, setup, response, or consequence changes. Reject repetition only when the same pair repeats the same action chain with the same function and visible result.

### Phase Variants

A recurring fighter may have probe, pressure, damaged, transformed, or finish-oriented phases without becoming a different character. Record only approved variants that visibly change performance:

```text
phase trigger:
what remains invariant: primary basis, role, force path, recovery, silhouette, or other identity proof
what may change: stance, range, support, tempo, weapon function, risk tolerance, or selected function tags
visible transition proof: step, regrip, stance/base change, altered guard, equipment change, recovered support, or other physical cue
exit condition:
```

A new facial expression, color effect, or intensity adjective is not a combat-phase change by itself. The next action grammar must visibly use the changed stance, range, support, or tactical function. Unapproved transformations stay local to the scene.

### Reuse Fingerprint

For a recurring opponent pair or repeated sequence, compare the planned chain against a compact fingerprint rather than banning all reuse:

```text
performer pair and objective
+ setup and range
+ route / level / support state
+ receiver answer or control relation
+ function and reversal source
+ consequence / end state
```

If most fields repeat, vary at least one causal layer that changes the visible exchange. A renamed move with the same setup, answer, route, and result is still repetition. A signature action may recur when its setup, answer, function, or consequence changes. Store only selected or approved fingerprints in the current project ledger or entity state history; do not turn the prompt into a global move database.

## 5. Scene Deployment

For the current fight:

1. Read the approved combat-profile version.
2. Identify the scene problem: opponent grammar, distance, objective, environment, duration, and generation budget.
3. Select only the function tags and approved phase variant needed for this beat.
4. For a recurring pair, compare one compact reuse fingerprint; vary the causal layer only when the prior setup, answer, route, function, and result would otherwise repeat.
5. Hand the identity constraints and selected functions to `$action-choreography-reference`.
6. Receive the designed route, contact, response, recovery, and end state.
7. Compile only the strongest visible identity anchors into the current prompt.

Short prompt-facing form:

```text
Combat identity: [primary basis], [role], [preferred range], [visible stance/force/rhythm signature].
This beat uses: [ENTRY/PROBE/etc.] through [one or two prompt-ready actions].
Identity proof: [one recurring silhouette/support/recovery cue].
Current allowed variation: [opponent- or environment-specific tactic].
Drift boundary: [one likely failure and positive replacement].
```

## 6. Approval And Versioning

Generated variation is a candidate, not a new fact. Promote a new action, transition, secondary basis, or recovery signature only when:

- the output is inspected and the mechanism is actually visible;
- it remains compatible with the primary combat identity;
- its function and application boundary are recorded;
- the user approves keeping it for later fights.

Send the approved update to `$entity-continuity-system` with entity ID, combat-profile version, evidence path, and effective scope. Single-scene improvisation stays local.

## Quality Gate

- The character remains identifiable without naming costume color or special effects.
- The primary basis owns stance, range, force path, rhythm, and recovery.
- Every selected action has a function in the current exchange.
- The secondary basis fills one explicit gap instead of creating a mixed-style catalogue.
- The prompt carries only a few visible identity anchors, not the entire move library.
- Temporary tactics do not silently overwrite the durable combat profile.
- A phase change alters visible action grammar rather than only expression or effects.
- Reuse is judged by setup, answer, route, function, and result—not by move name alone.
