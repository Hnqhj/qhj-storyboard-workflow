# 图生视频指南（Image-to-Video Guide）

## 核心规则（Core Rule）

只对图像无法展现的内容写提示词。一张静止图像已经包含主体身份、产品外形、服装、调色、构图和背景。重新描述这些静态细节常常导致漂移。添加运动、摄影机、时机、转化、布光变化、音频和保持约束。

## 最小模板（Minimal Template）

`[Image1] is the reference; preserve [identity/product/scene] exactly. Only [motion] changes. Camera: [one move]. Lighting: [source or transition]. Sound: [cue]. Constraint: [what must not change].`

## 两种 I2V 模式（Two I2V Modes）

实地观察自中文实践；在书写前先确定模式。

- **保持模式（Hold mode，图像即此刻）：** 在片段中分布三到四个自然的微动作——一次眨眼、一次呼吸、头发飘动、一次缓慢的视线移动——并用正反双重陈述锁定其余一切：`she stays seated by the window; she does not stand, turn, or leave frame`。不用摄影机运动，最多一个缓慢推入。
- **反应模式（React mode，主体身上发生了某事）：** 把一种情绪展开为子节拍，给它真实的落定时间——`she registers the sound, her eyes widen, color rises in her face over two to three seconds`。匆忙的情绪读起来像故障；给关键节拍至少两秒。如果图像明显是场景中段而非自然的开场帧，明确锚定起点：`the clip begins exactly at this moment`。

## 保持性语言（Preservation Language）

对脆弱锚点使用精确锁定：`preserve face identity`、`preserve logo and label`、`preserve bottle shape and cap geometry`、`preserve outfit and hairstyle`、`preserve room layout`。如果场景需要自然运动，不要锁定一切；只锁定必须保持稳定的部分。

## 好的 I2V 添加项（Good I2V Additions）

| 添加 | 示例 |
|---|---|
| 微表情 | `subject blinks once and lowers their eyes` |
| 产品光 | `thin highlight travels across the label` |
| 天气 | `rain streaks behind the subject; droplets bead on the surface` |
| 摄影机 | `slow dolly-in from current composition to tighter detail` |
| 氛围 | `dust catches the doorway beam and settles` |
| 音频 | `soft room tone, one key click at the endpoint` |

## 失败修复（Failure Fixes）

- 如果身份漂移：减少新的视觉描述，强化保持约束。
- 如果摄影机跳变：使用一个带起点和终点的摄影机运动。
- 如果产品扭曲：声明保持、静态身份、无外形变化、产品不转化。
- 如果输出仍是静止：添加一个物理动作和一个时间提示。
- 如果背景改变：保持环境布局，只让光、天气或氛围动起来。
- 如果手部变形：简化手部运动，或让手处在主动作之外。
