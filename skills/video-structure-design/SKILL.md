---
name: video-structure-design
description: "Design the macro structure of videos before scripting or shot design: hook, first frame, retention curve, beat order, information release, escalation, turning point, payoff, loop, CTA, duration maps, temporal hinges using 刚刚/正在/即将, social short-form structures, ads, trailers, teasers, music videos, character reels, product videos, AI video sequences, and series structures. Use when the user asks for 视频结构, 片子结构, 短视频结构, 开头怎么抓人, 留存, 节奏结构, 段落结构, 起承转合, 时间词, 情绪推进, 预告片结构, 广告片结构, MV结构, 角色出场结构, 15秒视频, 30秒视频, 60秒视频, viral structure, retention structure, hook payoff, or says a video feels flat, scattered, repetitive, too slow, too empty, or only has shots but no structure."
---

# Video Structure Design

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Purpose

Use this skill before writing scripts, storyboards, or AI-video prompts. It decides the video's macro skeleton: what the first second promises, how attention is renewed, where information turns, how the climax lands, and why the viewer stays until the end.

This skill is not the same as screenwriting. Screenwriting handles character, conflict, scene, and dialogue. Video structure handles duration, retention, segment order, information release, beat density, rhythm curve, ending button, loopability, and platform/use-case fit.

Use temporal hinge words when a video needs a natural emotional or behavioral progression. Structure can be driven by "刚刚发生的余温 -> 此刻的行动 -> 即将到来的压力/反转", so the viewer feels time moving instead of watching disconnected cool shots.

## Reference Routing

Read only the reference needed for the task:

- `references/core-structure-principles.md`: use for any video structure task. It defines hook, promise, escalation, turn, payoff, and loop.
- `references/duration-maps.md`: use for 5s, 8s, 15s, 30s, 60s, 90s, trailer, reel, or commercial timing.
- `references/structure-archetypes.md`: use when choosing a structure for character entrance, action traversal, product reveal, transformation, tutorial, mood piece, trailer, MV, or story short.
- `references/retention-information-release.md`: use when the video feels flat, slow, repetitive, confusing, or loses attention.
- `references/commercial-social-structures.md`: use for ads, Douyin/TikTok/Reels/YouTube Shorts, brand, product, creator-style, or CTA-driven videos.
- `references/ai-video-structure-packaging.md`: use when packaging a structure into an AI-video prompt or storyboard handoff.
- `references/source-map.md`: source links and research notes.

## Workflow

1. Identify the video's job:
   - entertain, sell, introduce a character, show a transformation, teach, tease, reveal a world, create a mood, or start a series.
2. Choose the viewer promise:
   - what does the first 1-3 seconds make the viewer expect?
3. Define the temporal hinge when useful:
   - what just happened before frame one, what is happening now, and what is about to interrupt or transform it.
4. Pick a structure archetype:
   - do not start with shots. Start with a beat skeleton.
5. Map duration:
   - assign time to hook, setup, development, turn, climax, payoff, and exit/loop.
   - treat this as an editorial planning map first. Do not automatically convert every structural interval into a hard timestamp in the generation prompt.
   - determine timing confidence from references, prior outputs, animatics, edit maps, content density, and action-phase needs.
   - when confidence is high, pass exact segment ranges to generation; when medium, pass approximate proportions; when low, pass order only.
6. Add retention resets:
   - visual contrast, new information, obstacle, reversal, scale shift, emotional beat, sound beat, or question renewal.
7. Define the ending:
   - payoff, CTA, cliffhanger, circular loop, punchline, transformation proof, final image, or series question.
8. Hand off:
   - send the structure to `screenwriting-story-craft` for drama or `cinematic-audiovisual-language` for shot grammar.

## 15-Second Defaults

When the user asks for a 15-second AI video, design a compact structure before any shot list:

```text
0-1.5s Hook: one striking image or question.
1.5-4s Orientation: who/where/what rule of the world.
4-7s Escalation: action starts or pressure appears.
7-10s Turn: new obstacle, reversal, scale change, or hidden information.
10-13s Peak: the strongest visual/action/emotional beat.
13-15s Payoff: consequence, exit image, cliffhanger, or loop point.
```

For emotional 15-second clips, map the temporal hinge across the duration:

```text
刚刚: the visible residue in the first frame.
正在: the present action that seems normal.
即将: the pressure sign that changes the viewer's expectation.
已经: the irreversible consequence by the final image.
```

If the user wants manga/comic-style cuts, keep this structure but turn each beat into a panel-like shot with a different function. Do not reduce the video to three generic cool shots.

For action or vehicle clips, require visible displacement across beats. The character/vehicle should change position, altitude, route, relationship to obstacles, or power status.

For action-led clips, do not default to "characters stand still, face off, then start fighting." Unless the intended structure is a ritual duel, psychological standoff, or pre-impact suspense, open in motion, pressure, aftermath, or near-contact:

```text
mid-action opening / impact aftermath / near-contact opening / chase-in opening / environmental pressure opening / reaction opening
```

The first second should already promise force, route, danger, or consequence. Static stance, mutual staring, slow posing, and delayed launch waste too much of a 5-15 second action clip.

For one-pass AI generation, prefer exact macro-segment ranges when they are high-confidence, while leaving internal shot durations flexible. If timing is uncertain, use temporal connectors instead of fabricated precision.

## Output Shapes

For a quick structure:

```text
视频任务：
观众承诺：
时间铰链：
结构类型：
时长分配：
开头钩子：
中段推进：
转折/高潮：
结尾按钮：
```

For an internal editorial timing map only:

```text
结构目标：
时间铰链：
0-2s Hook:
2-5s Setup:
5-9s Build:
9-12s Turn:
12-15s Payoff:
循环/CTA/结尾画面：
```

For diagnosis:

```text
结构问题：
- 开头承诺：
- 信息释放：
- 节奏曲线：
- 转折：
- 结尾回报：
重构建议：
```

For AI-video handoff:

```text
视频结构骨架：
每段功能：
可视化动作：
转场逻辑：
交给分镜的要求：
```

## Quality Gate

Before finalizing, check:

- Does the first second show a clear visual or emotional promise?
- If the clip depends on emotion, does the structure use time-state cues rather than isolated emotion labels?
- Is the video built around one dominant viewer question?
- Does every segment add new information, pressure, contrast, proof, or emotion?
- Is there a turn, not just a longer version of the same action?
- Does the ending pay off the promise or open a stronger next question?
- Does the duration fit the idea, or is the idea stretched too long?
- Are duration labels being used as planning estimates rather than unverified hard generation commands?
- If the final generation prompt contains exact segment ranges, what evidence supports them?
- Are macro-segment ranges clearly separated from micro-shot duration?
- Can the structure be handed to shot design without inventing missing logic?

## Avoid

- Do not confuse more shots with better structure.
- Do not write a story outline when the user needs a video retention skeleton.
- Do not let every beat do the same job: "cool action, cool action, cool action."
- Do not delay the premise in short-form video.
- Do not start action clips with default standstill face-off unless the standoff is the hook and has a clear visual pressure.
- Do not make the climax happen before the viewer understands what is at stake.
- Do not add CTA or ending text unless the video type needs it.
