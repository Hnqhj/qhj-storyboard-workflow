# 变更日志 — seedance-20

本项目所有值得记录的变更都记录于此。

当前有效发布版本：**6.1.0**。下方较旧的条目作为发布历史保留，并非有效的版本指引。

## 未发布（Unreleased）

_暂无未发布的变更。_

## [6.1.0] — 2026-06-22

### 新增

- 新增 `references/directing-engine.md`：位于镜头、灯光、运动与角色查找表之上的一层导演推理层。它读取一个场景的戏剧功能（功能、转折、视点、权力关系、潜台词），命名一个意图，并推导出单一而连贯的设置——镜头、焦段、灯光、调度、表演与声音全部强化那个意图，而不是堆叠泛泛的「电影感」描述词。
- 新增「导演嗓音（Director's Voice）」模型，包含六种 IP 安全的功能性风格原型，让一个项目保持统一而一致的导演手法；外加一条长篇视觉脊线，沿着相连片段推进尺度、运动、灯光与声音，并标记出在故事转折处打破既定模式的那个单一片段。
- 新增表演导演法：把情绪转化为每个节拍一个真实可见的动作，通过矛盾来演出潜台词；以及一项拒绝无动机技法的连贯性测试。
- 在导演引擎中新增 35 条类型化实战范例库，涵盖广告（产品、美妆、食品、汽车、高级时装、走秀、房地产、对镜陈述式推介）、表演与能量（音乐视频、运动、健身、旅行）、叙事与类型电影（亲密对白、双人戏、短剧、爱情、恐怖、黑色电影、动作、奇幻、科幻、怀旧）、动画与风格化（2D 动漫、3D/CG、定格、儿童）、观察式与真实（UGC、纪录片采访、自然/野生动物、宠物、定场）、以及技术类（变形/VFX、延时摄影）。每一条都是一份完整的「读场—意图—嗓音—设置—表演—编译提示词」推导，且各具独特的导演嗓音。
- 新增两个 eval 用例：`directing_scene_coherence` 与 `directorial_voice_across_sequence`。

### 变更

- 将导演引擎接入根技能的运行回路与加载映射，以及 `seedance-interview`、`seedance-interview-short`、`seedance-prompt`、`seedance-camera`、`seedance-lighting`、`seedance-motion`、`seedance-characters`、`seedance-sequence` 和 `seedance-continuation`，使场景导演、表演与统一的导演嗓音从访谈贯穿到提示词再到长篇续接。在序列片段卡中新增了 `arc_position` 字段。
- 将有效发布元数据、README 徽章、参考库、eval 元数据和验证器期望值提升到 v6.1.0（28 个子技能、57 个参考文档、114 个 eval 用例）。

### 自 v6.0.x 维护版延续

- 新增了对 EvoLink、OpenRouter、Kie.ai、PiAPI、LaoZhang、Runware、ModelsLab、AI/ML API、MuAPI、SeeGen 和 Segmind 的来源受限 provider/router 覆盖，同时仍将它们标记为第三方或 router 平台，而非官方 ByteDance 行为。
- 新增了一条面向中国大陆的 provider 搜索边界，将官方 ByteDance/Volcengine/BytePlus/Doubao/Jimeng/Jianying 平台，与不应在缺少 provider 自有文档的情况下被当作公开 API 提供方的工作流托管方、中文博客和业务伙伴新闻区分开来。
- 新增了来源受限的官方 Seedance 2.0 Mini 命名，包括 Volcengine 的 `doubao-seedance-2-0-mini-260615` 与 BytePlus 的 `dreamina-seedance-2-0-mini-260615` 平台 ID，以及「Seedance V2 Mini」的简称规则。
- 恢复了 Runway 专属于 Seedance 的 API 指南，使其与稳定的 Models、API Changelog、Inputs 和帮助链接一同成为一手来源，并对原始 HTTP 状态码不一致问题附加了检查器注意事项。

## [6.0.1] — 2026-06-20

### 新增

- 为中文、日文和韩文新增了完整的母语读者入口文档：`docs/README.zh.md`、`docs/README.ja.md` 和 `docs/README.ko.md`。
- 新增 `seedance-examples-ja` 和 `seedance-examples-ko`，让日文和韩文用户拥有有效的范例/改写技能，而不仅仅是词汇翻译。
- 在有效的中文、日文和韩文词汇参考中新增了 CJK 序列/续接、被接受素材、无文字本地化和安全改写短语。
- 为 CJK 首页、日文范例、韩文范例和本地化 CJK 续接行为新增了 eval 覆盖。

