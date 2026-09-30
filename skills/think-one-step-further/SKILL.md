---
name: think-one-step-further
description: 多想一步的底层推理：检查正确性、下一步动作、可迁移性、邻近优化、可能的下一处失败，以及已验证的经验是否该固化为胶囊。触发：举一反三、多想一步、底层逻辑、整体优化、整套优化、这个处理对不对、还需不需要做什么、有没有别处也能优化。 Apply a bottom-layer "think one step further" reasoning pass. Proactively use when the user says 举一反三, 多想一步, 底层逻辑, 整体优化, 整套优化, 这个处理对不对, 还需不需要做什么, 有没有别处也能优化, or when Codex is creating or revising reusable prompts, skills, workflows, plans, code changes, cleanup actions, visual/video directions, or deliverables that should be checked for correctness, next actions, transferability, adjacent optimizations, likely next failure points, and whether a verified lesson should become a durable capsule.
---

# Think One Step Further

## Overview

Use this skill as a lightweight final reasoning layer. It does not replace the active domain skill; it checks whether the current answer or action is actually complete, usable, transferable, and protected against the next likely failure.

For tiny tasks, apply the checks silently and keep the response short. For complex or reusable work, surface the useful parts under a concise "One Step Further" note.

## Reference Routing

Read `references/cross-domain-transfer.md` when the user asks for overall optimization, skill-suite updates, workflow architecture, prompt-system architecture, or when a local fix probably belongs in multiple related places.

## Core Loop

Before finalizing a response, action, prompt, file, or workflow, run these checks:

1. **Correctness check**: Is this solving the real problem, or only the literal request? Identify hidden assumptions, missing constraints, conflicts, risky shortcuts, and whether the chosen method matches the user's actual goal.
2. **Usability check**: Can the user use the result immediately? Add only the missing practical pieces: final file link, exact prompt, command, next click, verification status, reference-role map, negative prompt, or retry instruction.
3. **Aftercare check**: After this output lands, what will the user naturally need next? Decide whether to include it now, save it as a follow-up suggestion, or withhold it because it would distract.
4. **Transfer check**: What is the reusable mechanism behind this case? Look for adjacent places where the same structure, rule, vocabulary, checklist, template, or automation should also be improved.
5. **Failure forecast**: What is most likely to fail next: drift, ambiguity, inconsistent position, weak material, bad pacing, broken validation, unsafe deletion, stale data, missing tests, or user confusion? Add one guardrail when useful.
6. **Internalization check**: Is there enough real evidence to route this lesson to `$creative-casebook` and then `$capsule-engine`, or should it remain a tentative case-specific note?
7. **Attribution check**: If something failed, did I inspect my inputs, execution path, references, assumptions, and tool output before blaming the model, system, or configuration?

## Readiness Gate

Before handing off, decide whether the result is:

- **Ready**: the user can use it immediately; state verification and exact location/prompt/action if useful.
- **Ready with caveat**: the result is usable, but one risk or missing external input remains; name it plainly.
- **Needs one more pass**: a required check, file, source, reference role, validation, or safety step is missing; complete it before finalizing when possible.
- **Blocked**: a required fact, permission, tool, or user choice is unavailable; ask only for that missing piece.

Use this gate to avoid false completion. Do not claim a deliverable is done if the user still needs to infer how to use it.

For complex handoff, require evidence appropriate to the task: tests, rendered output, inspected file, query result, generated artifact, current source, or explicit caveat. Self-confidence is not verification.

## How To Generalize

Extract the pattern, not just the topic:

- From one failed AI video, derive controls for continuity, spatial staging, style ownership, motion readability, and retry diagnosis.
- From one good prompt, derive a reusable prompt skeleton, reference roles, material layer, camera layer, and preflight checks.
- From one computer cleanup, derive retention rules, excluded folders, reversible actions, and future organization structure.
- From one code fix, derive affected call sites, test surfaces, documentation/config updates, and regression risks.
- From one skill update, derive trigger metadata, shared wording, validation, and whether related skills need the same mechanism.

When borrowing from adjacent domains, prefer control vocabulary that can change the output: film language, editing, rendering, photography, product design, fashion, architecture, game art, UX, operations, safety, testing, information architecture, or project management.

## Propagation Rules

If a local fix reveals a shared rule, decide whether to propagate it:

- Propagate now when the change is mechanical, low-risk, and clearly belongs to the same skill family.
- Add a brief note instead when the change would expand scope, change taste direction, delete data, alter live systems, or require user preference.
- Do not create a new abstraction unless it prevents real repetition, reduces ambiguity, or protects a fragile workflow.
- When the lesson has evidence, conditions, boundaries, and future value, create or update a capsule instead of duplicating the full history across many skills.

## Output Discipline

Do not turn every answer into a long checklist. Use this scale:

- **Small request**: Answer directly; include only one extra sentence if it prevents a likely problem.
- **Medium task**: Add 2-4 concise bullets for what was checked, what remains, and what can be reused.
- **Complex deliverable**: Include a compact handoff: what changed, why it is ready, validation, next-use instructions, and one adjacent optimization.
- **Review or diagnosis**: Lead with the main issue, then the next action, then the transferable rule.

Avoid generic suggestions like "you can optimize more later." Name the exact thing to optimize, why it matters, and whether it is necessary now.

For complex work, use only the lines that matter:

```text
已处理：
可直接用：
已验证：
还需要你做：
顺手优化：
下一处风险：
```

## Decision Questions

Ask these internally:

- Did I handle the user's real intent, or only their surface words?
- Does the result remove work from the user, or secretly hand them another unresolved task?
- If the user uses this immediately, where could it break, drift, or confuse the model/system/person?
- Is this a one-off fix, or should the same architecture update another prompt, skill, folder, checklist, or workflow?
- What is the minimum extra step that would make the result safer, clearer, stronger, or more reusable?

## Coordination With Other Skills

When another skill is active, keep that skill's workflow as the primary method. Use this skill at the edges:

- At the start, clarify the real success condition if the request is broad or emotionally loaded.
- During work, notice whether a local fix implies a shared rule or cross-skill update.
- Before final output, verify usability, aftercare, transferability, and likely next failure.
- After confirmed results, use `$creative-casebook` to isolate the causal lesson and `$capsule-engine` to manage durable validation, activation, conflicts, and deprecation.

If this skill suggests a larger adjacent change, do it only when it is low-risk and clearly aligned with the user's request. Otherwise, mention the option briefly without derailing the current task.
