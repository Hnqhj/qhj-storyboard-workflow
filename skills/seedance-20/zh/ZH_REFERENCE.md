---
name: seedance-20
description: "This skill should be used when creating, improving, or troubleshooting Seedance 2.0 video on any surface - Dreamina, Jimeng, CapCut, Doubao, Volcengine/Ark, BytePlus, Runway's Seedance route, fal, or third-party provider/router surfaces such as EvoLink, OpenRouter, Kie.ai, PiAPI, LaoZhang, Runware, ModelsLab, AI/ML API, MuAPI, SeeGen, and Segmind - including text/image/video/reference-to-video prompts, first/last frame, dialogue, lip-sync and audio, IP-safe rewrites, API, pricing and model-ID questions, and zh/ja/ko/es/ru prompt work. Not for non-Seedance models (Sora, Veo, Kling, Runway's own Gen models) or image-only prompting."
license: MIT
metadata:
  version: "6.1.0"
---

# seedance-20

面向智能体驱动视频创作的 Seedance 2.0 运行回路。使用这一根技能来路由请求、核查事实、保护参考素材，并在加载专门子技能之前让提示词保持精简。

## 灵魂（Soul）

这个技能存在的意义，是让一个带着「感觉」而来的人，最终带着一部「片子」离开。以下一切都由三条原则支配：

1. **听懂文字背后的意图。** 用户描述的是结果（「让它有家的感觉」），而不是参数。每一道关卡和每一个子技能都要把感觉翻译成手艺；任何一个环节都不得把翻译工作甩回给用户。
2. **让故事保持鲜活。** 在整场对话中持有一个故事状态：主体、模式、视觉风格、参考素材、已确定的约束，以及此前失败过的东西。每个技能在发问之前先读取它、在行动之后再更新它。用户永远不应被迫重复一个决定，新的请求会继承已经建立起来的世界。
3. **随用户一起成长。** 对新手说人话，对专业人士说导演的语言——并且要注意到同一个用户会在一个项目过程中从前者成长为后者。语域随之调整；标准永不降低。

## 运行回路（Operating Loop）

1. 接收（Intake）：识别用户的目标、制作阶段、目标平台、模式、时长、画幅比、参考素材、音频需求、交付物，以及安全/IP 风险。如果在接收阶段就浮现出明确的安全、IP、肖像或规避风险，应在任何规划之前直接跳到安全关卡（第 9 步）。
2. 来源关卡（Source gate）：在做任何平台事实声明之前，加载 `[ref:api-status]` 和 `[ref:source-registry]`。对于 Runway、Volcengine、fal、provider/router，或面向中国大陆的平台细节，还应加载 `[ref:platform-surface-matrix]`。
3. 专业关卡（Professional gate）：如果用户要求电影、广告、营销战役、客户、交付、本地化、调色、声音、字幕、后期、QC 或多镜头工作，在起草前先加载 `[ref:pro-filmmaking-standards]`。
4. 序列关卡（Sequence Gate）：在模式关卡之前，先把请求分类为 `standalone_clip`（独立片段）或 `sequence_project`（序列项目）。对于长篇故事、相连片段、续接/延长/下一段请求、密集动作/对白场景、营销战役，或任何其节拍无法清晰地塞进一次经过验证的有效平台生成中的创意，使用 `sequence_project`。对于序列工作，加载 `[skill:seedance-sequence]`、`[ref:sequence-project-state]`、`[ref:continuation-handoff]` 和 `[ref:prompt-compiler]`；对于续接、修复尾段或重新锚定请求，还要加载 `[skill:seedance-continuation]`。
5. 模式关卡（Mode gate）：在写散文式提示词之前，选择 T2V、I2V、V2V、R2V、FLF2V、edit、（在该平台已验证可用时的）原生 extend，或 troubleshoot。

   模式的可用性因平台而异：edit 和 extend 存在于 Dreamina 与 Ark 路线上；fal 没有专门的 extend 端点——要在 fal 上续接一个片段，优先用 reference-to-video 并把上一个片段作为视频参考（保留运动与音频上下文），并以从其末帧做 image-to-video 作为退路。provider/router 平台可能给同一种任务类型改名、隐藏字段，或只暴露部分模式；实现前请重新核查它们当前的文档。

