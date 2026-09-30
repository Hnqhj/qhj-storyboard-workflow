---
name: ai-short-drama-storyboard
description: 短剧专项旧版：连续性圣经、关键帧图像提示词、Mambo V1.6 工程格式、仙侠年代场景契约，或分别索要 VIDEO_PROMPT、AUDIO_PLAN、NEGATIVE_PROMPT 时使用。普通剧本转镜头组不要调用。 Legacy/specialized short-drama development skill for explicit continuity-bible, keyframe-image prompt, Mambo V1.6 engineering format, xianxia period-scene contract, or separate VIDEO_PROMPT/AUDIO_PLAN/NEGATIVE_PROMPT requests. Do not invoke for ordinary script-to-camera-group prompts; script-camera-group-router plus narrative-camera-groups owns that workflow.
disable-model-invocation: true
---

# AI 真人短剧分镜

## User-Calibrated Camera-Group Override

For plot/script-to-AI-video prompt delivery, use `$narrative-camera-groups` as the final packaging owner. Treat each shot as a storyboard design unit, not automatically as a separate generation request. **Group by scene continuity first:** consecutive shots in the same location, time, blocking geography, and uninterrupted action/dialogue line form one camera group by default, even when the scene contains several reveals or dialogue turns. Use 14-28 seconds when possible and never exceed 30 seconds per generation unit; if a continuous scene exceeds a model limit, use generation segments under the same parent scene group where supported. Open a new camera group only for a scene/location change, meaningful time jump, deliberate closed handoff, or verified platform constraint. Show a timed shot table only for human understanding, then write one complete self-contained prompt per group. Inside that prompt, restate every shot in concrete prose; never paste or reference the table. This override remains active for Seedance 2.5/2.0 and Mambo packaging unless the user explicitly requests a different front-stage format for the current task.

把剧本转成可拍、可生成、可复用的镜头计划。先锁定连续性，再设计镜头，最后按目标模型组装提示词；不要把整段剧本直接改写成一条超长提示词。

## 工作原则

### 平台角色句柄（强制）

- 用户已在平台上传角色五视图时，所有生成提示词中的角色名必须加 `@`，使用平台中的精确角色句柄，例如 `@苏凌月`、`@苏建国`、`@刘大龙`。
- `@角色名`必须贯穿角色/资产锁定、事件节拍、对白说话者、声音说明和正向稳定约束；同一提示词内不混用裸角色名与带 `@` 的角色名。
- 剧本中每个可区分的人物都视为独立平台角色句柄，包括群体或临时角色；例如“黑衣小弟甲/乙”分别写成 `@黑衣小弟甲`、`@黑衣小弟乙`。不得把两个已上传五视图的角色合并成一个句柄。
- 与剧本同时提供的参考素材在模型提示词中使用 `@实际图片名`、`@实际视频名`、`@实际音频名` 及其职责说明；角色五视图仍使用 `@角色名`。首次出现写成 `@实际上传文件名（职责说明）`。`{{Image N}}`等编号仅作后台映射，不得用编号替代图片名、擅自改名或把参考素材替换成 `@角色名`。
- 镜头表是理解用信息，可使用普通角色名；完整可复制提示词内的每一个角色称谓都必须带 `@`。

- 把每个镜头视为独立定时的分镜设计单元；时长由动作、台词、反应和停留决定，不按等长模板机械分配。同一场景的连续镜头默认编入一个场景镜头组，14–28秒仅作为生成时长建议；每镜只保留一个主要可见变化。
- 建立不可漂移的角色 ID、服装、发型、年龄段、道具、场景 ID、时间、天气和主光方向；同时锁定人物关系资产：屏幕左右、共同朝向、相互距离、共享支撑物和说话者/倾听者职责。后续镜头只引用这些 ID 与关系锚点并补充本镜变化。
- 默认真人实拍、竖屏9:16；剧本转镜头组先按场景连续性分组，14-28秒为建议范围，单个生成段不超过30秒；单镜通常1-4秒，独立短镜时长以用户要求为准。生成模式由用户指定或按Seedance当前素材条件判定，不预设“6秒”或固定图生视频模式。
- 视觉提示词描述可见事实：人物、动作、位置、景别、镜头运动、光线、材质、环境和情绪。不要只堆 cinematic、电影感、8K 等空泛形容词。
- 一镜内避免无必要的换景、时间跳跃、多人复杂交互、长对白和大段屏幕文字。对白、旁白和字幕放在音频/后期字段，不塞进画面提示词。
- 使用真实人物外观时只描述虚构角色；不要要求未经授权的公众人物肖像或可识别真人复制。

