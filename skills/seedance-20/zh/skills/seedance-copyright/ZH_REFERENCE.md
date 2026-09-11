---
name: seedance-copyright
description: "This skill should be used when a Seedance 2.0 prompt mentions named characters, franchises, studios, celebrities, public figures, private people, brand logos, copyrighted scenes, songs, voices, or real-person likeness workflows and needs an IP-safe rewrite."
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

# seedance-copyright

在最终确定涉及受保护 IP、具名品牌、公众人物、私人、声音、logo、歌曲、工作室、确切场景或相似角色请求的提示词之前使用此技能。目标不是稀释创意；目标是用原创、经授权且更安全的制作语言保留创意功能。

## 意图

用户指向受保护作品并不是想偷——他们是在向你展示现存的、关于他们所爱之物最清晰的范例。任务是找出这份爱由什么构成，并把它作为安全地属于他们的东西还给他们。在同一个动作中保护权利持有人和用户的心。

## 改写原则

保留场景功能、类型、情绪、镜头逻辑、情绪节拍和制作意图。用原创原型、原创服装逻辑、原创世界细节和描述性风格层替换受保护的身份。

| 风险 | 替换为 |
|---|---|
| 具名角色或系列 | 原创原型、类型功能和非雷同的服装语言 |
| 工作室或在世创作者风格 | 媒介、材质、调色板、构图、线条质感和运动节奏 |
| 名人或私人 | 原创表演者描述或经授权的参考工作流 |
| 品牌 logo | 通用产品标记、空白标签，或在明确授权时使用用户自有品牌 |
| 歌曲、声音或表演 | 节拍、能量、配器、情绪，或新创作的声音指令 |
| 确切场景重现 | 一个具有相似叙事功能但不同设定/调度的原创场景 |

## 授权关卡

如果用户明确拥有品牌、素材或肖像权，保留经授权的元素，但仍以显式约束保护它们。如果授权不明确，提一个简短的确认，或提供一个安全的原创改写。不要从一张上传的图像、歌曲或视频推断权利。

对于真实人脸、肖像或声音，分开三个问题：有效平台是否支持该输入、用户是否拥有授权，以及提示词是否避免了在未经同意的情况下模仿一个公众人物或私人。一些平台使用经验证的虚拟肖像素材或授权流程；不要把那些塌缩成一条普适的允许或拒绝规则。

## 安全替换示例

不要写一个具名超级英雄在一个可识别的系列城市中飞荡，而要写：`original masked rooftop courier in a red weatherproof jacket leaps between rain-slick buildings, low handheld tracking camera, blue police lights far below, no logos or franchise symbols`。

## 输出合同

返回：风险类别、改了什么、安全替换提示词、授权要求，以及任何残余约束。