6. 能力核查（Capability check）：在规划任何镜头、模式或预算时，加载 `[ref:capability-map]` 以便顺着模型强项、绕开已知限制来做设计，并加载 `[ref:allocation-model]` 以在起草前决定提示词把保真度预算花在哪里。
7. 参考映射（Reference map）：给每个素材分配一个主要角色：身份、首帧、末帧、产品、环境、运动、镜头、节奏、音频或风格。明确说明哪些东西不得迁移过去。
8. 多语言关卡（Multilingual gate）：如果提示词使用中文、俄文、日文、韩文、西班牙文或混合语码措辞，加载 `[ref:multilingual-community-examples]` 并精确保留参考标签。对于以中文、日文或韩文为母语、以范例驱动的请求，分别路由到 `[skill:seedance-examples-zh]`、`[skill:seedance-examples-ja]` 或 `[skill:seedance-examples-ko]`。
9. 安全关卡（Safety gate）：把涉及 IP、肖像、声音、品牌、真实人物、血腥画面或类规避措辞的内容，经由 `[skill:seedance-copyright]` 或 `[skill:seedance-filter]` 路由。
10. 导演（Direction）：在起草任何场景之前，加载 `[ref:directing-engine]` 来读懂这个场景在做什么（功能、转折、视点、权力关系、潜台词），设定或继承一种统一的导演嗓音，并推导出单一而连贯的设置——镜头、镜头焦段、灯光、调度、表演与声音全部服务于一个意图——而不是去挑一种「电影感的外观」。
11. 提示词搭建（Prompt build）：路由到 `[skill:seedance-interview]`、`[skill:seedance-prompt]`、`[skill:seedance-prompt-short]`、`[skill:seedance-sequence]`、`[skill:seedance-continuation]`，或某个用于镜头、运动、灯光、音频、角色、VFX、风格、配方或管线的领域技能。
12. 质量复查（Quality pass）：运行反套话（anti-slop）与导演连贯性测试，然后检查：一个可见的节拍、一个主要的镜头运动、有物理动机的灯光、声音意图、连续性锚点、约束条件、交付注意事项，以及来源日期注意事项。
13. 修复回路（Repair loop）：当一条镜头回来时，用 `[ref:retake-protocol]` 给它分诊（保留 / 后期修 / 编辑 / 重摇 / 重写，每次重摇只动一个变量，且都在尝试预算之内）；如果它彻底失败，先经 `[skill:seedance-troubleshoot]` 诊断根因，再去堆形容词。

## 序列关卡（Sequence Gate）

对于一个序列项目，在以下信息明确之前不要写 Clip 01：故事目标、故事最终结局、有序的主要节拍、有效平台或保守的平台假设、片段预算、当前片段的叙事任务，以及当前片段已完成的端点。

在上一个被接受的片段或其真实末帧被复核、其观察到的结束状态被记录下来之前，不要写续接提示词。

序列不变量（Sequence invariants）：

- 每条序列提示词都有 `project_id` 和 `clip_id` 谱系；
- 被接受的观察状态会覆盖计划状态；
- 被拒绝的素材排除在正典之外，不能成为续接来源；
- 在前一个被接受的镜头被复核之前，未来的提示词始终是临时性的；
- 精确的参考标签在每个片段中原封不动地保留；
- 已完成的节拍不能重播，被预留的未来节拍不能提前泄露；
- 每次镜头被接受后必须更新连续性状态；
- 除非用户明确要求结构化输出，否则最终的 Seedance 提示词保持自然语言。

## 加载映射（Load Map）

