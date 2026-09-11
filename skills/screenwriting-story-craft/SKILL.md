---
name: screenwriting-story-craft
description: "Write and refine local or atomic screenplay units: loglines, short-film and AI-video micro-stories, beat sheets, individual scenes, action lines, dialogue, subtext, conflict, stakes, reversals, endings, and temporal hinges such as 刚刚/正在/即将. Use for 一句话故事、短片、小故事、单场戏、分场、对白、潜台词、人物动机、局部改稿、scene purpose, or when an approved project design needs concrete scene writing. For a full screenplay project, full-series spine, multi-episode outline, novel-to-drama adaptation, macro reversal plan, or time/POV continuity system, use develop-screenplay-project first. For diagnosis-only roundtables use script-doctor-roundtable; for retention and hook/payoff timing use video-structure-design."
---

# Screenwriting Story Craft

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Purpose

This skill owns **local writing execution**: one logline, micro-story, beat chain, scene, dialogue pass, or bounded rewrite. It does not own a full film/series project architecture. For 全剧骨架、故事圣经、分集接力、小说改短剧、全剧反转、时间/知识台账 or project-wide restructuring, start with **$develop-screenplay-project** and return here with its scene handoff package.

Use this skill to make visual ideas narratively sharp before writing shots or prompts. A good AI video idea should not only look cool; it should contain a visible desire, obstacle, choice, consequence, and change.

For video prompts, use `video-structure-design` first when the user needs duration, hook, retention, segment order, or platform structure. Then use this skill for character/conflict/drama, and use `cinematic-audiovisual-language` for shot grammar.

When the user asks for 剧本会诊、剧本医生、多评委诊断、投资/观众/编剧多视角评估, route first to `$script-doctor-roundtable`. After the user chooses a diagnosis direction, return here for concrete rewriting.

## Temporal Hinge Principle

Use time words to make emotion and behavior evolve naturally instead of commanding a static feeling. Build the character state with a three-part hinge:

```text
刚刚发生了什么 -> 此刻正在做什么 -> 即将发生什么
```

Good temporal hinges create emotional pressure:

- **刚刚 / 刚从 / 才经历**: leaves a visible residue such as joy, exhaustion, guilt, relief, makeup, dust, wet hair, a half-finished smile, or a relaxed body.
- **正在 / 此刻 / 一边...一边...**: gives the actor a playable present action.
- **即将 / 下一秒 / 还不知道 / 马上会**: creates anticipation, dread, irony, or a coming reversal.

Example: "他刚刚结束一个美好的假期，正拖着行李笑着回家，还不知道手机里即将弹出一条会让他崩溃的消息." This is stronger than "他从开心变崩溃" because it gives the performance a cause, a present action, and future pressure.

## Reference Routing

Read only the files needed for the task:

- `references/story-engine.md`: use for loglines, premise, theme, central dramatic question, structure, and story diagnosis.
- `references/character-conflict-stakes.md`: use for character design, motive, want/need, flaw, antagonist force, stakes, and emotional arc.
- `references/scene-beat-dialogue.md`: use for scene writing, beat structure, action lines, dialogue, subtext, and scene compression.
- `references/short-form-video-story.md`: use for 5s, 8s, 15s, 30s, trailer, teaser, TikTok/Reels/Douyin, AI video, or micro-short scripts.
- `references/script-format-output.md`: use when the user wants script pages, scene headings, treatment, outline, beat sheet, or prompt-ready story blocks.
- `references/source-map.md`: source links and research notes.

If the request is primarily about 视频结构, 留存, hook/payoff, 起承转合, 预告片结构, 广告片结构, MV结构, or platform timing, route to `video-structure-design` instead of using this skill alone.

## Workflow

1. For substantial, unfamiliar, historical, professional, cultural, scientific, or current-world premises, use `$creative-research-first` before plotting so the conflict and visible behavior are grounded.
2. Extract the story seed:
   - protagonist, world, problem, desire, obstacle, stakes, tone, and ending impression.
3. Define the temporal hinge when emotion or behavior needs to change:
   - what just happened, what is happening now, and what is about to happen.
4. Write the dramatic engine:
   - `Someone wants X, but Y blocks them, so they do Z, which costs/reveals W.`
5. Define the change:
   - What is different at the end: information, status, relationship, identity, danger, emotion, or world state?
6. Build beats:
   - setup, trigger, pursuit, complication, choice, consequence, image/end button.
7. Test every scene or beat:
   - does it reveal character, create conflict, move the plot, raise stakes, or change emotional temperature?
8. Compress for screen:
   - replace explanation with visible action, object behavior, spatial choice, reaction, or silence.
9. Hand off to shot design:
   - convert story beats into audiovisual functions before writing camera language.

## Micro-Story Rule

For 5-15 second AI videos, do not write lore. Design one visible irreversible change:

```text
start state -> pressure/obstacle -> character choice -> cost/reveal -> ending image
```

The choice must be visible as an action: crossing a line, using a forbidden object, refusing a command, breaking formation, hiding evidence, saving someone, stealing power, revealing identity, or abandoning safety.

When the clip needs an emotional turn, encode it as a temporal hinge: past residue -> present action -> incoming pressure. Avoid abstract labels like "sad", "angry", or "broken" unless they are supported by a visible before/after cause.

If a clip is only a mood/action showcase, still add one micro-story function: enter, test, fail, adapt, win, escape, reveal, or be marked.

## Output Shapes

For a quick story:

```text
一句话故事：
时间铰链：
人物：
冲突：
转折：
结尾画面：
```

For a 15-second AI video:

```text
故事核：
时间铰链：
角色欲望：
阻力：
15秒节拍：
0-3s ...
3-6s ...
6-9s ...
9-12s ...
12-15s ...
可转分镜的动作：
```

For scene/script work:

```text
场景目标：
场景冲突：
人物策略：
反转点：
场景结果：
剧本草稿：
```

For diagnosis:

```text
问题诊断：
- 主角欲望是否清楚：
- 阻力是否具体：
- 代价是否可见：
- 变化是否发生：
- 可删/可强化的段落：
```

## Quality Gate

Before finalizing, check:

- Can the story be expressed in one sentence without explaining lore?
- Does the protagonist actively want something?
- If emotion changes, is there a temporal hinge rather than a naked emotion label?
- Is the obstacle visible, specific, and stronger than convenience?
- Does the protagonist make a choice, not just experience cool visuals?
- Does the ending change the beginning?
- Can each beat be shown as action, image, object, reaction, or sound?
- Is the emotional hook clear before style and camera language are added?

## Avoid

- Do not write lore instead of drama.
- Do not make the protagonist passive unless passivity is the point and has consequences.
- Do not rely on vague stakes like "the fate of the world" unless the viewer can feel a specific personal cost.
- Do not add twists that only explain information but do not change character behavior.
- Do not make dialogue say exactly what the image already shows.
- Do not write unfilmable internal states without external behavior.
