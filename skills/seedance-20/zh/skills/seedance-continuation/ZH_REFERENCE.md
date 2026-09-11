---
name: seedance-continuation
description: "This skill should be used when a Seedance 2.0 user asks to continue, extend, make the next part, repair the tail, bridge between known frames, re-anchor drift, or create a successor prompt from accepted footage."
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

# seedance-continuation

将此技能用于无缝续接、有意的下一镜头、桥接片段、尾段修复，以及漂移后的重新锚定。一条续接提示词必须扎根于被接受的素材，而不仅仅是旧计划。

加载 `[ref:continuation-handoff]`、`[ref:sequence-project-state]`、`[ref:prompt-compiler]`、`[ref:reference-transfer-contract]` 和 `[ref:continuity-qc]`。当续接失败或漂移可见时，加载 `[ref:failure-atlas]`。加载 `[ref:directing-engine]`，使下一个片段继承项目的导演嗓音及其在长篇脊线上的位置；视觉外观绝不在片段之间重摇。

## 必需输入关卡

在写任何续接提示词之前，要求：

- `project_id`；
- 当前 `clip_id`；
- 有效的 `parent_clip_id`；
- 完整故事目标；
- 故事最终结局；
- 下一个计划的叙事任务；
- 被接受的上一个片段或被接受的末帧；
- `observed_end_state`；
- 连续性锁；
- 继承的导演嗓音和弧位置；
- 精确的参考注册表；
- 有效平台或保守平台配置。

如果来源不可用，说：「我有故事计划，但我没有上一次生成的实际结尾。请上传该片段或其末帧，或者准确描述结尾处可见的内容。我不应该凭空捏造续接状态。」

不要通过写一条投机性提示词来隐藏这种不确定性。

## 续接类型

`seamless_continuation`：相同镜头、相同地理、相同的进行中运动、相同或有动机的镜头延续，以及作为来源的被接受的上一段素材。

`intentional_next_shot`：一个剪辑式的切是合适的。故事连续性重要，但不承诺精确的帧连续性。不要称之为无缝。

`bridge_between_known_states`：必须连接一个定义好的起始状态和结束状态，在有效平台支持时通常用首/末帧生成。

`repair_tail`：上一段的最后几秒失败了。在继续之前先修复、编辑或重新生成尾段，因为从失败的尾段继续会放大错误。

`reanchor_after_drift`：身份、细节、地理、运动、音频或世界连续性退化了。回到正典身份、最强的被接受末帧、一个稳定的来源片段，或使用正典参考的一个新的有意镜头。

## 正典规则

被接受的观察素材覆盖计划状态。如果计划说主体到达了车门，但被接受的片段在距门两步处结束，下一条提示词就从两步外开始。它不重播航站楼出口，也不假设主体已在车内。

被拒绝的素材绝不更新正典，绝不成为父来源。

追踪 `extension_depth`。在深度 2 或更大时，警告反复延长会增加连续性风险。当可见漂移已经开始时，建议重新锚定，而不是盲目地再次延长。

## 输出合同

返回：

1. 续接类型。
2. 使用的来源证据。
3. 观察到的末态。
4. 下一个片段合同。
5. 连续性锁和允许的更改。
6. 要排除的已完成节拍。
7. 要排除的预留未来节拍。
8. 仅针对当前片段的最终自然语言 Seedance 提示词。
9. 更新后的项目状态胶囊，或对缺失来源证据的请求。
