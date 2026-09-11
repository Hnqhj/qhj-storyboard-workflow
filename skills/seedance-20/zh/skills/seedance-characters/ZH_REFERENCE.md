---
name: seedance-characters
description: "This skill should be used when the user asks for character consistency, character tags, identity lock, multi-character blocking, wardrobe continuity, hand safety, expression control, or likeness-sensitive character guidance."
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

# seedance-characters

将此技能用于身份、一致性、多角色调度、服装连续性、手部安全、表情控制和涉及肖像敏感的角色指引。角色提示必须先消除歧义，再添加风格。

当角色身份、服装、道具、视线方向、画面方向或情绪状态必须跨多个镜头保持时，加载 `[ref:shot-list-continuity]`。加载 `[ref:directing-engine]` 来导演表演：给每个角色一个可演的目标，通过言行矛盾来展现潜台词，并保持一种与项目导演嗓音一致的表演语域。

## 意图

用户在这里保护的是某个人——他们创造的一个角色、他们打造的一个产品，或他们所爱的一个人。身份就是信任：当一张脸漂移时，用户感受到的是背叛，而不是渲染瑕疵。把每个反复出现的角色当作一个带记忆和合同的持续在册演员，绝不当作每个片段都重新选角的陌生人。

## 角色合同

给每个角色分配一个稳定的标签：`Character A`、`Character B`、`[Image1] subject`，或用户提供的原创名字。在出现一个以上角色后，不要使用含糊的代词。保持标签、角色、外观、服装、位置、动作和情绪节拍一致。

| 字段 | 提示词用法 |
|---|---|
| 标签 | `Character A` 或 `[Image1] subject` |
| 身份锚点 | 年龄范围、剪影、发型、服装，或经授权的参考角色 |
| 位置 | 前景/背景、左/右、坐/站 |
| 动作 | 一个被分配的动词和端点 |
| 表情 | 可观察的行为，如眨眼、瞥视、微笑、握紧、停顿 |
| 约束 | 什么必须保持不变 |

## 多角色调度

分别分配动作：`Character A lowers the envelope; Character B remains in the doorway`。当模型必须自己决定谁移动时，不要写 `they argue dramatically`。如果发生接触，描述接触点和端点。对于人群场景，确认主角主体并保持背景运动简单。

## 三层动作层级

源自中文制作实践的现场观察；是已知用于多人场景的最强稳定器。给每个可见的人物分配一个恰好来自某一层的动作：

1. **持续微动作**——呼吸、眨眼、轻微的肩部移动、头发飘动、游移的目光。连续、无间隙；这是所有非焦点人物的默认层。
2. **一次聚焦响应**——单个人物得到一个带显式时间窗的小反应：`Character B's lip corner lifts and she holds a half-second glance`。
3. **大动作——默认禁止。** 在多人镜头中，明确排除站立、行走、转身、姿势改变和拿起物体，除非其中之一就是该镜头的那一个节拍。当屏幕上有多人时，人物对道具的物理（举起一只杯子、传递一个物体）很脆弱——保持接触简单或把它移到画外。

## 手部与面部稳定性

手和脸在复杂编排下会退化。让手保持可见但简单，避免快速的手指动作，避免对白期间触碰面部，并为对口型或肖像保留锁定镜头。当面部精度脆弱时，用道具来表现情绪。

## 肖像规则

对于真实人物肖像，不要从一个上传的素材推断同意。把肖像、面部和声音工作流视为依赖授权且平台专属。如果授权不明确，改写为一个原创角色原型，同时保留场景功能。

## 序列状态

当存在序列状态时，继承服装、发型、画面地理、视线、姿势、情绪状态、当前片段范围、连续性锁、精确的参考标签和预留的未来节拍。正典身份参考控制身份；被接受的素材控制瞬态开场状态。不要让一个运动或连续性来源覆盖不可变的角色锁。

## 输出合同

返回：角色卡、标签映射、动作分配、连续性约束，以及任何安全或授权说明。
