# Seedance 2.0 API 与平台状态

last_verified: 2026-06-20
confidence: 截至核实日期的公开来源快照；在注明处适用分节日期（Seedance 2.0 Mini、附加 provider/router 以及面向中国的搜索记录于 2026-06-20，平台防护与分辨率记录于 2026-06-14，海外 API 状态与 Replicate 记录于 2026-06-13，fal 一节于 2026-06-11 重新核实，更早的界面分节核实于 2026-05-30）；不保证每个界面上的访问权、定价、模型 ID、上传上限、授权行为或区域可用性

## 经公开来源确认

- 字节跳动官方 Seedance 2.0 页面描述了一个统一的多模态音视频架构，支持文本、图像、音频和视频输入。
- 字节跳动的发布帖称 Seedance 2.0 最多可使用 9 张图像、3 段视频片段、3 段音频片段，外加自然语言指令。
- 官方材料称参考可以引导视觉构图、相机语言、运动节奏、视觉效果和声音特征。
- 官方材料把视频延展与编辑描述为受支持的创作工作流。
- 官方材料描述了 15 秒多镜头音视频输出和双通道音频。
- arXiv 模型卡对于模型家族背景很有用，包括 4-15 秒音视频生成、论文中的原生 480p/720p 取景，以及一个 Fast 变体。
- 火山引擎/Ark 文档发布了 Seedance 2.0 教程和视频生成 API 导航，包括创建/查询/列表/取消-删除任务流程，但确切的 schema、价格、模型 ID、区域和限制必须实时重新核实。
- 火山引擎的模型列表页观察到于 2026-05-29 更新。
- 火山引擎的 Seedance 2.0 教程现在列出了 Mini 试用通知和 `doubao-seedance-2-0-mini-260615`，与较早的 `doubao-seedance-2-0-260128` 和 `doubao-seedance-2-0-fast-260128` 模型 ID 并列。
- 火山引擎的通用视频生成教程观察到于 2026-05-29 更新，是当前用于重新核实任务生命周期、首/末帧角色、return-last-frame、网页搜索工具，以及文件/参考组合的第一方场所。
- 火山引擎的提示词指南观察到于 2026-05-15 更新，强化了多模态参考提示。
- 火山引擎的定价页观察到于 2026-05-28 更新。引用火山引擎价格时只可附带界面、日期、币种、模型/分辨率/时长上下文，以及重新核实的提醒。对于未经实时验证的 JavaScript 渲染 BytePlus 页面，保留更强的"不报价"注意事项。
- 一篇火山引擎开发者社区文章称 Seedance 2.0 API 服务已上线，并提及人像/版权安全标准、人脸验证、人像授权、虚拟人像资产，以及 BytePlus 海外 API 服务。把这视为官方生态/新闻证据，而非 API 契约。
- 公开的 BytePlus 页面在静态抓取中可能是 JavaScript 渲染的。在未经实时官方验证的情况下，不要从此类页面引用 Seedance 2.0 BytePlus 定价或模型 ID。
- Runway 官方 Seedance 2 指南及其稳定的 Models、API Changelog、Inputs 和帮助页在 Runway 界面上列出了 Seedance 2.0/Seedance 2.0 Fast。Seedance 专属指南记录了 `seedance2` 示例和参考字段注意事项；若一个裸 HTTP 检查器报告 404，在弃用该来源前先通过浏览器/已索引的文档验证。
- BytePlus ModelArk 文档现在列出了 Dreamina Seedance 2.0 Mini、`dreamina-seedance-2-0-mini-260615`，以及 `dreamina-seedance-2.0-mini` 的定价行。把带连字符的 ID 和带点的定价标签视为 BytePlus 界面特有的名称，而非每个 provider 的规范名称。
- 2026-06-20 可见的附加 provider/router 页面包括 EvoLink、OpenRouter、Kie.ai、PiAPI、LaoZhang、Runware、ModelsLab、AI/ML API、MuAPI、SeeGen 和 Segmind。把它们视为界面特有的访问途径，而非官方的字节跳动/火山引擎/BytePlus 契约。
- 2026-06-20 面向中国的搜索确认最强来源仍为官方的 ByteDance Seed、火山引擎 Ark、BytePlus ModelArk、豆包、即梦/剪映，以及 CapCut/剪映界面。中文工作流帖、商业伙伴新闻或托管的 ComfyUI 工作流并非公开的 API 提供方，除非它们发布 provider 自有的 API 文档。
- 诸如 ComfyUI 之类的伙伴工作流文档暴露了 T2V、R2V 和 FLF2V 工作流词汇，但那些文档是界面特有的。
- 近期的音视频生成基准论文，包括 AVBench 和 VABench，对于围绕音视频一致性的评测词汇很有用，但它们不是 Seedance 平台访问来源。

