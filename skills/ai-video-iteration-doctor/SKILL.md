---
name: ai-video-iteration-doctor
description: "成片失败诊断与下一轮精确重试：定位失败桶，下一轮只改一个主变量。触发：崩了、不对、太假、动作软、运镜乱、站位变了、人脸变了、武器变了、穿模、抖动、闪烁、背景漂移、情绪转变生硬、质感差、风格廉价、节奏不对、画面糊、不够电影感。 Diagnose AI video/image generation failures and prescribe the next precise retry. Proactively use when the user says the result is wrong, needs retry, 崩了, 不对, 太假, 动作软, 运镜乱, 站位变了, 人脸变了, 武器变了, 穿模, 抖动, 闪烁, 背景漂移, 情绪转变生硬, 质感差, 渲染差, AO/PBR没出来, 风格廉价, 审美差, 风格不高级, 节奏不对, 画面糊, 不够电影感, 不够张力, or asks what to change in the next prompt."
---

# AI Video Iteration Doctor

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Core Intent

Use this skill after a generated image/video result fails. Diagnose the likely cause, choose the smallest next change, and write a prompt patch. The goal is controlled iteration, not rewriting everything every time.

If the user provides an output video, use `$ai-video-output-review` first to extract timestamped evidence and inspect what is visible. For a still image, inspect it directly. If they only describe the failure, diagnose from symptoms and ask only for missing details that block a useful fix.

## Workflow

### 长镜头失败的首轮分流

当用户反馈“一镜到底效果差、运镜乱、动作僵硬”时，先把主失败桶设为 `镜头/空间负荷` 或 `动作/物理`，不要直接重写整段提示词。记录四项证据：主体是否漂移、镜头交接是否有触发、动作接触是否产生后果、场景是否具备纵深与遮挡。若一项短片同时要求超过两次运镜模式变化、两次以上主要接触、一次以上场景穿越和慢动作效果，判定为提示负荷过高的首要嫌疑。

下一轮只改一个主变量：优先减少事件数量或扩大连续空间；保留人物身份、色彩和核心情绪。预期证据必须可观察，例如“镜头由角色转身自然进入跟拍”“双武器不再同时乱动”“穿门后仍保持同一运动方向”。连续失败两轮后，停止继续加形容词，改做短段落链式生成或重新设计主镜。

如果用户反馈“整体太像游戏，但只想要游戏式击杀特效”，将主失败桶设为 `风格边界`。下一轮把游戏感限制在击杀接触后的短暂局部效果（通常不超过0.3秒），并恢复实拍基底：真实人体惯性、脚底支撑、布料拖曳、自然镜头曝光和环境材质。若用户要求换场景，必须同时检查连续路线、纵深、遮挡物、地形节点和终点揭示空间；仅替换地点名称不算修复。

1. Record `expected / actual / first visible deviation / preserved successes` in plain language. Do not begin from a global verdict such as ‘not cinematic’.
2. Reconstruct the actual attempt before blaming the model: inspect the generated result, prompt, reference roles, mode, duration, source images, and contradictory constraints when available.
3. Choose one suspected causal layer: input/brief, reference responsibility, mode/parameter, identity/geometry, action/physics, camera, look/material, edit/post, or verified model limitation.
   - For Liu short-drama groups, also classify the visible failure into exactly one primary bucket: `表演/聆听`, `台词/口型`, `景别/切镜`, `动作/物理`, `特效/合成`, `连续性/资产`, `声音协议`, or `模型/平台`. Use secondary buckets only when the output is otherwise unusable; this prevents a broad rewrite from hiding the true cause.
4. State one primary change, what must remain unchanged, and the predicted visible evidence. Add at most two secondary fixes only when the result is otherwise unusable, and declare that such a round cannot prove causality.
5. If the same failure family repeats twice or more, pause normal patching and escalate to evidence gathering before writing the next full prompt:
   - use `$ai-video-output-review` for visible timestamped proof when an output is available;
   - use `$reference-hunting-board` / `$creative-research-first` for missing aesthetic, camera, action, effects, or sound references;
   - for action stiffness, unclear 套招/喂招, repeated movement, or bad body method, use `$action-choreography-reference` with real movement/action references before redesigning.
6. Write a retry patch that preserves what worked. When a parameter or platform mode is under test, record `syntax accepted` separately from `effect observed`; no error is not proof that the intended control was effective.
7. Before writing any negative or context-change wording, run a contamination check. Do not put the failed image, old context, old prop, old location, old style, or old action mode into the negative patch unless it is a broad recurring failure class. Convert the retry into current positive visible facts: what must now be visible, what changes state, what stays locked, and what kind of generic drift/artifact is forbidden.
8. Tell the user what not to change this round.
   - State the predicted visible evidence for the next attempt and the pass/fail observation to record. A retry is not considered informative unless the changed variable produces the expected evidence or a clearly different failure.
