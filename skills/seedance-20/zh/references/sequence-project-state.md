# 序列项目状态（Sequence Project State）

当一个 Seedance 请求变成一个多片段项目时，使用本参考文档。项目状态是真相来源；提示词是针对一次生成的临时编译指令。

## 操作模型（Operating Model）

用户创意 -> 故事脊柱 -> 世界观与连续性圣经 -> 序列方案 -> 当前片段契约 -> 当前片段提示词 -> 生成的拍摄 -> 观察拍摄审核 -> 规范对账 -> 下一片段契约 -> 下一提示词。

全局规划。局部生成。观察真实结果。更新规范。从实际采纳的素材继续。

## 规范状态（Canonical State）

把规范状态与临时状态分开。

规范参考控制身份和不可变设计：角色身份、产品身份、服装、产品几何、持久道具、地点和已批准的参考标签。

已采纳的先前素材控制临时开场状态：姿势、动作阶段、屏幕位置、摄影机阶段、环境布置、音频阶段、开放运动和未完成的手势。

## 必需的项目字段（Required Project Fields）

至少，一个项目状态包含 `schema_version`、`state_revision`、`project_id`、`project_mode`、`surface`、`clip_budget_sec`、`prompt_budget`、`story`、`world_bible`、`reference_registry`、`beats`、`clips`、`take_history`、`current_clip_id`、`canon_revision` 和 `updated_at`。

故事字段：`logline`、`story_promise`、`objective`、`initial_condition`、`final_outcome`、`target_duration_sec`、`tone` 和 `medium`。

节拍字段：`beat_id`、`description`、`narrative_function`、`status`、`assigned_clip_id` 和 `dependencies`。

片段血缘字段：`clip_id`、`parent_clip_id`、`sequence_index`、`prompt_version`、`generation_mode`、`source_clip_tag`、`status`、`narrative_job`、`already_happened`、`this_clip_only`、`reserved_for_later`、`planned_start_state`、`planned_end_state`、`observed_start_state`、`observed_end_state`、`continuity_locks`、`allowed_changes`、`continuity_breaks`、`accepted_deviations`、`transition_in`、`transition_out`、`open_motion_vectors`、`handoff_requirements` 和 `extension_depth`。

## 视觉状态（Visual State）

只追踪重要的东西，不要编造不清晰的细节。

角色：规范身份 ID、服装、发型、在世界中的位置、在画面中的位置、姿势、动作阶段、情感状态、目光、视线、移动方向、速度和身体朝向。

道具：身份、归属、位置、状态、运动和互动状态。

环境：地点、地理、背景布置、一天中的时间、天气、氛围和持久的实用元素。

摄影机：景别、高度、角度、支撑、路径、方向、速度、运动阶段、主体关系、对焦状态、曝光状态和终点。

布光：主光方向、强度、色彩关系、实用光源和转变状态。

音频：环境、已完成对白、活动对白、音乐阶段、SFX 阶段、活动的引擎或环境声，以及音频参考归属。

开放运动：主体方向与速度、摄影机方向与速度、运动中的道具、未完成的手势、布料或头发的余势、车辆运动，以及待处理的冲击恢复。

观察质量：`observation_confidence`、`uncertainties` 和 `requires_user_confirmation`。

## 对账（Reconciliation）

当一个已采纳片段与计划不同时：

1. 记录偏差。
2. 决定是接受为规范、修复、拒绝/重新生成，还是重新锚定下一个镜头。
3. 如果接受，更新下游规划。
4. 移除任何意外完成的节拍。
5. 把任何未完成的计划节拍带入下一个合适的片段。
6. 绝不在计划结尾没有发生时假装它发生了。

被拒绝的素材不改变规范，也不能成为延续父级。

## 项目状态胶囊（Project State Capsule）

使用一个可读的胶囊做跨会话延续。不能假设一段新对话拥有隐藏的先前记忆。

必需字段：

PROJECT ID:
STORY GOAL:
FINAL OUTCOME:
SURFACE:
REFERENCE TAGS:
CANONICAL REFERENCES:
ACCEPTED CLIPS:
CURRENT ACTUAL STATE:
OPEN MOTION:
COMPLETED BEATS:
NEXT CLIP JOB:
CONTINUITY LOCKS:
ALLOWED CHANGES:
RESERVED FUTURE BEATS:
EXTENSION DEPTH:
UNRESOLVED UNCERTAINTIES:
