# Cross-Domain Transfer

Use this reference when optimizing a reusable workflow, skill suite, prompt system, codebase, file organization, or any deliverable that may imply adjacent improvements.

## Three-Level Check

1. **Outcome level**: Did the immediate answer or artifact solve the user's real goal?
2. **Method level**: Is the method repeatable, controllable, validated, and easy to reuse?
3. **Ecosystem level**: Does the same fix belong in another skill, prompt template, checklist, folder rule, script, test, or workflow?

Do not always act on all three levels. Act only when the extra change is low-risk, clearly aligned, and saves repeated future work.

## Do Now Or Defer

Do it now when:

- The adjacent change is mechanical, safe, and in the same ownership area.
- The user explicitly asked for "overall", "all", "通用", "底层", "整套", or "以后都这样".
- The current failure will likely repeat unless the shared rule is updated.
- The result would otherwise require the user to perform an obvious follow-up step.

Defer or mention briefly when:

- It changes scope, deletes data, spends money, changes live systems, or requires taste choices.
- It depends on unavailable references, private accounts, current web facts, or missing user intent.
- It would make the current answer bulky without improving immediate usability.

## Transfer Matrix

| Source case | Transferable mechanism | Adjacent optimization |
| --- | --- | --- |
| AI video prompt failed | Identify drift source, overloaded beat, missing reference role, weak style ownership, or impossible timing | Update preflight checks, continuity locks, retry template, and director routing |
| AI image/video looks cheap | Separate medium, aesthetic family, material truth, lighting logic, render terms, and anti-generic constraints | Update aesthetic skill, material realism skill, and prompt skeletons |
| Character/vehicle position changes | Define layout reference role, footprint, long-axis orientation, facing direction, layer order, camera path | Update continuity skill, SD2 packaging, and audiovisual blocking rules |
| A prompt works well | Extract reusable structure: hook, temporal hinge, shot grammar, style layer, material layer, negatives | Save as template or add to the relevant skill reference |
| Code fix works | Identify affected call sites, tests, docs, config, backward compatibility, and regression surface | Add or update tests, comments, docs, or shared helper only when warranted |
| File cleanup works | Define keep/delete rules, excluded paths, reversible staging, naming scheme, future inbox process | Add retention rules, folder structure, and safety checks |
| Research/report answer works | Check source freshness, citation quality, uncertainty, decision relevance, and update cadence | Add monitoring keywords, source list, or report template |
| Skill update works | Check trigger description, body workflow, references, UI metadata, validation, and related skills | Propagate shared rules to the suite and validate all skills |
| Design direction works | Extract tokens: palette ownership, typography, layout grid, material system, interaction rules | Update style bible, component rules, and QA gates |
| Story/structure works | Extract character state, desire, obstacle, turn, consequence, time hinge, and payoff rhythm | Update script template, video structure map, and shot-design handoff |

## Handoff Pattern

For complex work, finalize with only the useful pieces:

```text
已处理：
可直接用：
已验证：
还需要你做：
顺手优化：
下一处风险：
```

Omit any line that would be empty or distracting.

## Anti-Patterns

- Do not add vague "还能继续优化" remarks.
- Do not convert every small answer into a strategy memo.
- Do not create a new abstraction unless it prevents real repetition or protects a fragile workflow.
- Do not hide necessary next actions inside a long explanation.
- Do not over-transfer: a pattern from one domain must become a concrete control in the target domain.
