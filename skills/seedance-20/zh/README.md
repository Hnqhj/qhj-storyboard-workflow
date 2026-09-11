<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="../assets/hero-light.svg">
  <img alt="Seedance 2.0 Skill OS — intent-first AI filmmaking. Route, verify, direct, deliver." src="../assets/hero-dark.svg" width="100%">
</picture>

# Seedance 2.0 技能操作系统（Skill OS）

**导演这个模型，别去微管每一帧画面。**

一个像电影导演那样执导 Seedance 2.0 的智能体——在写提示词之前先读懂每一个场景。<br>支持文本、图像、视频，以及带原生音频的「参考到视频」，IP 安全改写、带来源日期的平台事实，以及面向英语、中文、日本語、한국어的母语阅读路径。

[![Version](https://img.shields.io/badge/version-6.1.0-E2A75E?style=flat-square&labelColor=14110B)](#changelog)
[![Sub-skills](https://img.shields.io/badge/sub--skills-28-4A4438?style=flat-square&labelColor=14110B)](#skill-map)
[![References](https://img.shields.io/badge/references-57-4A4438?style=flat-square&labelColor=14110B)](#reference-library)
[![Evals](https://img.shields.io/badge/evals-114-4A4438?style=flat-square&labelColor=14110B)](#validation)
[![License](https://img.shields.io/badge/license-MIT-4A4438?style=flat-square&labelColor=14110B)](../LICENSE)

[从这里开始](#start-here) · [技能映射](#skill-map) · [参考库](#reference-library) · [视觉画廊](#visual-gallery) · [安装](#install)

English · [中文](../docs/README.zh.md) · [日本語](../docs/README.ja.md) · [한국어](../docs/README.ko.md)

</div>

> Codex local note (2026-07-10): this `zh` tree is retained as a Chinese reference mirror. Its former `SKILL.md` files have been renamed to `ZH_REFERENCE.md` so the canonical `seedance-20` active skill tree remains the only registered Seedance skill set.


作者：[Iamemily2050 (@iamemily2050)](https://github.com/Emily2040) · [Instagram](https://instagram.com/iamemily2050) · [X](https://x.com/iamemily2050) · [Website](https://iamemily2050.com)

平台上下文：[ByteDance Seedance 2.0](https://seed.bytedance.com/en/seedance2_0) · Dreamina · Jimeng · Doubao · [Volcengine Ark](https://www.volcengine.com/docs/82379/2291680?lang=zh) · [BytePlus ModelArk](https://docs.byteplus.com/en/docs/ModelArk/2291680) · [Runway Seedance 2](https://docs.dev.runwayml.com/guides/models/) · fal · provider/router 平台在 [`platform-surface-matrix.md`](references/platform-surface-matrix.md) 中追踪

更新于：**2026-06-22** · **v6.1.0 导演引擎：有动机的场景导演，以及贯穿一个故事的统一导演嗓音**

---

## 导演这个场景，别去装饰它

大多数工具都向模型索要一种「电影感的外观」。而一位导演会问这个场景在*做*什么——然后让镜头、焦段、灯光、调度、表演和声音全部服务于一个意图，以一种可辨识的统一嗓音，贯穿整个故事。

v6.1.0 的[**导演引擎**](references/directing-engine.md)把这种判断力编码了下来。它读取一个场景的戏剧功能——转折、视点、权力关系、潜台词——命名一个意图，然后推导出一套连贯的设置，而不是堆叠形容词。

**索要「电影感」：** `epic cinematic shot of a woman reading a letter, emotional, beautiful lighting`

**去导演它：** `Medium close-up, eye-level; she lowers the letter and her hands go still as a slow push-in arrives; soft window light behind her keeps her face plain; near-silence with one chair scrape — the realization lands in the stilled hands, not a word.`

然后它会在一个长故事的每一个短片段中保持统一的导演嗓音，并附带 **35 条完整推导的范例**——产品、音乐视频、恐怖、动漫、动作、喜剧、纪录片、高级时装、科幻等等——每一条都从头到尾完整展示。

> 一次揭示，其用光、构图、调度或表演方式都不会和一次告别相同。引擎拒绝泛泛的答案，推导出那个具体的答案。

## 母语起步 / Native Language Start / 多言語スタート / 다국어 시작

Seedance 2.0 技能操作系统以英语为可读基础，但 v6 线为中文、日文和韩文读者提供了一流的入口、可用的范例技能和母语提示词指引。在每种语言中都要原样保留参考标签（`[Image1]`、`[Video1]`、`[Audio1]`、`@图1`、`@视频1`）。

| 语言 | 起步路径 | 母语读者提示 |
|---|---|---|
| English | [`seedance-prompt`](skills/seedance-prompt/ZH_REFERENCE.md)、[`seedance-sequence`](skills/seedance-sequence/ZH_REFERENCE.md)、[`references/vocab/en.md`](references/vocab/en.md) | 使用精确的制作英语：一个可见节拍、一个镜头运动、真实的光，以及清晰的参考角色。 |
| 中文 | [`中文指南`](docs/README.zh.md)、[`seedance-vocab-zh`](skills/seedance-vocab-zh/ZH_REFERENCE.md)、[`seedance-examples-zh`](skills/seedance-examples-zh/ZH_REFERENCE.md)、[`references/vocab/zh.md`](references/vocab/zh.md) | 中文用户可从角色锁定、首尾帧、运镜、动作节奏开始；提示词要短、具体、保留参考标签，不把字幕交给模型生成。 |
| 日本語 | [`日本語ガイド`](docs/README.ja.md)、[`seedance-vocab-ja`](skills/seedance-vocab-ja/ZH_REFERENCE.md)、[`seedance-examples-ja`](skills/seedance-examples-ja/ZH_REFERENCE.md)、[`references/vocab/ja.md`](references/vocab/ja.md) | 日本語では、人物の同一性、衣装、構図、動きの終点を明確に書き、字幕や広告コピーは後処理で追加します。 |
| 한국어 | [`한국어 가이드`](docs/README.ko.md)、[`seedance-vocab-ko`](skills/seedance-vocab-ko/ZH_REFERENCE.md)、[`seedance-examples-ko`](skills/seedance-examples-ko/ZH_REFERENCE.md)、[`references/vocab/ko.md`](references/vocab/ko.md) | 한국어 프롬프트는 인물 고정, 카메라 움직임, 조명, 사운드를 짧게 분리하고 자막과 문구는 편집 단계에서 넣습니다. |

对于任何语言的较长故事，从 [`seedance-sequence`](skills/seedance-sequence/ZH_REFERENCE.md) 开始。要做一个被接受片段的下一部分，使用 [`seedance-continuation`](skills/seedance-continuation/ZH_REFERENCE.md)，并在写下一条提示词之前更新观察到的末态。

## 这个仓库为何存在

Seedance 2.0 技能操作系统是一个模块化的智能体技能包，用于执导 Seedance 2.0 视频生成。它围绕一条简单的原则构建：**导演这个模型，不要微管每一帧画面**。

这个仓库为 AI 助手提供了一个公开、可审计的 Seedance 工作操作系统。它定义了：何时访谈、何时写一条紧凑的提示词、何时加载技术参考、何时改写不安全的 IP 内容，以及何时排查一次糟糕的生成。

## 这个技能做什么

这个技能包把 Seedance 2.0 工作变成一套可重复的助手工作流：

- 把模糊的创意路由进简短的创意访谈，而不是过早地堆砌提示词。
- 在起草前先导演每一个场景：读懂其戏剧功能，设定一种统一的导演嗓音，让镜头、灯光、调度、表演和声音服务于一个意图而非泛泛的「电影感」外观——并在一个长故事的每一个片段中保持那种嗓音。
- 为 T2V、I2V、V2V、R2V、FLF2V、edit、extend、音频感知和首/末帧工作流编写完整或压缩的提示词。
- 按角色区分每一个参考素材：身份、环境、运动、镜头节奏、音频节拍、风格或端点。
- 让模型和平台声明保持带来源日期，使 API、定价、地区、配额和模型 ID 细节不被猜测。
- 在起草前先规划进模型强项：一张能力地图、一个保真度分配模型，以及一个解释每条规则为何有效的生成器机制工作模型。
- 在生成之后像制片人那样跑这次拍摄：五判定镜头分诊、单变量重摇、尝试预算和成本意识起草。
- 提供母语读者首页路径，外加英语、中文、日本語、한국어、西班牙语和俄语的更深层多语言电影词汇，包括角色绑定、首/末帧措辞、edit/extend 用词、安全用词、音频提示、续接用词和后期文字处理。
- 为中文、日文、韩文、俄英和西英提示词结构新增原创的社区启发范例。
- 为「treatment 到镜头表」的规划、镜头合同、连续性账本、ACES/调色交接、音频后期、字幕/本地化、画幅比变体、营销战役剪辑、交付/QC 和客户审片包，新增专业电影人工作流。
- 通过澄清良性制作上下文（而非隐藏不安全意图）来处理安全的误判修复。
- 把不安全的名人、受保护 IP、私人、品牌、logo、歌曲或声音请求改写为更安全的创意等价物。
- 用具体的修复杠杆诊断失败的输出：镜头、灯光、运动、参考角色、时长、构图、音频或安全用词。
- 附带验证脚本、eval 用例、来源数据和设计检查，使维护者在发布前能审查变更。

## 让视频比一次生成更长

不要盲目地让技能去延长原始提示词。续接必须基于被接受的已生成素材，因为 Seedance 可能不会恰好停在原始提示词所期望的地方。

1. 描述完整的创意以及它如何结束。
2. 技能把它分成相连的片段。
3. 生成 Clip 01。
4. 返回已生成的片段或其末帧。
5. 技能记录实际发生了什么。
6. 它从真实的结尾写出 Clip 02。
7. 重复，直到达成计划中的最终结局。

项目状态是事实的来源。片段合同是当前的制作任务。提示词是仅针对该任务的编译指令。被接受的已生成素材决定接下来发生什么。

## 专业电影人范围

这个包是为正在工作的电影和广告团队设计的，而不仅仅是为随意的提示词写作。它能帮助一个智能体产出该角色真正需要的成品：

| 角色 | 技能应当产出什么 |
|---|---|
| 导演 | treatment、场景节拍、表演意图、覆盖、镜头端点、审片笔记 |
| 摄影指导 / DP | 镜头合同、景别、镜头质感、机位支撑、运动、调度、灯光连续性 |
| 制片 / 代理商 | 客户 brief、权利图、审批关卡、营销战役变体、风险日志、审片包 |
| 剪辑 | 精选方案、edit/extend 决定、连续性交接、handle、无文字需求、合成笔记 |
| 调色 | 调色意图、ACES 感知交接、show-look 笔记、HDR/SDR 注意事项、产品色检查 |
| 声音团队 | 对白图、环境/SFX/音乐层、同步提示、stems、M&E、配音和响度笔记 |
| 本地化团队 | 字幕、SDH 字幕、强制旁白、配音指南、市场文案、无文字底板 |
| 交付/QC | 帧率、画幅比、裁切、调色、响度、字幕、元数据、命名、人工 QC 清单 |

对于这些请求，技能不应止步于一条提示词。它应当先返回制作对象，然后返回适配该方案的 Seedance 提示词或提示词批次。

## 从这里开始 {#start-here}

| 用户情境 | 先加载 | 输出 |
|---|---|---|
| 「我有一个模糊的创意。」 | [`seedance-interview`](skills/seedance-interview/ZH_REFERENCE.md) | 一份聚焦的创意 brief 和下一条提示词路径。 |
| 「这是个较长的故事 / 做成三个相连片段。」 | [`seedance-sequence`](skills/seedance-sequence/ZH_REFERENCE.md) | 完整的故事脊线、连续性圣经、序列图、Clip 01 合同，以及仅 Clip 01 提示词。 |
| 「续接这个视频 / 做下一部分。」 | [`seedance-continuation`](skills/seedance-continuation/ZH_REFERENCE.md) | 一个来源受限、源自被接受素材的续接，或对缺失片段/末帧的请求。 |
| 「我知道我想要的场景。」 | [`seedance-prompt`](skills/seedance-prompt/ZH_REFERENCE.md) | 一条制作就绪的 Seedance 提示词。 |
| 「让它真的有被导演过的感觉，而不只是电影感。」 | [`directing-engine`](references/directing-engine.md) | 每个场景一个意图，一套连贯的镜头/灯光/调度/表演/声音设置，以及贯穿故事的统一导演嗓音。 |
| 「让它简短而有力。」 | [`seedance-prompt-short`](skills/seedance-prompt-short/ZH_REFERENCE.md) | 一条压缩的 30–100 词提示词。 |
| 「我有一个图像/视频/音频参考。」 | [`reference-workflow`](references/reference-workflow.md) | 每个参考素材的角色图。 |
| 「用这个作首帧、那个作末帧。」 | [`first-last-frame-guide`](references/first-last-frame-guide.md) | 带端点锁的连续过渡。 |
| 「这条镜头 80% 对了——重生成还是保留？」 | [`retake-protocol`](references/retake-protocol.md) | 一个分诊判定、单变量重摇和尝试预算。 |
| 「它失败了或看起来很糟。」 | [`seedance-troubleshoot`](skills/seedance-troubleshoot/ZH_REFERENCE.md) | 一个根因诊断和修好的提示词。 |
| 「为什么会那样？」 | [`model-mechanics`](references/model-mechanics.md) | 失败背后的机制以及与之配合奏效的杠杆。 |
| 「这用到一个角色、品牌、名人或真实人物。」 | [`seedance-copyright`](skills/seedance-copyright/ZH_REFERENCE.md) | 一个保留创意功能的更安全改写。 |
| 「我需要它用于一部电影、客户、营销战役或交付。」 | [`pro-filmmaking-standards`](references/pro-filmmaking-standards.md) | 一份专业工作流方案、角色专属成品和提示词路径。 |
| 「把这份 treatment 变成镜头。」 | [`shot-list-continuity`](references/shot-list-continuity.md) | 镜头表、连续性账本和提示词批次结构。 |
| 「这需要字幕、配音、调色、声音或 QC。」 | [`delivery-qc`](references/delivery-qc.md) | 后期、本地化、音频、调色和交付检查。 |
| 「我需要 API、Runway、provider、定价、模型 ID 或制作工作流指引。」 | [`api-workflow`](references/api-workflow.md) | 一份来源受限的操作清单。 |
| 「这是 Seedance Pro/Fast/V2 吗？」 | [`model-name-map`](references/model-name-map.md) | 带来源日期的命名和平台注意事项。 |
| 「我用中文阅读或写提示词。」 | [`中文指南`](docs/README.zh.md)、[`seedance-vocab-zh`](skills/seedance-vocab-zh/ZH_REFERENCE.md)、[`seedance-examples-zh`](skills/seedance-examples-zh/ZH_REFERENCE.md) | 中文角色锁定、首尾帧、运镜、动作、音频和安全改写路径。 |
| 「我用日语阅读或写提示词。」 | [`日本語ガイド`](docs/README.ja.md)、[`seedance-vocab-ja`](skills/seedance-vocab-ja/ZH_REFERENCE.md)、[`seedance-examples-ja`](skills/seedance-examples-ja/ZH_REFERENCE.md) | 日本語の映画表現、参照ロール、動き、照明、音声、テキストレス納品の書き方。 |
| 「我用韩语阅读或写提示词。」 | [`한국어 가이드`](docs/README.ko.md)、[`seedance-vocab-ko`](skills/seedance-vocab-ko/ZH_REFERENCE.md)、[`seedance-examples-ko`](skills/seedance-examples-ko/ZH_REFERENCE.md) | 한국어 카메라, 조명, 동작, 사운드, 안전한 참조 역할 작성법. |
| 「我想要俄语/西班牙语或混合语言提示词范例。」 | [`multilingual-community-examples`](references/multilingual-community-examples.md) | 安全的社区启发结构和误判修复模式。 |
| 「我要把它作为智能体技能来安装或审查。」 | [`agent-compatibility`](references/agent-compatibility.md) | Codex/Agent Skills 结构和分发说明。 |

## 当前状态规则

Seedance 平台行为变化很快。在做关于 API 可用性、面部或肖像授权、上传限制、定价、地区可用性或模型名称的事实声明之前，加载 [`references/api-status.md`](references/api-status.md) 并检查其 `last_verified` 日期。

截至 2026-06-20，公开的官方来源将 Seedance 2.0 描述为支持文本、图像、音频和视频输入。官方发布与模型卡材料称参考可包含最多 9 张图像、3 个视频片段和 3 个音频片段。

Volcengine 和 BytePlus 文档现在将 Seedance 2.0 Mini 暴露为一条平台专属的模型通道。仅当有效平台确认时，才将 `Seedance V2 Mini` 视为 Seedance 2.0 Mini 的简称。当前来源可见的 ID 包括 Volcengine 上的 `doubao-seedance-2-0-mini-260615` 和 BytePlus 上的 `dreamina-seedance-2-0-mini-260615`。

Volcengine 文档还将 `doubao-seedance-2-0-260128` 和 `doubao-seedance-2-0-fast-260128` 保持为可见的 Ark 模型 ID，并在该平台上记录首/末帧角色用法。Runway 记录了 `seedance2`，时长 5-15 秒，可选图像、视频和音频参考。

截至 2026-06-20 追踪的第三方 provider/router 页面包括 EvoLink、OpenRouter、Kie.ai、PiAPI、LaoZhang、Runware、ModelsLab、AI/ML API、MuAPI、SeeGen 和 Segmind。

将每一个端点、模型 ID、价格、账户要求、面部/参考政策和输出权利声明都视为 provider 专属，并在实现前重新实时核查。面向中国大陆的搜索应优先采用官方 ByteDance、Volcengine、BytePlus、Doubao、Jimeng/Jianying 和 CapCut/剪映平台；工作流托管方或业务伙伴新闻除非发布 provider 自有的 API 文档，否则不是公开 API 提供方。

访问、定价、上传限制、地区、分辨率、音频组合规则和授权要求仍然是平台专属。

## V6 研究与声明边界

v6 发布线保留了一个带日期的研究层，用于更安全的数据挖掘、多语言提示、序列状态工作和平台声明：

- [`research-2026-05-30.md`](references/research-2026-05-30.md) 记录官方与现场观察到的信号。
- [`platform-surface-matrix.md`](references/platform-surface-matrix.md) 将模型能力与 Dreamina/Jimeng、Volcengine/Ark、BytePlus、ComfyUI 和 provider/router 行为区分开。
- [`model-name-map.md`](references/model-name-map.md) 防止 `Seedance 2.0`、`Seedance 2.0 Fast`、`Seedance 2.0 Mini`、`Seedance V2` 和含糊的 Pro 标签被混在一起。
- [`community-source-methodology.md`](references/community-source-methodology.md) 解释如何在不复制不安全范例的前提下挖掘公开提示词语料。
- [`multilingual-community-examples.md`](references/multilingual-community-examples.md) 从安全的社区模式挖掘中捕获安全的混合语言和本地化提示词结构。
- [`pro-filmmaking-standards.md`](references/pro-filmmaking-standards.md) 为镜头表、连续性、调色、音频、本地化和交付新增行业工作流边界。

## 操作系统一览

![Seedance 2.0 Skill OS operating diagram: seven gates feed the seedance-20 root, which routes to the core pipeline, governance, and multilingual vocabulary clusters, backed by the reference library and validators](../assets/skill-map.svg)

这张图就是契约：每个请求都要通过这些关卡，根负责路由它，验证器守住底线。六条通道按设计保持分离：

- 研究来源：带日期的官方、学术、平台和社区证据。
- 制作脊线：brief、镜头表、连续性、后期交接、本地化和交付/QC。
- 提示词路由器：访谈、提示词写作、压缩、配方和排障。
- 多模态参考：图像、视频、音频、首帧、末帧和角色绑定素材。
- 安全关卡：IP、肖像、声音、品牌、真实人物、过滤和平台政策检查。
- 质量 eval：schema 检查、来源新鲜度、词汇完整性、设计审计和行为用例。

## 视觉画廊 {#visual-gallery}

为这套系统创作的概念艺术，已生成并精选。每张图都配有可搜索的替代文本，使画廊保持可审计；README 上方的工作视觉是遵循设计标准的手工矢量资源。

### Hero 镜头

![Seedance 2.0 command-center hero showing brief, references, prompt, post, QC, subtitles, audio waveform, and shot cards](../assets/hero-command-center.png)

![Global filmmaker mode hero showing director, DP, editor, colorist, sound mixer, localization lead, and QC lead on a cinematic production stage](../assets/hero-global-filmmaker-mode.png)

### 文字密集型信息图

![What this skill can do infographic: brief, references, prompt, generate, post, deliver](../assets/infographic-skill-capabilities.png)

![CDN video delivery map infographic: creator, origin, CDN edge, global review, delivery, fast playback, regional cache, version control, and QC before publish](../assets/infographic-cdn-delivery-map.png)

![Reference role map infographic: image equals identity, video equals motion, audio equals timing](../assets/infographic-reference-role-map.png)

![Production to delivery infographic: brief, shot list, generate, edit, localize, QC](../assets/infographic-production-delivery.png)

![Professional QC stack infographic: picture, color, audio, text, rights, metadata](../assets/infographic-professional-qc-stack.png)

### 操作系统艺术

![Seedance 2.0 Skill OS infographic: source registry, prompt router, multimodal references, safety gates, and eval loop](../assets/skill-os-infographic.png)

![Seedance 2.0 cinematic skill map: modular skill clusters around an AI filmmaking director console](../assets/skill-map-cinematic.png)

## 技能映射 {#skill-map}

### 核心管线

| 技能 | 何时使用 |
|---|---|
| [`seedance-interview`](skills/seedance-interview/ZH_REFERENCE.md) | 创意模糊、未成形或需要创意方向。 |
| [`seedance-interview-short`](skills/seedance-interview-short/ZH_REFERENCE.md) | 用户想要快速 brief，而非长访谈。 |
| [`seedance-sequence`](skills/seedance-sequence/ZH_REFERENCE.md) | 请求是长故事、相连片段集、营销战役序列或多次生成的场景。 |
| [`seedance-continuation`](skills/seedance-continuation/ZH_REFERENCE.md) | 用户想续接、延长、修复尾段、桥接已知状态或重新锚定被接受素材。 |
| [`seedance-prompt`](skills/seedance-prompt/ZH_REFERENCE.md) | 用户需要从清晰概念得到一条完整提示词。 |
| [`seedance-prompt-short`](skills/seedance-prompt-short/ZH_REFERENCE.md) | 提示词必须被压缩以获得更强的 Seedance 表现。 |
| [`seedance-camera`](skills/seedance-camera/ZH_REFERENCE.md) | 必须指定镜头行为、镜头质感、景别或运动。 |
| [`seedance-motion`](skills/seedance-motion/ZH_REFERENCE.md) | 身体运动、物体运动、编排或物理动作很重要。 |
| [`seedance-lighting`](skills/seedance-lighting/ZH_REFERENCE.md) | 情绪、时间、氛围或光线过渡驱动镜头。 |
| [`seedance-characters`](skills/seedance-characters/ZH_REFERENCE.md) | 角色身份、多角色调度或一致性很重要。 |
| [`seedance-style`](skills/seedance-style/ZH_REFERENCE.md) | 用户需要一种视觉风格，但不借用不安全的工作室/系列 IP。 |
| [`seedance-vfx`](skills/seedance-vfx/ZH_REFERENCE.md) | 粒子、破坏、能量、天气、魔法或变形效果很重要。 |
| [`seedance-audio`](skills/seedance-audio/ZH_REFERENCE.md) | 对白、对口型、音乐、环境声或音频参考行为很重要。 |
| [`seedance-pipeline`](skills/seedance-pipeline/ZH_REFERENCE.md) | 用户询问 API、网页工作流、ComfyUI、后期制作或集成。 |
| [`seedance-recipes`](skills/seedance-recipes/ZH_REFERENCE.md) | 用户想要类型模板或可重复的制作配方。 |
| [`seedance-troubleshoot`](skills/seedance-troubleshoot/ZH_REFERENCE.md) | 输出质量差、不稳定、模糊、偏离提示词或被拦截。 |

### 治理与质量

| 技能 | 何时使用 |
|---|---|
| [`seedance-copyright`](skills/seedance-copyright/ZH_REFERENCE.md) | 出现受保护 IP、公众人物、真实人物、品牌、logo、歌曲或确切场景。 |
| [`seedance-antislop`](skills/seedance-antislop/ZH_REFERENCE.md) | 提示词语言泛泛、臃肿或充满空洞的质量助推词。 |
| [`seedance-filter`](skills/seedance-filter/ZH_REFERENCE.md) | 一条良性提示词被过宽的过滤拦截或降级。通过澄清正当制作上下文来修复误判，绝不通过隐藏意图。 |

### 多语言词汇

| 技能 | 何时使用 |
|---|---|
| [`seedance-vocab-en`](skills/seedance-vocab-en/ZH_REFERENCE.md) | 英文用词套话过多、塞满空洞质量词，或触发误判过滤。 |
| [`seedance-vocab-zh`](skills/seedance-vocab-zh/ZH_REFERENCE.md) | 需要中文提示词压缩或普通话电影词汇。 |
| [`seedance-vocab-ja`](skills/seedance-vocab-ja/ZH_REFERENCE.md) | 需要日语电影词汇。 |
| [`seedance-vocab-ko`](skills/seedance-vocab-ko/ZH_REFERENCE.md) | 需要韩语电影词汇。 |
| [`seedance-vocab-es`](skills/seedance-vocab-es/ZH_REFERENCE.md) | 需要西班牙语电影词汇。 |
| [`seedance-vocab-ru`](skills/seedance-vocab-ru/ZH_REFERENCE.md) | 需要俄语电影词汇。 |
| [`seedance-examples-zh`](skills/seedance-examples-zh/ZH_REFERENCE.md) | 需要中文工作范例或范例安全改写。 |
| [`seedance-examples-ja`](skills/seedance-examples-ja/ZH_REFERENCE.md) | 需要日文工作范例、续接范例、无文字本地化模式或安全改写。 |
| [`seedance-examples-ko`](skills/seedance-examples-ko/ZH_REFERENCE.md) | 需要韩文工作范例、续接范例、无文字本地化模式或安全改写。 |

## 参考库 {#reference-library}

| 参考 | 用途 |
|---|---|
| [`api-status.md`](references/api-status.md) | 当前带日期的平台和 API 状态。 |
| [`source-registry.md`](references/source-registry.md) | 来源层级和证据标签。 |
| [`research-2026-05-30.md`](references/research-2026-05-30.md) | 带日期的来源与现场观察快照。 |
| [`agent-compatibility.md`](references/agent-compatibility.md) | Agent Skills 结构、Codex 兼容性和打包说明。 |
| [`api-workflow.md`](references/api-workflow.md) | Volcengine、BytePlus、Runway、provider/router API、异步任务、参考文件、定价和制作工作流清单。 |
| [`capability-map.md`](references/capability-map.md) | 在提示前先顺着模型强项、绕开已知限制做设计。 |
| [`directing-engine.md`](references/directing-engine.md) | 读懂场景，选择一个意图，让每个乐器协调，保持统一的导演嗓音，并在一个长故事中塑造视觉外观。 |
| [`model-mechanics.md`](references/model-mechanics.md) | 规则为何有效：生成器的八种机制、新案例推导、按机制索引的诊断。 |
| [`retake-protocol.md`](references/retake-protocol.md) | 迭代经济学：镜头分诊、单变量规则、尝试预算、成本意识、镜头日志。 |
| [`sequence-project-state.md`](references/sequence-project-state.md) | 有状态项目模型、正典调和、视觉状态字段和项目状态胶囊。 |
| [`continuation-handoff.md`](references/continuation-handoff.md) | 被接受来源的续接关卡、观察状态捕获、续接类型和节拍排除。 |
| [`prompt-compiler.md`](references/prompt-compiler.md) | 把项目状态和当前片段合同编译成一条自然语言提示词。 |
| [`reference-transfer-contract.md`](references/reference-transfer-contract.md) | 精确标签保留、参考角色分离和迁移/忽略条款。 |
| [`surface-prompt-profiles.md`](references/surface-prompt-profiles.md) | 平台专属的时长、提示词预算、参考角色、时间线、编辑、延长和音频约束。 |
| [`event-density.md`](references/event-density.md) | 针对已完成、当前、预留和暂不展示节拍的片段范围防火墙。 |
| [`continuity-qc.md`](references/continuity-qc.md) | 跨被接受片段的不可变与瞬态连续性边界检查。 |
| [`failure-atlas.md`](references/failure-atlas.md) | 序列与续接故障诊断，附一个主要修复变量。 |
| [`dense-storyboard-mode.md`](references/dense-storyboard-mode.md) | 密集多镜头、分阶段单镜头和 2D 分镜合同。 |
| [`allocation-model.md`](references/allocation-model.md) | 一次生成把保真度预算花在哪里：身份 vs 运动 vs 场景密度。 |
| [`multishot-grammar.md`](references/multishot-grammar.md) | 镜头标签、镜头数乘秒数预算，以及单次生成内部的剪切语法。 |
| [`2d-anime-grammar.md`](references/2d-anime-grammar.md) | 赛璐珞/动漫媒介语法：层、爆发式 vs 保持式运动、无镜头规则。 |
| [`pro-filmmaking-standards.md`](references/pro-filmmaking-standards.md) | 电影、广告、后期、本地化和交付工作的专业制作脊线和来源边界。 |
| [`cinematography-shot-language.md`](references/cinematography-shot-language.md) | 镜头合同、景别、镜头质感、机位支撑、运动、调度和覆盖语言。 |
| [`shot-list-continuity.md`](references/shot-list-continuity.md) | treatment 到镜头表工作流、连续性账本和专业交接字段。 |
| [`color-pipeline-aces.md`](references/color-pipeline-aces.md) | ACES 感知调色意图、show-look 笔记、HDR/SDR 交接和调色 QC 边界。 |
| [`aspect-ratio-delivery.md`](references/aspect-ratio-delivery.md) | 创意构图、交付容器、社交剪辑、安全区和无文字/版本规划。 |
| [`subtitles-localization.md`](references/subtitles-localization.md) | 字幕、SDH、强制旁白、配音、无文字和文化本地化规划。 |
| [`audio-post-delivery.md`](references/audio-post-delivery.md) | 对白、SFX、音乐、stems、M&E、响度、配音和同步交接指引。 |
| [`delivery-qc.md`](references/delivery-qc.md) | 针对画面、调色、音频、字幕、权利、元数据、版本管理和人工 QC 的专业预检。 |
| [`examples-by-mode.md`](references/examples-by-mode.md) | T2V、I2V、V2V、R2V、FLF2V、edit、extend 和排障的模式专属提示词范例。 |
| [`multilingual-community-examples.md`](references/multilingual-community-examples.md) | 来自安全社区模式挖掘的原创中文、俄文、日文、韩文、西文和混合语言提示词结构。 |
| [`platform-surface-matrix.md`](references/platform-surface-matrix.md) | 模型 vs 平台的声明边界。 |
| [`model-name-map.md`](references/model-name-map.md) | Seedance 命名、Fast 变体和 Pro 标签注意事项。 |
| [`first-last-frame-guide.md`](references/first-last-frame-guide.md) | FLF2V、首帧和末帧提示。 |
| [`field-observed-tips.md`](references/field-observed-tips.md) | 安全的实践者工作流模式。 |
| [`community-source-methodology.md`](references/community-source-methodology.md) | 安全的公开语料挖掘和标注规则。 |
| [`platform-constraints.md`](references/platform-constraints.md) | 稳定的平台风险规则。 |
| [`quick-ref.md`](references/quick-ref.md) | 紧凑的路由和提示词清单。 |
| [`reference-workflow.md`](references/reference-workflow.md) | 如何映射图像、视频、音频和分镜参考。 |
| [`i2v-guide.md`](references/i2v-guide.md) | 图像到视频最佳实践。 |
| [`prompt-examples.md`](references/prompt-examples.md) | 安全的可复制粘贴提示词范例。 |
| [`genre-guides.md`](references/genre-guides.md) | 类型专属提示词模式。 |
| [`storytelling-framework.md`](references/storytelling-framework.md) | 叙事设计和视觉分层。 |
| [`intent-vs-precision.md`](references/intent-vs-precision.md) | 意图优先的哲学。 |
| [`audio-guide.md`](references/audio-guide.md) | 音频、对白、节拍同步和对口型指引。 |
| [`anti-slop-lexicon.md`](references/anti-slop-lexicon.md) | 弱短语替换表。 |
| [`filter-vocab.md`](references/filter-vocab.md) | 针对被拦截/降级提示词的更安全用词。 |
| [`frontend-design-system.md`](references/frontend-design-system.md) | README 和 SVG 设计标准。 |
| [`json-schema.md`](references/json-schema.md) | 用于管线的结构化提示词包装。 |
| [`eval-rubric.md`](references/eval-rubric.md) | 如何评判 eval 输出。 |
| [`progressive-disclosure.md`](references/progressive-disclosure.md) | 根、子技能和参考的边界。 |
| [`vocab/en.md`](references/vocab/en.md) | 英语精度词汇、套话陷阱和过滤误触修复。 |
| [`vocab/zh.md`](references/vocab/zh.md) | 用于紧凑提示词的中文电影词汇。 |
| [`vocab/ja.md`](references/vocab/ja.md) | 用于紧凑提示词的日语电影词汇。 |
| [`vocab/ko.md`](references/vocab/ko.md) | 用于紧凑提示词的韩语电影词汇。 |
| [`vocab/es.md`](references/vocab/es.md) | 用于紧凑提示词的西班牙语电影词汇。 |
| [`vocab/ru.md`](references/vocab/ru.md) | 用于紧凑提示词的俄语电影词汇。 |

## 安装 {#install}

对 Agent Skills 的客户端支持仍因工具而异。Codex 将一个技能记录为一个目录，含必需的 `ZH_REFERENCE.md`，可选的 `scripts/`、`references/`、`assets/`，以及可选的 `agents/` 元数据。

Codex 从工作目录向上扫描 `.agents/skills` 位置，外加用户/管理员/系统技能位置。一个带 `ZH_REFERENCE.md` 的仓库根形如技能文件夹，但仍需被安装/复制到被扫描的技能目录下，或作为插件分发以便自动发现。

这个仓库现在包含 `agents/openai.yaml` 和一个本地 Codex 安装器。要在这台 Windows 工作站或任何本地 Codex 配置上安装它，运行：

```bash
python scripts/install_codex_skill.py --force
```

当设置了 `CODEX_HOME` 时，安装器把仓库复制到 `$CODEX_HOME/skills/seedance-20`，否则复制到 `~/.codex/skills/seedance-20`。安装后重启 Codex，使 `$seedance-20` 出现在可用技能列表中。

这个仓库把密集的事实保留在参考中，使有效技能保持小巧。

如果你的客户端支持直接从 GitHub 仓库安装技能，使用这个仓库 URL：

```text
https://github.com/Emily2040/seedance-2.0
```

对于手动安装，把这个仓库复制到你的智能体客户端使用的技能目录。目录名应与根技能名 `seedance-20` 一致。把下表当作要在你自己客户端中验证的常见本地目标，而非普适支持保证。

| 平台 | 典型安装目标（在你的客户端中验证） |
|---|---|
| Claude Code | `.claude/skills/seedance-20/` |
| Codex | `.agents/skills/seedance-20/` 或经 `scripts/install_codex_skill.py` 安装到 `~/.codex/skills/seedance-20/` |
| Google Antigravity | `.agents/skills/seedance-20/`（工作区）或 `~/.gemini/antigravity-cli/skills/seedance-20/`（全局） |
| OpenClaw | 工作区 `skills/seedance-20/` 或经 `openclaw skills install` 安装到 `~/.openclaw/skills/seedance-20/`（ClawHub 兼容；技能已携带 `openclaw:` 元数据） |
| Hermes Agent | 项目 `skills/seedance-20/` 或经 `hermes skills install` 安装到 `~/.hermes/skills/seedance-20/` |
| Gemini CLI 风格工作区 | `.gemini/skills/seedance-20/` |
| GitHub Copilot 工作区 | `.github/skills/seedance-20/` |
| Cursor 工作区 | `.cursor/skills/seedance-20/` |
| Windsurf 工作区 | `.windsurf/skills/seedance-20/` |

## 验证 {#validation}

在每次发布前运行这些检查：

```bash
python scripts/validate_skills.py --strict
python scripts/content_audit.py --strict
python scripts/eval_schema_check.py --strict
python scripts/design_audit.py --strict
python scripts/source_registry_check.py --strict
python scripts/vocab_schema_check.py --strict
python scripts/project_state_check.py --strict
python scripts/continuity_chain_check.py --strict
python scripts/behavior_contract_check.py --strict
python scripts/sequence_eval_check.py --strict
python scripts/generation_run_check.py --strict
python scripts/prompt_lint.py --self-test --strict
python -m unittest discover -s tests -v
python -m compileall scripts tests
git diff --check
```

CI 工作流在 push 和 pull request 上运行相同的检查。

## 设计标准

首页遵循一套编辑型设计系统，而非默认 AI 风格：暖色的墨与纸主题、衬线展示字体搭配等宽规格标签、单一琥珀强调色，以及细线电影母题——无渐变、无辉光。

报头和运行图是手工构建的主题感知 SVG（`assets/hero-dark.svg`、`assets/hero-light.svg`、`assets/skill-map.svg`），通过 `prefers-color-scheme` picture 元素提供；生成的位图艺术仅存在于精选的视觉画廊，包括文字密集型信息图。

README 必须在 GitHub 移动端、暗色模式和窄宽度下保持可读。SVG 资源必须包含 `<title>` 和 `<desc>` 元素，仅使用内部 CSS，并避免外部字体、脚本或资源。Token 和规则见 [`references/frontend-design-system.md`](references/frontend-design-system.md) 和 [`docs/frontend-redesign.md`](docs/frontend-redesign.md)。

## 变更日志 {#changelog}

见 [`CHANGELOG.md`](CHANGELOG.md)。当前发布：**v6.1.0**。

## 许可证

MIT © 2026 Iamemily2050 (@iamemily2050)