### 变更

- 将有效发布元数据、README 徽章、eval 元数据、验证器期望值和范例提示词版本提升到 v6.0.1。
- 收紧了 README 路由，使中文、日文和韩文读者从母语文档与有效技能起步，而不是从已迁移的遗留参考起步。

## [6.0.0] — 2026-06-20

历史性的 v6 序列编译器基础发布。

### 新增

- 新增有状态的序列架构：`seedance-sequence`、`seedance-continuation`、序列项目状态、续接交接、提示词编译器、平台提示词配置、参考迁移合同、事件密度、连续性 QC、密集分镜模式和故障图谱（failure atlas）参考。
- 为项目状态、片段合同、镜头复核、提示词规格和生成运行记录新增了 JSON schema。
- 新增了用于提示词检查、项目状态、连续性链、行为合同、序列 eval 和生成运行夹具的确定性本地验证器。
- 为机场续接、观察偏差、独立片段、紧凑 I2V、R2V 角色隔离、分阶段单镜头、密集 2D 分镜、序列续接、首/末帧过渡和单层视频编辑新增了「黄金范例（golden examples）」。
- 新增 47 个序列状态 eval 用例、生成基准夹具和 JSONL 生成运行示例。

### 变更

- 根路由现在会在模式关卡之前运行序列关卡，并要求在续接提示词之前先有被接受的来源素材或观察到的末态。
- 访谈、提示词、短提示词、排障、镜头、运动、角色、音频、灯光、风格和配方技能现在会在存在时继承序列状态、连续性锁、已完成节拍、预留的未来节拍和精确的参考标签。
- README、技能映射、参考库、验证命令、智能体兼容性说明、eval 评分细则、JSON schema 参考和 CI 工作流现在都反映 v6.0.0。
- README 引入了母语读者起步路径，从中文开始，链接进入有效的词汇与范例系统；完整的日文和韩文对等支持（母语文档与范例技能）在 v6.0.1 中跟进。
- 提示词预算指引改为按平台区分，而非把任意字符数当作普适标准。

## [5.5.2] — 2026-06-12

### 变更

- 深度校对发布。对每一个 markdown、脚本、矢量和数据文件扫查了拼写错误（90 词词表）、重复词、双句号、行尾空白、标点前空格、markdown 表格列数不匹配、YAML frontmatter 有效性和字体声明一致性。仓库中存在一个缺陷：运行图说明类上遗留的 font-weight 500——统一为 400，使全部三个矢量资源共享单一字重。
- 将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.5.2。

## [5.5.1] — 2026-06-12

### 新增

- 新增跨智能体兼容性矩阵：针对 Google Antigravity、OpenClaw（ClawHub 兼容）和 Hermes Agent 的已验证安装路径与路由；一条 Trae（ByteDance）提示；30 余个已报告兼容 ZH_REFERENCE.md 的客户端层级（Cline、Roo Code、Goose、Amp、OpenCode、Kiro、Qwen Code、Continue、Crush、Droid、OpenHands、Letta 等）；以及注册表/市场渠道说明，附带对未发布列表的「不得声称」规则。
- 将 README 安装表扩展到九个已验证目标，加上对每一个其他符合标准客户端的可移植形态规则。

### 变更

- 完善了首页字体系统：用于字标和运行图根部的高对比度编辑型衬线字体栈（Didot / Bodoni MT / Hoefler Text / Baskerville / Palatino，Georgia 回退），将标语重塑为句首大写的衬线斜体格言，并在全部三个矢量资源上采用更轻、更通透的等宽规格标签；更新了设计 token。
- 修正了 OpenClaw 安装行（使用其自己的路径与 CLI，而非 Claude 工作区路径），并将智能体兼容性验证日期提升到 2026-06-12。
- 将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.5.1。

## [5.5.0] — 2026-06-12

这次次版本号提升标志着在 5.4.6-5.4.9 线上构建的制作弧的完成：能力提取、六语言反套话系统、人话访谈、编辑型首页、模型机制和灵魂层——如今由「迭代经济学」收尾。

### 新增

- 新增 `references/retake-protocol.md`：五判定镜头分诊（保留 / 后期修 / 编辑 / 重摇 / 重写），锚定到配置模型的主要花费、单变量规则、带书面停止条件的尝试预算、起草便宜/锁定昂贵的成本意识（附实时核查注意事项）、可审计的镜头日志，以及诚实的「不生成」退出口。
- 新增 eval 用例 `retake_triage_discipline`（61 个受保护用例）：对可保留镜头的条件反射式重生成判为失败。