## 决策优先级与输出密度

- 优先级固定为：剧本事实/原台词 → 用户明确禁用项与参考图 → 人物、场景、道具连续性 → 动作与情绪可生成性 → 摄影风格与装饰性细节。
- 参考图只锁定它实际提供的内容：场景图锁空间和光线，人物图锁脸、发型与服装；没有提供的角色不要擅自复制参考人物。用户要求“开头不使用参考图”时，只提取文字设定，不沿用参考图站位。
- 每镜先确定唯一视觉任务，再写提示词。动作镜头按“触发 → 发力 → 路径 → 接触/位移 → 受力结果 → 末帧”组织；高速或特效动作必须写出启动和中间过程，不能用“瞬移、突然出现、金光一闪”代替过程。
- 分镜描述必须尽可能具体且可执行：逐镜写清首帧姿态、重心与支撑、触发动作、连续运动路径、接触/受力反馈、呼吸与视线、衣料/发丝/道具的次级运动、台词节拍和末帧状态；不使用只写“走过去、看着、说话、挥手”的空泛动词。
- 人物表演与动作必须自然流动：保留预备、发力、减速、惯性、收势和反应的时间差，动作之间不能瞬间切换或关节突然定格；说话时让换气、口型、下颌、眼神、肩背和手部动作彼此错开并服务语义，禁止木偶式站定、机械点头、同步转头、连续重复同一手势或无理由改变姿态。
- 剧情转分镜提示词一律采用 `$narrative-camera-groups` 的完整交付格式：理解用镜头表在代码块外，每个**场景镜头组**各有一份可独立复制、独立生成的完整提示词。同一场景内的多个镜头必须合并在同一组，不得按剧情节拍、台词句数或景别变化擅自新建镜头组。不得输出“紧凑版”“压缩版”“精简版”或省略重复字段；只有确有多个场景组时，才逐组完整重写主题、时长、参考图、连续性、分镜、声音和约束。
- 负面词按身份、人体、摄影、文字和风格分层，只保留当前镜头会失败的约束；不要机械复制一整套与本镜无关的负面词。

## 导演化设计规则

