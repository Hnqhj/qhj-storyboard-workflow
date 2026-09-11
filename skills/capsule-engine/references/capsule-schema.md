# Capsule Schema

## Classification

- `capsule_class`: `pattern | synthesis | architecture | response`
- `knowledge_kind`: `fact | rule | process | opinion | hypothesis`
- `status`: `candidate | provisional | validated | active | deprecated | archived`

These are separate axes. Capsule class describes its structural role; knowledge kind describes the nature of its claim.

## Core Fields

- `id`: stable generated identifier.
- `name`: concise retrieval name.
- `summary`: one-sentence decision-changing lesson.
- `what_worked`: executable control or successful mechanism.
- `when_to_apply`: trigger condition.
- `why_it_works`: causal explanation.
- `failure_conditions`: boundaries, side effects, and invalid scenarios.
- `bound_scenarios`: JSON list of supported scenarios.
- `tags`: JSON retrieval list.
- `source_refs`: JSON list of evidence references.
- `target_skills`: JSON list of skills that consume the capsule.
- `supersedes`: optional older capsule id.

## Metrics

All metric values are between `0` and `1`.

- `evidence_confidence`
- `context_fit`
- `utility_score`
- `freshness`
- `stability`

## Events

Event types include:

- `capture`
- `application_success`
- `application_failure`
- `application_neutral`
- `counterexample`
- `promotion`
- `activation`
- `deprecation`
- `archival`
- `synthesis`
- `link`

Every event should state source, context, result, and context key when applicable.

## Spores

Spore kinds:

- `decision`
- `gotcha`
- `discovery`
- `tradeoff`
- `fix`
- `hypothesis`

Spore states:

- `pending`
- `consumed`
- `rejected`

A spore is not trusted merely because it was captured.
