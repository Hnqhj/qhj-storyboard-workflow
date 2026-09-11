---
name: seedance-vocab-ko
description: "This skill should be used when the user asks for Korean Seedance 2.0 prompt wording, Korean cinematic vocabulary, Korean prompt compression, or translation of camera, lighting, action, VFX, audio, or production terms into Korean."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - video-generation
  - vocab
  - ko
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

# seedance-vocab-ko

使用本 skill 来获取韩语 Seedance 2.0 提示词措辞与电影词汇。保持活跃 skill 指引精简；扩展的遗留术语列表已移至 `references/migrated/seedance-vocab-ko-original.md`。

规则：
- 翻译制作意图，而非逐字直译英文废话。
- 完整保留参考标签：`[Image1]`、`[Video1]`、`[Audio1]`。
- 在风格形容词之前，优先保留具体名词、动作动词、运镜、光源和声音提示。
- 除非工作流已获授权，避免使用受保护名称、工作室名、名人姓名和品牌名。

返回：紧凑的韩语提示词、可选的英文回译、关键词汇选择，以及相关时的安全/IP 说明。
