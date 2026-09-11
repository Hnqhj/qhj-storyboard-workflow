# 真人短剧提示词库

本文件用于测试和组合提示词。先选一个视觉基底，再加入角色、动作、摄影、光线和声音模块；每次只改一个变量，便于比较模型输出。

## 1. 真人写实基底

```text
photorealistic live-action short drama, natural human skin texture, subtle facial asymmetry,
realistic fabric and hair, grounded production design, professional cinematography,
natural depth of field, restrained color grading, clean frame
```

悬疑/夜景可追加：

```text
cool desaturated palette, practical street lights, wet asphalt reflections,
controlled contrast, motivated shadows, quiet urban tension
```

情感/白天可追加：

```text
soft window light, warm neutral palette, gentle falloff, intimate atmosphere,
natural eye highlights, understated emotional performance
```

不要同时使用互相冲突的“柔和低对比”和“极端黑白高对比”。色调只选一个主方向。

## 2. 景别、角度和运镜模块

| 用途 | 模块 | 适合表达 |
|---|---|---|
| 交代空间 | `wide establishing shot, eye-level` | 地点、时间、人物关系 |
| 关系推进 | `medium two-shot, 35mm lens` | 两人站位和互动 |
| 情绪观察 | `medium close-up, 50mm lens` | 克制表情和对白 |
| 信息强调 | `close-up, 85mm lens` | 眼神、手、道具 |
| 主观压迫 | `slightly low angle` | 权力、威胁、失衡 |
| 脆弱/被观察 | `slightly high angle` | 孤立、迟疑、退缩 |
| 稳定可信 | `locked-off camera` | 事实揭示、冷静对话 |
| 贴近人物 | `slow push-in` | 情绪逐步收紧 |
| 追随动作 | `gentle handheld follow` | 逃跑、跟踪、急促移动 |
| 揭示关系 | `slow lateral track` | 从遮挡物后露出第二人物 |

提示：一镜只用一个主运镜。除非模型明确支持，否则不要把推镜、环绕、升降和变焦串在一条提示词里。

## 3. 角色基底模板

```text
[C01], a fictional [age]-year-old [gender] Chinese [profession],
[face shape], [hair], [skin tone], [distinctive non-sensitive feature],
wearing [wardrobe and color], [one fixed accessory], authentic neutral expression
```

连续性规则：

- 固定信息放在每个镜头提示词的前半段，变化信息放在动作句之后。
- 选择 1–2 个稳定识别特征即可，例如“左眉尾短疤 + 深绿色帆布包”；不要为同一角色每镜创造新的发型和饰品。
- 情绪用可见行为表达：`jaw tightens`, `hesitates before answering`, `eyes avoid contact`，不要只写 `very sad`。

## 4. 场景基底模板

```text
[L01], [place type] at [time of day], [layout and depth],
[two or three repeatable props], [weather], key light from [direction],
background activity kept minimal, realistic location texture
```

示例：

```text
[L01], a narrow apartment corridor at 8 p.m., pale green walls and a frosted window at the far end,
one red umbrella by the shoe rack and a warm ceiling practical, light rain outside,
cool ambient fill from the window, warm key from above, realistic worn paint texture
```

## 5. 三镜头测试包：雨夜未接来电

### 固定设置

- 画幅：竖屏 9:16
- 每镜：6 秒
- 模式：先生成 `KEYFRAME_PROMPT`，再用图生视频
- 角色：`C01` 林晚，28 岁，短黑发，米色风衣，深绿色帆布包；`C02` 周野，30 岁，黑色夹克，旧银色手表
- 场景：`L01` 雨夜公寓楼下，`L02` 狭窄走廊
- 连续性：雨水、服装和背包不变；所有镜头屏幕方向为左到右

### S01 建立钩子

