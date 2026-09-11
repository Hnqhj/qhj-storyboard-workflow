# Output Templates

## User-Calibrated Narrative Prompt Override

When `$narrative-camera-groups` is active, its delivery contract overrides the generic AI-video and Seedance segment templates below. Use this reference only to supply storyboard fields. The final visible package must use approximately 20-second groups, a human-only timed shot table outside the paste target, and one complete self-contained prompt per group that restates every shot in prose. Platform limits may force a different duration only when the active surface is known and the user has not explicitly chosen the approximately 20-second workflow.

## Professional Storyboard Table

```text
分镜模式：
视听目标：
信息梯：
空间锁定：
节奏曲线：

| # | 时长 | 功能 | 画面/构图 | 景别/机位 | 动作 | 运镜 | 转场/声音 | 张力机制 | AI注意 |
|---|---:|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |  |
```

Use this when the user wants a complete storyboard or production-style answer.

## High-Tension Beat Board

```text
高张力策略：
- 张力来源：
- 主导视线：
- 视觉压力曲线：
- 禁止堆叠：

Beat 1:
功能：
画面：
镜头：
动作：
剪辑/声音：
为什么有张力：

Beat 2:
...
```

Use this when the user wants cinematic pressure and a richer explanation.

## AI Video Prompt Storyboard

```text
全局锁定：
空间/轴线：
节奏：
生成可执行性：
- 单段/拆段：
- 输入图/参考图职责：
- 每段动作负载：
- 主导运镜：
- 负面策略：

分镜提示：
1. ...
2. ...

连续性锁定：
负面约束：
```

Keep language paste-ready. Put negative constraints in the same block if the user needs one-copy generation.

For image-to-video, treat the input image as the first-frame visual anchor. Do not rebuild identity, costume, layout, or style from scratch; specify only the motion, camera change, expression/prop/environment response, and the locks that must remain unchanged.

Use platform-aware negative strategy:

- if the platform supports a separate negative prompt, keep it short and concrete;
- if the platform has weak or no negative-prompt support, rewrite failure constraints as positive locks inside the main prompt;
- avoid making unsupported "no/don't" instructions the only guardrail for identity, layout, camera, or subject count.

Use segment-aware packaging:

- keep one generated segment when the beat has one location, one time state, one subject/action focus, one dominant camera move, and the target duration can carry it;
- use continuous extension when the same scene should keep moving forward and the end frame can naturally become the next segment's start;
- use a hard cut or separate prompt when location, time, lighting logic, axis/viewpoint, reference role, character group, or action phase changes;
- split before the prompt contains multiple scene changes, competing subject actions, style shifts, or more camera moves than the platform can reliably execute;
- for every split, write a handoff: previous end state, next first-frame anchor, what must remain locked, what is allowed to change, and the cut reason.

## Seedance Storyboard-To-Prompt Handoff

```text
目标：
目标平台/素材句柄：
总时长与画幅：
素材职责：
- {{Image 1}}:
- {{Video 1}}:
- {{Audio 1}}:

拆段：
| Segment | Source shots | Est. duration | One action spine | Camera owner | Handoff state |
|---|---|---:|---|---|---|

【完整可复制提示词 - Segment A】
[visual/style/material lock]
[asset roles]
[continuous shot paragraph(s): composition + camera + action/dialogue + sound]
[targeted constraints]
```

Use this when the user asks to turn storyboard/shot list into Seedance-ready prompts. If the active target expects `@图片N` syntax, map the asset handles to that dialect; otherwise keep Liu's local `{{Image 1}} / {{Video 1}} / {{Audio 1}}` format.

Rules:

- Keep each generated segment around 4-15 seconds for the generic Seedance handoff. When `$narrative-camera-groups` is active, use its 18-24 second default and 30-second hard ceiling unless a verified platform limit requires otherwise.
- One segment needs one main action spine and one dominant camera behavior.
- Preserve whole dialogue lines inside one segment.
- Use a handoff state for every split.
- Put planning notes outside the copyable prompt block.
- Do not use `@material[...]` in Liu's local final prompt unless the user explicitly targets that syntax.

## Product / Prop Ad Storyboard