9. If the user asks for a complete prompt, or the next attempt is likely to be copied directly into Jimeng/Seedance, route the patch through `$jimeng-sd2-prompting` and deliver one standalone copyable block with negative constraints inside it. Do not leave the user to merge a patch with an old prompt manually.
10. If a `$creative-production-ledger` exists, create the retry as a child attempt and record the isolated `--change` delta; never overwrite the failed parent attempt.
11. After the user confirms the new result, route reusable evidence to `$creative-casebook`: record the visible result, isolated prompt delta, applicability, side effects, and whether a shared skill should inherit the lesson.
12. If needed, route to specialist skills:
   - `$ai-video-output-review` for timestamped extraction, contact sheets, prompt/reference comparison, and post-generation acceptance review.
   - `$cross-shot-consistency-audit` when an already selected multi-shot sequence needs an anchor-based drift matrix and repair priority before choosing the retry.
   - `$bounded-explore-select` when many viable candidates need scoring, elimination, feedback, and a stopping decision before any retry is justified.
   - `$character-continuity-bible` for identity/prop drift.
   - `$cinematic-audiovisual-language` for weak camera logic, repeated shots, unclear axis/screen direction, staging drift, or incoherent cuts.
   - `$screenwriting-story-craft` for stiff emotional transitions, missing temporal hinge, unclear desire/obstacle, or weak micro-story.
   - `$action-choreography-reference` for weak or unreadable action, weightless weapons, sliding support, missing center-of-mass logic, identical martial styles, impossible braking, or contact without recoil.
   - `$action-rhythm-editing` for pacing and impact.
   - `$visual-style-aesthetic-direction` for cheap/generic/incoherent aesthetic direction or style drift.
   - `$ai-material-realism` for fake texture, weak render language, missing AO/contact shadows/PBR/anisotropic highlights, or plastic CG.
   - `$visual-reference-vocabulary` for missing vocabulary after the shot grammar problem is understood.
   - `$ai-video-prompt-preflight` when the next prompt is long, multi-reference, action-heavy, or likely to fail again.
   - `$jimeng-sd2-prompting` for final prompt formatting.
   - `$creative-casebook` when the user says a result worked, failed in a repeatable way, should be remembered, or should become a template/rule.

Read `references/failure-diagnosis-map.md` for symptom-to-fix mappings.

## Output Shape

```text
诊断：
主要问题：
最可能原因：

下一轮只改：
保留：
不要改：

提示词补丁：
...

负面限制补丁：
...

结果确认后沉淀：
...
```

For Liu camera-group retries, append:

```text
主失败桶：表演/聆听 | 台词/口型 | 景别/切镜 | 动作/物理 | 特效/合成 | 连续性/资产 | 声音协议 | 模型/平台
本轮唯一变量：
预期可见证据：
验收观察：
```

## Guardrails

- Change one main variable per retry unless the result is unusable; write the predicted visible evidence before running.
- Do not promote a universal rule from one random A/B result. Repeat a minimal sample or verify on a new scene before cross-project reuse.
- Preserve successful parts explicitly.
- Distinguish observed failure from inferred cause. Say "most likely" when the execution evidence is incomplete.
- Do not call something a model limitation until prompt overload, reference conflict, unsupported mode, asset weakness, and workflow errors have been checked.
- Do not recommend longer prompts by default. Often the fix is removing conflicting instructions.
- Do not fix weak camera, stiff emotion, or position drift by adding style adjectives. First repair shot function, temporal hinge, blocking, axis, or reference roles.
- Do not fix weightless action by adding more shake, sparks, debris, speed lines, or "powerful" adjectives. First repair actor/load relation, support, mass distribution, contact response, and inertia resolution.
- Do not fix fake-looking ACT/POV fights by adding more camera aggression alone. First repair the underlying action relationship, but do not expose the old five-part "attack intent -> preload -> attack-line proof -> forced response -> new state" formula as a visible prompt template. Use it only as an internal diagnostic check. For SD2/Seedance copyable prompts, translate it into the tested natural cause-effect wording: "when A does X, B is visibly forced into Y; A uses that result to do Z; the spacing/angle/elevation becomes N." The viewer should see contact, receiver response, and changed state, not a tactical essay.
- Do not fix weak aesthetics with name-salad references. First choose medium domain, style family, color ownership, rendering hierarchy, and anti-cheapness constraints.
- Do not fix material/render failures by dumping keywords. Attach AO, PBR, anisotropy, GI, SSS, or volumetrics to visible surfaces and light conditions.
- Do not keep writing full new prompts after the same failure repeats. First inspect the generated output, compare it with at least one suitable reference or known-success case, and define the smallest evidence-backed change.
- If a 10-15 second clip fails, suggest splitting into shorter clips.
- If identity or prop drift is the issue, put locks earlier and reduce camera/action complexity.
