---
name: seedance-filter
description: "This skill should be used when a Seedance 2.0 prompt is blocked, rejected, silently degraded, or likely to trigger a content filter; or when the user asks for a safer rewrite without losing the creative intent."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - content-filter
  - safety
  - rewrites
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

# seedance-filter

当提示词被拦截、被降级处理或可能触发内容过滤器时，使用本 skill。其职责不是绕过安全系统，而是用更安全的表层措辞保留正当的创意意图。

诊断问题：
1. 风险是否基于身份：名人、公众人物、具名角色、品牌、标识、嗓音或面孔？
2. 风险是否涉及暴力、色情、未成年人、自残或武器措辞？
3. 风险是否涉及版权或平台政策？
4. 风险是否为可用中性制作语言替换的误报措辞？

改写规则：
- 将受保护身份替换为原创原型。
- 将露骨伤害替换为非露骨的动作后果。
- 将武器强调替换为编排、走位或道具中性的动作。
- 仅当参考为拥有/已授权时，才将 clone/copy/replicate 替换为参考导向的节奏。

返回：可能的触发类别、安全改写、保留的意图、被移除的词项，以及一个重试变体。

遗留细节已移至 `references/migrated/seedance-filter-original.md`。