### 变更

- 运行回路的修复步骤现在会在排障之前先给回来的镜头分诊；`seedance-troubleshoot` 把部分成功路由到分诊而非重写。
- 校准了 README 徽章（47 个参考、61 个 eval），并将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.5.0。

## [5.4.9] — 2026-06-12

### 新增

- 新增 `references/model-mechanics.md`：以八种机制（注意力预算、分布拉力、无 NOT、轨迹先验、误差累积、参考主导、面积缩放细节、音视频联合）构建的生成器可用心智模型，一种带实战范例的新案例推导方法，以及一张接入 `seedance-troubleshoot` 的按机制索引的诊断表——标注为内部推理，绝非架构声明。
- 新增灵魂层：根部的灵魂章节（听懂文字背后的意图；在整场对话中保持故事状态鲜活，使用户永不重复决定；随用户调整语域），以及在全部 24 个子技能中一个独立的意图章节。
- 新增带诚实不确定性断言的新案例机制推理 eval 用例（60 个受保护用例）。

### 变更

- 将俄语对白支持明确保留为现场观察：按仓库的声明边界规则，多语言对白声明归因于俄语覆盖，而非官方页面。
- 将 `seedance-troubleshoot` 中的未知故障经由基于机制的诊断路由；将能力地图交叉链接到机制。
- 校准了 README 徽章（46 个参考、60 个 eval），并将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.4.9。

## [5.4.8] — 2026-06-12

### 新增

- 新增编辑型首页设计系统：手工构建的主题感知 SVG 报头（`hero-dark.svg`/`hero-light.svg` 置于 `prefers-color-scheme` picture 元素之后）、规格风格的运行图（`skill-map.svg`）、统一的扁平方形墨/琥珀徽章，以及 `frontend-design-system.md` 中的设计 token——无渐变、无辉光，衬线展示字体压过等宽标签。
- 新增来自中文社区研究的现场技法：用于多人稳定性的三层动作层级（`seedance-characters`）、I2V 的 Hold/React 模式（`i2v-guide.md`）、用于 UGC/直播/电影写实的源外观锁（`seedance-style`）、Dreamina/Jimeng 带括号的时间线骨架（附 zh 模板，`multishot-grammar.md`、`vocab/zh.md`）、氛围连贯性声明、能力地图中的道具物理脆弱性，以及三个配方族：短剧、口播和家居漫游。
- 新增来自俄语社区研究的俄语对白工程（`vocab/ru.md`、`seedance-vocab-ru`、`audio-guide.md`）：短句规则、西里尔字母对转写的现场矩阵、每次生成一个说话人、用于全配音作品的后配音退路，以及「自俄罗斯联邦访问」包装注意事项。
- 新增多人动作层级的 eval 用例（59 个受保护用例）。

### 变更

- 加固 `scripts/design_audit.py`，使其要求主题感知矢量报头，并拒绝矢量资源中的渐变、模糊滤镜和缺失的衬线/等宽字体栈。
- 在运行回路接收阶段新增安全快速通道：明确的安全、IP、肖像或规避风险在任何规划之前路由到安全关卡（压力测试发现）。
- 在两个主题变体中都将 hero 规格行右对齐到内容边距。
- 将生成的位图艺术迁移到精选的视觉画廊；README 的工作视觉现在是矢量。
- 将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.4.8。

## [5.4.7] — 2026-06-11

### 新增

- 新增多语言反套话层：在全部六个词汇文件（en、zh、ja、ko、es、ru）中各加入语言专属的「套话陷阱（Slop Traps）」表，每一个都把该社区自己的空洞质量词转化为产生那种感觉的物理元素，植根于社区记录的实践。
- 新增 `skills/seedance-vocab-en`：英语精度词汇，带 51 行功能表、去套话流程和过滤感知的同音词修复（仅为清晰；真正有风险的内容路由到过滤边界）。
- 在 `anti-slop-lexicon.md` 和 `seedance-antislop` 中新增六类套话分类法：空洞评价词、借来的图像模型 token、标签沙拉、否定套话、形容词堆叠和跨语言「感觉后缀」词，附标签沙拉与否定修复章节。
- 为英语套话与过滤词汇、以及中文「感觉词」分解新增了 eval 用例（共 58 个用例）。
- 在来源注册表中新增一行 fal 来源、向 api-status 重核清单新增 fal 模型页 URL，并验证了 r2v 请求字段和分级专属分辨率（2026-06-11）。