- 短剧节奏硬约束：每个镜头组都要尽早给出可见钩子或冲突压力，优先在前1–2秒让观众看到威胁、关系失衡、异常动作或关键反应；中段必须出现一次升级、阻断、反转或权力变化，组末必须留下明确后果/新状态。删去不改变信息、关系或行动的中性铺垫和重复空镜。
- 场景卡至少锁定时间、空间布局、前景/中景/背景纵深、两件可重复背景物、天气和主光方向；色号仅在需要严格统一色彩时使用，不作为每镜硬性字段。
- 情绪用可拍信号呈现：视线目标、呼吸、停顿、下颌、肩背、手指、重心和距离。情绪要有起始、触发、升级和组末落点，不能全程同一强度。
- 对话场先确定共同活动和关系姿态，再分配微动作。说话者用视线、换气或已有道具承载语义；倾听者用延迟呼吸、手部停顿、重心或一次克制回应接住台词。避免双方同时转头、同时吸烟、同时点头或每句都换姿势。
- 真人表演基础优先调用 `$live-action-performance-direction`：先确定给定情境、当下目标、可玩行动、聆听方式、潜台词和身体重心，再把结果写入台词与动作镜头；情绪弧线和强度递进再调用 `$emotional-performance-direction`，不要用抽象情绪词代替可见行为。
- 短剧对白采用“反应驱动覆盖”而不是机械的“说话者覆盖”，但不强制每句切反应：先判断台词字数、语义完整度、冲突等级和同场角色数量。过短的回应、命令、语气词或无需他人接收的信息，可在同一镜头内完成；只有当反应能新增信息、改变关系/权力、暴露听者策略、推动下一动作或制造悬念时，才切给主要听者、次级见证者或道具/空间后果。高冲突台词通常需要反应覆盖，但若台词极短且反应无法形成信息增量，也保持连续镜头。
- 反应覆盖采用弹性分配而非固定比例：短句优先同镜完成，中等或含关系转折的台词安排一类有效反应，长句、威胁、羞辱、反转、权力宣告和动作指令按需要安排一至两类反应。反应可以是独立镜头、同镜前后景、声音先行后切或群体/道具后果；切镜依据反应落点、权力变化、视线转移、动作中断或信息揭示，不按每句台词机械切换。
- For two-person romance, confrontation, argument, confession, reconciliation, breakup, farewell, or explicit 正反打 requests, use `$relationship-dialogue-direction` before prompt packaging. It owns the relationship contract, performance relay, axis-aware coverage, and shot handoff; this Skill owns the short-drama continuity bible and shot design, while `$narrative-camera-groups` owns final group packaging.
- 一镜只写一种主要运镜；固定机位不是全局禁令。用户授权动态动作时，可使用跟拍、甩镜、环绕或速度变化，但每个连续镜头仍只保留一个主运动，改变机位就拆成相邻镜头。
- 每镜在后台按“承接首帧 → 本镜可见变化 → 结束状态 → 下一镜承接信号”设计。承接信号只选最清楚的一项：动作/手部状态、视线、道具、同方向背景运动、声音、遮挡或光线；后镜开头必须明确接住，不得只因想换景别而切镜。
- 特写使用必须克制：默认以全景/中景/近景完成空间、关系、走位和常规对白，特写只在强烈动作、装逼/能力展示、关键受力、决定性眼神或不可替代的道具证据等明确峰值使用；连续特写或无信息的人脸特写一律删掉。表现人物位置转变、逼近、后退、落地、换位和复杂调度时，优先切全景或中景让路线与距离可读。所有推镜头原则上推向人物上半身、手部、道具或关系构图，不直接推到人脸；近景默认保持腰部以上并保留肩背、手势、视线或对手关系，不做纯脸部占满画面。
- 视觉风格优先写具体材质如何响应环境：皮肤、衣料、金属、混凝土、积水、烟雾分别怎样受主光、风、湿度和运动影响。锁定风向、水迹、烟雾、移动灯光等环境状态，不用单纯堆“高级、电影感、氛围感”。
- 特效按“来源 → 形态 → 运动路径 → 与人物/环境互动 → 衰减方式”描述。例如灵力应写清从何处产生、如何流动、怎样影响衣物/空气、何时减弱；不要只写“高级特效、金光粒子”。
- 台词语速统一约束：普通对白控制在每秒 2.8–3.2 个汉字，平均按 3 个汉字/秒估算；低声、克制或情绪化语气控制在每秒 2–3 个汉字，平均按 2.5 个汉字/秒估算。急促争执或短促命令可短暂提高到每秒 3.5–4 个汉字，但不得连续长句使用；快节奏通过剪辑、动作密度和声画承接实现，不通过抢读台词实现。VO 标明“嘴唇紧闭/不动”；超过镜头可承载时，拆分台词、改为后期配音或明确跨镜延续，不抢读原文。
- 声音只按“人物台词/可见呼吸 → 动作与材质拟声 → 必要静默”设计；允许脚步、衣料、手部、武器、撞击、碎裂、身体接触和墙地反应等有明确物理来源的声音。所有视频禁止背景音乐、配乐、BGM、环境氛围铺底、风铃、紧张低频、情绪音垫、悬疑提示音和任何只表达情绪/氛围的音效。
- 先用正向稳定约束说明必须保持什么，再补少量负面词：例如“同一护栏、左/右关系、共同朝向、烟雾风向保持连续”。不要只靠“禁止变化、禁止穿帮”让模型猜不变项。

具体的九模块映射、动作特效句式、参考图策略和质量检查见 `references/video-methodology-distilled.md`。

## 工作流

### 1. 读取与补全输入

提取题材、集数/片段、地点、时间、人物、台词、情绪转折、关键道具和结尾钩子。信息缺失时先列出假设，再继续产出，不要凭空增加改变剧情的事实。只在会影响镜头结果时追问：目标视频模型、画幅/时长、是否有角色参考图、对白是否由模型生成、是否需要口型同步。

