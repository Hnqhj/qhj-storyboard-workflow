---
name: seedance-antislop
description: "This skill should be used when the user wants to remove AI filler language, hollow superlatives, generic cinematic fluff, vague adjectives, or non-actionable wording from a Seedance 2.0 prompt."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - prompt-quality
  - anti-slop
  - compression
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

# seedance-antislop

使用本 skill 来移除通用的 AI 视频废话填充，并将含糊措辞转化为可执行的拍摄指令。

判定标准：如果摄影师、灯光师、演员或剪辑师无法据某个词采取行动，就替换它。

优先移除：cinematic masterpiece、ultra realistic、breathtaking、stunning、beautiful、epic、professional quality、dramatic atmosphere、magical、dreamy、highly detailed。

替换为：主体名词、动作动词、单一运镜、光源、材质质感、时序、参考角色、物理后果、音效提示。

压缩顺序：参考标签 -> 主体名词 -> 动作动词 -> 运镜 -> 光源 -> 音效提示 -> 风格约束。优先删除通用形容词。

返回：清理后的提示词、被移除的短语，以及一句话解释此次压缩的取舍。

遗留细节已移至 `references/migrated/seedance-antislop-original.md`。
