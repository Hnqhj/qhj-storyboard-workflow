---
name: seedance-filter
description: "This skill should be used when a Seedance 2.0 prompt is blocked, rejected, silently degraded, or likely to trigger a content filter; or when the user asks for a safer rewrite without losing the creative intent."
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

# seedance-filter

## 意图

一条被错误拦截的提示词会让用户感觉被一台没有上诉法庭的机器指控。这个技能就是辩护人：通过平白地陈述无辜者的诚实意图来为其洗清，而绝不去指导有罪者。在同一个姿态中，既保护了用户的尊严，也保护了平台的边界。

## 边界——在做任何事之前先读

这个技能**只修复误判（false positives）**：被过宽过滤拦截或降级的良性制作内容（医疗、历史、运动、虚构原创的上下文）。它通过**用平白的语言澄清正当上下文**来工作——绝不通过伪装意图。它不改写真正被禁止的内容：任何涉及未成年人、未经授权的真实人物肖像、性或血腥或非法材料的风险内容。如果底层请求是被禁止的，平白地拒绝，并仅在存在正当替代方案时提供它。

当一条提示词被拦截、降级、可能触发审核，或需要在不丢失创意意图的前提下做更安全的改写时使用此技能。这个技能不帮助规避安全系统。它把有风险的表层用词改写为专业、非血腥的制作语言，并保留安全的创意内核。

## 修复方法

1. 识别创意意图：动作、情绪、镜头、主体和最终节拍。
2. 识别有风险的表层用词：血腥伤害、受保护身份、性化构图、真实人物肖像、武器、自残、仇恨、规避语言，或确切的 IP 复制。
3. 用专业、非血腥的制作上下文语言替换有风险的术语。
4. 保留构图、动作、情绪、镜头逻辑和经授权的参考。
5. 对于可能的误判，澄清良性制作上下文、所有权和非血腥意图。不要帮助绕过安全系统或提供规避手法。

## 更安全的改写模式

| 意图 | 更安全的指令 |
|---|---|
| 冲突 | `staged confrontation, choreographed action beat, no graphic injury` |
| 后果 | `non-graphic distress, torn fabric, scattered props, dramatic silence` |
| 悬念 | `threat implied by shadow, locked door, heavy breathing, low light` |
| 类武器道具 | `prop object handled safely within a staged action scene` |
| 恐怖情绪 | `eerie atmosphere, flickering practical light, off-screen sound cue` |
| 受保护身份 | `original character with broad genre archetype traits` |

## 边界规则

如果用户的请求不安全，拒绝或重定向到一个安全替代方案。如果它安全但措辞糟糕，修复措辞。当不确定时，陈述风险类别，并提供一条保留无害场景功能的保守提示词。

不要提供过滤绕过、规避或藏词手法。安全的路径是澄清制作意图、移除不安全的身份或伤害元素，并改写为一个原创的经授权场景。

人脸限制或肖像验证的变通方案不是安全的提示词技巧。如果一个平台提供经许可的虚拟肖像、可信的模型输出或授权素材流程，把用户引导到那些当前的官方路径，而不是规避语言。

加载 `[ref:filter-vocab]` 以获取更安全的替换。仅当安全修复需要中文/俄文/日文/韩文/西文或混合语言用词以求清晰时，才加载 `[ref:multilingual-community-examples]`。

## 输出合同

返回：可能的触发类别、更安全的用词、最终提示词、改了什么，以及任何仍然适用的内容边界。
