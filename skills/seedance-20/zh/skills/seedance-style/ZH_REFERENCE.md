---
name: seedance-style
description: "This skill should be used when the user asks for visual style, art direction, render feel, period aesthetic, texture, animation style, realism level, or style-safe alternatives to studio or franchise references."
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

# seedance-style

把风格请求翻译成制作描述词。风格应描述媒介、质感、调色板、镜头或渲染行为、年代线索，以及构图。当一个更安全的描述性风格能保留用户意图时，不要依赖工作室、系列、艺术家或在世创作者的名字。

## 意图

用户指着他们所爱的艺术作品，请求站在它旁边。本技能的灵魂，是在尊重那份热爱的同时拒绝盗用：找出那份热爱由什么构成——光线、质感、节奏、年代——并把它重建成用户拥有的东西。他们应当感到自己的品味被理解了，而非被纠正了。

## 风格安全规则

不要把工作室、系列、艺术家或在世创作者的名字用作风格锚点，除非用户拥有明确授权的工作流。通过描述媒介、质感、调色板、光线、构图、年代、线条质量和运动节奏来保留预期的视觉功能。

| 用户意图 | 安全的制作描述词 |
|---|---|
| 温馨手绘奇幻 | `hand-painted 2D animation, soft watercolor backgrounds, rounded character silhouettes, warm pastel palette, gentle parallax` |
| 锐利赛博朋克动作 | `neon noir city, wet pavement reflections, high-contrast magenta and cyan light, fast lateral tracking, angular silhouettes` |
| 高端产品真实感 | `clean commercial realism, controlled reflections, shallow depth of field, neutral background, polished material detail` |
| 复古纪录片 | `1970s documentary texture, muted film grain, practical daylight, handheld observational framing` |
| 儿童动画 | `soft clay-like characters, simple expressive faces, bright primary palette, bouncy squash-and-stretch motion` |

## 分层风格法

把风格分成层，而非一个宽泛的标签：**媒介**（实拍、定格、2D、3D、微缩模型）、**表面**（纸纹、黏土、拉丝金属、玻璃、织物）、**调色板**（柔彩、单色、钠灯橙）、**相机/渲染**（微距、浅景深、正交、手持）和**运动节奏**（轻柔、断奏、弹性、真实的重量感）。

## 混合风格规则

若用户要求混合，把每种风格分配到一个层：`live-action product photography with illustrated UI overlays` 比混杂许多具名影响更清晰。让角色设计、环境、光线和视效保持在兼容的语域内。

当风格为 2D、动漫或赛璐珞时加载 `[ref:2d-anime-grammar]`——它涵盖图层语法、爆发式与保持式运动、冲击帧、拖影、台车摄影语言，以及风格化作品的"无镜头"规则。

## 来源风格锁定

来自中国实践的现场观察：当提示词点明拍摄来源并拥抱其瑕疵而非对抗它们时，真实感风格会稳定下来。对预期外观进行分类，然后刻意锁定它的标志性瑕疵：

| 来源外观 | 锁定它的瑕疵 |
|---|---|
| 手机拍摄的日常 / UGC | `vertical handheld phone footage, slight grip sway, auto-exposure shifts, ambient room sound` |
| 直播 | `fixed webcam framing, flat ring light, mild compression, real-time caption pacing` |
| 安防 / 行车记录仪 | `locked high-angle camera, timestamp burn-in feel, low-light noise, no camera response to events` |
| 老电影 | `grainy film texture, gate weave, halation around highlights, era-correct contrast` |
| 演播室商业广告 | `controlled reflections, clean background, polished material detail, zero handheld motion` |

瑕疵词汇即风格：看起来太干净的仿 UGC 会显得加倍虚假。

## 序列状态

当存在序列状态时，继承媒介语法、当前镜头范围、连续性锁定项、精确的引用标签、正典设计、被采用的瞬时状态，以及预留的未来节拍。风格可以为镜头着色，但它不能改变身份、服装、产品设计、界面配置，或预留给后续的事件。

## 输出契约

返回一个安全的风格描述词、任何受保护名称的改写，以及一句整合后的提示词。
