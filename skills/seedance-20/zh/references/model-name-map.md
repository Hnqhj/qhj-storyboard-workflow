# 模型名称映射（Model Name Map）

last_verified: 2026-06-20

当用户说 "Seedance Pro"、"Seedance V2"、"Seedance V2 Mini"、"Seed2.0 Pro" 或某个 wrapper 特定的模型名时，使用本文件。

## 规范名称（Canonical Names）

| 名称 | 含义 | 指引 |
|---|---|---|
| Seedance 2.0 | ByteDance Seed 视频生成模型系列 | v2 视频模型家族的正确公开名。用作默认措辞。 |
| Seedance 2.0 Fast | 官方/产品与 wrapper 平台报告的更快 Seedance 2.0 变体 | 当活动平台暴露它时，用于草稿、迭代或低延迟讨论。重新核对确切的分辨率、时长和定价。 |
| Seedance 2.0 Mini | 在 Volcengine、BytePlus 和 Dreamina 平台上暴露的更轻量官方 Seedance 2.0 系列通道 | 仅当活动平台暴露 Mini 时使用。把 `Seedance V2 Mini` 当作简写，而非规范措辞。实时重新核对 API 可用性、时长、分辨率、定价和账户门槛。 |
| Doubao Seedance 2.0 | Volcengine/Doubao 口味的平台命名 | 当作产品/API 平台标签，而非一种不同的创作方法。 |
| `doubao-seedance-2-0-260128` | 在 5 月 29 日教程中观察到的 Volcengine Ark 模型 ID | 仅在重新核对活动控制台/文档后用于实现示例。不要当作通用的 BytePlus/全球可用性。 |
| `doubao-seedance-2-0-fast-260128` | 在 5 月 29 日教程中观察到的 Volcengine Ark Fast 模型 ID | 仅当活动平台暴露 Fast 变体且当前定价/限制已核对时使用。 |
| `doubao-seedance-2-0-mini-260615` | 在 2026-06-20 官方文档中观察到的 Volcengine Ark Mini 模型 ID | 仅在 Volcengine 上、且重新核对 6 月 15 日–6 月 22 日的仅试用门槛是否已结束、API 访问是否上线后使用。 |
| `doubao-seedance-2-0-pro-260215` | Volcengine Ark Pro 模型 ID（2026-06-14 报告，此处未经控制台核实） | 仅在重新核对实时 Ark 控制台后使用。不要与 `doubao-seed-2-0-pro-*` LLM 混淆（见"非 Seedance"小节）。 |
| `dreamina-seedance-2-0-260128` / `-fast-260128` | BytePlus ModelArk 模型 ID——Volcengine `doubao-` ID 的国际对应版（2026-06-14 报告） | BytePlus 用 `dreamina-` 前缀，而 Volcengine 用 `doubao-`。同一模型家族、不同平台；引用前重新核对实时 ModelArk 文档。 |
| `dreamina-seedance-2-0-mini-260615` / `dreamina-seedance-2.0-mini` | 在 2026-06-20 官方文档中观察到的 BytePlus ModelArk Mini 模型 ID 和定价行标签 | 仅在 BytePlus 上使用。带连字符的 ID 和带点的定价标签是平台特定的；实现前实时重新核对 API 支持、定价和 1080p 支持。 |
| `seedance2` | Runway API 模型 ID | 仅用于 Runway 的 API 平台。不要替代 Volcengine/Doubao 模型 ID。 |
| fal Seedance 2.0 端点 | fal 托管的 Seedance 2.0 平台：`text-to-video`、`image-to-video`、`reference-to-video`，每个都带 `/fast` 档位 | 仅在 fal 平台使用 fal 端点命名（2026-06-09 验证）。引用前实时重新核对端点 ID、分辨率档位和按秒计价。不要替代 Volcengine、Doubao 或 Runway 模型 ID。 |
| `seedance-2.0-text-to-video` | EvoLink 在其公开 Seedance 2.0 页面上显示的模型值 | 仅在 EvoLink 的 API 平台使用。实现前重新核对图像/参考/视频模式、定价、回调支持和人脸/参考策略。 |
| `bytedance/seedance-2.0` | 在公开模型页面上看到的 OpenRouter 模型 slug 及相关供应商/路由命名 | 仅用于记录它的供应商/路由平台。编码前重新核对该路由是否支持文生视频、图生视频、首/尾帧或多模态参考输入。 |
| PiAPI `seedance` 加 `seedance-2-preview` / `seedance-2-fast-preview` | 来自 PiAPI 公开 Seedance 文档的任务模型和任务类型模式 | 仅与 PiAPI 的通用任务 API 一起使用。引用前重新核对当前任务类型、低限制变体、资产库要求和定价。 |
| Runware `bytedance:seedance@2.0` / `bytedance:seedance@2.0-fast` | 在公开模型文档中可见的 Runware 模型 ID | 仅在 Runware 上使用。重新核对确切的操作支持，因为供应商页面可能以不同方式对文、图、视频、音频、编辑和扩展进行分组。 |
| LaoZhang `/seedance/api/v3` 路由 | LaoZhang 供应商特定的 Seedance API 平台 | 仅当用户面向 LaoZhang 时使用。在当前 LaoZhang 文档中重新核对端点路径、模型值、鉴权和任务生命周期。 |
| Kie.ai、ModelsLab、AI/ML API、MuAPI、SeeGen、Segmind Seedance 路由 | 供应商特定的 wrapper 或路由名称 | 当作供应商特定标签，而非规范名称。实现前实时重新核对文档和账户访问，尤其是人脸/参考处理和输出权利。 |
| Seedance V2 | 社区简写 | 规范化为 Seedance 2.0，除非用户明显指的是某个 wrapper 特定模型。如果用户说 `Seedance V2 Mini`，仅在核对活动平台后规范化为 Seedance 2.0 Mini。 |
| Seedance 2.0 Pro | 含糊的社区简写 | 不要假设这是官方视频模型名。询问是哪个平台，或带保留地规范化为 Seedance 2.0 / Fast。 |
| Seed2.0 Pro | 在 Seedance 视频模型系列之外看到的独立 Seed/Doubao 命名 | 不要与 Seedance 2.0 视频生成混淆。 |
| Seedance 1.5 Pro | 更早的 Seedance 世代 | 仅用于历史比较。不要把它的限制与 Seedance 2.0 混在一起。 |