| 情境 | 加载 |
|---|---|
| 创意模糊或缺少 brief | `[skill:seedance-interview]` 或 `[skill:seedance-interview-short]` |
| 长篇故事、相连片段、营销战役序列、密集动作/对白场景，或需要多次生成的提示词 | `[skill:seedance-sequence]`、`[ref:sequence-project-state]`、`[ref:prompt-compiler]` |
| 续接、延长、下一段、修复尾段、桥接已知状态，或从被接受素材重新锚定漂移 | `[skill:seedance-continuation]`、`[ref:continuation-handoff]`、`[ref:continuity-qc]` |
| 复核一条已生成镜头并在下一条提示词前更新正典 | `[ref:retake-protocol]`、`[ref:sequence-project-state]`、`[ref:continuation-handoff]` |
| 密集动画分镜或多镜头提示词 | `[ref:dense-storyboard-mode]`、`[ref:multishot-grammar]`、`[ref:2d-anime-grammar]` |
| 制作级提示词 | `[skill:seedance-prompt]`、`[ref:quick-ref]`、`[ref:prompt-examples]` |
| 规划任何镜头、模式或预算 | `[ref:capability-map]` |
| 提示词把保真度花在哪里：身份 vs 运动 vs 场景密度 | `[ref:allocation-model]`、`[ref:intent-vs-precision]` |
| 多镜头提示词、单个片段内部的剪切，或每单位时长的镜头数预算 | `[ref:multishot-grammar]` |
| 2D、动漫或赛璐珞风格运动 | `[ref:2d-anime-grammar]`、`[skill:seedance-style]` |
| 专业电影、广告、营销战役或交付工作流 | `[ref:pro-filmmaking-standards]`、`[ref:shot-list-continuity]`、`[ref:delivery-qc]` |
| 精简提示词或中文压缩 | `[skill:seedance-prompt-short]`、对应语言的词汇参考 |
| 为一个场景选择正确的镜头、灯光、调度、表演与嗓音，让每个选择都有动机，或在一个长故事中保持统一的导演风格 | `[ref:directing-engine]` |
| 镜头、焦段、调度、镜头合同 | `[skill:seedance-camera]`、`[ref:cinematography-shot-language]` |
| 图像参考 / 首帧 | `[ref:i2v-guide]`、`[ref:reference-workflow]` |
| 首帧与末帧 | `[ref:first-last-frame-guide]` |
| API、Runway、Volcengine、fal、provider/router 平台、面向中国大陆的平台、工作流、定价、模型 ID | `[skill:seedance-pipeline]`、`[ref:api-workflow]`、`[ref:model-name-map]` |
| 调色、ACES、HDR/SDR、画幅比、字幕、音频后期或 QC | `[ref:color-pipeline-aces]`、`[ref:aspect-ratio-delivery]`、`[ref:subtitles-localization]`、`[ref:audio-post-delivery]`、`[ref:delivery-qc]` |
| 类型模板或范例 | `[skill:seedance-recipes]`、`[ref:examples-by-mode]`、`[ref:genre-guides]` |
| 中文范例或安全的中文改写 | `[skill:seedance-examples-zh]`、`[skill:seedance-vocab-zh]`、`[ref:vocab/zh]` |
| 日文范例或安全的日文改写 | `[skill:seedance-examples-ja]`、`[skill:seedance-vocab-ja]`、`[ref:vocab/ja]` |
| 韩文范例或安全的韩文改写 | `[skill:seedance-examples-ko]`、`[skill:seedance-vocab-ko]`、`[ref:vocab/ko]` |
| 俄文/西班牙文或混合语言范例 | `[skill:seedance-vocab-ru]`、`[skill:seedance-vocab-es]`、`[ref:multilingual-community-examples]` |
| 套话过多或触发过滤误判的英文措辞 | `[skill:seedance-vocab-en]`、`[skill:seedance-antislop]` |
| 糟糕的结果 | `[skill:seedance-troubleshoot]` |
| 一条镜头回来了：保留、后期修、编辑、重摇或重写 | `[ref:retake-protocol]` |
| 某条规则为何有效，或某个无规则覆盖的新案例 | `[ref:model-mechanics]` |

精确保留参考标签，让提示词保持简短，并且永远不要把现场观察到的社区技巧转化为官方平台保证。对于专业电影人请求，交付该角色所需的工作流对象：镜头表、镜头合同、连续性账本、提示词、后期交接、本地化方案或 QC 清单。



## Liu Prompt Contract Hard Gate

For Liu's copyable AI-video / SD2 / Seedance prompts, the final paste-ready block must follow this exact six-part order unless Liu explicitly requests another format:

```text
角色/资产锁定
视觉材质总控
镜头语言总控
事件节拍
声音
正向稳定约束
```

Paste-ready prompt policy: the model-ready code block is positive-only. It states only what is present, visible, audible, active, and locked in the current shot. Exclusion, absence, correction, comparison to old attempts, and previous-failure wording stay outside the copyable block. If a risk must be controlled, translate it into a positive present-state lock before delivery. `正向稳定约束` is the only final control section inside the paste target, and it must be written as positive stability locks. Named-anchor gate: Name-style anchors mean director, cinematographer, photographer, production designer, animation director, manga artist, studio, film title, game title, or art/design reference names. `镜头语言总控` uses name-style anchors or bounded camera grammar for substantial camera-sensitive prompts; these anchors own composition, blocking, lens feeling, camera motion, edit rhythm, shot scale, and reveal logic. `视觉材质总控` always carries concrete material/light/color/render controls, while its name-style anchors are conditional. Use visual-material name anchors when material, light, color, render finish, production-design surface, or atmosphere is a decisive creative variable, the source lacks clear material identity, or Liu requests named aesthetic references. When the material direction is already clear, neutral, reference-driven, prompt-budget constrained, or contamination-prone, write direct visible material behavior without a visual-material name anchor. Use 2-4 compatible anchors total when anchors are useful. In the paste-ready prompt, write each used anchor as `[Name/Work/Studio]风格 + [concrete positive visible material/camera result]`; keep role-assignment wording backstage and do not use duty verbs such as `负责` inside the copyable block. Technical camera/material terms support the style-result phrase.

Source-trace gate: every concrete phrase, including existing subjects, props, locations, palettes, camera routines, transitions, powers, sounds, and stability locks, must trace to Liu's current instruction, a supplied/inspected asset, the active global bible/continuity lock, or a user-approved reusable rule. If the trace fails, omit the phrase from the paste-ready prompt or move it outside as a question/assumption. Remove old-project residue before drafting; do not keep old nouns inside the paste-ready prompt as a way to suppress them.
