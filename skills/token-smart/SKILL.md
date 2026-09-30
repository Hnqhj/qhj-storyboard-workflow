---
name: token-smart
description: 精简上下文、工具调用、重复检查与叙述，同时保留任务范围与必要验证。触发：省 token、精简执行、按需应用 token-smart 偏好。 Reduce avoidable context, tool calls, repeated checks, and narration while completing the requested work. Use when asked to save tokens, work lean, or apply an installed token-smart preference; preserve task scope and necessary validation.
---

# Token Smart

Optimize unnecessary work, not required work. Follow the user's requested depth, complete deliverables, domain requirements, and the host's instructions. Use the user's language.

## Working rules

- **Read to decide.** Start with the current request and a small relevant state summary. Search names or keywords, then read the matching sections and their needed dependencies. Reuse unchanged evidence; widen the read when a concrete question remains. A summary points to originals; it does not replace evidence or authorize actions.
- **Choose one lead.** Use only the skills that change the current decision. Simple lookup, formatting, and fixes settled by inspection need no elaborate method stack. Load branch references only when their trigger applies.
- **Reuse the working path.** Understand the real inputs, callers, and outputs before editing. Prefer existing behavior, a standard library, or a small direct implementation over new dependencies and abstractions.
- **Check a real failure.** Before a check, know what failure it can detect and what would change if it failed. Prefer executable checks for objective facts. Once relevant checks pass, deliver; repeat or widen them only after new changes, new failures, stale inputs, or a remaining material concern. User-required tests still apply.
- **Spend reasoning where it changes the result.** Use focused self-review for ordinary work. Add independent review for material external impact, security or data-loss risk, unresolved critical uncertainty, or an explicit request. Never claim to change model, reasoning effort, billing, or context settings unless the host actually exposes and confirms that change.
- **Delegate only independent work.** A bounded subtask needs an input, output, and completion condition. Send the smallest self-contained brief instead of full history. Start evaluations with representative cases; expand only when the evidence can change the decision.
- **Carry state, not a transcript.** For long work, reuse the host's task summary or one task-scoped note with the goal, verified progress, unresolved issues, and source pointers. Do not duplicate existing memory or create a note for a trivial task. On recurring runs, check for changed state or missing work before expensive processing.
- **Trim commentary, not the result.** Give conclusions, necessary evidence, and real blockers. Avoid routine reading/thinking reports and repeated summaries. Preserve requested code, analysis, citations, and full artifacts; expand when asked.

Stop when the requested deliverables and relevant checks are complete. If essential input or authorization is missing, ask the smallest question that changes the next action; continue independent authorized work.

## Installation explanation

When handling installation or a request to explain this pack, read [onboarding.md](references/onboarding.md), or [onboarding.en.md](references/onboarding.en.md) for English, and relay it briefly to the user. The installer also prints this explanation. Do not read or repeat onboarding during ordinary tasks.

Installation makes the skill discoverable, not guaranteed to run in every turn. Persistent activation requires an explicit host instruction; a skill file cannot create a startup event. No token-saving percentage is established by these instructions.
