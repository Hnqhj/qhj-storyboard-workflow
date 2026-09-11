# `seedance-audio` 的遗留正文

迁移于 2026-04-27 的 v5.1.0 期间。除非在 `references/api-status.md` 或 `references/source-registry.md` 中得到确认，否则将此处的平台、政策、API 与安全声明视为遗留内容。

---

# seedance-audio

面向 **Seedance 2.0 视频生成** 的音频设计、唇音同步与多角色对白。

> **来源情报**：ByteDance 官方 Seedance 2.0 发布博客（seed.bytedance.com）、抖音创作者社区、CSDN 从业者教程，2026 年 Q1。西方来源的真实世界数据极少。

---

## ⚠️ 关键区分：即梦平台上的两个独立工具

即梦平台托管了**两个完全不同的工具**，二者都涉及唇音同步。混淆它们是最常见的文档错误。

| 工具 | 模型 | 在哪里找 | 它做什么 |
|------|-------|--------------|--------------|
| **视频生成** | **Seedance 2.0** | 即梦 → 视频生成 → Seedance 2.0 | 生成完整视频片段（4–15 秒），具备原生音视频联合生成。音频是生成输出的一部分。 |
| **数字人** | **OmniHuman-1** | 即梦 → 数字人 | 肖像动画工具——上传一张面孔图像 + 音频 → 生成具备精确唇音同步的说话头像。具有大师/快速/标准模式。 |

**本 skill 仅涵盖 Seedance 2.0 视频生成。**
大师模式、快速模式、标准模式及 OmniHuman-1 引擎都属于**数字人工具**——而非 Seedance 2.0。不要把这些概念引入此处。

---

## 范围

- Seedance 2.0 原生音频生成架构
- 音频参考输入系统（节奏、氛围、节拍、唇音同步）
- 视频生成提示词中的对白规格与唇音同步
- 多角色唇音同步：已确认的问题与已知的变通办法
- 已知失败模式与现场验证的修复
- 平台音频约束（格式、时长、文件限制）
- 已暂停的功能（2026 年 2 月执行）
- 声音层设计
- 卡点（beat-sync）技术
- 声音驱动的视觉时序

## 范围之外

- 数字人功能及其大师/快速/标准模式 → 独立工具
- OmniHuman-1 → 独立模型、独立功能
- 冲击 VFX 物理 → 见 [skill:seedance-vfx]
- 音乐驱动的运镜剪切 → 见 [skill:seedance-camera]
- 版权执行 → 见 [skill:seedance-copyright]

---

## Seedance 2.0 音频如何工作

对于大多数用例，**用自然语言描述你想要的声音。** 模型理解声音概念。

- `The scene is silent except for the sound of wind.`
- `A heavy metal track plays.`
- `The sword makes a "shing" sound when drawn.`

仅在需要精确唇音同步或音乐视频卡点时才使用 `@Audio1` 参考。

Seedance 2.0 使用**统一多模态音视频联合生成架构**。音频与视频一起生成——而非作为独立的处理流程。这是它与较旧视频模型的核心架构差异。

**模型自动生成的内容：**
```
Ambient audio:     environmental sounds matched to visual scene
Background music:  mood-appropriate score matched to visual content  
Sound effects:     event-locked sounds (footsteps, impacts, etc.)
Dialogue:          natural speech with lip-sync when characters talk in the prompt
```

**音频参考输入做什么：**
当你把一个 MP3 作为 `@Audio1` 上传时，你提供的是一个**参考**，它影响：
- 视觉剪辑的节奏与节拍
- 生成音频的氛围与音调特征
- 卡点剪切时序
- 用于对白生成与唇音同步的语音/言语参考

音频输入**不**保证模型会原封不动地播放你上传的精确音频——它把文件当作参考，而非播放轨道。（需要精确音频保留时的变通办法见失败模式 1。）

---

## 平台音频约束（硬限制）

违反这些会导致无错误消息的静默失败。

