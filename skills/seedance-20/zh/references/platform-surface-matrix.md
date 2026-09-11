# 平台矩阵（Platform Surface Matrix）

last_verified: 2026-06-20

Seedance 2.0 的能力声明必须把模型与产品平台分开。一项功能对模型为真，同时仍可能在某个特定平台上被门控、不可用、被改名、定价不同或受策略限制。

访问说明（2026-06-13）：海外 Seedance 2.0 API 在一次版权驱动的暂停后存在争议——见 `api-status.md`。在依赖任何第三方平台前实时验证访问，并且未独立确认其托管 Seedance 2.0 之前，不要在此添加任何平台。

| 平台 | 证据类型 | 典型用途 | 当前指引 |
|---|---|---|---|
| ByteDance Seed 官方模型页 | 官方 | 宽泛的能力框定 | 仅用于高层模型定位。它确认了多模态音视频生成、参考、表演、布光、阴影和摄影机控制。 |
| ByteDance 官方发布帖 | 官方 | 能力细节与已知限制 | 用于关于输入模态、参考数量、视频扩展/编辑、双声道音频和遗留弱点的最强公开声明。 |
| Volcengine Ark / ModelArk 文档 | 官方平台文档 | API 任务流程与模型平台 | 在给出端点、区域、配额、定价或文件限制前重新核对。截至 2026-06-20，Volcengine 以 `doubao-seedance-2-0-mini-260615` 暴露 Seedance 2.0 Mini，但官方文档称其在 6 月 22 日前为试用门控。 |
| Volcengine 视频生成教程 | 官方平台文档 | 异步任务生命周期、首/尾帧角色、返回尾帧、网络搜索工具和参考文件组合 | Volcengine 字段的 5 月 29 日当前信号。仅用于 Volcengine；实现前重新核对确切 schema、权益、定价和人脸参考行为。 |
| Volcengine 开发者社区文章 | 官方生态/新闻文章 | API 可用性、安全与采用语境 | 对记录 API 服务推出、肖像/版权标准、人脸验证、虚拟肖像和 BytePlus 海外服务有用。不要当作 API schema、定价表或账户权益保证。 |
| BytePlus ModelArk 文档 | 官方平台文档 | 国际 API 与文档平台 | 在生产指引前重新核对。BytePlus 以 `dreamina-seedance-2-0-mini-260615` 和一个 `dreamina-seedance-2.0-mini` 定价行暴露 Seedance 2.0 Mini，但只引用可见或独立验证的声明。 |
| Runway Seedance 2 | 官方第三方平台 | 带 Seedance 2 模型访问的 API/网页生成 | Runway 记录了 `seedance2`、5–15 秒时长、图像/视频/音频参考、上传 URI、音频组合规则和套餐/区域注意事项。当作 Runway 平台行为，而非 Volcengine 或 BytePlus 行为。 |
| Runway MCP | 官方智能体连接器平台 | 智能体可访问的图像/视频生成 | 对智能体工作流规划有用。它不证明 ByteDance API 访问，也不改变 Seedance 模型限制。 |
| fal | 官方第三方平台 | 通过 fal 的 Seedance 2.0 端点生成 | 2026-06-09 验证：fal 记录了 text-to-video、image-to-video（起始图加可选结束图）和 reference-to-video，每个都带 /fast 档、4–15 秒或 auto 时长、六种宽高比加 auto，以及按秒计价。fal 的文字指南说 480p/720p，而模型和定价页面列出 1080p——在调用时按端点验证分辨率。此平台无 extend 端点。当作 fal 平台行为，而非 Volcengine 或 BytePlus 行为。 |
| Atlas Cloud | 第三方聚合器平台 | 通过异步视频生成 API 托管 Seedance 2.0 | 2026-06-13 验证：Atlas Cloud 托管实时 Seedance 2.0（text-to-video、image-to-video、reference-to-video，外加 fast 变体）。其 OpenAI 兼容端点仅覆盖 LLM/chat；**Seedance 视频生成使用 Atlas Cloud 自己的异步 API**——`POST /api/v1/model/generateVideo`，带诸如 `bytedance/seedance-2.0/text-to-video` 的模型 id，返回一个在 `/api/v1/model/prediction/{id}` 轮询的 prediction id——而非 OpenAI SDK 形态。它是数个转售 Seedance 访问的聚合器之一；把端点、定价、模型 ID、配额和护栏当作聚合器特定的，使用前重新核对，且绝不呈现为官方 ByteDance 行为。本仓库不为任何转售商背书；为完整性列出。 |
| Replicate | 第三方模型托管平台 | 在官方 `bytedance` 命名空间下托管 Seedance 2.0 | 2026-06-13 验证：Replicate 在其标准异步 prediction API 后列出 `bytedance/seedance-2.0`（text-to-video、image-to-video、多模态参考输入 `[Image1]/[Video1]/[Audio1]`、原生音频）；查模型页面获取支持的分辨率，而非假设模型级最大值。一个信誉良好、广泛使用的模型托管——但仍是平台特定的：重新核对定价、限制和实时访问（见 `api-status.md` 中的海外 API 状态说明），且绝不呈现为官方 ByteDance 行为。本仓库不为任何托管背书；为完整性列出。 |
| WaveSpeedAI / Higgsfield / Pollo | 第三方托管平台 | 额外的已验证 Seedance 2.0 托管 | 2026-06-14 验证（供应商自有页面）：WaveSpeedAI（异步作业 API，t2v/i2v + fast/turbo/"spicy" 变体，480p/720p/1080p 档），Higgsfield（创作者 UI，多模态输入；未发现明确记录的公开 API），Pollo（网页模型页 + 统一作业 API）。与每个托管同样的规则：视频用异步提交/轮询，实时重新核对，聚合器/托管特定而非官方。本仓库不为任何一个背书。 |
| EvoLink / OpenRouter / Kie.ai / PiAPI / LaoZhang | 第三方供应商/路由平台 | 额外的 Seedance 2.0 API 访问路由 | 2026-06-20 从供应商自有页面或文档验证：EvoLink 记录 `/v1/videos/generations` 加 `/v1/tasks/{task_id}`；OpenRouter 列出 `bytedance/seedance-2.0`；PiAPI 记录带 Seedance 任务类型的通用任务 API；LaoZhang 记录 `/seedance/api/v3` 基路径；Kie.ai 发布 Seedance 2.0 API 访问。把模型 ID、鉴权、基 URL、轮询、定价、人脸/参考支持、输出 URL 和内容策略当作供应商特定的。本仓库不为任何转售商背书。 |
| Runware / ModelsLab / AI/ML API / MuAPI / SeeGen / Segmind | 第三方供应商/路由平台 | 额外的 Seedance 2.0 或 Seedance 2 Fast 模型托管路由 | 2026-06-20 从供应商自有页面或文档验证。这些页面列出 Seedance 2.0、Seedance 2.0 Fast 或相关 ByteDance 视频路由，但它们的字段和模型名各异。仅在核对实时文档和账户访问后，把它们当作供应商特定集成的候选。本仓库不为任何转售商背书。 |
| Dreamina / 即梦 网页 UI | 官方产品平台 | 创作者工作流 | 行为可能与 API 不同。不要把网页 UI 的限制、积分、人脸检查或上传规则推广到每个平台。 |
| Dreamina Seedance 2.0 Mini | 官方产品平台 | 更低成本/更快的 Dreamina 网页生成通道 | 仅作为 Dreamina 网页平台证据。不要在不核对 Volcengine/BytePlus 文档或控制台的情况下，从营销文案推断 API 字段、模型 ID、定价或 1080p 支持。 |
| ComfyUI 合作伙伴节点文档 | 合作伙伴工作流文档 | T2V、R2V、FLF2V 工作流 | 对工作流词汇和平台注意事项有用。标为 ComfyUI 特定而非通用 Seedance 行为。 |
| 第三方 wrapper | 社区/商业 wrapper | 访问抽象 | 仅对实地模式和集成思路有用。不要把 wrapper 的模型名、价格或护栏行为呈现为官方。 |
| 社区提示词语料 | 实地观察 | 提示词模式挖掘 | 挖掘结构、时序语法、词汇和失败模式。不要直接抄袭不安全、IP 敏感或真人示例。 |
| Agent Skills 文档 | 智能体打包文档 | 仓库布局与安装语言 | 用于技能结构和渐进式披露指引。不要把仓库安装路径当作通用客户端保证。 |

