---
name: seedance-sequence
description: "This skill should be used when a Seedance 2.0 request is a long story, connected set of clips, multi-generation scene, campaign sequence, dense storyboard, continuation-ready plan, or any idea that must be divided into stateful clips."
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

# seedance-sequence

当用户的想法大于一次可靠的生成、当请求相连的镜头，或当用户说续接、延展、下一部分、第二部分、下一场景或做得更长时，使用本技能。全局规划，局部生成：本技能规划整个故事，但只编译下一个未解决的镜头。

加载 `[ref:sequence-project-state]`、`[ref:continuation-handoff]`、`[ref:prompt-compiler]`、`[ref:surface-prompt-profiles]`、`[ref:event-density]` 和 `[ref:continuity-qc]`。当存在参考素材时加载 `[ref:reference-transfer-contract]`，当请求包含很多镜头或动画分镜板时加载 `[ref:dense-storyboard-mode]`。加载 `[ref:directing-engine]` 为整个故事设定一个导演语态，并规划长篇主线，使风格在每段镜头中都出自同一只手。

## 意图

用户想做的是一部影片，而非一堆提示词。本技能保护跨生成的动作线索：什么已经发生、什么正在发生、什么尚不能发生，以及被采用的素材实际展示了什么。规划是全局的；提示词是局部的。

## 序列分类器

当故事超出已核实的当前界面时长、要求多段相连镜头、包含若干叙事节拍、是一个影片场景、广告、营销活动、音乐序列、动作场景、对白场景，或使用续接/延展/下一部分的措辞时，分类为 `sequence_project`。否则分类为 `standalone_clip` 并返回简明提示词路径。

对每个请求还需分类：

- 生成输入模式：T2V、I2V、V2V、R2V、FLF2V、edit、当前界面已核实可用时的原生 extend，或 troubleshoot；
- 序列关系：standalone、sequence_first_clip、seamless_continuation、intentional_next_shot、bridge_between_known_states、repair_tail，或 reanchor_after_drift；
- 镜头结构：compact_single_take、phased_single_take、dense_multishot、first_last_frame_transition，或 video_edit_contract；
- 媒介语法：live_action、3d_animation、2d_animation、product_or_object，或另一种受支持的媒介；
- 界面配置：精确的引用标签惯例、已核实的时长范围、提示词预算、受支持的参考角色、时间线语法、剪辑/延展可用性、音频行为，以及约束。

若界面未知，使用保守的通用配置。不要捏造时长、提示词上限、参考数量或标签语法。

## 构建流程

1. 在 Clip 01 之前确立故事承诺与最终结局。
2. 识别角色、产品或叙事目标，并借助 `[ref:directing-engine]` 为整个项目设定一个导演语态，规划长篇主线——景别、相机运动、光线对比和声音应如何从开场推进到高潮再到释放，以及哪一段镜头打破模式以标记转折。
3. 提取有序的节拍，并给每个节拍分配一个状态：planned、current、completed、omitted 或 replaced。
4. 用当前界面预算或保守假设把节拍划分为生成大小的镜头。
5. 给每段镜头一个叙事任务和一个完成的终点。
6. 定义计划开场状态、计划结束状态、连续性锁定项、允许的变化，以及对延展友好的交接要求。
7. 把后续镜头存储为暂定意图卡，而非最终提示词。
8. 只从当前镜头契约编译第一个未解决的镜头提示词。
9. 生成后，要求提供该镜头或末帧，记录已观察到的起/末状态，校准正典，然后才编译下一条提示词。

使用对初学者友好的语言。这样说是合理的："这个想法需要三次相连的生成。我现在会规划完整的故事，但一次敲定一条提示词，使每条新提示词都匹配 Seedance 实际产出的内容。"

## 序列图字段

每张镜头卡必须包含 `clip_id`、`sequence_index`、`parent_clip_id`、`narrative_job`、`target_duration_sec`、`generation_mode`、`shot_structure`、`already_happened`、`this_clip_only`、`reserved_for_later`、`planned_start_state`、`planned_end_state`、`transition_in`、`transition_out`、`continuity_locks`、`allowed_changes`、`arc_position` 和 `status`。`arc_position`（open、rising、turn、climax 或 release）记录该镜头在导演主线上的位置，使其景别、运动、光线和声音趋势继承项目语态。

Clip 01 可以计划"走出航站楼并到达打开的车门"，终点为"主体站在打开的后门旁"，同时把"上车"和"车辆驶离"预留给后续镜头。不要把所有计划镜头粘进一条生成提示词里。

## 输出契约

对于一个新序列，返回：

1. 项目摘要。
2. 故事主线。
3. 最终结局。
4. 世界观与连续性圣经，包括所选导演语态和长篇风格主线（景别、运动、光线和声音如何推进，以及哪段镜头打破模式）。
5. 序列图。
6. Clip 01 契约。
7. Clip 01 的自然语言最终 Seedance 提示词。
8. 后续镜头的暂定意图卡。
9. 在敲定 Clip 02 之前返回所生成镜头或末帧的指令。
10. 项目状态胶囊。

除非用户要求，否则不要输出内部 JSON。可读的胶囊才是跨会话的交接。