### 1.5 创意对齐闸门（新剧本默认必做）

用户第一次提供新剧本、剧情段落或全新场景时，先检查参考素材完整性，再给出恰好三套针对本剧情的分镜概念和一套导演推荐；在概念确认前不输出正式镜头表或完整镜头组提示词。三套概念必须分别说明镜头结构、摄影/运镜、短剧节奏、动作/特效/表演重点、Seedance生成风险和适用原因。用户明确说“直接生成、不要问、按你推荐、沿用上一段”，或已经锁定镜头顺序/景别/运镜/时长/特效/参考图用法时，跳过等待并执行推荐路线。

素材完整性检查至少包含：每个角色的身份/五视图、服装与状态、场景布局、关键道具/武器、动作或特效依据、连续性首尾状态、音频/节拍需求。缺失内容按P0/P1/P2列出，并说明会影响身份、站位、动作、特效、节奏还是仅影响装饰。P0缺失时可给临时概念，但不得把临时假设伪装成已锁定事实。

以下情况跳过创意对齐闸门并直接执行：用户明确说“直接生成、不要问、按你推荐、沿用上一段”；用户已经给出镜头顺序、景别、运镜、时长、特效和参考图用法且无关键歧义；或当前请求只是修改已确认方案中的一个局部字段。

维护当前项目的偏好账本：目标模型、画幅、镜头节奏、常用景别、运镜倾向、特效强度/色彩、参考图作用、对白方式和提示词长度。后续场景沿用已确认偏好，只询问本场新增或冲突的决策，不重复提问。

### 2. 结构化剧本

在创意对齐闸门完成或被明确跳过后，输出一句话 logline、起承转合 beat、每个 beat 的戏剧目的和可见行为。把内心独白改写成可观察的眼神、停顿、手部动作、走位或道具动作；没有可见行为的台词单独标为 VO/字幕。

### 3. 建立连续性圣经

为每个角色创建 `C01` 之类的稳定 ID：年龄段、肤色/脸型、发型、服装、鞋、饰品、性格外化动作、说话节奏和禁变项。为每个地点创建 `L01`：空间布局、关键背景、主光方向、色温、天气和可重复道具。另建简短关系资产：谁在画面哪侧、面向哪里、彼此距离、共享支撑物/活动、谁主动谁回应。每镜标明角色 ID、地点 ID、入画/出画方向、视线目标、道具状态和环境状态。

### 4. 拆解镜头

按戏剧信息而不是按句号机械切镜。台词切镜优先让人物说完整一句或自然半句，在语义落点、停顿、换气或对方开始接收时切换，避免在一个词的中间截断；这只是参考而非铁律。若突发动作、冲击、危险、反应抢拍或信息揭示必须提前切，可在声音桥中保留台词连续性，并确保观众能听清完整词义。不要机械套用“建立镜头 → 轮流特写 → 空镜收尾”；先确定观众本镜新看到什么，再选择主景别（远景、全景、中景、近景、特写、过肩）和一个主要运镜（固定、推、拉、横移、跟拍、手持、摇镜）。每次切镜必须同时记录前镜结束状态、后镜首帧和承接信号；没有新信息或可验证承接价值的镜头合并或删除。

### 5. 组装提示词

先生成角色/场景基底，再拼接本镜头的动作和摄影参数。分别输出：

1. `KEYFRAME_PROMPT`：用于生图或首帧，写静态构图和瞬间姿态。
2. `VIDEO_PROMPT`：用于文生视频或图生视频，写单一连续动作、运镜、时长和结束状态。
3. `AUDIO_PLAN`：人物台词、口型/语气、纯拟声音效、静默节点和字幕建议；明确写“无任何音乐和情绪/氛围音效”。
4. `NEGATIVE_PROMPT`：只放会破坏结果的约束，不堆互相冲突的风格词。

根据模型能力调整：图生视频只写相对首帧的变化；文生视频补齐人物与场景基底；支持原生音频的模型才在视频提示词中写短对白，否则把对白留在 `AUDIO_PLAN`。

### 6. 交付前检查