### 变更

- 在实时验证后，将快速级（fast-tier）多镜头可靠性限制从官方重新标注为现场观察；将陈旧的 fal 分辨率冲突重构为分级专属状态。
- 加固 `scripts/vocab_schema_check.py`：每个语言文件都必须有「套话陷阱」章节；将 Text 和 Editing 加入严格必需功能。
- 将四个能力参考（`capability-map.md`、`allocation-model.md`、`multishot-grammar.md`、`2d-anime-grammar.md`）注册进验证器和 README 参考库，并用必需 ID 保护了全部 58 个 eval 用例。
- 通过把参考素材问题折叠进批次，使人话访谈保持在其五问上限内。
- 校准了 README 徽章（24 个子技能、45 个参考、58 个 eval），并在多语言词汇行中加入英语。
- 将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.4.7。

## [5.4.6] — 2026-06-11

### 新增

- 新增能力提取参考层：`capability-map.md`（顺着模型强项、绕开已知限制做设计）、`multishot-grammar.md`（镜头标签、镜头数乘秒数预算、单次生成内部的剪切语法）、`2d-anime-grammar.md`（带无镜头规则的赛璐珞/动漫媒介语法）和 `allocation-model.md`（一次生成把保真度预算花在哪里）。
- 在 `api-status.md` 中新增带日期的 fal 平台章节，含各端点参数（t2v/i2v/r2v）、参考限制、定价注意事项、480p/720p 对 1080p 的文档冲突、seed 语义和 reference-to-video 优先续接指引，外加 `platform-surface-matrix.md` 和 `model-name-map.md` 中的 fal 行以及根技能中的 fal 路由。
- 新增技法深化：`reference-workflow.md` 中的运动迁移、`audio-guide.md` 中的「音频作时钟」、`first-last-frame-guide.md` 中带持续载体的变形方法，以及 `seedance-motion` 中的物理优先提示。
- 新增四个 eval 用例：fal 平台规格验证、被禁止请求的人话拒绝、错误模型的仅手艺路由，以及无电影背景的人话访谈（共 56 个用例）。

### 变更

- 用人话触发词、含 fal 的完整平台列表和明确的非触发条件重写了根技能描述。
- 新增了运行回路能力与配置核查、按平台区分的模式可用性把关，以及新参考的加载映射行。
- 为无电影背景的用户重新设计了 `seedance-interview` 和 `seedance-interview-short`：可选的人话问题（附声明的默认值）、感觉到片子的翻译、专家检测和「先提议后调整」的微处理脚本流程。
- 为 `seedance-filter` 新增明确的「仅误判」边界，并将其 README 一句话重构为「修复误判，绝不通过隐藏意图」。
- 加固 `scripts/install_codex_skill.py`，使其从安装载荷中排除图像资源、文档和 CI 配置，并打印安装载荷大小（约 594 KB 而非约 19 MB）。
- 将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.4.6。

## [5.4.5] — 2026-05-30

### 新增

- 新增七个生成的视觉画廊资源：两张电影级 hero 镜头，以及五张关于技能能力、CDN 交付、参考角色、制作交付和 QC 的文字密集型信息图。
- 新增 README 视觉画廊覆盖，使首页将该技能呈现为专业电影人操作系统，而非单张泛泛的图片。
- 为六图以上的视觉画廊要求新增了 eval 覆盖。
- 在 `agents/openai.yaml` 新增 Codex UI 元数据，并在 `scripts/install_codex_skill.py` 新增本地安装器。

### 变更

- 为文字密集型信息图资源更新了 README hero、徽章、设计标准、前端重设计说明和前端设计系统规则。
- 更新了安装指引，使仓库可安装到 `$CODEX_HOME/skills/seedance-20` 或 `~/.codex/skills/seedance-20` 以供 Codex 直接使用。
- 强化 `scripts/design_audit.py`，使其要求视觉画廊、验证 PNG 头、强制最小尺寸并对陈旧视觉指引判为失败。
- 将有效技能元数据、验证器期望值和 eval 元数据提升到 v5.4.5。

## [5.4.4] — 2026-05-30

### 新增

