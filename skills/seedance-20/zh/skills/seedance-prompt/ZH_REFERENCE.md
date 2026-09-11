---
name: seedance-prompt
description: "This skill should be used when the user asks to write, improve, translate, compress, or debug a Seedance 2.0 video prompt; mentions T2V, I2V, V2V, R2V, camera direction, prompt quality, or provides reference assets for a production-ready prompt."
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

# seedance-prompt

从清晰的概念或所提供的参考素材构建可用于生产的 Seedance 提示词。把提示词当作一份简短的拍摄简报：它必须说明画面上有什么变化、相机做什么、光线和声音贡献什么，以及什么必须保持稳定。让最终提示词控制在平台提示词预算之内，并在交付前移除填充词。

加载 `[ref:quick-ref]` 获取清单，加载 `[ref:reference-workflow]` 处理多模态参考，加载 `[ref:i2v-guide]` 处理图生视频，加载 `[ref:first-last-frame-guide]` 处理首/末帧工作，当范例有用时加载 `[ref:examples-by-mode]`，加载 `[ref:shot-list-continuity]` 处理多镜头专业计划，加载 `[ref:multishot-grammar]` 处理镜头标签语法、镜头数×秒数预算以及单次生成内的剪切位置，加载 `[ref:multilingual-community-examples]` 处理中文/俄文/日文/韩文/西班牙文或混合语言提示词。当存在序列状态时，加载 `[ref:prompt-compiler]` 并只编译当前镜头契约。

## 意图

这是存在于某人脑海中的场景与存在于屏幕上的场景之间的翻译器。用户已经想象出了它；这份工作就是在传送途中尽可能少地丢失。成功就是一次生成已足够接近，让他们能去反应而非去解释。每次修订都继承故事已经决定的一切，只改变反应所要求的那一处——草稿是一场对话，而非一次重启。

## 导演公式

在填充各槽位之前，先决定这个镜头在做的那一件事。加载 `[ref:directing-engine]`，解读场景，点名一个单一意图，并让那个意图共同选择相机、光线、走位、表演和声音，使它们相互强化而非相互竞争。下面的公式是一个连贯设置的容器，而非一份独立装饰物的清单；若项目语态已设定，就让这个镜头处于其中。

使用 `Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints`。把主体和主要动作放在最前，因为靠前的从句设定镜头的层级。若某个参考素材已经展示了某项信息，就不要强行填满每个槽位；对于 I2V，只描述静态图像无法展示的运动、相机、定时、变换、音频和保留约束。

| 槽位 | 用于 | 可直接用于提示词的范式 |
|---|---|---|
| Subject | 模型必须追踪的锚点。 | `Original ceramic perfume bottle on black acrylic, label preserved exactly` |
| Action | 可见的变化。 | `condensation beads form and slide down the glass over five seconds` |
| Scene | 仅限参考素材中尚未呈现的内容。 | `quiet rain-lit kitchen counter, shallow depth of field` |
| Camera | 一个带终点的主要运动。 | `slow dolly-in from medium product shot to macro label detail` |
| Light and style | 物理光线加上安全的视觉语言。 | `warm practical key from frame left, cool blue rim, clean commercial realism` |
| Audio | 环境底噪、音效、对白或静默。 | `Sound: low room tone, soft glass chime on final frame` |
| Constraints | 保留项与排除项。 | `logo, shape, label, and cap geometry remain unchanged` |

## 模式闸门

在起草前选择模式。**T2V** 需要主体、动作、场景、相机、光线、风格和约束，因为尚无任何可见之物。**I2V** 从 `[Image1]` 开始，只添加运动、时间、相机、光线过渡、音频和保留项。**V2V** 应把 `[Video1]` 映射到源片段、相机运动、动作节奏、走位、剪辑目标或延展锚点，而非意外迁移身份。**R2V** 必须列出每个参考角色并陈述什么不得迁移。**FLF2V** 用 `[Image1]` 作首帧、`[Image2]` 作末帧，然后只描述连续的过渡。

