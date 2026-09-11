---
name: seedance-copyright
description: "This skill should be used when a Seedance 2.0 prompt mentions named characters, franchises, celebrities, public figures, brand logos, copyrighted scenes, music titles, streamer originals, or real-person likeness workflows and needs an IP-safe rewrite."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - copyright
  - ip-safety
  - policy
metadata:
  version: "5.1.0"
  updated: "2026-04-27"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: ""
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-copyright

使用本 skill 来改写涉及受保护角色、系列作品、名人、公众人物、品牌标识、受版权保护的场景、音乐曲目名、工作室风格或真人肖像工作流的高风险提示词。

保留创意功能、情绪、题材、镜头行为和故事节拍。移除受保护的身份、确切的外观、商标化的服装、标识、具名角色、名人姓名以及工作室/系列标签——除非用户拥有明确授权的工作流。

改写公式：
- 受保护身份 -> 原创原型
- 品牌/系列/工作室名称 -> 制作类描述词
- 精确场景复刻 -> 具有相似戏剧功能的新场景
- 名人/公众人物肖像 -> 虚构角色或授权肖像工作流

安全示例：
- “an original masked acrobat hero swings through Tokyo” -> “an original masked acrobat hero swings between neon rooftops.”
- “soft hand-painted storybook animation style” -> “soft hand-painted storybook animation with warm natural light.”
- “Studio Trigger action” -> “bold ink outlines, flat color fills, high-contrast cel shading, smear frames.”

返回：风险诊断、被移除的内容、保留的意图、安全改写后的提示词，以及可选的更严格改写版本。

遗留细节已移至 `references/migrated/seedance-copyright-original.md`。
