# 镜头组 JSON 校验输入

`shot_group_linter.py` 接受一个 JSON 对象。它只做机械检查，导演仍需判断表演、信息和审美。

```json
{
  "delivery_contract": "liu_camera_group",
  "output_format": "six_part",
  "audio_authority": "default",
  "group_duration": 16,
  "opening_state": "角色已在大厅右侧站定，警察位于前方",
  "ending_state": "苏凌月伸手扶起苏建国",
  "one_action_spine": "跪求 -> 扶起 -> 安抚",
  "first_frame_anchor": "苏建国跪地抓住警察裤腿",
  "handoff_state": "苏凌月已伸手，下一组从扶起动作开始",
  "scene_type": "hybrid",
  "references": [
    {"name": "废墟夜景.png", "role": "场景布局与光线参考"},
    {"name": "动作预演.mp4", "role": "动作、节奏与运镜参考"}
  ],
  "shots": [
    {
      "start": 0,
      "end": 3,
      "duration": 3,
      "shot_size": "中景",
      "camera_position": "桌侧两人关系线内侧",
      "camera_height": "胸口高度",
      "angle": "轻微侧前方平视",
      "lens": "40mm 中性透视",
      "focus_dof": "中等景深，焦点从来者转到对手眼睛",
      "lighting": "窗外冷色侧光，室内暖色实景灯补面，接触阴影清晰",
      "movement": "固定机位，轻微跟随",
      "action": "@角色从门口迈入并停在桌前",
      "performance": "呼吸收紧，停步后先看桌面再看向对手",
      "dialogue": "无台词",
      "speaker": "@角色",
      "listener": "@对手",
      "reaction": "@对手停止翻页，抬眼确认",
      "cut_trigger": "对手抬眼后切",
      "handoff": "视线方向承接到下一镜",
      "endpoint_state": "两人完成对视，空间关系保持清楚",
      "micro_beats": [
        {"start": 0, "end": 1, "description": "@角色迈入门内，脚步落地，视线先落到桌面"},
        {"start": 1, "end": 3, "description": "@角色停在桌前抬眼，对手抬眼确认并形成对视"}
      ],
      "proof_task": "交代两人距离和桌面道具"
    }
  ]
}
```

`output_format` 对所有剧本输入固定为 `six_part`。完整剧本先全局拆组；
局部片段只建立局部镜头组。两者都必须有镜头表，并为每个镜头组提供
详细六段式提示词。

`audio_authority` 可用：

- `default`：只允许人物台词、画外音和有物理来源的拟声；
- `explicit_user`：用户明确要求音乐、氛围或情绪音效；
- `authoritative_script`：权威剧本明确要求这些声音。

后二者必须能追溯到明确来源；它们只解除声音类别禁用，不降低 cue 功能、
时点和混音清晰度检查。

必填：`delivery_contract`、`group_duration`、`shots`，以及每镜的 `start`、
`end`、`duration`、`shot_size`、`camera_position`、`camera_height`、
`angle`、`lens`、`focus_dof`、`lighting`、`movement`、`action`、
`performance`、`dialogue`、`cut_trigger`、`handoff`、`endpoint_state`。
每镜还必须有 `micro_beats` 列表；列表中的每项包含 `start`、`end`、
`description`，并且连续覆盖该镜头的完整时间窗。
无台词镜头的 `dialogue` 明确写“无台词”，不能留空。

当 `delivery_contract` 为 `liu_camera_group` 时，建议填写并在正式交付前检查：
`opening_state`、`ending_state`、`one_action_spine`、`first_frame_anchor`、`handoff_state`。

可用时长契约：

- `liu_camera_group`：14-28 秒；
- `generic_seedance_clip`：4-15 秒；
- `storyboard_only`：不强制组时长。

对白镜头补充 `speaker`、`listener`、`reaction`，特写补充 `proof_task`。
提示词中的六段必须依次出现且都有实质内容；`事件节拍`逐镜复写上述
摄影、灯光、动作、表演、原文台词、剪切和承接信息。`同上`、`沿用`、
`参考镜头表`、`保持不变`等跨引用写法会直接校验失败。

在最终 `事件节拍` 中，镜头窗口下面嵌套输出镜头内 T 节拍，例如：

```text
镜头01｜0-2秒｜中景……
T=0-1s：进入与起始动作……
T=1-2s：动作完成、反应或状态改变……
```

T 使用镜头组时间轴；每个 T 段只承载一个可观察的动作、表演、运镜或
结果变化。镜头内静止保持也要写成带边界的 T 段，不能用无时间范围的
“持续”“保持”替代。

`scene_type` 可用 `dialogue`、`emotion`、`action`、`hybrid`，用于镜头数量软预算提示。

`references`为可选数组；填写后，`--prompt`模式会要求每个真实名称以`@名称`出现在提示词中。首次出现仍应带职责说明，例如`@废墟夜景.png（场景布局与光线参考）`。

命令示例：

```powershell
python scripts/shot_group_linter.py shot-group.json --prompt group-prompt.txt
```

加入 `--strict` 后，软预算、长镜头、特写证明任务缺失和提示词结构缺失等警告会升级为失败；适合正式交付前使用。普通创意草稿可不加该参数。