| 模式 | 起草优先级 | 常见错误 | 修复 |
|---|---|---|---|
| T2V | 用紧凑的分层构建整个镜头。 | 一段镜头里事件太多。 | 保留一个可见节拍和一个终点。 |
| I2V | 保留可见身份；添加运动。 | 反复重述图像，直到产品或面孔漂移。 | 写 `preserve [Image1] exactly`；只添加动态变化。 |
| V2V | 迁移运动、相机或定时。 | 复制未授权的肖像或场景细节。 | 使用自有/已授权/获许可的参考，并限制迁移角色。 |
| R2V | 给每项素材分配独立角色。 | 一个参考被要求控制身份、姿势、场景和风格。 | 拆分角色或优先最重要的角色。 |
| FLF2V | 从首帧移动到末帧。 | 把末帧当作模糊的氛围而非终点。 | 陈述 `[Image2]` 是最终视觉目标。 |
| Edit | 在改变一个图层的同时保留源片段。 | 重写整个场景而失去连续性。 | 写 `[Video1] is the source clip; change only...` |
| Extend | 仅从被采用的源素材续接。 | 从一个计划中的结尾起始或捏造片段状态。 | 路由到 `[skill:seedance-continuation]` 并使用已观察到的末态。 |

## 序列边界

通用提示词技能不得独立捏造续接状态。若用户要求续接、延展、做第二部分或使用前一段片段，则路由到 `[skill:seedance-continuation]`，除非被采用的片段/末帧及已观察到的末态已存在于序列状态中。

对于序列提示词，保留 `project_id`、`clip_id`、`parent_clip_id`、连续性锁定项、精确的引用标签、实际的开场状态、已完成节拍的排除项，以及预留的未来节拍。最终提示词保持自然语言并只覆盖当前镜头。

## 提示词构建流程

首先，识别那个单一的可见节拍：揭示、到达、决定、变换、接触、追逐或消失，并点名它所服务的那一个意图。接着，在添加形容词之前分配参考角色。然后，按导演公式的顺序写一份紧凑的初稿，让相机、光线、表演和声音都瞄准那个意图。最后，运行一次自检和来自 `[ref:directing-engine]` 的执导连贯性测试：一个主体、一个主要动作、一个有动机的主相机运动、有物理动机的光线、写成可见手势而非情绪词的表演、已分配的角色标签、声音意图，以及没有空洞的增强词。

## 压缩规则

当提示词过长时，按此顺序删减：重复的风格形容词、泛泛的质量词、参考素材中可见的背景细节、次要相机运动、次要动作，以及臆测性的情绪标签。保留保留约束、动作定时和角色映射。若用户请求双语或混合语言提示词，仅为清晰度而使用语言混用：参考角色、对白语言、技术性相机术语，以及安全的制作约束。不要用另一种语言来掩盖不安全的意图。

## 输出契约

返回：

1. 模式：T2V、I2V、V2V、R2V、FLF2V、edit 或 extend。
2. 参考角色映射（若有）。
3. 控制在已核实的当前界面提示词预算之内的最终提示词。
4. 在有用时，可选的中文压缩版本。
5. 当提示词属于专业序列时的分镜表或交付说明。
6. 相关时的安全或版权说明。

在定稿前，执行一次反套话检查并移除模糊的质量增强词。



## Liu copyable-prompt hard gate

When the output is for Liu and is meant to be pasted into AI-video / SD2 / Seedance generation, do not use a loose natural-language paragraph. The final paste-ready prompt must follow this order unless Liu explicitly requests another format:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

Paste-ready prompt policy: the model-ready code block is positive-only. It states only what is present, visible, audible, active, and locked in the current shot. Exclusion, absence, correction, comparison to old attempts, and previous-failure wording stay outside the copyable block. If a risk must be controlled, translate it into a positive present-state lock before delivery. Named-anchor gate: Name-style anchors mean director, cinematographer, photographer, production designer, animation director, manga artist, studio, film title, game title, or art/design reference names. `镜头语言总控` uses name-style anchors or bounded camera grammar for substantial camera-sensitive prompts; these anchors own composition, blocking, lens feeling, camera motion, edit rhythm, shot scale, and reveal logic. `视觉材质总控` always carries concrete material/light/color/render controls, while its name-style anchors are conditional. Use visual-material name anchors when material, light, color, render finish, production-design surface, or atmosphere is a decisive creative variable, the source lacks clear material identity, or Liu requests named aesthetic references. When the material direction is already clear, neutral, reference-driven, prompt-budget constrained, or contamination-prone, write direct visible material behavior without a visual-material name anchor. Use 2-4 compatible anchors total when anchors are useful. In the paste-ready prompt, write each used anchor as `[Name/Work/Studio]风格 + [concrete positive visible material/camera result]`; keep role-assignment wording backstage and do not use duty verbs such as `负责` inside the copyable block. Technical camera/material terms support the style-result phrase.

Before finalizing, source-trace every concrete phrase. If a noun, prop, place, palette, camera routine, transition, enemy, power, sound cue, or stability lock comes from an old project, default template, or previous failure rather than the current request, supplied/inspected asset, active global bible/continuity lock, or user-approved reusable rule, remove it and rewrite the prompt before delivery.