```text
KEYFRAME_PROMPT
Vertical 9:16, photorealistic live-action short drama, wide establishing shot of L01,
C01 stands alone under a weak apartment awning, beige trench coat, short black hair,
deep green canvas bag on her right shoulder, rain streaks crossing the foreground,
empty street behind her, a red umbrella near the entrance, eye-level camera, 35mm lens,
cool blue ambient night light with one warm doorway practical, wet asphalt reflections,
clean frame, no text, no logo, no watermark.

VIDEO_PROMPT
Vertical 9:16, single continuous 6-second shot from the supplied keyframe.
C01 checks her phone, freezes when a call ends, then looks toward the dark entrance.
Camera makes a slow push-in, focus shifts from the rain in foreground to her eyes,
preserve her face, beige coat, green bag and left-to-right screen direction.
End with her hand still around the phone, restrained tension, realistic rain and body motion.

AUDIO_PLAN
Ambient rain, distant traffic, one short phone vibration, no spoken dialogue.

NEGATIVE_PROMPT
anime, cartoon, 3d render, beauty filter, face morphing, extra fingers, duplicated people,
readable phone text, subtitles, watermark, abrupt zoom, scene change, overacting, flicker.
```

### S02 关系进入

```text
KEYFRAME_PROMPT
Vertical 9:16, photorealistic live-action short drama, medium two-shot in L01,
C01 under the awning on frame left, C02 steps into frame right from the rain,
C02 wears a black jacket and an old silver watch, both faces visible in profile,
the red umbrella and warm doorway remain in background, eye-level camera, 50mm lens,
cool rain light mixed with warm practical light, natural skin texture, clean frame, no text.

VIDEO_PROMPT
Vertical 9:16, single continuous 6-second shot from the supplied keyframe.
C02 stops one step away and raises his palm to signal wait; C01 does not turn fully,
only her eyes move toward him. Camera performs a gentle lateral track to the right,
keep both characters at the same scale and preserve the awning, rain and screen direction.
End on the unresolved eye-line between them.

AUDIO_PLAN
Rain and wet footsteps. C02, low and breathless, says in Mandarin: "你还是来了。"

NEGATIVE_PROMPT
identity drift, wardrobe change, extra people, lip-sync distortion, extra fingers, fused hands,
camera orbit, sudden scene change, readable signage, subtitles, logo, watermark, theatrical posing.
```

### S03 道具揭示

```text
KEYFRAME_PROMPT
Vertical 9:16, photorealistic live-action short drama, close-up of C01's hands and phone,
the beige trench coat sleeve and deep green canvas bag edge are visible, a missed-call screen
shown as soft unreadable light with no legible characters, C02's blurred shoulder in background,
85mm lens, shallow depth of field, warm doorway reflection on the phone, cool rain bokeh,
clean frame, no text, no logo, no watermark.

VIDEO_PROMPT
Vertical 9:16, single continuous 6-second shot from the supplied keyframe.
C01 turns the phone face down, revealing the old silver watch on C02's wrist as his hand
briefly enters frame and stops before touching hers. Camera stays locked off; focus racks
from the watch to the phone edge. End before contact, leaving a clear edit point.

AUDIO_PLAN
Phone case taps against her palm, rain becomes quieter, one low musical pulse, no new dialogue.

NEGATIVE_PROMPT
readable text, subtitles, watermark, deformed hands, extra fingers, fused props, object duplication,
focus pumping, camera shake, romantic kiss, new wardrobe, face morphing, abrupt cut.
```

## 6. 负面约束分层

只保留与当前镜头相关的 8–18 个词：

1. **身份层**：`face morphing, identity drift, age change, wardrobe change`。
2. **人体层**：`extra fingers, fused hands, duplicated limbs, unnatural eyes`。
3. **摄影层**：`flicker, focus pumping, rolling shutter, abrupt zoom, jump cut`。
4. **画面层**：`subtitles, watermark, logo, readable text, unwanted crowd`。
5. **风格层**：只有在模型明显跑偏时才加 `anime, cartoon, 3d render, illustration`。

## 7. 参考来源与检索关键词

- 开源工作流参考：[AIYOU - AI-Powered Short Drama Production Platform](https://github.com/yubowen123/AIYOU_open-ai-video-drama-generator)，重点参考其“角色设计 → 分镜 → 视频”的节点化顺序和真人风格词分类。
- 官方模型文档可能随版本变化，测试时搜索：`Runway video prompting guide`、`Veo video prompt guide`、`Kling image to video prompt`、`Sora storyboard prompt`。
- 不要把任意平台的分辨率、镜头时长或词权重当成通用规则；以当前模型界面和一组 A/B 测试结果为准。
