# 来源登记表

last_verified: 2026-06-20

在对 Seedance 2.0 平台行为做出事实性声明之前，先使用本登记表。优先采用一手公开来源，附上验证日期，并将易变声明标记为需重新核查。本文件是一份声明边界地图，而非对每个产品平台或区域访问权限的保证。

## 证据标签

| 标签 | 含义 | 必需措辞 |
|---|---|---|
| `confirmed` | 在验证日期可直接在一手公开来源中看到。 | `Public sources state... as of [date].` |
| `volatile` | 可能因平台、账户、区域、定价页面或模型更新而变化。 | `Recheck before giving numbers or promises.` |
| `field-observed` | 反复出现的创作者/从业者模式，但非官方平台真相。 | `Field observation, not guaranteed platform behavior.` |
| `unverified` | 看似合理但未经一手来源确认。 | `Requires testing or owner confirmation.` |
| `internal` | 源自本 skill 包的仓库指引。 | `Use as workflow guidance, not external fact.` |

## 一手来源层级

| 主题 | 首选来源 | 证据标签 | 验证说明 | 声明边界 |
|---|---|---|---|---|
| 核心模型能力 | ByteDance Seedance 2.0 官方页面：https://seed.bytedance.com/en/seedance2_0 | confirmed | 在发布说明、API 声明或营销文案之前重新核查。 | 仅用于宽泛的公开能力框定。 |
| 发布能力与已知限制 | ByteDance Seedance 2.0 官方发布文章：https://seed.bytedance.com/en/blog/seedance-2-0-official-launch | confirmed | 讨论多模态参考、编辑、音频及平台示例时重新核查。 | 不要把发布示例当作每个平台上的保证行为。 |
| 模型卡与论文 | arXiv 模型卡：https://arxiv.org/abs/2604.14148 | confirmed | 对模型家族语境与基准告诫有用。 | 提供方撰写的论文；不要用作当前商业访问的证明。 |
| API 教程与平台文档 | BytePlus ModelArk 与 Volcengine Ark 文档：https://docs.byteplus.com/en/docs/ModelArk/2291680、https://docs.byteplus.com/en/docs/ModelArk/1520757、https://www.volcengine.com/docs/82379/1520757?lang=zh 及 https://www.volcengine.com/docs/82379/2291680?lang=zh | volatile | 在提供 API 流程指引之前，重新核查端点、请求字段、模型 ID、任务流与定价。 | API 形态可能因区域、账户、发布渠道或试用门槛而异。 |
| 视频生成任务生命周期 | Volcengine 视频生成教程：https://www.volcengine.com/docs/82379/2298881?lang=zh | volatile | 在实现之前，重新核查 create/query/list/cancel-delete 流程、首/尾帧角色、返回尾帧、工具及文件引用规则。 | 官方平台，但字段与账户支持可能变化。 |
| 模型 ID 与定价 | Volcengine 模型列表/定价及 BytePlus 定价页面，包括 https://docs.byteplus.com/en/docs/ModelArk/1544106 | volatile | 在引用数字或 ID 之前始终立即重新核查。Seedance 2.0 Mini 的 ID 在 2026-06-20 可在来源中看到，但在官方文档中访问到 6 月 22 日仍受试用门槛限制。 | Volcengine 价格只能在标注日期、货币、模型、平台与告诫的前提下引用；切勿从不完整的 JS 渲染页面推断 BytePlus 定价。 |
| API 服务生态新闻 | Volcengine 开发者文章：https://developer.volcengine.com/articles/7628567056649125942 | volatile | 用作 API 服务推出、安全标准、肖像授权、虚拟肖像及 BytePlus 海外服务声明的官方生态/新闻证据。在文档/控制台中重新核查实现。 | 非 API 合同、价格表或权益保证。 |
| BytePlus 定价页面 | BytePlus ModelArk 定价文档：https://docs.byteplus.com/en/docs/ModelArk/1544106 及旧文档如 https://docs.byteplus.com/en/docs/ModelArk/1099320 | volatile | 在引用 Seedance 2.0 定价、配额或模型 ID 之前，重新核查实时官方页面或控制台。BytePlus 目前显示 `dreamina-seedance-2.0-mini` 定价行，且该行不支持 1080p。 | 部分页面在静态抓取中由 JavaScript 渲染；不要从不完整的静态内容推断定价。 |
| 提示词指南 | Volcengine Seedance 2.0 提示词指南：https://www.volcengine.com/docs/82379/2222480?lang=zh | confirmed | 在添加多模态参考措辞或提示词示例时重新核查。 | 提示词建议是官方指引，而非每个平台都暴露每项控制的保证。 |
| 首/尾帧工作流 | Volcengine 教程与 ComfyUI 合作伙伴文档：https://www.volcengine.com/docs/82379/2298881?lang=zh 及 https://docs.comfy.org/zh/tutorials/partner-nodes/bytedance/seedance-2-0 | volatile | Volcengine 记录了首/尾帧角色；ComfyUI 使用 FLF2V 工作流词汇。在使用精确字段之前重新核查活跃平台。 | `FLF2V` 标签是平台特定的，但首/尾帧能力在 Volcengine 上有文档记录。 |
| 面孔、肖像与声音行为 | 活跃产品平台、官方政策与用户授权 | volatile | 重新核查当前平台行为与授权语境。 | 不要从文件上传推断同意。 |
| Runway Seedance 2 平台 | Runway API 与帮助文档：https://docs.dev.runwayml.com/guides/seedance/、https://docs.dev.runwayml.com/guides/models/、https://docs.dev.runwayml.com/api-details/api_changelog/、https://docs.dev.runwayml.com/assets/inputs/ 及 https://help.runwayml.com/hc/en-us/articles/50488490233363-Creating-with-Seedance-2-0 | volatile | 在生产使用之前，重新核查时长、画幅、音频/参考组合规则、上传处理、区域可用性、套餐要求及 SDK 支持。Seedance 专属指南携带最具模型特定性的 Runway 示例；如果原始 HTTP 检查器报告 404，在弃用之前通过浏览器/已索引文档验证。 | 官方 Runway 平台，非 ByteDance/Volcengine API 合同。 |
| fal Seedance 2.0 平台 | fal 模型/API 页面：https://fal.ai/models/bytedance/seedance-2.0/text-to-video、https://fal.ai/models/bytedance/seedance-2.0/image-to-video 及 https://fal.ai/models/bytedance/seedance-2.0/reference-to-video | volatile | 在引用数字或编写 API 调用之前，重新核查端点、请求字段、分辨率档位、时长及每秒定价。 | 官方 fal 平台行为，非 Volcengine、BytePlus 或 Runway 行为。Fast 端点共享已记录的 schema；fast 档位的多镜头可靠性下降是现场观察，而非官方。 |
| 其他提供方/路由平台 | 提供方自有页面与文档：https://evolink.ai/seedance-2-0、https://openrouter.ai/bytedance/seedance-2.0、https://kie.ai/seedance-2-0、https://piapi.ai/seedance-2-0、https://piapi.ai/docs/seedance-api/seedance-2、https://docs.laozhang.ai/en/api-capabilities/seedance2-video-generation、https://runware.ai/docs/models、https://modelslab.com/seedance-2、https://docs.aimlapi.com/api-references/video-models/bytedance/seedance-2.0、https://muapi.ai/、https://seegen.ai/ 及 https://www.segmind.com/models/seedance-2.0 | volatile | 在编写代码或引用数字之前，重新核查每个提供方页面、API 文档、端点基础 URL、模型 ID、定价、账户访问、审核、面孔/参考 schema、输出 URL 有效期及权利条款。 | 仅为第三方提供方/路由行为；非官方 ByteDance、Volcengine、BytePlus、Runway 或 fal 行为。本仓库不背书任何托管方。 |
| 面向中国的提供方检索 | 官方中文/产品来源：https://seed.bytedance.com/zh/seedance2_0、https://www.volcengine.com/docs/82379/2291680?lang=zh、https://www.volcengine.com/docs/82379/1520757、https://jimeng.jianying.com/ai-tool/home 及 ByteDance 自有的 Doubao/Jimeng/Jianying/CapCut 平台；工作流或新闻示例包括 RunningHub 工作流与商业合作伙伴报道 | field-observed | 在将中文结果视为公开 API 提供方之前，重新核查当前官方中文文档与提供方自有页面。 | 不要将工作流托管方、博客或商业合作伙伴新闻列为自助 API 平台，除非它们发布了提供方自有的 API 文档。 |
| Agent Skills 结构 | OpenAI Codex Agent Skills 文档：https://developers.openai.com/codex/skills、OpenAI Academy 插件/skills 讲解：https://openai.com/academy/codex-plugins-and-skills/、OpenAI Codex Plugins 文档及 Agent Skills 开放标准：https://agentskills.io/ | confirmed | 在更改安装指引或根 skill 布局之前重新核查。 | 打包指引，非 Seedance 平台能力。 |
| Runway MCP agent 平台 | Runway MCP 公告：https://runwayml.com/news/mcp | confirmed | 仅用于 agent 平台可用性。 | 不改变 Seedance 模型能力；套餐与连接器访问是 Runway 特定的。 |
| 音视频评估词汇 | AVBench 与 VABench 论文：https://arxiv.org/abs/2605.24652 及 https://openaccess.thecvf.com/content/CVPR2026/papers/Hua_VABench_A_Comprehensive_Benchmark_for_Audio-Video_Generation_CVPR_2026_paper.pdf | field-observed | 用于诸如音视频同步与跨模态一致性等评估维度。 | 基准框定，非产品访问或官方 Seedance 性能证明。 |
| 专业镜头语言 | ASC 运镜教育与制作镜头清单实践：https://theasc.com/article/shot-craft-camera-movement/ 及 https://www.studiobinder.com/blog/shot-list-template-free-download/ | field-observed | 用于镜头合同、运镜及镜头清单字段。 | 行业工作流指引，非 Seedance 能力证明。 |
| 连续性实践 | ScreenSkills 场记角色：https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/technical/script-supervisor-film-and-tv-drama/ | field-observed | 用于连续性锚点，如服装、道具、视线、画面方向及备注。 | 角色指引，非平台行为。 |
| 色彩管理与 ACES | ACES 文档与 AMF 规范：https://docs.acescentral.com/background/overview/ 及 https://docs.acescentral.com/amf/specification/ | confirmed | 用于调色管线词汇与交接元数据。 | 提示词可以描述一种观感；它无法认证 ACES 合规。 |
| 画幅与交付容器 | DCI、ISDCF 及买方/平台规范：https://www.dcimovies.com/dci-specification/ 及 https://registry-page.isdcf.com/ | field-observed | 用于画幅/容器分离与命名注意事项。 | 始终遵循合同约定的交付规范。 |
| 字幕与隐藏字幕 | Netflix 定时文本、WebVTT 及无障碍规则：https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements、https://w3c.github.io/webvtt/ 及 https://www.law.cornell.edu/cfr/text/47/79.1 | volatile | 用于字幕/SDH/强制旁白规划与字幕安全取景。重新核查买方、语言、区域及平台要求。 | 交付要求因买方、语言、区域及平台而异。 |
| 音频响度与后期 | ITU BS.1770、EBU R128、ATSC A/85 及买方声音规范：https://www.itu.int/rec/R-REC-BS.1770、https://tech.ebu.ch/fr/publications/r128、https://www.atsc.org/atsc-documents/a85-techniques-for-establishing-and-maintaining-audio-loudness-for-digital-television/ 及 https://partnerhelp.netflixstudios.com/hc/en-us/articles/360001794307-Netflix-Sound-Mix-Specifications-Best-Practices-v1-6 | volatile | 用于分轨、M&E、同步、响度及混音交接用语。重新核查目标买方或平台规范。 | 提示词音频不是经过认证的最终混音。 |
| 交付与 QC | SMPTE IMF、DPP 规范、Netflix 交付规范及 MovieLabs OMC：https://www.smpte.org/standards/st2067、https://www.thedpp.com/specs/、https://partnerhelp.netflixstudios.com/hc/en-us/sections/10066414335891-Delivery-Specifications 及 https://movielabs.com/ontology-for-media-creation/ | volatile | 用于交付预检与元数据/版本管理指引。在最终交付之前重新核查合同约定的平台规范。 | 合同约定的平台规范优先于通用指引。 |
| 社区实践 | 抖音、Bilibili、CSDN、Reddit、Habr、创作者笔记、工作流截图 | field-observed | 仅用作从业者指引。 | 标记为非官方；不要陈述为模型保证。 |
| 本地化与混合语言提示 | 日语、韩语、西班牙语、俄语及多语言社区指南加论坛观察 | field-observed | 在发布前重新核查公开页面；仅用于词汇与示例结构。 | 代码混合可以澄清安全提示词，但绝不要将其视为官方过滤行为或安全规避。 |
| 社区提示词语料库 | YouMind/OpenLab、公开提示词画廊、论坛合集 | field-observed | 仅在安全分类后挖掘结构、时序、词汇与失败模式。 | 不要将不安全、IP 敏感或真人提示词复制进活跃示例。 |
| 仓库指引 | README、ZH_REFERENCE.md、references、evals | internal | 与来源登记表及 API 状态保持一致。 | 工作流指引，非平台事实的外部来源。 |

## 必需的声明模式

回答平台状态问题时，说：`As of 2026-06-20, public official sources describe Seedance 2.0 as supporting text, image, audio, and video inputs, including multimodal references for composition, camera language, motion rhythm, visual effects, and sound. Volcengine documents first/last-frame roles, Runway documents a Seedance 2 surface, fal documents text-to-video, image-to-video, and reference-to-video endpoints, and additional provider/router pages list Seedance 2.0 access, but access, pricing, model IDs, upload limits, regions, resolution, audio-combination rules, face/reference handling, and authorization behavior remain surface-specific and should be rechecked.`

回答定价、配额、上传限额、模型 ID 或区域可用性问题时，不要猜测。说明这些值是易变的，需要核查当前官方平台。

回答相似性、肖像与声音问题时，分开三件事：技术平台支持、权利/授权及提示词安全。不要从文件上传推断同意。

使用社区来源时，说：`Field observation, not guaranteed platform behavior.`
