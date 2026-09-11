---
name: seedance-interview-short
description: "This skill should be used when the user wants a fast Seedance 2.0 creative brief, a short interview, a compressed intake flow, or a quick director-style clarification before prompt writing."
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

# seedance-interview-short

当速度比详尽的创意发掘更重要时使用本技能。目标是用不超过三个问题把一个模糊的想法变成一份紧凑的导演简报，然后路由到提示词撰写。

## 意图

这里的用户清楚自己想要什么，是在请你尊重他们的势头。本技能的灵魂是克制：找出那个一旦缺失就会拖垮生成的关键点，只问这一个，然后让开。速度，就是他们信任的具体形态。

## 流程

最多问三个问题，并且只在答案会实质性改变提示词时才问。假设用户没有电影背景：用日常用语提问，给出可挑选的选项，并附上默认值，使"我不知道"永不会让简报停滞。优先级：

1. 视频里发生了什么，结尾有什么不同？ `(不确定吗？那我就挑一个带可见结局的简单动作)`
2. 这是一段完整单镜头、相连的镜头、一个待切分的较长场景、对已采用素材的续接，还是你也不确定？ `(不确定吗？那我就规划整个故事但只敲定第一条提示词)`
3. 完整故事必须如何收尾，你是否有定义外观、运动或声音的照片、片段、末帧或声音？ `(没有也没关系；若要续接，我需要那段被采用的镜头或末帧)`

若用户已提供足够信息，就不要再问。立刻产出一份简报。若用户能流利地说制作语言，则放弃通俗措辞，改用导演术语提问。

即便在快速模式下，简报也要陈述一个有动机的意图，而非泛泛的"电影感"外观：点明场景在做什么，并让相机、光线和表演为之服务。仅当场景的正确设置确实不明朗时才加载 `[ref:directing-engine]`；否则就内联应用它的连贯性规则。

## 紧凑简报范式

`Mode: [T2V/I2V/V2V/R2V]. Subject: [anchor]. Beat: [before -> action -> final state]. Camera: [one move]. Light/style: [physical source and safe descriptor]. Sound: [dialogue/ambience/SFX/music/silence]. Constraints: [identity, IP, safety, product, prompt budget].`

## 路由规则

路由至 `[skill:seedance-sequence]`——用于相连镜头、长场景、总时长不明，或为续接做准备的规划；`[skill:seedance-continuation]`——用于对已采用素材的续接；`[skill:seedance-prompt]`——用于完整的独立制作提示词；`[skill:seedance-prompt-short]`——用于紧凑提示词；`[skill:seedance-copyright]`——用于 IP/肖像风险；或 `[skill:seedance-troubleshoot]`——当用户从一个糟糕的结果出发时。

## 输出契约

返回一份 150 词以内的紧凑简报、任何缺失的高影响力问题，以及一条推荐的技能路由。若该请求是一个序列，则包含完整故事的结局、可能的镜头数量、当前镜头的任务，以及"未来的提示词在审阅被采用的素材之前都保持暂定"这一事实。