检查角色外观、服装、道具、屏幕方向、视线、关系锚点、光线、风向、水迹、烟雾和背景移动是否跨镜一致；检查每镜是否只有一个主要变化、台词与微动作是否逐段对齐、说话者之外是否有有效听者/旁观者反应、反应是否改变关系或信息、时长是否可生成；逐对检查“前镜末帧 = 后镜首帧”或承接信号明确成立；检查提示词是否误含水印、logo、字幕或未授权真人。发现风险时给出“风险与替代镜头”，不要默默改剧情。
- 影视级摄影检查：每个主要镜头是否写明机位/视高/角度、焦段或镜头视角、光圈/景深/对焦主体、主辅轮廓光或实景光源、方向、软硬、色温、阴影/反射与曝光行为；这些参数是否服务空间、关系、动作或情绪信息，而不是空泛堆砌。

### 6.1 反馈驱动的修订

- 用户只修改景别、运镜、时长、特效、参考图或输出长度时，只重写受影响镜头，保留其他已确认连续性。
- 用户已经选择过镜头结构、摄影策略或特效强度时，把选择写入偏好账本；除非新剧本与原选择冲突，否则不要再次询问。
- 用户反馈“像瞬移/过程太少”时，增加可见的预备、加速、路径和中段反馈；用户反馈“拖尾难看”时，改为具体的光流、粒子、空气折射或局部曝光轨迹，并禁止完整人形复制。
- 用户反馈“穿帮”时，先检查空间轴线、人物左右、手持物、服装和动作首末帧，再决定是否补一个最小连接镜头。

## 默认交付格式

创意方向未确认时只输出素材完整性检查与三套分镜概念，不输出下列正式交付。确认后，除非用户另有要求，按以下顺序输出：

1. **制作假设**：只列会影响生成结果的模型、画幅、时长、参考图和音频假设。
2. **剧本拆解**：需要时输出 logline/beat；短提示词请求可省略。
3. **连续性圣经**：角色、场景、道具和色彩规则，固定项与变化项分开。
4. **分镜表/提示词**：剧本转视频统一使用 `$narrative-camera-groups` 的“场景连续性优先 + 组内多镜头 + 人类理解用镜头表 + 每场景组独立完整提示词”；14-28秒仅为建议时长。只有用户明确只要单镜、关键帧或短测试时，才使用 `KEYFRAME_PROMPT`、`VIDEO_PROMPT`、`AUDIO_PLAN` 等单镜格式。
5. **测试与风险**：复杂动作优先给 3–5 个连续镜头或最小测试包，并指出最可能失败的连接点。

普通请求若用户要求“完整、精细、电影化导演稿”，可把连续性圣经和分镜前置为五段式：`角色/资产锁定`、`视觉材质总控`、`事件节拍`、`声音`、`正向稳定约束`。五段内容必须服务后续镜头，不得变成空泛风格说明；用户要求 Seedance/曼波 V1.6 时，将它们编译进既有组级前置、【角色状态】、构图/内容描述、人物动作和声音字段，不额外新增前台区块。

## 提示词模板

将方括号字段替换为具体内容，不要原样输出占位符：

```text
KEYFRAME_PROMPT
[FORMAT], photorealistic live-action short drama, [SHOT_SIZE] of [CHARACTER_ID] in [LOCATION_ID],
[age/face/hair/wardrobe from character bible], [static pose and visible emotion],
[foreground/midground/background layout], [relationship anchor and sightline], [lens and camera height],
[light direction and color temperature], [specific material response and production design], clean frame, no text, no logo, no watermark.

VIDEO_PROMPT
[FORMAT], single continuous [DURATION]-second shot. Start from the supplied keyframe.
[CHARACTER_ID] starts in [START_STATE] and performs one clear action: [ACTION], while [PERFORMANCE_BEAT or small secondary reaction].
Camera [CAMERA_MOVE] at [SPEED], [FOCUS_BEHAVIOR], preserve the same face, hair, wardrobe, prop state and screen direction.
Keep [POSITIVE_CONTINUITY_CONSTRAINTS] and the same wind/smoke/light/material direction. End on [END_STATE]; the next cut is motivated by [BRIDGE_CUE]. Natural human motion, realistic hands and eye-lines, restrained acting.

AUDIO_PLAN
Dialogue: "[short line]" in [language], [voice/tempo/emotion]; listener response: [physical breath/hand/eye-line or none]. Foley: [source-coupled action/material sounds only]. Silence: [intentional gap if useful]. Audio rule: dialogue plus pure foley only, no music, no ambience bed, no emotional or mood effects.

NEGATIVE_PROMPT
anime, cartoon, illustration, 3d render, plastic skin, beauty filter, face morphing, identity drift,
extra fingers, extra limbs, broken hands, duplicated people, unnatural lip sync, floating props,
warped text, subtitles, watermark, logo, abrupt scene change, jump cut, overacting, flicker, blur.
```