## 海外 API 状态 —— 版权暂停 *(记录于 2026-06-13)*

权威报道（Variety 和 CNBC，2026 年 2 月-3 月）记录：在 Seedance 2.0 于 2026-02-12 在中国发布后，迪士尼、华纳兄弟、派拉蒙、Netflix 和美国电影协会就涉嫌 IP 侵权向字节跳动发出停止侵权函，字节跳动**暂停了计划中的海外 API 推出（约 2026-03-15）**，待解决并增加防护。这对指引意味着什么：

- 把海外/全球 Seedance 2.0 API 访问视为**有争议且易变的**，而非保证可用。在依赖任何界面之前，验证实时访问权、区域和版权立场。
- 第三方界面（fal、Atlas Cloud、Replicate、EvoLink、OpenRouter、Kie.ai、PiAPI、LaoZhang、Runware、ModelsLab、AI/ML API、MuAPI、SeeGen、Segmind 等）在不同日期展示过实时的 Seedance 2.0 端点；那并不确立稳定的官方全球可用性——访问权已经变动并可能再次变动。在投产前立即重新核实。
- 这场纠纷使本仓库的常设规则变得可操作而非假设性：绝不复现受保护角色、场景或真实人物肖像——正是这一行为触发了暂停。

## 平台防护 —— 现已上线 *(记录于 2026-06-14)*

权威报道（SCMP、CNBC、The Next Web，2026 年 2 月-4 月）记录了字节跳动为应对纠纷而为 Seedance 2.0 增加的防护。这些已不再是假设性的——把它们视为官方界面上的当前平台行为，并设计提示词以与之*协同*工作：

- **真实人脸输入拦截：** 从含有真实人脸的图像或视频生成被限制（反深伪）。不要假定真实人物参考会被接受；通过 `[skill:seedance-copyright]` 路由肖像工作。
- **受版权角色拦截：** 生成可辨识的受保护角色（如 Shrek、SpongeBob、Darth Vader）被拦截。这是执法，而不仅是政策——`[skill:seedance-filter]` 的原创角色改写才是可行路径。
- 输出上的**可见水印 + C2PA 内容凭证**，以及带主动 IP 监测的**隐形水印**（字节跳动声明即使在模型输出被分享或篡改之后，它也能识别并采取行动）。

对技能的含义：误报修复和 IP 安全改写不是可选的打磨——它们是一条提示词通过实时护栏的方式。界面特有行为仍会有差异；在当前界面上验证。

## 分辨率 —— 模型与界面 *(记录于 2026-06-14)*

主要来源（arXiv 模型卡和 ByteDance Seed 页面）声明 Seedance 2.0 的**原生输出分辨率为 480p/720p**。更高分辨率是**界面特有的，而非模型原生保证**，甚至单个界面的文档之间也会不一致：火山引擎/Ark（Pro）、BytePlus、Atlas Cloud、Runway 和 WaveSpeed 暴露 **1080p**；fal 的文字指南说 480p/720p，而其模型与定价页列出 1080p（见下方 fal 一节）。把 480p/720p 视为基线能力，把任何 1080p/"2K"主张视为需在调用时逐端点验证的界面特性——绝不当作通用的模型规格。

## fal —— 授权提供方，全球 *(添加于 2026-06-10；字段、分辨率和定价于 2026-06-11 重新核实)*

