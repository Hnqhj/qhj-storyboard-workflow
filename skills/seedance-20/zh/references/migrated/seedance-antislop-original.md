# `seedance-antislop` 的遗留正文

迁移于 2026-04-27 的 v5.1.0 期间。除非在 `references/api-status.md` 或 `references/source-registry.md` 中得到确认，否则将此处的平台、政策、API 与安全声明视为遗留内容。

---

# seedance-antislop

消灭空洞语言。每个词都必须配得上它的位置。

---

## 什么是 AI Slop（废话）？

**AI Slop（废话）** 是*感觉上*具有描述性、但包含零可测量指令的语言。
它是训练数据平均化的残渣——那些在文本语料库中出现在"好视频"附近、却没有告诉模型任何它无法自行假定的内容的词。

**AI Hum（自夸）** 是 AI 系统默认添加的自我吹捧旁白层：
*"Certainly! Here is a stunning, cinematic, breathtaking, high-quality prompt that masterfully captures..."*

两者都会降低输出质量。废话浪费 token 预算。自夸触发通用模式。

**Platform Slop（平台废话）** 是第三种类型：AI 为避免拒绝而插入的通用、面向全年龄的样板。当作者想要某种由故事驱动的内容时，它会产生一个"猫在凌晨 3 点弹钢琴"的片段。这是 2026 年 2 月内容过滤收紧后创意用户的主要失败模式。

---

## 唯一的测试

> **"相机、测光表或秒表能测量这个吗？"**

如果能 → 保留它。
如果不能 → 删除它或用可测量的东西替换。

| 词 | 可测量？ | 裁决 |
|---|---|---|
| `cinematic` | 否 | ❌ 删除或替换 |
| `45° key light camera-left` | 是 | ✅ 保留 |
| `stunning` | 否 | ❌ 删除 |
| `slow push-in over 6 s` | 是 | ✅ 保留 |
| `epic` | 否 | ❌ 删除或分解 |
| `18mm wide, dolly back 3 m` | 是 | ✅ 保留 |
| `8K ultra-real` | 否 | ❌ 删除 |
| `stable exposure, clean edges` | 是 | ✅ 保留 |

---

## 废话主黑名单

一看到这些词就删除。它们是触发通用输出的**不可测量填充物**。

### 最高级助推词
`stunning` · `breathtaking` · `incredible` · `amazing` · `beautiful` · `gorgeous` · `magnificent` · `spectacular` · `extraordinary` · `phenomenal` · `jaw-dropping` · `mind-blowing`

### 质量断言
`masterpiece` · `award-winning` · `professional` · `ultra-high-quality` · `top-quality` · `world-class` · `best-in-class` · `premium quality`

### 分辨率表演
`8K` · `4K ultra HD` · `super resolution` · `hyper-detailed` · `insanely detailed` · `extreme detail` · `photorealistic`（当用作助推词、而非具体风格目标时）

### 模糊的美学声明
`cinematic` · `epic` · `dramatic` · `artistic` · `creative` · `unique` · `immersive` · `captivating` · `engaging` · `compelling`

### AI 自我吹捧（Hum 层——完全移除）
`certainly` · `of course` · `here is` · `I will now create` · `masterfully` · `expertly crafted` · `carefully designed` · `thoughtfully composed` · `beautifully rendered`

### 空洞的氛围词
`magical` · `ethereal` · `transcendent` · `otherworldly` · `surreal`（除非超现实主义是刻意的风格）· `mystical` · `enchanting` · `whimsical`（除非童话是目标）

### 冗余强调
`very` · `really` · `truly` · `so` · `extremely` · `super` · `highly`，当它们置于任何描述词之前时

### 平台安全废话（新增——2026 年 2 月）
这些由过度谨慎的过滤规避模式添加。它们使内容平淡且通用：
`family-friendly` · `safe for all ages` · `fun and lighthearted` · `wholesome` · `uplifting` · `positive` · `heartwarming` —— **除非这些确实是你的创意意图。**

---

## 分解模式

当移除一个废话词时，用可观察的组件替换它。

### `cinematic` → 分解为：

```
❌  cinematic lighting
✅  single hard key 45° camera-left, amber gel, deep shadow camera-right, no fill
```

```
❌  cinematic shot
✅  slow dolly push-in from MS to CU over 8 s, anamorphic 2.39:1, shallow DOF
```

```
❌  cinematic color
✅  teal shadows, orange-amber midtones, desaturated highlights, slight crush in blacks
```

### `epic` → 分解为：

```
❌  epic battle scene
✅  wide establishing shot, 200 soldiers clashing on a muddy plain,
    handheld low-angle, dramatic brass swell, slow-motion at impact 0.3×
```

```
❌  epic landscape
✅  extreme wide shot, mountain range at dusk, god rays through cloud break,
    drone descending from 800 m to 50 m over 12 s
```