## API 形态规则（API Shape Rule）

2026-06-20 在此处核查的每个开发者平台（fal、Replicate、Volcengine Ark、BytePlus ModelArk、Atlas Cloud、Runway、WaveSpeed、Pollo、EvoLink、OpenRouter、Kie.ai、PiAPI、LaoZhang、Runware、ModelsLab、AI/ML API、MuAPI、SeeGen、Segmind）均已验证：Seedance 2.0 的**视频生成始终是一个异步作业**——提交任务、获得 id、轮询至就绪、取 URL。一些路由把作业包在统一或 OpenAI 兼容的平台里，但视频生成本身仍使用供应商特定的异步语义。绝不要把 LLM/chat 请求形态交给用户用于 Seedance 视频。

## 面向中国的搜索说明（China-Facing Search Note）

2026-06-20 的中文搜索发现，面向中国的官方平台已在此列出：ByteDance Seed、Volcengine Ark、BytePlus ModelArk、Doubao、即梦/剪映，以及 CapCut/剪映。RunningHub 式的托管 ComfyUI 工作流和中文商业合作伙伴新闻可作有用语境，但除非供应商自有 API 页面暴露端点、模型 ID、定价、账户访问和策略条款，否则它们不是自助 API 平台。

## 平台特定声明（Surface-Specific Claims）

在回答关于生产使用的问题时，包含：

- 平台名，
- 验证日期，
- 已知的模型或工作流名称，
- 该声明是官方、合作伙伴、wrapper 还是实地观察，
- 使用前必须重新核对什么。

## 真人规则（Real-Person Rule）

真人图像、肖像和声音是授权敏感的。一些平台可能提供身份验证流程，另一些可能拒绝或限制真人参考。不要从上传的资产推断同意。

## V2V、R2V 和 FLF2V 边界（V2V, R2V, and FLF2V Boundary）

ByteDance 官方材料支持多模态参考、I2V/R2V 示例、编辑和扩展。Volcengine 现已在其视频生成平台上记录首帧和尾帧角色。把 `FLF2V` 保留为一个标签注意事项，因为工作流名称因产品平台而异，但不要说首/尾帧本身仅限合作伙伴。