```
Format:       MP3 only.
              WAV, AAC, OGG, FLAC, M4A are accepted with no error
              but produce no lip-sync or fail silently. #1 silent failure cause.
Duration:     ≤ 15 seconds per audio file. Hard limit.
              Optimal range: 3–8 s for best lip-sync accuracy.
File budget:  Max 3 audio clips per generation (part of the Rule of 12).
Bitrate:      128–320 kbps recommended. Below 64 kbps degrades sync.
Size:         ≤ 10 MB per file.
Noise:        Background noise in audio degrades phoneme recognition.
              Use clean, noise-free recordings.
```

---

## 对白与唇音同步

Seedance 2.0 从两条路径生成唇音同步：

**路径 1 —— 文本驱动的对白**（最可靠）：
```
Character A says: "We leave at dawn."
Framing: medium close-up, locked-off camera.
Character lips match the dialogue naturally.
```

**路径 2 —— 音频驱动**（音频驱动）：
```
Upload MP3 audio as @Audio1.
In prompt: "Lip-sync matches @Audio1 exactly. Camera: medium close-up, locked."
```

**可靠唇音同步的关键规则：**
- 保持台词简短。长对白会降低视觉稳定性。
- 把对白放进引号：`Character says: "We leave at dawn."`
- 指明取景：`medium close-up, locked-off camera`
- 移除头部/面部运动 token（点头、转头、摇头）——它们与唇部引擎竞争
- 用时序指明停顿：`"brief pause at 2s, then continues"`

---

## ⚠️ 多角色唇音同步：官方未解决

ByteDance 自己的官方 Seedance 2.0 发布博客明确指出：

> **"Seedance 2.0 仍需继续解决多人口型匹配、偶现音频失真等问题"**
> 翻译："Seedance 2.0 still needs to continue solving multi-person lip-sync matching and occasional audio distortion issues."

这不是社区抱怨。它是 Seedance 团队的官方承认。单次生成中的多人唇音同步在 2026 年 Q1 时是 Seedance 2.0 中一个**开放、未解决的问题**。

**多角色时实际会发生什么：**
- 模型可能只让一个角色的嘴动
- 两个角色可能都产生混乱或错位的嘴部动作
- 两个角色之间的音频路由不可靠
- 即使提示词相同，结果也不一致

**变通办法：分别生成 + 合成**

这是抖音创作者使用的现场验证解决方案：

```
STEP 1 — Split dialogue audio by character
  Character A lines → CharA.mp3 (≤8 s each segment, MP3, 128–320 kbps)
  Character B lines → CharB.mp3 (≤8 s each segment, MP3, 128–320 kbps)

STEP 2 — Generate each character separately
  Generation 1: Character A reference image + CharA audio segment 1
    Prompt: "Medium close-up, locked camera. Character A speaks.
             Lip-sync matches @Audio1 exactly. No head rotation."

  Generation 2: Character B reference image + CharB audio segment 1
    Prompt: "Medium close-up, locked camera. Character B listens,
             expression engaged but mouth closed."

  Generation 3: Character B reference image + CharB audio segment 2
    Prompt: "Character B speaks. Lip-sync matches @Audio1. Same framing."

  ...repeat for each dialogue exchange.

STEP 3 — Composite in CapCut / Jianying / Premiere
  - Place both character clips in a PiP (picture-in-picture) layout
  - Apply Linear Mask between the two figure positions
  - Set feather: 15–20% to avoid hard edges
  - When A speaks: A layer = generated video / B layer = static original image
  - When B speaks: swap layers
  - Silent character uses still image = zero extra generation credits
```

**为什么这有效：**
每次生成都只有一张面孔 → 干净的音频路由 → 可靠的同步。
合成的图层切换制造出双向对话的错觉，而模型从不需要一次处理两张嘴。

---

## 已知失败模式与修复

这些失败模式记录自抖音/Bilibili 创作者社区报告（2026 年 Q1）及 ByteDance 官方评估。

### 失败 1：模型重写或替换上传的音频（音频被乱改）

**症状**：你上传了自己的 MP3；生成的视频播放完全不同的音频——模型替换或更改了你的内容。

**为什么会发生**：当 Seedance 的原生音频生成引擎检测到它知道如何生成的音频（环境声、音乐、SFX）时，可能会覆盖参考。模型把音频输入当作参考信号，而非播放指令。相互竞争的运动 token 会放大此行为。