**端点：** `text-to-video`、`image-to-video`（起始图 + 可选 `end_image_url` 用于 A→B）、`reference-to-video`——每个都带一个 `/fast` 档位。
**时长：** 4–15 秒或 `auto`（模型按提示词复杂度调整大小；多镜头 → 更长）。**画幅：** 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / auto。
**参数 (t2v)：** `prompt`、`resolution`、`duration`、`aspect_ratio`、`generate_audio`（默认开启；**音频不额外收取生成费用**）、`seed`（**复现辅助，而非硬锁定**——即便同一 seed 输出也可能变化）。
**参数 (i2v)：** t2v 字段加上 `image_url`（起始帧）和可选 `end_image_url`（A→B）。不要把图像字段发给 t2v 端点。
**参数 (r2v)：** 参考素材放入数组字段 `image_urls`、`video_urls`、`audio_urls`（于 2026-06-11 验证）——不要为参考复用 i2v 的 `image_url`/`end_image_url` 字段；实现前重新核实实时 schema。
**参考 (r2v)：** @Image×9、@Video×3、@Audio×3、≤12 个文件。图像 JPEG/PNG/WebP ≤30 MB；视频 480–720p，合计 ≤15 秒、总计 <50 MB；音频 MP3/WAV 各 ≤15 MB，合计 ≤15 秒；**音频需要 ≥1 张图像或视频。**
**分辨率（于 2026-06-11 验证）：** 标准端点列出 480p/720p/**1080p（≈$0.682/秒）**；fast 端点上限为 720p。文字指南此前曾滞后于 schema——在调用时逐端点验证。
**定价（报价前实时验证）：** 720p 标准 ≈$0.30/秒 · fast ≈$0.24/秒 · 视频参考 ×0.6 · 1080p ≈$0.682/秒。
**提示：** 散文式执导；多镜头用 `Shot 1:/Shot 2:` 标签；r2v 文档还接受时间戳节奏短语作为次要提示。**Fast 档位：** 官方 fal 文档给 fast 端点相同的 schema 和多镜头支持；现场反馈在多镜头、慢动作和推轨运动上仍偏好标准档位——把那视为现场指引，而非 provider 文档。
**无专用 extend 端点**——extend 是 Dreamina 应用的特性。要在 fal 上续接一段片段，优先用 reference-to-video，把前一段片段作为视频参考（保留运动和音频上下文）；从前一段片段的末帧链式 image-to-video 是后备方案。

## Seedance 2.0 Mini *(记录于 2026-06-20)*

官方火山引擎和 BytePlus 文档现在把 Seedance 2.0 Mini 暴露为更轻量的 Seedance 2.0 系列分支。使用规范的公开措辞 `Seedance 2.0 Mini`，而非 `Seedance V2 Mini`，除非在引用用户或封装标签。

- **火山引擎 Ark：** 可见模型 ID `doubao-seedance-2-0-mini-260615`。火山引擎通知称从 2026 年 6 月 15 日到 6 月 22 日，它仅通过控制台体验中心提供且并发限制为 1，API 支持预计在北京时间 6 月 22 日之后。在给出 API 指令前于 6 月 22 日后重新核实此项。
- **BytePlus ModelArk：** 可见模型 ID `dreamina-seedance-2-0-mini-260615`；BytePlus 文档描述了通过 Model Playground 的相同 2026 年 6 月 15 日-6 月 22 日试用窗口限制。BytePlus 定价页也显示 `dreamina-seedance-2.0-mini` 行并声明该行不支持 1080p。报数前实时重新核实定价。
- **Dreamina/CapCut 网页：** 官方 Dreamina 页面把 Seedance 2.0 Mini 描述为更快/更低成本且在 Dreamina 中可用。把其工作流主张视为 Dreamina 网页界面行为，而非 API schema。

不要把 Seedance Mini ID 与 `doubao-seed-2-0-mini-*` 混淆，后者属于非 Seedance 的 Seed/豆包模型命名分支。

## 附加 Provider/Router 界面 *(记录于 2026-06-20)*

这些是第三方或 router 界面。它们对集成规划有用，但每一个都可能重命名模式、改动 schema、隐藏字段、改变定价，或施加其自有的审核与账号规则。

- **EvoLink：** 公开页面记录了 `POST /v1/videos/generations`、通过 `GET /v1/tasks/{task_id}` 轮询、Bearer 鉴权、`seedance-2.0-text-to-video`、4-15 秒时长、480p/720p/1080p 质量选项，以及按秒计费。
- **OpenRouter：** 模型页把 `bytedance/seedance-2.0` 列为视频模型，带 text-to-video、含首/末帧控制的 image-to-video，以及多模态 reference-to-video。把 provider 路由、token/秒计费和受支持的 provider 视为 OpenRouter 特有。
- **Kie.ai、PiAPI 和 LaoZhang：** 公开页面或文档列出 Seedance 2.0 API 访问，但 schema 各异。PiAPI 记录了一个通用任务 API，模型为 `seedance`，任务类型为 `seedance-2-preview` / `seedance-2-fast-preview`；LaoZhang 记录了 `/seedance/api/v3` 基础路径；Kie.ai 的公开页强调 API 访问和多模态支持。实现前重新核实确切字段。
- **Runware、ModelsLab、AI/ML API、MuAPI、SeeGen 和 Segmind：** provider 页面列出 Seedance 2.0、Seedance 2.0 Fast 或相关的字节跳动视频路由。仅把它们视为附加的 provider/router 候选；在未经实时验证的情况下，不要把它们的模型 ID、人脸处理、水印、版权或价格主张复制进官方示例。

## 面向中国的提供方搜索 *(记录于 2026-06-20)*

对于中国提供方的问题，从官方或字节跳动自有的界面开始：ByteDance Seed、火山引擎 Ark、BytePlus ModelArk、豆包、即梦/剪映，以及 CapCut/剪映。RunningHub 式的托管工作流可作为有用的工作流证据，商业伙伴报告可显示商业采用，但两者都不应被视为公开的 API 提供方，除非该提供方发布其自有的 API 文档、模型 ID、定价、账号访问规则和审核条款。

## 操作性措辞

除非更新的主要来源另有说明，否则使用此措辞：

> 截至 2026-06-20，公开的字节跳动来源把 Seedance 2.0 描述为一个统一的多模态音视频生成模型，带文本、图像、音频和视频输入。官方发布与模型卡材料称参考可包含最多 9 张图像、3 段视频片段和 3 段音频片段。火山引擎/Ark、Runway、fal 和附加的 provider/router 页面发布了 Seedance 2 文档或访问途径，但访问权、模型 ID、定价、文件上限、区域可用性、分辨率、音频组合规则、人脸/参考处理和人像授权仍是界面特有的，必须在投产使用前重新核实。

## 模型命名规则

- 对官方视频模型线使用 `Seedance 2.0`。
- 仅当当前界面暴露 Fast 变体时使用 `Seedance 2.0 Fast`。
- 仅当当前界面暴露 Mini 分支时使用 `Seedance 2.0 Mini`；把 `Seedance V2 Mini` 视为简写，而非规范命名。
- 仅对 Runway 的 API 界面使用 `seedance2`。
- 仅在该提供方界面上使用 provider/router 模型 ID，例如 EvoLink 的 `seedance-2.0-text-to-video`、OpenRouter 的 `bytedance/seedance-2.0`、PiAPI 任务类型，或 Runware 的 `bytedance:seedance@2.0`。
- 在没有当前来源的情况下，不要把 `Seedance 2.0 Pro` 称作官方视频模型名称。把它视为含糊的封装或社区措辞。
- 不要把 `Seed2.0 Pro` 或豆包/Seed 通用模型名称与 Seedance 视频生成混淆。

参见 [`model-name-map.md`](model-name-map.md)。

## 主张边界

- 说明 API 可用性、定价、模型 ID、上传上限、权益规则、速率限制和区域可用性必须对照当前主要来源核实。
- 除非当前主要来源如此说，否则避免主张某个 API 全球可用或不可用。
- 除非当前主要来源如此说，否则避免主张人脸或人像上传被普遍支持或普遍拦截。
- 把模型能力与产品界面行为分开。Dreamina/即梦、豆包、火山引擎/Ark、BytePlus/ModelArk、ComfyUI、fal、provider/router 界面和第三方封装可能各异。
- 把第三方封装价格和模型别名视为封装特有，而非官方。

## 已知限制类别

官方/provider 材料和现场观察指出以下区域脆弱：

- 细节稳定性，
- 超真实感，
- 动态活力，
- 多主体一致性，
- 文字渲染，
- 复杂编辑，
- 音频失真，
- 多说话者对口型，
- 产品/徽标保留，
- 真实人物授权与界面门控。

## 真实人物、人像与嗓音规则

真实人物的人脸、人像和嗓音工作流需要授权、法律/伦理合规，以及平台特定支持。不要从已上传的素材推断许可。不要在没有明确授权、合规适用规则与用户同意要求的工作流的情况下，帮助模仿公众人物、私人、名人或嗓音。

## 待重新核实的主要来源

- https://seed.bytedance.com/en/seedance2_0
- https://seed.bytedance.com/en/blog/seedance-2-0-official-launch
- https://replicate.com/bytedance/seedance-2.0
- https://variety.com/2026/film/news/paramount-disney-bytedance-cease-and-desist-seedance-ai-infringement-ip-1236663663/
- https://www.cnbc.com/2026/02/16/bytedance-safeguards-seedance-ai-copyright-disney-mpa-netflix-paramount-sony-universal.html
- https://arxiv.org/abs/2604.14148
- https://www.volcengine.com/docs/82379/1330310?redirect=1&lang=zh
- https://www.volcengine.com/docs/82379/1520757?lang=zh
- https://www.volcengine.com/docs/82379/2291680?lang=zh
- https://www.volcengine.com/docs/82379/2298881?lang=zh
- https://www.volcengine.com/docs/82379/2222480?lang=zh
- https://www.volcengine.com/docs/82379/1544106?lang=zh
- https://developer.volcengine.com/articles/7628567056649125942
- https://docs.byteplus.com/en/docs/ModelArk/2291680
- https://docs.byteplus.com/en/docs/ModelArk/1520757
- https://docs.byteplus.com/en/docs/ModelArk/1544106
- https://docs.byteplus.com/en/docs/ModelArk/1099320
- https://fal.ai/models/bytedance/seedance-2.0/text-to-video
- https://fal.ai/models/bytedance/seedance-2.0/image-to-video
- https://fal.ai/models/bytedance/seedance-2.0/reference-to-video
- https://docs.dev.runwayml.com/guides/seedance/
- https://docs.dev.runwayml.com/assets/inputs/
- https://evolink.ai/seedance-2-0
- https://openrouter.ai/bytedance/seedance-2.0
- https://kie.ai/seedance-2-0
- https://piapi.ai/seedance-2-0
- https://piapi.ai/docs/seedance-api/seedance-2
- https://docs.laozhang.ai/en/api-capabilities/seedance2-video-generation
- https://runware.ai/docs/models
- https://modelslab.com/seedance-2
- https://docs.aimlapi.com/api-references/video-models/bytedance/seedance-2.0
- https://muapi.ai/
- https://seegen.ai/
- https://www.segmind.com/models/seedance-2.0
- https://docs.dev.runwayml.com/guides/models/
- https://docs.dev.runwayml.com/api-details/api_changelog/
- https://help.runwayml.com/hc/en-us/articles/50488490233363-Creating-with-Seedance-2-0
- https://docs.comfy.org/zh/tutorials/partner-nodes/bytedance/seedance-2-0
- https://arxiv.org/abs/2605.24652
- https://openaccess.thecvf.com/content/CVPR2026/papers/Hua_VABench_A_Comprehensive_Benchmark_for_Audio-Video_Generation_CVPR_2026_paper.pdf