### `stunning` → 删除，然后强化名词：

```
❌  stunning sunset
✅  sunset, golden-red horizon, 5 min after sun has dipped, long shadows,
    warm backlight 3200K, silhouette of tree line
```

### `beautiful` → 指明哪个属性具有吸引力：

```
❌  beautiful woman
✅  woman, sharp cheekbones, calm expression, direct eye contact — [then add lighting that serves her]
```

### `8K ultra-real` → 用输出合同替换：

```
❌  8K ultra-real photorealistic
✅  stable exposure, no flicker, clean edge definition, no hallucinated geometry
```

### `masterpiece` → 完全移除：

```
❌  create a masterpiece video of a flower blooming
✅  flower blooming timelapse. Macro push-in. Soft diffused daylight. No camera movement.
```

### `ethereal` → 指明光学成因：

```
❌  ethereal forest scene
✅  forest, heavy morning fog, shafts of diffused light through canopy,
    floating dust motes, cool teal cast, static wide shot
```

### `magical` → 指明效果：

```
❌  magical atmosphere
✅  floating glowing particles, slow upward drift, warm amber light source below frame,
    gentle lens flare at 3 s
```

### `dramatic` → 分解为张力触发器：

```
❌  dramatic lighting
✅  hard single key from 60° above camera-left, deep shadow fill ratio 1:8, no bounce

❌  dramatic scene
✅  two figures, 1.5 m apart, both still. Static camera. Wind lifts coat at 3 s.
    No dialogue. Low-frequency drone audio.
```

---

## 前/后对比：完整提示词修复

### 示例 1 —— 产品广告

```
❌  Create a stunning, cinematic, ultra-high-quality advertisement for our amazing
    perfume bottle. Make it look incredibly beautiful and photorealistic. 8K quality.
    Breathtaking lighting. Masterpiece level.

✅  Glass perfume bottle on white marble. Camera slow orbit 90° over 8 s.
    Soft studio key top-left, rim light rear-right. Macro DOF on label.
    No text. No people.
```

*移除：* 14 个废话 token。*获得：* 3 条可测量的灯光指令、1 条运镜路径、2 条约束。

---

### 示例 2 —— 动作场景

```
❌  An epic, breathtaking, jaw-dropping fight scene between two amazing warriors
    in a stunning mystical forest. Ultra-cinematic. World-class choreography.
    Make it feel truly extraordinary and immersive. 4K masterpiece.

✅  @Image1 warrior A (dark armour). @Image2 warrior B (white cloth).
    A charges → B sidesteps → B counter-kick to A's chest → A stumbles into tree.
    Ancient forest, fog, shafts of light. Handheld low-angle, whip-pan at impact 4 s.
    0–4 s real-time; 4–6 s 0.3× slow-motion; 6–10 s real-time.
    Impact sfx at 4 s, ambient forest wind throughout.
```

*移除：* 16 个废话 token。*获得：* 完整的编排、时序、运镜、音频提示。

---

### 示例 3 —— 情绪片段

```
❌  A truly magical, ethereal, incredibly beautiful scene of a woman walking
    through an enchanting, mystical forest at night. Stunning visuals. Cinematic masterpiece.

✅  Woman in white dress walks slowly through night forest.
    Bioluminescent ground plants, cool blue ambient light, breath visible.
    Steadicam follow from behind, medium shot, slow pace.
    Quiet footstep sfx, distant owl, no music.
```

*移除：* 12 个废话 token。*获得：* 具体光源、可见呼吸、摄影机机架、音频设计。

---

### 示例 4 —— 建筑

```
❌  Showcase our amazing, breathtaking, world-class skyscraper in a stunning
    cinematic drone shot. Ultra-high quality. Make it look absolutely incredible
    and awe-inspiring.

✅  Glass tower, 60 floors. Drone approach from south-east, altitude 300 m,
    slow descent to 80 m over 12 s. Golden hour, warm side light.
    Lens flare at apex. No people. No text.
```

---

### 示例 5 —— 中文提示词修复

```
❌  美丽的、震撼的、史诗级的、超高质量的、电影感十足的、令人叹为观止的视频

✅  女性独自走在雨夜街道。霓虹反光，湿地面。
    缓慢跟拍，中景，肩后视角。
    雨声环境音，远处钢琴。低饱和蓝绿色调。
```

---

### 示例 6 —— 音频被忽略的失败（来自 10,000 次生成研究的现场数据）

来自从业者研究的最主要失败模式之一：零音频规格的提示词无论视觉质量如何，都会产生平淡、缺乏生气的结果。

```
❌  Person walking through forest
    [no audio spec → model fills with generic ambient wash]

✅  Person walking through forest.
    Audio: leaves crunching underfoot, distant bird calls, gentle wind through branches.
    No music. Natural ambience only.
```