**修复（由抖音创作者现场验证——时间戳反向套路法）：**
```
Fix A — Explicit preservation instruction:
  Add to prompt: "Audio @Audio1 plays exactly as uploaded from 0s to end.
                  Do not modify or replace the audio content."

Fix B — Remove competing audio tokens:
  Strip all ambient/SFX/music tokens from the prompt.
  Do not write: "background rain", "jazz music", "street noise"
  These invite the native audio engine to take over.

Fix C — Simplify:
  Reduce prompt to under 50 words total.
  Complex prompts increase the chance of audio substitution.
```

### 失败 2：唇音失同步 / 嘴部错位

**成因与修复：**
```
Cause: Audio too long (>10 s is the practical ceiling, not 15 s)
Fix:   Trim to 3–8 s for best results. The 15 s limit is technical maximum,
       not the sweet spot.

Cause: Noisy audio (background music, reverb, crowd noise in the MP3)
Fix:   Clean the audio before uploading.
       Remove background noise, reverb, and crowd sound.

Cause: Fast speech rate
Fix:   Record at ~80% of natural speaking pace. Slightly slower = better sync.

Cause: Head/face motion tokens in prompt
Fix:   Remove "nodding", "turning head", "looking away" — these compete
       with the phoneme engine. Use "locked camera, neutral expression".

Cause: Multi-speaker audio uploaded for single-character generation
Fix:   Always split audio by speaker before uploading. Never upload a
       conversation track and expect one character to lip-sync it.
```

### 失败 3：多角色唇音同步损坏

**根本原因**：Seedance 2.0 中已确认的开放问题（ByteDance 官方承认，2026 年 2 月）。

**修复**：使用上述的分别生成 + 合成工作流。绝不在单次生成中尝试双角色唇音同步。

### 失败 4：静默的音频格式失败

**症状**：上传成功，未显示错误，但输出没有唇音同步或出现通用生成失败。

**成因**：文件不是 MP3。WAV、AAC、OGG、FLAC、M4A 都会静默失败。

**修复**：上传前转换为 MP3（128–320 kbps，≤15 秒，≤10 MB）。
```
FFmpeg command: ffmpeg -i input.wav -codec:libmp3lame -b:a 192k output.mp3
```

### 失败 5：偶发的音频失真

**状态**：ByteDance 在 Seedance 2.0 发布说明中官方承认。
不可预测。社区尚未记录可靠的预防方法。

**当前缓解**：如果发生音频失真，重新生成。社区测试中，较短的片段（4–6 秒）显示更低的失真率。

### 失败 6：音频超过 15 秒 → 失败或截断

**修复 —— 分段生成管线：**
```
1. Split audio at natural pause points into 3–8 s segments (not 15 s slices)
2. Each segment becomes one generation
3. Use the same character reference image across all segments
4. Maintain identical framing, lighting, camera angle in the prompt
5. Stitch in CapCut/Jianying with 0-frame cuts (dissolves break lip continuity)
```

### 失败 7：语音克隆 / 面孔转语音功能

**状态**：自 2026 年 2 月起暂停（ByteDance 执行——隐私/版权）。
未宣布恢复时间表。

**当前替代方案：**
- 使用外部 TTS 工具（ElevenLabs、Minimax TTS 等）生成干净的语音 MP3
- 将该 MP3 作为你的音频参考上传

### 失败 8：真人面孔上传被拦截

**状态**：自 2026 年 2 月 15 日起被拦截（ByteDance 执行）。

**变通办法：**
- 先生成一张 AI 角色插画（使用即梦图像生成）
- 将该插画作为角色参考
- 不要上传真人照片

---

## 声音层结构

Seedance 2.0 联合生成音频与视频。即使未明确指定，音频层也会影响节奏与剪切感。

```
Ambient bed:      continuous environmental sound
Foreground SFX:   1–2 event-locked sounds
Music cue:        entry time + arc (rising / falling / steady)
Silence design:   deliberate absence — where silence matters most
```

**紧凑语法：**

