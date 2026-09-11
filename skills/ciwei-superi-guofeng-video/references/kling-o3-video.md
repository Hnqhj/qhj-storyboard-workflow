# Kling O3 Video Workflow

Use this reference when the user uploads a generated historical character image, wants image-to-video, asks for a different action from the same image, describes a failed Kling O3 result, or asks for a 3-shot mini story.

## Image Reading Checklist

Before writing, infer internally:

- identity: noblewoman, maid, scholar, emperor, official, villager, artisan, swordswoman, etc.
- emotion: restraint, hesitation, alertness, sorrow, shame, anger, resolve, hidden tenderness
- gaze: direct, side glance, lowered eyes, looking back, avoiding someone, watching someone
- hands: sleeve, fan, hairpin, cup, scroll, sword, table, collar, hanging naturally
- scene: palace, inner room, study, window, corridor, courtyard, street, inn, boat, tea house
- natural action: turn eyes, lower gaze, tighten fingers, lift sleeve, pause, step back, breathe in, turn slightly, hold prop tighter

Do not reveal this checklist unless the user asks.

## Core Kling O3 Prompt Template

```text
【可灵 O3 图生视频提示词】
请基于这张原图生成一段 5 秒古装剧电影感视频，不要重新生图，不要改变原图人物脸型、五官、服装、发型、妆容、头饰、背景、构图和整体风格。人物此刻像是[根据图片自动判断的剧情动机]。

视频开始时，人物保持原图姿态，眼神先[微表情起点]，随后[微表情变化]，像是情绪刚刚露出一点又被压回去。接着人物顺着原图的姿势自然完成一个小动作：[一个主要动作]。动作幅度中等偏小，但要肉眼可见，不突兀，不像表演。

动作结束后，人物情绪沉下来，呈现出[情绪落点]，眼神像有一句话没有说出口。环境只做克制的微动：[环境微动]。镜头为 5 秒古装剧电影感，缓慢推进或轻微侧移，浅景深，重点捕捉人物眼神、微表情和这个小剧情动作。整体画面像古装剧剧情中的一秒，不是古装写真，不是角色展示，不是 AI 待机人物。

【负面提示词】
不要重新生成新人物，不要改变脸型，不要改变五官，不要改变发型，不要改变服装，不要改变妆容，不要改变头饰，不要改变背景，不要改变构图，不要换场景，不要换镜头角度，不要变成写真摆拍，不要角色展示，不要静态待机，不要只眨眼呼吸，不要大幅度动作，不要跳舞，不要转圈，不要夸张表演，不要脸部变形，不要油腻皮肤，不要塑料脸，不要磨皮过度，不要眼神空洞，不要手指畸形，不要多手指，不要头饰乱飞，不要服装融化，不要背景融化，不要画面闪烁，不要人物漂移，不要突然拉远，不要快速运镜，不要字幕，不要文字，不要水印。
```

## Action Design Rules

Use one main action only.

Good actions:

- fingers slowly tighten around sleeve, fan, cup, sword, scroll, or collar
- gaze shifts away then returns
- chin tightens slightly while body remains almost still
- hand lowers from a paused gesture
- sleeve is pulled back a little
- character takes a very small half-step back
- character turns slightly toward/away from someone
- prop is held tighter as emotion settles

Bad actions:

- dance, spin, run, fight, big turn, sudden walk-away
- only breathing/blinking
- multiple unrelated actions in one 5-second prompt
- dramatic performance gesture that was not implied by the source image

## Environment Micro-Motion

Use 1-3 subtle details:

- candle flame flickers
- lantern light trembles
- veil or bead curtain moves lightly
- hair tassel or sleeve edge moves slightly
- dust floats in warm light
- rain/mist/snow moves outside window
- steam rises from tea
- water reflection trembles

Environment must support the character; it cannot become the main subject.

## Next Menu After Video Prompt

```text
下一步你想做什么？

A. 我去可灵 O3 生成视频，生成好后回来让你帮我优化
B. 用同一张图再生成一个不同剧情动作版本
C. 把这条视频提示词改得更克制一点
D. 把这条视频提示词改得更有情绪张力一点
E. 继续生成下一张同风格图片
F. 做成连续 3 个镜头的小剧情
G. 重新开始一个新人物

你直接回复选项字母即可。
```

## Single Image, Multiple Actions

When the user asks for "单图多动作" or chooses B repeatedly, generate 3 alternatives. Keep the same image, identity, costume, and scene. Change only the story action/emotional beat.

```text
【同一张图的 3 个不同剧情动作版本】

版本 1：更克制
[5 秒提示词]

版本 2：更有张力
[5 秒提示词]

版本 3：更适合封面/爆点
[5 秒提示词]

【统一负面提示词】
[negative prompt]
```

## Failed Video Optimization

When the user uploads/describes a failed result, diagnose first.

```text
我先帮你判断这个视频的问题：

1. 主要问题：[问题总结]
2. 可能原因：[为什么提示词导致这个问题]
3. 修正方向：[应该增强/削弱什么]

【修正版可灵 O3 提示词】
[修正版]

【修正版负面提示词】
[负面提示词]

下一步你想做什么？
A. 用这个修正版再跑一次
B. 再保守一点，减少动作幅度
C. 再明显一点，增强动作幅度
D. 换一个剧情动作
E. 继续下一张图
F. 重新开始
```

Common fixes:

- Face changed: strengthen preserve identity, reduce action, avoid camera angle change.
- Too static: add one visible hand/gaze action, keep environment subtle.
- Too much motion: reduce to one hand/finger/gaze action, remove body movement.
- Camera shakes: specify locked camera with slow push-in only.
- Hands break: avoid complex finger movement; use sleeve/prop grip instead.
- Costume melts: reduce body turn and fabric motion; preserve silhouette.
- Background drifts: keep original background, fixed composition, shallow movement only.

## Three-Shot Story Mode

When the user asks for a continuous 3-shot story, output three independent Kling O3 prompts. Each is still 5 seconds and copy-ready.

Emotion structure:

- Shot 1: emotion is triggered
- Shot 2: emotion is suppressed
- Shot 3: emotion lands or reverses

```text
【连续剧情模式：3 个 5 秒镜头】

镜头 1：情绪被触发
[可灵 O3 提示词 1]

镜头 2：情绪被压住
[可灵 O3 提示词 2]

镜头 3：情绪落点
[可灵 O3 提示词 3]

【统一负面提示词】
[负面提示词]

下一步你想做什么？
A. 继续做第 4 个镜头
B. 修改其中一个镜头
C. 重新设计 3 镜头剧情
D. 回到单镜头模式
E. 重新开始新人物
```

