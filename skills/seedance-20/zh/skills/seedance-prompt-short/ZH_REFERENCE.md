---
name: seedance-prompt-short
description: "This skill should be used when the user asks for a compact Seedance 2.0 prompt, short Chinese prompt, prompt compression, 30-100 word output, or removal of unnecessary prompt language."
license: MIT
metadata:
  version: "6.1.0"
  updated: "2026-06-22"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-prompt-short

在不丢失生产信号的前提下压缩 Seedance 提示词。一条短提示词仍然需要模式、主体、动作、相机、光线，在有用时还需声音，以及约束。在移除物理细节之前先移除填充词。

当存在序列状态时，压缩必须保留连续性锁定项、精确的引用标签、实际的开场状态、当前镜头动作、终点、已完成节拍的排除项，以及预留的未来节拍。不要把那些防止续接重演已完成动作或泄露未来动作的词压缩掉。

## 意图

压缩是一种关于用户最珍视什么的判断行为。在删减中幸存下来的，是他们镜头的灵魂；其余的一切先走。若用户会为某个被删的词而惋惜，那它从来就不是填充词。

## 压缩优先级

按此顺序保留：

1. 引用标签及其角色。
2. 主体或产品身份。
3. 动作动词与可见终点。
4. 一个相机运动。
5. 物理光源或氛围。
6. 音频提示或静默指令。
7. 安全、IP 或连续性约束。
8. 序列状态从句：实际开场状态、连续性锁定项、已完成节拍，以及预留节拍。

在删除保留约束之前，先删除泛泛的形容词、重复的风格标签、明显的背景细节、次要相机运动和次要动作。

对于双语或混合语言压缩，加载 `[ref:multilingual-community-examples]`。只保留能厘清参考角色、对白、相机术语或安全制作约束的语言混用。

## 紧凑模板

| 需求 | 模板 |
|---|---|
| T2V | `[Subject] [action and endpoint] in [scene]. Camera: [one move]. Light/style: [physical source]. Sound: [cue]. Constraint: [risk/continuity].` |
| I2V | `[Image1] preserved; only [motion/light/camera] changes. Camera: [one move]. Sound: [cue]. Constraint: [what must not change].` |
| V2V | `[Video1] controls [motion/camera/timing] only; new subject [anchor]. [Action]. Do not transfer [identity/scene/logo].` |
| 中文 | `[Image1]为参考，严格保持[主体]不变；仅加入[动作/光线/镜头]。声音：[提示]。` |

## 输出契约

返回一条紧凑提示词，理想情况下为 30-100 个英文词，或在用户要求中文或最大压缩时返回等效的中文提示词。仅当移除了某些重要内容时，才包含一行说明。
