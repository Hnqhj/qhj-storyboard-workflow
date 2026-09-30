---
name: creative-casebook
description: 创意案例库：把成功与失败的生成结果转成可复用的案例卡、提示词增量、模板、评估规则与定向技能更新。触发：这个效果好、这个不行、记住这个、复盘一下、沉淀经验、做成案例、模板库、案例库、为什么这次有效、下次沿用。 Turn successful and failed creative generations into reusable case cards, prompt deltas, templates, evaluation rules, and targeted skill updates. Proactively use when the user says 这个效果好, 这次可以, 这个不行, 记住这个, 复盘一下, 沉淀经验, 做成案例, 模板库, 案例库, 为什么这次有效, 下次沿用, or when repeated AI image/video prompting, character design, cover design, shot design, reference workflows, or retry cycles reveal a transferable lesson.
---

# Creative Casebook

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism:

- Confirm the observed result is real evidence, not an assumption based only on the prompt.
- Separate the successful layer from the failed layer.
- Extract a reusable control, not a vague taste judgment.
- Decide whether the lesson belongs only in a case card or should update a shared skill, template, checklist, or negative block.

## Core Intent

Convert user feedback and generated outputs into durable creative evidence. Preserve the relationship between input, visible result, diagnosis, and next prompt change so future work does not repeat the same experiment blindly. Send mature lessons to `$capsule-engine`; do not treat the casebook itself as the final knowledge store.

Do not store private assets, raw prompts, or user files outside the current task unless the user explicitly asks. When updating shared skills, store generalized rules rather than identifying project details.

## Evidence Rule

Prefer this evidence order:

1. Generated image/video inspected directly; for video, prefer `$ai-video-output-review` timestamped frames and contact-sheet evidence.
2. User identifies the exact successful or failed element.
3. Prompt and reference roles are available for comparison.
4. Inference from description only.

Mark inferred conclusions as tentative. Do not claim a prompt phrase caused an effect when several variables changed together.

## Workflow

1. Identify the case goal, model/mode, duration/aspect ratio, references, and starting prompt.
2. Record what visibly worked:
   - identity/continuity
   - composition/blocking
   - story/emotion
   - shot grammar/camera
   - action/rhythm
   - aesthetic system
   - material/light/rendering
   - model stability
3. Record what visibly failed using the same categories.
4. Find the smallest prompt/reference/workflow delta most likely responsible.
5. Extract the transferable rule in control language:
   - when to use it
   - what it controls
   - what it must not override
   - likely side effects
   - how to verify it
6. Decide the destination:
   - case card only
   - candidate capsule
   - reusable prompt fragment
   - negative constraint
   - preflight check
   - retry rule
   - update to one or more skills
7. Keep conflicting lessons conditional. A rule that helps a locked portrait may hurt a high-speed action shot.
8. When the lesson has evidence, application conditions, failure boundaries, and future value, use `$capsule-engine` to create a candidate. Keep ambiguous lessons in the casebook.

Read `references/case-card-template.md` when producing or saving a reusable case.

## Promotion Rules

Promote a lesson into a shared skill when at least one is true:

- The same failure occurred more than once.
- The mechanism is independently supported by audiovisual, rendering, design, safety, or engineering logic.
- The fix applies across multiple scenes or projects.
- Missing the rule causes expensive retries, continuity loss, unsafe actions, or repeated user correction.

Keep it as a case-specific note when:

- Only one generation supports it.
- Several variables changed together.
- The effect may be model/version dependent.
- It depends on one character, image, location, or taste choice.

## Output Shape

```text
案例判断：
目标：
有效部分：
失败部分：
关键变量：
最可能因果：

可复用规则：
适用条件：
副作用/禁用条件：
验证方式：

建议沉淀到：
是否创建候选胶囊：
下一轮只改：
```

For a positive result, still name what should remain locked. For a failed result, preserve what worked and change one main variable first.

## Guardrails

- Do not confuse correlation with causation.
- Do not save adjective-only lessons such as "more cinematic" or "more premium".
- Do not generalize platform-specific behavior into a universal law without marking the model/mode.
- Do not overwrite a shared skill because of one ambiguous generation.
- Do not collect cases without a retrieval key: domain, model/mode, symptom, mechanism, and outcome.
- Do not turn the casebook into a chronological diary; keep only decision-changing lessons.