```text
产品/道具广告分镜策略：
- 目标动作：认知 / 考虑 / 转化 / 记忆
- 使用情境：谁在什么压力、愿望或任务下需要它
- 产品识别：前3秒或首组镜头如何出现产品、品牌或关键轮廓
- 尺度与手部关系：尺寸、佩戴、握持、安装、触感
- 材质/机制证明：纹理、工艺、按钮、开合、变形、性能反馈
- 结果/记忆帧：使用后改变了什么，最后留下哪一帧
- CTA/收束：要观众理解、记住或执行什么

| # | 时长 | 功能 | 画面证据 | 产品信息 | 人/手/环境关系 | 镜头/光线 | 声音/文案 | AI注意 |
|---|---:|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |
```

Use this when the user asks for product, prop, brand, commercial, ecommerce, launch, feature-demo, or object-centered storyboard work.

Rules:

- Lead with need/context or early product recognition; do not hide the product behind abstract beauty shots unless mystery is the stated concept.
- Every beauty shot must prove at least one concrete point: scale, material, mechanism, use, benefit, comparison, or memory.
- Include human/use relation when size, comfort, credibility, or conversion matters.
- For platform ads, add aspect ratio, safe-zone, first-3-second hook, audio/text reinforcement, and CTA notes.
- Keep this as a normal storyboard mode unless the product concept explicitly requires danger, speed, pursuit, or conflict.

## Fight / Action Line Storyboard

```text
打戏分镜策略:
- 人物姿态契约: 谁的姿态代表什么性格/价值冲突
- 形状对比: 方/圆/三角/折叠/舒展/重心/节奏差异
- 动态线载体: 身体 / 兵器 / 服装 / 人群 / 场景结构 / 运镜透视
- 动作短句: 蓄势 -> 动线 -> 接触/擦过 -> 受力反应 -> 余势/改位
- 场面递进: 单人线 -> 兵器线 -> 脊柱/服装线 -> 人群线 -> 空间透视线 -> 运镜线

| # | 时长 | 功能 | 姿态/角色信息 | 主导动态线 | 画面/构图 | 动作与受力结果 | 运镜/剪辑 | 场面线条 | AI注意 |
|---|---:|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |  |
```

Use this when the user asks for 打戏分镜, 武打, 动作分镜, 近身格斗, 兵器战, action-PV, or a fight sequence where posture, force path, and line-based scene scale matter.

Rules:

- Start from character posture and shape contrast before adding big camera moves.
- Give every action phrase one readable force line and one receiver/consequence.
- In `主导动态线`, never write only "强动态线" or "大动态"; write `载体 + 起点 -> 路径 -> 目标 -> 结果`.
- In `动作与受力结果`, name the physical cause chain: support foot / waist / shoulder / weapon / impact / recoil.
- Use full-body/full-weapon readability before fragmenting into close-ups.
- Escalate scene scale by organized line density, not by random crowd or constant shake.
- For AI video, keep each segment to one main action spine, one dominant camera behavior, and explicit silhouette/line locks.

## Diagnosis

```text
主要问题：
1. ...

需要重写的分镜层：
- 信息梯：
- 空间连续：
- 镜头变化：
- 张力机制：
- AI可执行性：

替换方案：
...
```

Use this when reviewing a storyboard, prompt, reference breakdown, or generated result.

## Reference Breakdown To Storyboard

```text
参考片整体语法：
- 场景功能：
- 空间/轴线：
- 景别与节奏曲线：
- 转场/声音逻辑：

可迁移机制：
1. ...

不可迁移风险：
- 原片角色/美术/情节不可直接复制：
- 不适合当前项目的镜头习惯：

改写后的分镜策略：
- 信息梯：
- 空间锁定：
- 张力或克制机制：
- AI可执行性：
```

Use this when turning a reference clip into a new storyboard. Do not extract isolated attractive shots before identifying the reference's whole-clip grammar. Transfer functions, spatial logic, rhythm, and transition mechanics; avoid copying scene-specific plot, composition, character business, or copyrighted visual arrangement.

## Micro Forward Tests

Use these during self-iteration or manual validation:

1. Quiet emotional scene:
   - "两个人在雨夜便利店分手，15秒，克制但有余震。"
2. High-tension action:
   - "单人持长枪穿过坍塌走廊，15秒，不要敌人，但要危险感。"
3. Product reveal:
   - "一款未来耳机的30秒广告分镜，要有材质和使用场景。"
4. AI video image-to-video:
   - "基于一张角色图做5秒图生视频，只能让角色微动作和镜头推进。"

Check whether the skill outputs shot function, spatial lock, rhythm curve, tension control, and negative constraints without overloading.
