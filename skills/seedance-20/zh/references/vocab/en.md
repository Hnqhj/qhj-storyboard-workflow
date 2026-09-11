# 英语词汇表

本参考用于精确的英语 Seedance 提示词措辞。英语是默认的提示语言，也是审核最严格的平台，它会同时以两种方式失败：空洞的质量词（"cinematic, stunning, 8K"）添加零信号，而模糊的、近似威胁的措辞会触发误报过滤。精确性同时修复两者——具体的制作英语对模型与过滤器都读起来更好。保持参考标签不变：`[Image1]`、`[Video1]` 与 `[Audio1]` 保持字面原样。

| 功能 | 英语措辞 | 它决定了什么 |
|---|---|---|
| 角色 | `[Image1] is the first frame` | 锁定开场构图 |
| 角色 | `[Image2] is the last frame` | 设定最终视觉目标 |
| 角色 | `[Image1] locks character identity` | 面孔、发型与服装保持稳定 |
| 角色 | `[Video1] controls camera movement only` | 运动供体，无外观迁移 |
| 角色 | `[Video1] controls action rhythm only` | 节奏供体，不迁移其他内容 |
| 角色 | `[Audio1] controls tempo and mood only` | 剪辑的时钟，而非其内容 |
| 首尾帧 | `keep the first frame unchanged` | 锚定开场状态 |
| 首尾帧 | `treat the last frame as the final visual target` | 端点，而非氛围参考 |
| 首尾帧 | `one continuous motion, no jump cut` | 强制单一过渡路径 |
| 首尾帧 | `preserve the same character, wardrobe, and layout` | 跨帧连续性锁定 |
| 镜头 | `slow push-in` | 替代 "cinematic zoom" |
| 镜头 | `pull back to reveal the space` | 有动机的揭示，而非 "epic wide" |
| 镜头 | `stable lateral tracking` | 干净的横向移动 |
| 镜头 | `locked medium shot` | 面孔与对白的稳定性 |
| 镜头 | `macro close-up` | 材质与产品细节 |
| 镜头 | `low-angle shot` | 不用 "epic" 一词的气势 |
| 镜头 | `over-the-shoulder shot` | 对话几何关系 |
| 镜头 | `handheld with slight breathing sway` | 受控的纪录片能量 |
| 景别 | `medium close-up` | 带语境的情绪 |
| 景别 | `wide establishing shot` | 先有场地后有人 |
| 景别 | `three-quarter profile` | 有立体感的面部角度 |
| 镜头规格 | `24mm wide spatial feel` | 空间与语境 |
| 镜头规格 | `50mm natural portrait perspective` | 真实的面孔 |
| 镜头规格 | `macro lens on material detail` | 以质感为主体 |
| 光照 | `soft backlight` | 无发光词汇的分离 |
| 光照 | `warm practical light from the left` | 有源、有方向的暖色 |
| 光照 | `cool moonlight rim` | 不用 "moody" 的夜间轮廓 |
| 光照 | `volumetric light through thin mist` | 可见光束，物理成因 |
| 光照 | `wet asphalt reflecting neon` | 反射即光源 |
| 运动 | `fog parts around the footsteps` | 环境对主体作出反应 |
| 运动 | `droplets merge and slide down the label` | 产品运动，物理化 |
| 运动 | `a slow head turn that stops` | 有端点的表演节拍 |
| 运动 | `fabric settles after the gesture` | 收尾动作证明该运动 |
| VFX | `gold particles rise, catch the backlight, and dissipate` | 源头、路径、端点 |
| VFX | `thin electrical arcs crawl along the cable` | 效果锚定到一个物体 |
| VFX | `cold vapor rolls over the rim and sinks` | 密度与方向 |
| 音频 | `quiet room tone` | 有存在感的静音 |
| 音频 | `one clear spoken line in quotes` | 唇音同步能承载的对白 |
| 音频 | `a single soft metallic tick` | 一个声音，一个事件 |
| 音频 | `no music until after the line` | 直白陈述的混音优先级 |
| 音频 | `distant traffic bed under rain` | 分层环境声，无废话 |
| 文字 | `no on-screen text, no watermark` | 文字属于后期 |
| 剪辑 | `match cut on the circular shape` | 命名的转场，而非 "cool" |
| 剪辑 | `hard cut on the downbeat` | 剪辑绑定到声音 |
| 约束 | `keep the logo, label, and shape unchanged` | 产品身份锁定 |
| 约束 | `no identity change, no object redesign` | 漂移防护 |
| 约束 | `one action, one camera move` | 六个词的预算规则 |
| 约束 | `nothing else moves` | 隔离主体运动 |
| 安全 | `staged confrontation, no graphic injury` | 不带伤害解读的动作 |
| 安全 | `original character with broad archetype traits` | 不带相似性的身份 |
| 安全 | `prop object handled safely` | 不带威胁解读的物体 |

## 废话陷阱

英语提示词会招来空洞的评价词。每个都增加 token 且零信号；用相机、麦克风、测光表或秒表能检测到的东西替换它们。

| 废话 | 改说 |
|---|---|
| cinematic | 写明景别、运镜与光源 |
| epic | 物理规模：人群数量、镜头距离、结构高度 |
| stunning / breathtaking | 那一个为之加分的可见对比或揭示 |
| beautiful | 颜色、质感、材质、光的行为 |
| masterpiece / award-winning | 删除；质量不是一个请求 |
| 8K / ultra-HD / hyper-detailed | 删除；分辨率是渲染设置，不是散文 |
| dynamic | 具体的运动、其速度与其端点 |
| dramatic | 站位、阴影、静默或镜头压迫 |
| atmosphere of mystery | 什么被隐藏、被什么隐藏：门口、阴影、雾 |
| ultra-realistic | 材质行为、皮肤质感、自然运动 |
| insanely detailed | 那两个重要的、被命名的细节 |
| trending / viral style | 实际格式：竖屏、快速钩子、字幕安全取景 |

## 过滤器误触修复

英语承载最重的审核。仅对被误解的安全提示词使用此项——修复在于清晰，而非规避。真正被禁止的内容会通过 filter skill 路由到直白的拒绝。

| 易触发的英语 | 专业澄清 |
|---|---|
| shoot the scene / shooting | film the scene, capture the take |
| kill the lights | cut the lights to black |
| gun it / shot after shot | accelerate hard / take after take |
| execution of the move | the move performed cleanly |
| dead silence | held silence, room tone only |
| blow up the image | enlarge the image to full frame |
| fight breaks out | choreographed action beat begins, no graphic injury |

任何真正有风险的内容——未成年人、真人相似性、性或图像化内容——都不是措辞问题；将其路由到 filter skill 的边界以获得直白的拒绝。

加载 `filter-vocab.md` 获取完整的误报修复表，加载 `anti-slop-lexicon.md` 获取核心替换规则。
