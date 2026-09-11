# Capsule Architecture

## Evidence Flow

```text
spore
  -> case card or direct architecture decision
  -> candidate capsule
  -> provisional after one successful context
  -> validated after two independent successful contexts
  -> active after explicit propagation decision
  -> deprecated or narrowed after counterexample
```

## Promotion Rules

Candidate to provisional:

- one recorded success;
- the result is observable;
- the event names a context key.

Provisional to validated:

- at least two successful events;
- at least two distinct context keys;
- `evidence_confidence >= 0.70`;
- no unresolved counterexample after the latest success.

Validated to active:

- explicit activation;
- target scenario or target skill is named;
- failure conditions exist;
- conflict links have been reviewed.

Policy activation:

- allowed for an explicit user-confirmed architecture or operating decision;
- capsule class must be `architecture`;
- knowledge kind must be `process` or `rule`;
- evidence confidence must be at least `0.85`;
- activation event must say it is a policy decision rather than empirical proof.

## Metric Behavior

Successful application:

- increase utility, context fit, and stability modestly;
- never raise evidence confidence automatically merely because the output looked good.

Failed application:

- reduce utility and context fit;
- keep the capsule active if the failure is outside its bound scenario;
- narrow the scenario when the mechanism remains sound.

Counterexample:

- reduce evidence confidence and stability;
- demote `active -> validated` or `validated -> provisional`;
- record the exact condition that breaks the rule.

Staleness:

- reduce freshness only;
- trigger review for platform versions, laws, prices, APIs, model behavior, and other unstable facts;
- do not lower truth confidence solely because a capsule was unused.

## Conflict Resolution

- **Synergy**: combine in orchestration; do not necessarily merge storage.
- **Complement**: preserve separate capsules and define ordering.
- **Conflict**: add a decision condition that selects one.
- **Tension**: keep both as competing values; require explicit tradeoff.
- **Supersedes**: deprecate the older capsule while retaining history.

## Retrieval

Retrieve by:

- domain;
- model or platform;
- symptom;
- mechanism;
- bound scenario;
- target skill;
- status.

Prefer active capsules. Include validated capsules when exploring or diagnosing. Do not silently apply candidate capsules.

## Skill Propagation

Store only the concise control in `SKILL.md`:

```text
When [condition], do [control], because [mechanism]. Avoid [failure boundary].
```

Keep source evidence, counts, dates, conflicts, and metrics in the database.
