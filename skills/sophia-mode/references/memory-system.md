# Sophia Memory System

Use this reference only when creating, migrating, or updating Sophia memory files.

## Layers

- L0 identity wake-up: minimal stable facts about the user and Sophia's interaction style.
- L1 session state: current task, active project, recent decisions, pending follow-ups.
- L2 semantic state: durable preferences, rules, tool procedures, boundaries.
- L3 historical memory: timestamped events, decisions, task history, and evidence.
- Capsule layer: validated reusable operational knowledge with scenario bindings, metrics, application events, conflicts, and skill targets.

Do not cold-load full memory. Load the smallest relevant layer first, then expand only if needed.

## Write Filter

Ask three questions before writing:

1. Is it worth remembering?
2. Is it unambiguous?
3. Is it self-contained enough to be useful later?

Write when value is at least moderate and the entry is clear enough. Temporarily stage information that is valuable but ambiguous or incomplete. Discard routine logs, greetings, normal heartbeats, and duplicate status messages.

Each durable entry should include:

- Date: `YYYY-MM-DD`
- Source: user-confirmed, official/source-verified, search-verified, or inference
- Confidence: high, medium, or low

## Entity Page Template

Use this structure for important people, projects, concepts, and events:

```markdown
# Entity Name

## Current State
> Last updated: YYYY-MM-DD

The latest compiled understanding. This section may be rewritten.

### Core Facts
- Fact:
- Relation:

### Open Items
- [ ] Item

---

## Timeline
> Append only.

### YYYY-MM-DD | Event Type
- Source:
- Confidence:
- Detail:
```

## Routing

- Identity, values, and behavior: `SOUL.md`
- User facts and preferences: `USER.md` or `memory/entities/people/主人.md`
- Events and decisions: `MEMORY.md` or entity timeline
- Tool procedures and gotchas: `TOOLS.md`
- Credentials and sensitive facts: `SECRET.md`, never copied into ordinary logs
- Current session: `SESSION-STATE.md`
- Reusable capability capsules: `D:/SophiaMemory/data/sophia_memory.sqlite`, managed by `C:/Users/liu1/.codex/skills/capsule-engine/scripts/capsule_engine.py`

## Spores

Extract a spore only when the idea is new, reusable, and can be stated in one sentence.

Types:

- `decision`: a choice that should guide later work
- `gotcha`: a pitfall to avoid
- `discovery`: a useful new finding
- `tradeoff`: a reusable decision tradeoff
- `fix`: a repair that prevents recurrence

Do not create spores for trivia, routine status, or unverified guesses.

## Capsule Routing

- Personal fact, preference, project state, commitment: normal Sophia memory.
- One concrete generation or workflow experiment: `$creative-casebook`.
- New one-sentence observation: spore.
- Reusable rule with conditions and boundaries: candidate capsule.
- Repeated independently successful rule: validated capsule.
- Explicitly approved routine behavior or skill control: active capsule.

Do not duplicate full capsule evidence into entity pages or SKILL.md. Keep only a concise operating rule in the consuming skill.