## 模型适配速查

- **图生视频**：依赖首帧和角色参考图；`VIDEO_PROMPT` 以“从当前画面开始 + 一个动作 + 结束状态”为主，避免重复长外观描述。
- **文生视频**：把连续性圣经中的人物和地点摘要放在 `VIDEO_PROMPT` 前半段，再写景别、动作、运镜和音频；在 `$narrative-camera-groups` 工作流中，一条完整提示词生成一个包含多个连续镜头的镜头组。
- **生图/关键帧**：去掉时间词、运镜词和复杂对白，强调瞬间姿态、构图、光线和可见道具；优先生成同一角色的正面、侧面和表情参考。
- **竖屏短剧**：人物脸部和手部尽量落在中上部安全区，给字幕留底部空间；需要聊天界面时用“无可读文字的手机屏幕”，后期叠字。

## Seedance 2.5 / 曼波 V1.6 模式

当用户提到 `Seedance 2.5`、`Seedance`、`曼波`、`V1.6`、`30 秒生成分组`，或要求按其工程格式输出时，必须先完整读取 `references/mambo-v1.6-seedance.md`，再设计和输出。该参考文件控制平台字段与编译方式；`$narrative-camera-groups` 继续控制用户可见的镜头组时长、理解用镜头表与每组完整提示词，除非用户本次明确要求改用曼波前台格式。

执行该模式时：

- 新剧本仍先执行创意对齐闸门；只有用户明确要求直接生成或已经锁定导演方案时，才直接进入曼波时间轴编译。
- 字符级锁定原台词、标点和顺序，不翻译、不润色、不纠错；OS 必须按原文标记。
- 先完成导演分镜和逐镜独立定时，再按场景连续性形成镜头组；同场景优先保持一个组，不得为了凑满 30 秒跨场景拼接或添加空镜。只有平台限制才可把同一场景拆成连续生成段，并保留同一场景 ID和首尾状态。
- 使用连续绝对时间窗 `第 X—Y 秒（Z秒）`；硬切必须拆成相邻分镜，并在后镜内容开头写 `【第 X 秒硬切】`。
- 维护人物状态账本、空间站位、轴线、左右手、服装、道具和动作首末帧；后镜首帧必须承接前镜末帧。
- 用户本次明确要求曼波 V1.1 原生前台格式时，只输出参考文件第 7 节规定的单一 Markdown 代码框；其他剧情转分镜提示词继续使用 `$narrative-camera-groups` 的镜头表加每组完整提示词格式。
- 任何情况下禁止眼睛发光、瞳孔发亮或光束眼；用正常瞳孔、自然反光和可见表演表达情绪。

## 参考资料

需要更细的风格词或模型差异时，按需读取 `references/prompt-library.md`；需要固定分镜字段、示例和 QA 清单时，读取 `references/storyboard-schema.md`；需要设计用户选择题、执行偏好账本，或将用户方法论文档应用到场景、情绪、台词和特效设计时，读取 `references/video-methodology-distilled.md`；需要 Seedance 2.5 的曼波 V1.6 完整执行协议时，读取 `references/mambo-v1.6-seedance.md`。参考资料中的示例可直接测试，不等同于任何平台的保证参数。

这些参考资料属于通用方法或测试素材；进入 Liu 真人短剧正式交付时，始终回到 `liu-short-drama-contract.md` 和 `short-drama-director-stack.md`，不得把参考库中的音乐、氛围声或短时长示例带入最终提示词。

For model-neutral Chinese historical drama or xianxia multi-shot work, read `references/xianxia-period-scene-contract.md` before building the continuity bible. Preserve its world, costume, prop, location, and power rules across keyframes and video clips.