- 新增专业电影人参考层：`pro-filmmaking-standards.md`、`cinematography-shot-language.md`、`shot-list-continuity.md`、`color-pipeline-aces.md`、`aspect-ratio-delivery.md`、`subtitles-localization.md`、`audio-post-delivery.md` 和 `delivery-qc.md`。
- 为导演、DP、制片、剪辑、调色、声音团队、本地化团队和交付/QC 团队新增了 README 专业范围。
- 为镜头合同、多镜头连续性、ACES/调色交接、画幅比交付、字幕/本地化、音频后期、QC 预检和全球营销战役版本管理新增了 eval 覆盖。
- 为镜头合同、无文字本地化和营销战役剪辑矩阵新增了专业工作流来源记录和社区模式记录。

### 变更

- 将根技能、管线、访谈、提示词、镜头、运动、角色、灯光、音频、配方和排障技能路由进新的专业制作参考。
- 为制作阶段、镜头表、连续性锚点、调色管线、字幕方案、音频交付物、交付元数据和 QC 检查扩展了 JSON schema 支持。
- 用专业镜头合同、本地化交接和交付 QC 范例扩展了范例。

## [5.4.3] — 2026-05-30

### 新增

- 新增 `assets/skill-map-cinematic.png`，并用一张生成的电影级位图信息图替换 README 技能映射展示。
- 新增 `references/multilingual-community-examples.md`，含原创的中英、俄英、日英、韩英和西英范例。
- 新增安全的混合语言误判修复指引，在不提供过滤规避手法的前提下澄清良性制作上下文。
- 为多语言误判修复和电影级信息图/首页要求新增了 eval 覆盖。

### 变更

- 用一张更专业的电影级操作系统信息图替换 `assets/skill-os-infographic.png`。
- 用多语言社区启发结构扩展了提示词范例和模式范例。
- 用本地化的日文、韩文、西班牙文、俄文和混合语言提示词模式记录更新了社区模式数据。
- 更新了设计验证，要求生成的技能映射位图与 hero 和操作系统信息图并存。

## [5.4.2] — 2026-05-30

### 新增

- 新增 `references/api-workflow.md` 和 `references/examples-by-mode.md`，使 API 用法、Runway/Volcengine 工作流差异、edit/extend、音频参考处理、FLF2V 和模式专属范例可从有效技能中发现。
- 为音频参考冲突、中文官方风格参考公式、edit/extend 路由、俄文结构化提示词、镜头表连续性、画廊安全分类、VFX 参考修复和延长退化新增了 eval 覆盖。
- 新增了更丰富的 Runway Seedance 2 和 Volcengine 5 月 28-29 日来源记录，包括 `seedance2`、任务生命周期、首/末帧角色措辞、定价页注意事项和 Runway MCP 上下文。

### 变更

- 将 README hero 图重建为一个电影级 Seedance 制作控制场景，含参考帧、时间线、产品揭示、镜头机位和音频波形。
- 将日文、韩文和西班牙文词汇参考扩展为带参考标签保留、镜头、运动、灯光、音频、edit、extend 和安全语言的制作就绪表。
- 收紧了有效技能路由，使提示词、镜头、运动、音频、管线、配方、排障、版权和过滤模块在任务需要时加载新的深度参考。
- 用分类后的多语言模式替换了浅层社区挖掘记录，这些模式保留可复用结构，同时拒绝不安全的 IP、名人、品牌和绕过内容。

### 修复

- 修正了 Codex Agent Skill 安装措辞，使仓库根文件除非从正确路径安装或扫描，否则不被描述为自动加载。
- 将已迁移的遗留材料保持为仅警告且隔离，使陈旧的本地笔记无法覆盖当前来源受限的指引。

## [5.4.1] — 2026-05-30

### 新增

- 新增 `assets/skill-os-infographic.png` 和一个解释技能操作系统通道的 README 章节。
- 新增 `references/agent-compatibility.md`，用于 Codex/Agent Skills 打包、渐进式披露和安装注意事项。
- 新增 5 月 30 日来源记录，涉及 Volcengine 5 月 29 日的模型列表/教程更新、Volcengine API 服务生态文章、Agent Skills 文档和近期音视频 eval 基准词汇。

### 变更

- 将带日期的研究快照刷新为 `research-2026-05-30.md`，将来源数据文件刷新为 `sources.seedance-2026-05-30.json`。
- 收紧了 README 安装措辞，使本地技能路径被视为客户端专属目标，而非普适安装保证。
- 更新了验证脚本和设计检查，以强制新的信息图、智能体兼容性参考、v5.4.1 元数据和 5 月 30 日来源数据。

### 修复

- 将 FLF2V 措辞明确保持为合作伙伴/平台专属，除非当前的一手 API 页面暴露了那个确切的工作流名称。
- 新增了更强的 BytePlus 注意事项：不要在没有实时官方验证的情况下从 JavaScript 渲染页面引用 Seedance 2.0 BytePlus 定价或模型 ID。

