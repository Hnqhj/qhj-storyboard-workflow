---
name: seedance-pipeline
description: "This skill should be used when the user asks about Seedance 2.0 workflow operations, API planning, BytePlus ModelArk, Dreamina/Jimeng surfaces, provider/router APIs, China-facing surfaces, ComfyUI, post-production, stitching, batch workflow, or integration planning."
license: MIT
metadata:
  version: "6.1.0"
  updated: "2026-06-22"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-pipeline

将本技能用于操作性工作流、API、web 界面、后期制作和集成规划。

## 意图

每个 API 问题的背后，都有一个带着截止日期、预算，并把某件事押在"明天它能跑起来"上的人。本技能的灵魂，是成为房间里那个用日期、来源和路径来回答、而非用乐观主义来回答的声音。可靠，是这位用户所需要的善意。

## 状态规则

对于当前的 API 与平台主张，始终加载 `[ref:api-status]`。当用户说 Pro、Fast、V2 或某个封装模型 ID 时，加载 `[ref:model-name-map]`。不要依赖陈旧的发布状态记忆。
对于实现规划、任务生命周期、Runway/火山引擎/各 provider 字段差异、定价注意事项、上传处理和生产就绪度，加载 `[ref:api-workflow]`。
对于专业影视、商业广告、代理、本地化、后期和交付工作流，加载 `[ref:pro-filmmaking-standards]`。在说某项素材已可交付之前，加载 `[ref:delivery-qc]`。

## 工作流划分

1. Web 工作流：Dreamina/即梦界面、参考素材、提示词、输出审阅。
2. API 工作流：火山引擎、BytePlus、Runway、fal 或 provider/router 文档、模型 ID、鉴权、文件处理、任务创建、轮询/查询、取消/删除、任务台账和检索。
3. 专业制作工作流：处理稿、分镜表、连续性台账、参考素材版权映射、审核循环、后期交接，以及交付/QC。
4. 后期工作流：剪辑、套底、拼接、防抖、音频清理、字幕/隐藏字幕、调色、本地化、版本管理、无字版，以及交付。
5. 首/末帧工作流：映射首帧、末帧、过渡动作、身份锁定项，以及结尾目标。
6. Runway 工作流：模型 `seedance2`、`runway://` 上传、音频参考组合规则、套餐/区域注意事项，以及 SDK 类型滞后，这些都是 Runway 特有的。
7. Provider/router 工作流：EvoLink、OpenRouter、Kie.ai、PiAPI、LaoZhang、Runware、ModelsLab、AI/ML API、MuAPI、SeeGen、Segmind 或类似界面必须标注为 provider 特有，并在给出代码或定价指导前重新核实。
8. 面向中国的工作流：优先选用官方的字节跳动/火山引擎/BytePlus/豆包/即梦/剪映来源；在没有 provider 自有文档的情况下，工作流托管方、中文博客和商业伙伴新闻并非公开的 API 提供方。
9. 社区工作流：除非有来源，否则 ComfyUI 或非官方节点必须标注为社区/未验证。
10. 语料挖掘工作流：在复用前对来源进行分类；提取结构与词汇，而非不安全的原始提示词。

## 输出契约

返回工作流路径、来源状态、所需输入、制作阶段、验证步骤、交付假设和风险。对于专业作业，包含下一个要创建的产物：简报、分镜表、连续性台账、提示词批次、审核包、本地化矩阵或 QC 预检。
