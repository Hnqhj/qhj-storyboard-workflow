---
name: capsule-engine
description: 知识胶囊引擎：把真实证据、用户反馈、案例卡、重复失败、已验证修复与架构决策转成带生命周期的可复用知识胶囊，含质量指标、应用事件、冲突链接、技能传播与弃用。触发：胶囊、孢子、内化、能力沉淀、经验变能力、知识进化、规则升级。 Convert real evidence, user feedback, case cards, repeated failures, verified fixes, and architecture decisions into scoped reusable knowledge capsules with lifecycle states, separate quality metrics, application events, conflict links, skill propagation, and deprecation. Proactively use when the user says 胶囊, 孢子, 内化, 能力沉淀, 合成智慧, 经验变能力, 置信度, 知识进化, 规则升级, 这条要进入系统, or when a validated lesson should move from creative-casebook into durable Sophia memory or update one or more skills.
---

# Capsule Engine

## Bottom-Layer Reasoning

Apply `think-one-step-further` before writing or promoting a capsule:

- Confirm the lesson changes a future decision or action.
- Separate observed evidence from inference.
- Bind the rule to conditions and failure boundaries.
- Decide whether it belongs in memory, a capsule, a skill, or all three.
- Avoid creating duplicate rules or fake precision.

## Core Intent

Turn evidence into durable capabilities without turning memory into a diary. Use one SQLite database as the single source of truth:

`D:\SophiaMemory\data\sophia_memory.sqlite`

The capsule tables coexist with Sophia's existing memory tables. Do not create a second runtime copy.

## Knowledge Layers

Keep these distinct:

1. **Spore**: one new observation, correction, tradeoff, fix, or hypothesis.
2. **Case card**: one concrete experiment with inputs, output, result, and prompt/workflow delta.
3. **Capsule**: a minimal reusable rule with evidence, scope, boundaries, and validation history.
4. **Skill**: an executable workflow that may use many active capsules.
5. **Director/orchestrator**: selects and sequences skills for the current task.

Use `$creative-casebook` before this skill when the evidence comes from a generated result that needs diagnosis.
Use `$evidence-driven-self-iteration` to detect recurring findings and stale areas. A scheduled audit finding is evidence to investigate, not automatic proof for capsule promotion.

## Lifecycle

Use:

```text
candidate -> provisional -> validated -> active -> deprecated -> archived
```

- **candidate**: captured but not independently verified.
- **provisional**: one successful application or useful confirmation.
- **validated**: at least two independent successful contexts and adequate evidence confidence.
- **active**: explicitly approved for routine use or skill propagation.
- **deprecated**: retained for history but replaced, unsafe, or no longer preferred.
- **archived**: no longer part of normal retrieval.

Application is an event, not a status. Record success, failure, neutral result, and counterexample separately.

User-confirmed architecture or operating-policy decisions may be activated without two empirical trials when clearly marked as a policy decision, not an empirical truth.

## Metrics

Never compress everything into one confidence number:

- `evidence_confidence`: credibility of the supporting evidence.
- `context_fit`: how well the capsule matches its bound scenarios.
- `utility_score`: whether applying it helps.
- `freshness`: how current the evidence is.
- `stability`: how consistently it survives different applications.

Age may lower freshness. It must not automatically make a fact false.

## Workflow

1. Capture a spore or receive a case card.
2. Search existing capsules for overlap, conflict, or a narrower existing rule.
3. Create a candidate capsule only if it changes future behavior.
4. Record:
   - what works
   - when to apply
   - why it works
   - failure conditions
   - bound scenarios
   - source references
5. Apply it in real work and record an event with a distinct `context_key`.
6. Allow the tool to advance candidate/provisional capsules from independent successful contexts.
7. Before activation, check conflicts, side effects, target skills, and retrieval tags.
8. Propagate only the generalized control into related skills.
9. Deprecate or narrow the capsule when counterexamples appear.

Read:

- `references/capsule-architecture.md` for lifecycle, promotion, synthesis, and conflict rules.
- `references/capsule-schema.md` for field definitions.

## Deterministic Tool

Use `scripts/capsule_engine.py`.

```powershell
python scripts/capsule_engine.py init
python scripts/capsule_engine.py stats
python scripts/capsule_engine.py search "站位"
python scripts/capsule_engine.py validate
```

Create a candidate:

```powershell
python scripts/capsule_engine.py create `
  --name "参考图职责隔离" `
  --capsule-class pattern `
  --knowledge-kind rule `
  --summary "每张参考只承担明确控制职责" `
  --what-worked "显式声明身份、布局、风格和材质参考的职责边界" `
  --when-to-apply "多参考图或全能参考工作流" `
  --why-it-works "减少参考之间争夺身份、构图和风格控制权" `
  --failure-conditions "单图工作流或模型不支持多参考职责" `
  --scenario "SD2全能参考" `
  --tag "reference-role" `
  --source-ref "user-confirmed case"
```

Record evidence:

```powershell
python scripts/capsule_engine.py record --id CAPSULE_ID --outcome success `
  --context-key "sd2-motorcycle-scene" --context "角色+摩托+站位图" `
  --result "身份和前后关系保持稳定" --source "generated output inspected"
```

Activate a validated capsule:

```powershell
python scripts/capsule_engine.py activate --id CAPSULE_ID `
  --target-skill jimeng-sd2-prompting --target-skill character-continuity-bible
```

## Promotion And Propagation

Do not promote because a rule sounds intelligent.

Promote when:

- evidence is inspectable;
- the mechanism is stated concretely;
- application conditions and failure boundaries exist;
- independent successful contexts support it, or it is an explicit user-confirmed architecture policy;
- no unresolved conflict makes the rule unsafe;
- the target skill benefits from the rule.

When propagating, write the smallest executable control into the target skill and keep full evidence/history in the capsule database.

## Synthesis

Combine capsules only when the result removes real duplication or creates a useful higher-order workflow.

Relations:

- `synergy`: strengthens the same outcome.
- `complement`: handles a different layer or scenario.
- `conflict`: cannot both apply under the same conditions.
- `tension`: preserve both and choose by context.
- `supersedes`: newer capsule replaces an older one.
- `derived_from`: capsule was synthesized from others.
- `feeds_skill`: capsule supplies a skill rule.

Do not assign arbitrary percentage weights. Express contribution through capabilities, conditions, dependencies, and conflicts.

## Guardrails

- Do not run random learning or heartbeat activity merely to create records.
- Scheduled self-audits may inspect and record evidence, but must not create or promote capsules merely because the schedule ran.
- Do not create capsules for routine status, compliments, greetings, or one-off wording.
- Do not promote a single ambiguous generation into a universal rule.
- Do not treat frequency of use as truth.
- Do not overwrite evidence history; append events.
- Do not store secrets, raw private assets, or unnecessarily identifying project data.
- Do not change or delete active capsules silently; deprecate or supersede them with a reason.
