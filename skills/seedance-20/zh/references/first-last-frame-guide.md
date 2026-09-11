# 首帧/尾帧指南（First/Last Frame Guide）

last_verified: 2026-05-30

用本指南处理 FLF2V、首帧/尾帧转场、中文 `首帧/尾帧`，或生成两张图像之间运动的请求。

来源边界：ByteDance 官方材料支持多模态参考、编辑、扩展和 R2V 示例。火山引擎（Volcengine）现已在其视频生成平台上记录了首帧和尾帧角色。精确的 `FLF2V` 标签仍属于产品平台词汇，因此在实现时使用当前活动平台的字段名。

## 核心原则（Core Principle）

首帧定义片段从哪里开始。尾帧定义目标状态。提示词应只描述转场逻辑、摄影机行为、布光连续性、音频意图，以及哪些东西必须保持不变。

## 参考角色（Reference Roles）

| 角色 | 英文措辞 | 中文措辞 | 俄文措辞 |
|---|---|---|---|
| 首帧 | `[Image1] is the first frame.` | `@图1 为首帧。` | `[Image1] как первый кадр.` |
| 尾帧 | `[Image2] is the last frame.` | `@图2 为尾帧。` | `[Image2] как последний кадр.` |
| 身份锁定 | `Preserve the same subject identity, outfit, shape, and scene logic.` | `保持同一主体、服装、形状和场景逻辑。` | `Сохранить того же персонажа, одежду, форму и логику сцены.` |
| 仅转场 | `Generate only the motion between the two frames.` | `只生成两帧之间的连续动作。` | `Сгенерировать только переход между кадрами.` |

## 平台字段说明（Surface Field Notes）

| 平台 | 实用措辞 |
|---|---|
| Volcengine/Ark | 用当前文档核实 `first_frame`、`last_frame`、`image_with_roles`、时长、分辨率，以及视频/音频参考能否与首帧/尾帧模式混用。 |
| Runway | 在 Runway 平台上使用 `promptImage` 位置如 `first` 或 `last`，并在假设其字段与 Volcengine 一致前重新核对当前 API 文档。 |
| ComfyUI / 合作伙伴工作流 | `FLF2V` 是有用的工作流简写，但仍要确认节点的精确输入及人脸/肖像策略。 |

## 提示词模板（Prompt Template）

```text
[Image1] is the first frame. [Image2] is the last frame.
Preserve [subject/product/character], [outfit/logo/shape], and scene layout.
Generate a continuous transition from [starting state] to [ending state].
Motion: [one physical action path].
Camera: [one controlled move or locked frame].
Lighting: [source and continuity].
Sound: [ambience/dialogue/SFX/music/silence].
Constraints: no new text, no watermark, no identity change, no object redesign.
```

## 产品安全转场（Product-Safe Transition）

`[Image1] is the first frame and [Image2] is the last frame. Preserve the bottle logo, label, glass shape, cap geometry, and color exactly. Only the condensation and light change: droplets gather at the shoulder, slide toward the label, and a narrow warm highlight travels left to right. Camera stays locked in a medium product shot. Sound: low room tone, one soft glass tick at the end.`

## 角色安全转场（Character-Safe Transition）

`[Image1] is the first frame and [Image2] is the last frame. Preserve the original character's face structure, hairstyle, jacket, and room layout. The character slowly stands from the chair, turns toward the window, and stops in the final pose. Camera: locked medium shot with a slight push-in. Lighting: same cool window light, warmer lamp glow at the end. Sound: quiet room tone and soft floor creak.`

## 转化方法（Transformation Method）

实地观察的技术；在承诺结果之前先测试。当提示词点明两个终点状态外加"持续载体"（persisting carrier）——即在变化中存留并承载连续性的元素：一个标识、一个剪影、一个光源、一个摄影机位置——转化就会成功。

- 状态 A、状态 B 与载体：`the paper crane unfolds into a flat sheet; the red wax seal stays fixed at center frame throughout.`
- 让载体占据视线：观者追踪那个不变的元素，而它周围的一切都在转化，这能掩盖中间帧的怪异。
- 困难的案例可分解为首帧/尾帧步骤：生成 A → 载体稳定的中点，然后中点 → B 作为第二次 FLF2V，再把它们剪在一起。
- 匹配剪辑（match-cut）变体：在剪辑两侧保持载体的屏幕位置与缩放，让周围环境互换。

## 常见失败（Common Failures）

| 失败 | 修复 |
|---|---|
| 主体变形 | 只锁定重要的身份锚点；移除多余的风格变化。 |
| 产品/标识被重绘 | 使用锁定摄影机，只说光/天气在动。 |
| 跳切 | 添加 "continuous transition" 和一条物理动作路径。 |
| 摄影机混乱 | 用锁定画面或一个缓慢推入替换多个运动。 |
| 结尾偏离目标 | 声明 `[Image2]` 是最终视觉目标，而不仅是情绪参考。 |