## [5.4.0] — 2026-05-27

### 新增

- 在 `assets/hero-cinematic.png` 新增一张生成的电影级 README hero 图。
- 新增带日期的研究与来源层（后续延续为 `research-2026-05-30.md`），外加 `platform-surface-matrix.md`、`model-name-map.md`、`first-last-frame-guide.md`、`field-observed-tips.md` 和 `community-source-methodology.md`。
- 在 `data/` 下新增结构化来源与社区模式数据文件。
- 新增来源新鲜度与词汇 schema 验证器。
- 为模型名准确性、来源新鲜度、首/末帧工作流、中文/俄文角色绑定、不安全绕过拒绝和社区语料安全新增了 eval 用例。

### 变更

- 将 `api-status.md` 和 `source-registry.md` 刷新到 2026-05-27 的来源边界。
- 用角色绑定、首/末帧、镜头、灯光、音频、编辑、约束和安全术语扩展了有效的中文和俄文词汇参考。
- 更新了提示词、管线、配方、过滤和多语言技能，使其路由进新的研究和 FLF2V 参考。
- 更新了 CI 与发布验证，使其运行六项检查而非四项。

### 修复

- 防止了含糊的 `Seedance 2.0 Pro` 命名被当作官方 Seedance 视频模型名。
- 让公开提示词语料挖掘以安全为先：提取结构与词汇，而非不安全的原始范例。

## [5.3.0] — 2026-05-08

### 修复

- 移除了遗留的重复 `user-invokable` frontmatter 键，并将验证器更新为规范的 `user-invocable` 字段。
- 扩展了此前单薄的制作模块、多语言词汇路由器和参考词表，使每个技能都可作为独立入口点使用。
- 用来源层级、证据标签、声明边界和易变平台声明所需的措辞深化了 `references/source-registry.md`。

### 变更

- 将所有技能元数据、README 徽章、验证器文本和 eval 元数据更新到 `5.3.0`。
- 将根 `ZH_REFERENCE.md` 重新压缩为一个精简路由器，同时把详细指引保留在子技能和参考中。

### 新增

- 新增八个 eval 用例，涵盖 VFX 物理、多语言词汇、中文范例、反套话修复和短访谈路由。

## [5.2.0] — 2026-05-08

### 修复

- 修复了部分完成的 v5.1 部署：恢复了多行 Markdown、多行 YAML frontmatter、真实的 Python 脚本、非空的 eval 和缺失的 GitHub Actions 工作流。
- 替换了使 README、参考和脚本渲染糟糕的旧单行有效文件。
- 将全部 23 个子技能的 frontmatter 块规范化为 `metadata.version: "5.2.0"` 和 `metadata.parent: "seedance-20"`。

### 变更

- 将面向 GitHub 的 README 重新设计为更干净的项目首页，带 start-here 表、技能映射、参考库、验证章节和设计标准。
- 用一套克制的电影控制设计系统替换了霓虹/过载的视觉语言。
- 将过大的有效子技能转换为精简的程序化路由器，同时通过补丁器备份/迁移路径保留旧的本地内容。
- 将平台指引更新为来源感知、带日期戳的语言。

### 新增

- 新的 SVG 前端资源：`assets/hero-dark.svg`、`assets/hero-light.svg` 和 `assets/skill-map.svg`。
- 验证脚本：`scripts/validate_skills.py`、`scripts/content_audit.py`、`scripts/eval_schema_check.py` 和 `scripts/design_audit.py`。
- CI 工作流：`.github/workflows/validate-skills.yml`。
- Eval：`evals/evals.json`，含 18 个真实测试用例。
- 参考：`api-status.md`、`source-registry.md`、`audio-guide.md`、`anti-slop-lexicon.md`、`filter-vocab.md`、`progressive-disclosure.md`、`eval-rubric.md` 和 `frontend-design-system.md`。

## [5.1.0] — 2026-05-08

验证、状态和渐进式披露修复发布。被 v5.2.0 取代，因为推送的 v5.1 文件部分塌缩且不完整。

## [5.0.0] — 2026-03-03

意图优先提示词发布。引入了导演公式（Director Formula）、短提示词偏好、扩展的参考和四模态工作流路由。

## 历史发布

更早的 v3.x 和 v4.x 发布构建了模块化技能结构、多语言词汇、范例库、排障模块和平台支持矩阵。完整的遗留变更日志见仓库历史。