## 回答模式（Answer Pattern）

如果用户说 "Seedance 2.0 Pro"，回答：

`I will treat this as Seedance 2.0 unless you mean a specific wrapper's Pro label. Official public video-model wording is Seedance 2.0 and, on some surfaces, Seedance 2.0 Fast. Seed2.0 Pro is a different naming lane and should not be used as the Seedance video model name without source confirmation.`

如果用户说 "Seedance V2 Mini"，回答：

`I will treat this as Seedance 2.0 Mini only if the active surface exposes the Mini lane. Official source-visible examples are Volcengine's doubao-seedance-2-0-mini-260615 and BytePlus ModelArk's dreamina-seedance-2-0-mini-260615; API access, pricing, duration, and resolution are surface-specific and need a live recheck.`

## 非 Seedance 模型（不要混淆）

这些不是 Seedance，不应触发 Seedance 特定的语法、规格或平台。版本于 2026-06-14 验证；引用前重新核对。

| 名称 | 它实际上是什么 | 备注 |
|---|---|---|
| Seedream（如 Seedream 4.5） | ByteDance 的**图像**生成模型 | 同一厂商、近乎相同的名字（Seedr**ea**m 对 Seed**a**nce）。最高混淆风险。不是视频。 |
| Doubao-Seed-2.0（`doubao-seed-2-0-pro-*`） | ByteDance 在 Volcengine 上的 **LLM** | 共享 Ark 平台和 "Seed" 血统，但它是语言模型，不是 Seedance 视频。 |
| Doubao-Seed-2.0 Mini（`doubao-seed-2-0-mini-*`） | ByteDance 的 **Seed/Doubao** 模型命名通道，不是 Seedance 视频 | 不要把它与 `doubao-seedance-2-0-mini-260615` 混淆。缺少的 `ance` 很关键。 |
| Sora 2（OpenAI） | 竞争视频模型 | 注意：OpenAI 宣布 Sora 落幕——应用约 2026 年 4 月关闭，API 约 2026 年 9 月结束。不是 Seedance。 |
| Veo 3.1（Google） | 竞争视频模型（家族：3.1 / Fast / Lite） | "Veo 3" 是上一代。不是 Seedance。 |
| Kling 3.0（快手） | 竞争视频模型（"Omni" = 其多模态变体） | 不是 Seedance。 |
| Runway Gen-4.5 | Runway 自己的视频模型系列 | 与 Runway 通过其 API *托管* Seedance 2.0 不同。不是 Seedance。 |
| Hailuo / Vidu / Luma Ray3 / Pika / Wan | 其他竞争视频模型 | 不是 Seedance。 |

对于这些，仅提供通用电影工艺——绝不提供 Seedance 参考标签、镜头语法或平台特定设置。

## Wrapper 名称（Wrapper Names）

第三方 wrapper 可能暴露诸如 `doubao-seedance-2.0`、`doubao-seedance-2.0-fast`、OpenRouter 风格的 slug、PiAPI 任务类型、Runware ID 或带供应商前缀的变体等名称。它们对实现可能有用，但不是本仓库对官方命名的真相来源。

不要从 JavaScript 渲染的定价页面引用当前 BytePlus Seedance 2.0 定价或模型 ID，除非该值已在当前官方页面或控制台中验证。Volcengine 价格只能附上来源日期、模型、平台、币种和重新核对警告后引用。
