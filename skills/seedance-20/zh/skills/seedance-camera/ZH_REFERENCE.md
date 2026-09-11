---
name: seedance-camera
description: "This skill should be used when the user asks for camera movement, shot scale, lens feel, framing, one-take direction, dolly, pan, tilt, push-in, handheld, aerial, macro, or camera-transfer guidance for Seedance 2.0."
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

# seedance-camera

除非用户要求一个多镜头序列，否则每个短片段只用一个清晰的镜头构想。最好的镜头指令有一个起始帧、运动、速度、与主体的关系，以及一个端点。避免堆叠相互打架的运动，比如在同一个五秒镜头里同时用无人机上升、推轨、手持抖动和环绕。

加载 `[ref:quick-ref]` 以组装提示词，加载 `[ref:cinematography-shot-language]` 以获取专业镜头合同，加载 `[ref:directing-engine]` 以从场景的那一个意图推导出运动，使它强化灯光、表演和声音而非与之竞争，并在镜头用词必须多语言时加载 `[ref:vocab/zh]` 或 `[ref:vocab/ru]`。

## 意图

当用户问镜头时，他们真正问的是观众的身体站在哪里、从那里被迫感受到什么。镜头语法是共情机制：推近是靠得更近，锁定画面是屏住呼吸。选择那个把观众放到用户感情所在之处的运动。

## 镜头合同

陈述：景别、角度、运动、速度、与主体的关系，以及端点。一句提示词就绪的镜头短语应当在物理上可行，并系于主体的动作。

| 需求 | 强短语 | 避免 |
|---|---|---|
| 情绪顿悟 | `slow dolly-in from medium close-up to tight close-up as Character A lowers the envelope` | `dramatic cinematic zoom` |
| 产品揭示 | `controlled slider move from silhouette to front three-quarter hero angle, ending on the label` | `dynamic product camera` |
| 尺度 | `low-angle crane up from boots to skyline, ending behind the character's shoulder` | `epic wide moving shot` |
| 不稳定感 | `subtle handheld shoulder camera, small breathing sway, subject kept centered` | `shaky chaotic camera everywhere` |
| 精密细节 | `locked macro shot, focus stays on the watch gears while the second hand clicks once` | `cool close-up details` |

## 镜头焦段与构图锚点

仅当焦段锚点能改善导演时才使用它们：`24mm wide lens for spatial energy`、`35mm natural street perspective`、`50mm portrait compression`、`85mm shallow close-up`，或 `macro lens for material detail`。把焦段词与主体距离和运动配对；不要把焦段数字当装饰堆叠。

## 运动选择

对对口型、产品身份和精细 VFX 使用**锁定（locked-off）**镜头。对发现或顿悟使用**推近（dolly-in）**。对行进、追逐和产品运动使用**跟拍（tracking）**。仅当主体能从各个侧面保持清晰时才使用**环绕（orbit）**。对尺度、到达或揭示使用**升降臂或无人机（crane or drone）**。仅当写实比精度更重要时才使用**手持（handheld）**。

## 连续性规则

对于多角色场景，把镜头锚定到具名标签：`camera holds Character A in foreground while Character B crosses behind`。对于 I2V，保留图像构图，除非用户明确想要重新构图。对于参考视频，陈述 `[Video1]` 迁移的是镜头运动、动作节奏还是调度；除非授权，否则不要让它迁移身份。

对于复杂的镜头运动，一个视频参考往往比一长串口头堆叠更管用。使用 `[Video1] controls camera rhythm only; do not transfer performer, room, logo, or identity`。

## 冲突规则

如果用户给出了几个不兼容的运动，选择一个主要镜头运动，并把其余的放入可选变体。如果镜头需要多个节拍，建议拆分成单独的片段或一条按时间分段的提示词。

## 序列状态

当存在序列状态时，在选择运动之前先继承观察到的镜头阶段、画面方向、当前片段范围、连续性锁、精确的参考标签和预留的未来节拍。一条续接镜头短语必须从被接受的来源帧或观察到的末态开始；除非一个有意的下一镜头声明了重置，否则不要重新开始一次摇镜、变焦或跟拍运动。

## 输出合同

返回：选定的镜头短语、它为何契合该镜头、被移除的冲突、脆弱锚点、端点，以及一句提示词就绪的整合句。