音频语境让 AI 视频感觉真实，即使在视觉上显然是 AI 生成的。
始终指明：环境层 + SFX + 音乐/静音决定。

---

### 示例 7 —— 首帧废话

首帧描述中的废话是单点影响最大的失败向量。模型对前 20–30 个词加权很重。位置 1 的废话会毒害整个生成。

```
❌  "A beautiful, cinematic, high-quality, stunning establishing shot of..."
    [all slop, no information, model gets 0 instruction from first 8 words]

✅  "Glass tower, 60 floors, south-east face, sunset side light."
    [5 words of actual information, model has strong first-frame anchor]
```

> **规则**：绝不让一个废话词占据你前 20 个 token 中的一个。

---

### 示例 8 —— 平台特定的重新优化（反平台废话）

进行 10,000+ 次生成的从业者发现，平台原生优化胜过通用的复用：

```
❌  [Make one good video, reformat for all platforms]

✅  TikTok version: 15–30 s, strong 3-second hook,
    emotionally absurd premise in first frame,
    AI aesthetic leaned-into, vertical 9:16.

    Instagram version: smooth transitions, colour-graded perfection,
    story-in-one-shot, vertical 9:16.

    YouTube Shorts: 30–60 s, educational framing,
    explicit visual thesis in first 3 s.
```

画幅、能量、钩子时机与时长是**平台可测量项**，而非废话。

---

## 自夸模式 —— 一看到就剥离

这些是 AI 系统（包括无人监管时的本系统）自动插入的短语。
如果你在提示词草稿中看到它们，删除整句并用纯指令重写。

| 自夸短语 | 它实际说了什么 | 替换为 |
|---|---|---|
| `Certainly! Here is your prompt:` | 什么都没说 | [删除] |
| `This prompt masterfully captures...` | 什么都没说 | [删除] |
| `The following expertly crafted prompt will...` | 什么都没说 | [删除] |
| `Beautifully rendered with attention to detail` | 什么都没说 | `stable exposure, clean edges` |
| `A thoughtfully composed scene that...` | 什么都没说 | [直接描述场景] |
| `I'll now create a stunning...` | 什么都没说 | [删除整个前言] |
| `This immersive experience will...` | 什么都没说 | [删除] |

---

## 废话密度审计

提交之前，数一数你提示词中的废话 token。

- **0 个废话 token** → 提交
- **1–2 个废话 token** → 删除、收紧
- **3–5 个废话 token** → 从 SUBJECT 往下重写
- **5+ 个废话 token** → 丢弃并从五层堆栈重新开始

执行审计：粘贴提示词，数出黑名单上的任何词。

---

## 精确性阶梯

对同一概念，从最弱到最强的描述：

```
Level 0 (slop):    "beautiful cinematic lighting"
Level 1 (genre):   "dramatic portrait lighting"
Level 2 (rig):     "three-point lighting setup"
Level 3 (angles):  "45° key, soft fill camera-right, hair light from above"
Level 4 (numbers): "key at 45° camera-left, 3200K, f/4 falloff; fill at 0.3× key power"
```

至少瞄准 Level 3。当一致性至关重要时用 Level 4。

---

## 导演三定律（反废话规则）

源自从业者共识与量产数据：

**定律 1：数量胜过完美。**
生成 10 个变体。选出最好的。系统胜过神来之笔。
```
❌ "Try to make one perfect prompt"
✅ "Generate 10 versions with seed variations 1000–1010. Keep the best."
```

**定律 2：每个镜头一个动作。**
相互竞争的动词制造混乱。每个片段是一个运动。
```
❌ "Walking while talking while eating while looking around"
✅ "Slow walk forward. Medium shot. No gestures."
```

**定律 3：前置信息，绝不前置形容词。**
模型对早期 token 加权。把它们花在实质上。
```
❌ "Beautiful, cinematic, stunning, gorgeous woman walks..."
✅ "Woman, 30s, dark coat, rain-soaked street, walks toward camera..."
```

---

## 把正向约束作为质量控制

⚠️ **Seedance 2.0 不支持负向提示词。** 没有 `--no` 语法，没有 `negative:` 字段。
使用**正向约束**——描述你想要什么，而非你不想要什么。

```
❌  --no watermark --no distorted hands --no blurry edges
✅  clean background, no overlaid text, stable hand positions,
    crisp edge definition, no hallucinated geometry
    [state as plain positive requirements]
```

策略：与其列出要排除的内容，不如指明你期望的输出合同。
相同的信息，正确的方向。与模型协作，而非与其架构对抗。

---

## 路由

提示词构建 → [skill:seedance-prompt]
无废话的风格 → [skill:seedance-style]
QA / 输出评审 → [skill:seedance-troubleshoot]