```
Sound: rain bed + distant train hum.
SFX: chess piece click at 2s.
Music: low piano note enters at 3s, resolves on last frame.
Silence holds final 0.5s.
```

---

## 混音意图

```
Dialogue scene:   dialogue clean and prominent, music low, ambient subtle
Music-driven:     music leads, ambient secondary, no dialogue
SFX-driven:       environmental sounds prominent, no music
Action:           layered SFX prominent, music rhythmic, no dialogue
Atmospheric:      ambient dominant, sparse SFX, no music or faint drone
```

---

## 对白提示词语法

**单角色：**
```
Character A (deep male voice) says: "I told you not to come here."
Framing: medium close-up, locked-off camera.
Lip-sync matches @Audio1 exactly. No head rotation.
```

**双角色（分别生成——见合成工作流）：**
```
Generation 1 (Character A's turn):
  Character A says: "I told you not to come here."
  Character B listens silently, expression neutral.
  [Use Character A reference image only]

Generation 2 (Character B's turn):
  Character B says: "You didn't leave me a choice."
  [Use Character B reference image only]
```

**时间戳锚定：**
```
At 0s: character begins speaking quietly.
At 2s: brief pause, character looks down.
At 4s: character resumes with urgency.
Lip-sync follows @Audio1 throughout.
Camera locked, no head rotation.
```

---

## 多语言生成

```
Character speaks in Mandarin: "[dialogue]"
Character speaks in English: "[dialogue]"
Character speaks in Cantonese: "[Cantonese dialogue]"
Character speaks in Sichuan dialect: "[dialect text]"
Character speaks in Japanese: "[dialogue]"
Character speaks in Korean: "[dialogue]"
```

已确认方言支持，包括中国地方方言。支持 8 种以上语言。

**最佳实践**：使用与提示词中书写语言相匹配的音频参考。

---

## 卡点 / Beat-Sync 技术

用于音乐同步的视觉剪辑：

1. 上传场景图像 + 一个音乐参考音频/视频
2. 提示词：

```
@Image1 through @Image6 are scene images.
@Audio1 provides rhythm and beat reference.
Cut scene transitions on musical downbeats.
Characters move with energy matching the music tempo.
Visual pacing: fast during chorus, slower during verse.
```

**卡点最佳实践：**
- 5–7 张场景图像效果最好（越多 = 越多剪切 = 越复杂的编排）
- 使用明显有节奏的音频（而非环境或氛围曲目）
- 短片段（4–8 秒）在节奏精度上比 15 秒片段更可靠
- 卡点与对白同步在一次生成中互斥——绝不混用两者

---

## 声音驱动的时序

用音频提示锚定视觉事件：

```
Sound: thunder crack at 3s.
Visual: lightning illuminates the scene exactly at the thunder crack.
Character flinches at the sound.
```

---

## Agent 陷阱

1. **只用 MP3，始终如此。** WAV/AAC/OGG/FLAC/M4A 都会静默失败。无错误消息。
2. **每段最多 15 秒。最佳点是 3–8 秒。** 10 秒后同步质量下降。
3. **多角色唇音同步官方未解决。** ByteDance 自己说的。用合成。
4. **模型把音频当作参考，而非播放。** 如需精确保留音频，用时间戳锚定。
5. **干净音频 = 更好的同步。** 嘈杂的源会显著降低音素识别。
6. **放慢语速。** 略慢于自然语速可提升同步精度。
7. **移除头部运动 token。** "点头""转头"会与唇部引擎竞争。
8. **语音克隆已暂停**（2026 年 2 月）。改用外部 TTS。
9. **真人面孔上传被拦截**（2026 年 2 月）。使用 AI 生成的角色美术。
10. **卡点与对白在一个提示词中互斥。**
11. **更短的片段 = 更好的同步。** 在自然停顿处拆分长对白，而非任意剪切。
12. **跨片段保持一致的取景/光照**，使拼接片段无痕剪切。
13. **偶发音频失真是已知 bug。** 发生时重新生成。
14. **大师/快速/标准模式在 Seedance 2.0 中不存在。** 那些属于独立的即梦数字人（OmniHuman-1）工具。
