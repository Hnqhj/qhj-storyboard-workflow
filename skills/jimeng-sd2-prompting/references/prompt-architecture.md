# Jimeng SD2 / Seedance 2.0 Prompt Architecture

Use this reference to create original, pasteable prompts. Do not copy public prompt-library examples verbatim; distill their structure into new prompts for the user's scene.

## Liu Compact Master Hierarchy — 2026-07-10 superseding gate

For Liu's final paste-ready prompt, this gate overrides legacy long templates and negative-slot examples later in this reference:

- Fixed order: `角色/资产锁定 -> 视觉材质总控 -> 镜头语言总控 -> 事件节拍 -> 声音 -> 正向稳定约束`.
- Global masters are the highest-level invariants, but they stay compact: one high-density visual/material master and one high-density camera master.
- Event beats inherit the masters. They add only temporal change: subject state, action cause/result, camera proof, transition, and endpoint.
- Choose one primary fidelity spend and one secondary spend. Specialist outputs are selected and compressed, never concatenated wholesale.
- In I2V/R2V, inspected reference assets carry spatial appearance and layout; text focuses on motion, timing, camera path, sound, and endpoint.
- The paste-ready block remains positive-only and source-traced. Any legacy exclusion/negative examples below are diagnostic history, not valid Liu paste-ready syntax.
- If a phrase does not change a visible or audible decision, remove it.

## Liu Local Asset Token Rule

For Liu's paste-ready prompts, first-use asset mentions supplied with the script must combine the exact uploaded name-based handle with a parenthesized role scope: `@角色立绘.png（角色身份与外观参考）`, `@场景夜景.jpg（场景或道具参考）`, `@动作预演.mp4（动作、节奏与运镜参考）`, and `@干拟声.wav（对白与拟声参考）`. Do not deliver generic `参考图1/图1/image1`, invented names, bare `{{Image N}}`编号, `@material[...]`, or pseudo material-layer tags. If a platform document uses another handle style, translate it into Liu's exact `@图片名`/`@视频名`/`@音频名` format before final delivery. Put the complete camera style in `镜头语言总控`; ordinary event beats inherit it, while only a genuine special-camera beat adds its trigger and concrete visible result.

For a whitebox / Blender previs / mocap video reference, write its role explicitly:

```text
@动作预演.mp4（动作、身体重心、镜头远近与切镜逻辑参考）：迁移动作节奏与运镜证据。
```

## Core Model Assumptions

Seedance 2.0 is commonly used as a multimodal video model: text, image, video, and audio can all steer generation. It is best treated as a director system, not a keyword blender. Strong prompts assign reference roles, define a limited action arc, and specify camera/lighting/rhythm.

