# Self-Iteration Review Protocol

## Review Windows

- Recent: files and evidence from the last 7 days.
- Recurring: same finding fingerprint in at least 2 recorded audits.
- Stale: source notes older than their domain's expected change rate.
- Deep review: architecture and cross-skill overlaps, normally monthly or after repeated correction.

## Finding Categories

- `structure`: invalid or hard-to-maintain skill structure.
- `routing`: wrong skill/source/tool selected.
- `quality`: output repeatedly misses user expectations.
- `continuity`: identities, props, scenes, or rules drift.
- `research`: stale or missing external knowledge.
- `verification`: work was delivered without adequate checks.
- `duplication`: same rule exists in multiple places and may diverge.
- `safety`: destructive, external, paid, private, or irreversible risk.
- `system-bloat`: new mechanisms add complexity without user value.

## Severity

- `critical`: unsafe action, data loss risk, broken database, or invalid core mechanism.
- `high`: repeated user correction, major workflow failure, or unusable deliverable.
- `medium`: recurring friction, weak routing, stale important source, or maintainability issue.
- `low`: formatting, metadata, or optional polish.

## Root-Cause Questions

1. Was the real intent misunderstood?
2. Was the wrong source of truth used?
3. Was the professional domain knowledge missing?
4. Was the correct skill not triggered or sequenced?
5. Was the prompt overloaded, underspecified, or contradictory?
6. Was validation missing?
7. Is the issue local, or does it reveal a shared mechanism?

## Change Gate

Automatic change is allowed only when all are true:

- evidence is named;
- change scope is small;
- change is reversible;
- no private/external/destructive action is involved;
- validation is available now;
- the change does not override a user-confirmed value or taste decision.

Otherwise report a recommendation.

## New-Information Gate

An external development is relevant only if it changes:

- platform capability or limitation;
- prompt/reference strategy;
- professional vocabulary or technique;
- safety/legal boundary;
- tool availability;
- a current active capsule or skill rule.

Interesting but unactionable discoveries remain spores.

## Clean Audit

A clean audit is valid. Record:

- inspected evidence;
- validators run;
- no material change made;
- one optional monitoring focus for the next run.
