---
name: performance-scene-director
description: 统一设计影视情绪表演场景，包括怒戏、哭戏、哀戏、喜戏、乐戏、混合情绪，以及 5–15 秒单角色氛围/美型/时尚/古风人物短片。用于 AI 视频/图像提示词、Seedance/即梦/Pika/Runway 情绪片段、表演微动作、身体动作与发丝布料饰品的次级滞后、稳定结尾、参考图角色表演迁移和五类情绪导演 skill 的共享底座。
---

# Performance Scene Director

## 核心定位

这是 Liu 的**统一情绪表演导演底座**。它合并怒戏、哭戏、哀戏、喜戏、乐戏的共同流程：先判断情绪类型和强度，再设计表演弧线、微动作、镜头距离、光色、声音和 AI 视频提示词。

For two-person romance, argument, confession, reconciliation, breakup, farewell, or shot-reverse-shot scenes, use `$relationship-dialogue-direction` after identifying the primary emotion. This Skill still owns the primary emotion arc; the relationship skill maps it into asymmetric performer exchange and coverage.

使用它时，不要把情绪写成抽象标签。把情绪转成可拍、可演、可生成的身体行为：

```text
过去发生了什么 -> 现在角色如何压住/释放/转移情绪 -> 外界压力如何逼近 -> 最后一秒留下什么余韵
```

## 情绪选择

读取 `references/emotion-profiles.md`，选择一个主情绪画像：

- **怒**：愤怒、冷怒、暴怒、对峙、控诉、压到临界点。
- **哭**：眼泪、崩溃、情绪释放、催泪、高浓度爆发。
- **哀**：悲伤、孤独、失去、怀念、空、低浓度长尾。
- **喜**：欢喜、惊喜、欣喜、释怀、眼睛发亮的内在情绪。
- **乐**：玩乐、嬉闹、戏谑、轻喜剧、群体节奏、外在放松。

只选一个主情绪。混合情绪时，另一个只能做副色，例如“含泪之怒”“笑中带泪”“哀里有释然”。不要让两个情绪同时抢主导。

## 输出流程

一次完整使用必须产出：

1. **情绪判断**：主情绪、子类型、强度上限、是否需要哭/笑/吼/沉默。
2. **时间铰链**：刚刚发生、正在发生、即将发生。
3. **表演弧线**：5 层递进或节奏变化，避免一开始就满格。
4. **微动作**：眼神、呼吸、下颌、手、肩、步伐、停顿、触物、回避视线。
5. **镜头策略**：镜头距离跟随情绪浓度；特写只给决定性微动作。
6. **光色声音**：光线、色温、环境声、音乐/静默、呼吸/衣物/物件声音。
7. **可复制提示词**：包含主体、事件、时间线、风格、环境和负向约束。
8. **下一轮观察点**：如果生成后失败，下一版优先看什么。

## 表演强度规则

情绪不是越大越好。默认使用“压住比释放更高级”的原则：

```text
2/10：表面正常，只有微小异常
4/10：刺激出现，呼吸/眼神/手部变化
6/10：主动压制，角色试图不让别人看见
8/10：临界点，身体露馅但还没完全释放
10/10：释放或反向沉默，必须有后果
```

根据情绪调整：

- 怒：最高级常在 7–8 分，声音降低、身体变静，比狂吼更危险。
- 哭：最强常在“忍不住前一秒”，眼泪可以少，呼吸和吞咽更关键。
- 哀：通常不超过 5 分，靠留白、重复动作、空镜和时间感。
- 喜：眼睛先亮，嘴角后到；第一反应常是愣住和确认。
- 乐：靠节奏和群体传染，不靠“大家哈哈大笑”。

## 镜头策略

镜头必须服务表演，不要抢戏：

| 情绪状态 | 镜头建议 |
|---|---|
| 压抑、隐忍 | 中近景或稳定近景，轻微推近，保留呼吸空间 |
| 临界点 | 近景或特写，锁定眼睛、下颌、手指、喉结、肩膀 |
| 爆发 | 中景先给身体，再切近景，不要一上来就极近 |
| 哀与留白 | 远景、背影、空椅子、物件、长停顿 |
| 喜与乐 | 更开放的中景/群像，允许眼神交汇和身体动起来 |

提示词句式：

```text
Camera begins in a still medium close-up, holding enough space for the actor to hide the emotion; as the pressure lands, the camera makes a slow restrained push-in and ends on the tiny change in the eyes, not on a forced dramatic gesture.
```

## 声音策略

声音优先级：

1. 呼吸变化
2. 环境静默或环境声
3. 物件声音：杯子、门、纸、衣料、脚步
4. 音乐只做底层情绪，不要替代表演

强情绪场景可以不用音乐。沉默、吞咽、衣物摩擦、远处噪音常比配乐更高级。

## 参考图/视频规则

如果用户上传角色图：

- 必须保留身份、服装、发型、年龄感、气质。
- 只迁移“表演状态”，不要让情绪改变角色脸型和身份。

如果用户上传表演/影视参考：

- 只提取表演机制：眼神、呼吸、停顿、身体方向、镜头距离、光色。
- 不默认复制演员身份、IP、场景或台词。

当任务是 5–15 秒单角色氛围、人物美型、时尚/古风展示，或结果出现动作循环、重置、身体与发丝布料不同步时，读取 `references/atmospheric-character-short.md`。它是表演底座的短片分支，不是新的情绪 owner。

使用 `@material[...]` 时写清：

```text
@material[character_ref] locks identity and outfit.
@material[performance_ref] transfers only restrained breathing rhythm and eye behavior; do not transfer identity.
```

## 可复制提示词模板

```text
情绪导演判断：
- 主情绪：
- 子类型：
- 强度上限：
- 时间铰链：

表演弧线：
1. ...
2. ...
3. ...
4. ...
5. ...

镜头/光色/声音：
- Camera:
- Lighting:
- Sound:

完整可复制提示词：
"[主体] 刚刚经历 [事件]，正在 [可见动作]，即将 [情绪后果]。表演不是直接展示情绪，而是通过 [微动作] 暴露情绪。Camera ... Lighting ... Sound ... End on ... Negative: no exaggerated acting, no generic crying/laughing/rage pose, no identity drift, no melodramatic overacting."

下一轮观察：
- 看眼神/呼吸是否成立
- 看情绪是否过早满格
- 看镜头是否抢过表演
```

## 负向约束

按场景挑选：

```text
no melodramatic overacting, no instant full-intensity emotion, no forced crying, no fake smile, no generic rage shouting, no random tears without buildup, no exaggerated facial distortion, no identity drift, no camera move that hides the actor's face at the emotional turn, no music overpowering the performance
```

## 与五个旧情绪 skill 的关系

`anger-scene-director`、`crying-scene-director`、`sorrow-scene-director`、`joy-scene-director`、`delight-scene-director` 是轻量触发入口。它们保留各自情绪词和专属画像，但创作流程以本 skill 为共享底座。