Recommended duration strategy (generic standalone tests; Liu's short-drama contract takes precedence):

- 5 seconds: one action, one camera move, best stability.
- 8-10 seconds: one clear action arc with a beginning and ending state.
- 13-15 seconds: use exact macro-segment ranges when timing confidence is high; otherwise use approximate or untimed connected beats. Keep internal shot timing flexible.
- Longer story: generate in separate clips; use tail-frame continuity. In Liu's script-to-camera-group workflow, each group remains 14-28 seconds, never over 30 seconds, with the shortest complete duration selected.

Standalone generation assumption:

- If the user generates clips separately, the model has no memory of earlier prompts or earlier clips unless those assets are supplied again.
- State the current form, current weapon size, scene, and pose at the start of every standalone prompt.
- Avoid "上一段之后", "承接前面", "从小弓继续", or "刚才变形完成" unless a prior video/tail frame is actually provided.
- Use "开头已经是..." for standalone clips that start in a later story state.

## Master Formula

For weight-sensitive action, insert an action-physics layer before camera and material:

```text
[actor-to-weapon strength + mass distribution + support/center path
+ contact response + follow-through/braking + stable end state]
```

Compact block:

```text
动作物理：[角色力量等级]相对[武器负载]；武器为[握把侧/均衡/前端重/头重/柔性延迟]质量分布；
[脚/手/地面/墙/载具/缆索]提供支撑；动作由[动力链]启动；
接触后[双方与环境反应]；最后通过[制动路径]稳定到[终止姿态]。
```

Use this order:

```text
[reference roles if any]，
[Format/genre + aspect/total duration]，
[global visual master: medium + aesthetic family + palette + line/shape
+ material-light system + rendering hierarchy + optics + forbidden drift]，
[main subject + locked identity + world/prop locks]，
[scene + time + atmosphere]，
[action progression: start -> motion -> end]，
[camera movement + lens/framing]，
[lighting + color + material detail]，
[sound/dialogue if needed]，
[consistency constraints + negatives]
```

Compact Chinese template:

```text
一段[时长][比例]的[类型/风格]视频。[主体锁定]位于[场景]，[动作从A到B]。
镜头写成`X风格 + 具体可见运镜结果`，再接[跟随对象/机位/焦段/运镜路径/动作触发/证明任务/交接终点]，[光线/色调/材质]，[节奏/声音]。
全程保持[脸/服装/道具/空间]一致，禁止[常见失败项]。
```

## Mode Templates

### Text-to-Video

Use when no images are supplied.

```text
一段5秒的电影感短视频。夜雨中的黑色机车停在霓虹巷口，车身带细微水珠和磨损划痕，排气管有蓝紫色高温氧化。大卫·芬奇风格 + 低机位35mm精确慢推让车体几何与雨夜巷道保持稳定；引擎震动触发镜头跟随机车前轮轴线缓慢靠近，证明水膜反光与机械细节，最终停在油箱与车把形成的三分之二构图。地面积水倒映红蓝霓虹，主灯从左后方形成冷色轮廓光，雾气从排气口缓慢散开。
```

### Image-to-Video

Use when the user provides one main image. Preserve the image first; add only plausible motion.

```text
以@角色立绘.png（角色身份、外观、服装、道具与构图参考）为视觉基准，保持人物五官、发型、服装、道具、构图和背景稳定。生成5秒视频：人物缓慢抬眼，发丝和披风被轻微风吹动，手中的武器产生细小金属反光变化。押井守风格 + 极轻微慢推保持人物轮廓与背景透视稳定；抬眼动作触发镜头跟随面部轴线缓慢靠近，证明眼神与金属反光变化，最终停在肩部以上近景。冷色侧逆光增强金属边缘。
```

### First/Last-Frame

Use when start and end frames exist. Describe the transition path.

```text
以@首帧构图.png（首帧、角色身份与初始构图参考）作为开场，以@尾帧构图.png（尾帧姿态与结束构图参考）作为终点，生成8秒平滑过渡视频。
0-2秒：押井守风格 + 极轻微靠近保持人物与背景透视稳定；呼吸、发丝和衣料微动触发镜头跟随面部轴线缓慢前移，证明初始身份与表情，肩线开始转动时交接下一运镜相位。
2-6秒：押井守风格 + 克制的15度短弧绕呈现人物朝向变化；角色向画面右侧转身触发镜头跟随肩线沿同方向弧绕，证明面部角度、身体朝向与空间关系，动作减速时交接尾帧对齐相位。
6-8秒：押井守风格 + 同一弧线柔和减速形成稳定终点；镜头跟随角色最终肩线沿短弧末端收束，证明尾帧姿态与构图已经对齐，最终停在@尾帧构图.png（尾帧姿态与结束构图参考）的空间关系。全程保持同一角色、同一服装与同一场景空间。
```

### Multi-Reference

Assign roles clearly. Do not simply list assets.

```text
使用@角色立绘.png（角色身份、外观与服装参考）锁定角色，@场景色调.jpg（场景与色调参考）锁定环境，@镜头运动.mp4（镜头运动与节奏参考）锁定运镜，@音乐参考.wav（音乐节拍与氛围参考）锁定声音。生成10秒竖屏广告片。
进入：大卫·芬奇风格 + 精确低机位跟拍保持人物与橱窗几何稳定；人物从暗处迈入霓虹橱窗时触发镜头跟随脚步前进，证明服装轮廓、步态与湿润地面反光，第二个鼓点触发镜头交接身体轴线。
揭示：大卫·芬奇风格 + 受控上摇把注意力从脚步转移到面部；第二个鼓点触发镜头跟随身体轴线上摇，证明角色身份、表情与霓虹光层，上摇接近眼线时交接终点相位。
终点：大卫·芬奇风格 + 近景微推后稳定停驻；角色目光落向镜头触发相机跟随面部轴线短推，证明最终表情和产品式人物呈现，最终停在肩部以上稳定近景。角色脸型和服装保持稳定。
```

### Ordered Multi-Shot

Use for 10-15 second clips or short narrative beats. Choose exact, approximate, or untimed segment progression according to timing confidence; do not equate segment timing with cut timing.

```text
【角色/资产锁定】
同一主角、黑伞、黑色皮衣与雨夜街区保持稳定。
【视觉材质总控】
克制的冷色电影摄影，黑蓝主色与少量暗红反射；湿润沥青、黑伞和皮衣呈现真实粗糙度、水膜与窄边高光。
【镜头语言总控】
大卫·芬奇风格 + 精确受控的低机位侧跟、中景前推与近景下漂形成冷静观察；动作与视线触发切镜，画面轴线保持一致。
【事件节拍】
开场：大卫·芬奇风格 + 低机位精确侧跟保持人物与街道几何稳定；脚步踏入积水触发镜头跟随主角从左向右移动，证明行进路线与雨夜空间；伞面掠过前景触发下一镜。
中段：大卫·芬奇风格 + 中景缓慢前推把注意力从环境收束到表情；主角放慢脚步并回头触发镜头跟随面部方向推进，证明表情与霓虹反光；伞沿水滴下坠触发下一镜。
结尾：大卫·芬奇风格 + 近景短促下漂后平稳回到人物面部；水滴落下触发镜头跟随伞沿向下移动，再交接到主角近景，证明停步后的安静终态；背景车灯沿同一方向虚化掠过。
【声音】
雨声、脚步水花与远处车流逐渐收窄，主角轻声说一句“走吧”，声音低而清晰。
【正向稳定约束】
主角身份、服装、黑伞、雨夜场景、光线方向、镜头轴线与动作路径持续一致。
```

### Standalone 15-Second Action Prompt

Use when the user wants one clip generated independently, but the clip itself needs many action peaks.

```text
【角色/资产锁定】
@角色立绘.png（人物身份、服装、武器造型、色调与初始构图参考）：锁定当前角色与资产。

【视觉材质总控】
[媒介、色彩、材质、光线与运动清晰度]

【镜头语言总控】
[完整全片镜头风格：名词美学锚点、透视、镜头家族、畸变、运动能量、构图/剪辑节奏、揭示逻辑]

【事件节拍】
开场：第一帧已经处于[当前形态、距离与动作压力]。
推进：[第一个状态变化、动作路线与空间结果]。
转折：[攻防、支撑、高度或主动权发生变化]。
峰值：[决定性动作、接触证据与直接后果]；若此拍需要特殊镜头，补写“[冲击/遮挡]触发[特殊运镜]，形成[可见结果]”。
收势：[制动、余波与清晰终态]。

【声音】
[每个主要节拍的声音焦点与变化]

【正向稳定约束】
[身份、服装、武器尺寸、材质响应、轴线、动作路径与镜头注意力保持稳定]
```

Rules:

- Ordinary event beats inherit the camera master and write body/weapon action, state change, contact, consequence, and endpoint. Only a genuine special-camera beat adds a local trigger plus concrete visible result compatible with the master.
- For action density, prefer short peaks over long slow motion.
- Put the global visual master before the detailed action and shot structure. Keep it compact and authoritative so style defines the generation domain without replacing motion.
- If the strongest beat uses naked-eye 3D, limit it to the final peak or one designated impact.

## Camera Vocabulary

Use only the camera moves that matter:

- 慢推 / push in: increases focus and tension.
- 后拉 / pull back: reveals environment or loneliness.
- 跟拍 / tracking: follows walking, running, vehicle movement.
- 环绕 / orbit: shows character or product hero presence; keep angle small for stability.
- 上摇 / tilt up: reveals scale from feet/object to face/building.
- 俯拍 / overhead: useful for layout, crowds, food, product process.
- 低机位 / low angle: power, speed, pressure.
- 手持轻晃: documentary or UGC energy; use carefully.
- 一镜到底: use for spatial continuity; keep action simple.

Camera syntax:

```text
大卫·芬奇风格 + 低机位35mm精确侧跟保持空间几何稳定；镜头沿角色右侧匀速跟随，角色停步触发轻微前推，最终停在面部特写。
```

## Consistency Locks

Use these when the user cares about identity or product fidelity:

```text
全程保持同一人物五官、发型、妆容、服装、身材比例和道具不变。
保持产品Logo位置、颜色、材质、包装形状不变。
保持首帧构图、背景透视、光线方向和色调一致。
动作只发生在[指定部位/主体]，其他元素保持稳定。
```

## Negative Prompt Blocks

General:

```text
禁止文字、字幕、Logo、水印、画面闪烁、主体变形、肢体错误、换脸、换装、背景漂移、无关人物、低清晰度、过度锐化。
```

Image-to-video:

```text
禁止改变原图身份、服装、构图、背景、道具数量；禁止新增镜头外物体；禁止大幅度旋转导致人物崩坏。
```

Commercial/product:

```text
禁止产品变形、标签错字、包装比例改变、Logo漂移、反光糊成白斑、手指遮挡产品关键卖点。
```

## Iteration Strategy

Change one variable per retry:

1. If motion is weak: strengthen the verb and reduce scene detail.
2. If identity drifts: move identity lock earlier and reduce camera rotation.
3. If camera is chaotic: specify one camera move only and add "画面稳定".
4. If material looks fake: add concrete roughness, reflection, texture, or lighting conditions.
5. If long clip falls apart: split into 5-8 second clips and stitch in editing.

## Image / First-Frame Prompt Add-On

When making a still frame for SD2, write it as a video-ready frame:

```text
可作为即梦SD2首帧的电影感关键帧：主体位于画面[位置]，留出[运动方向]空间，光线从[方向]进入，衣料/发丝/烟雾/水面具备可动元素，构图稳定，背景有明确纵深，避免过满构图。
```

## Research Basis

Checked on 2026-06-14:

- ByteDance Seed official Seedance 2.0 page: multimodal text/image/audio/video input, director-level control, motion stability, physical realism.
  https://seed.bytedance.com/zh/seedance2_0
- Runway Seedance 2.0 help: supported modes, durations, aspect ratios, resolutions, input counts and reference roles.
  https://help.runwayml.com/hc/en-us/articles/50488490233363-Creating-with-Seedance-2-0
- Dreamina / CapCut Seedance 2.0 resource: multimodal reference workflow, first/last-frame mode, platform @AssetName reference style, prompt clarity tips; for Liu final prompts, translate first use to scoped handles such as `@图片名（...参考）` / `@视频名（...参考）`.
  https://dreamina.capcut.com/resource/seedance-2-0-prompt
- Community prompt-skill examples reviewed for structural patterns such as base structure, time-coded segments, consistency locks, and long-video continuation; do not copy them verbatim.
  https://github.com/MapleShaw/seedance2.0-prompt-skill

Rechecked on 2026-06-29:

- ByteDance Seed official Seedance 2.0 page still describes multimodal text/image/audio/video input and director-level control, supporting the role-based prompt architecture rather than a keyword-only style.
  https://seed.bytedance.com/zh/seedance2_0
- Volcengine / BytePlus ModelArk video generation API documentation for Seedance 2.0 was updated on 2026-06-25; exact endpoint parameters, account access, durations, ratios, audio/reference behavior, and model names are platform-specific and must be rechecked before hard-coding them into prompts, scripts, or automations.
  https://www.volcengine.com/docs/82379/1520757
