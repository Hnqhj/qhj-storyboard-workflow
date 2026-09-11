# Seedance 提示词 JSON Schema

当用户想要结构化输出，或当自动化流水线需要稳定字段时，使用本 schema。

```json
{
  "mode": "t2v | i2v | v2v | r2v | flf2v | edit | extend | audio-led",
  "duration": "string",
  "aspect_ratio": "string",
  "references": [
    {"tag": "Image1", "role": "identity | product | pose | environment | style | first_frame | last_frame | reference_image"},
    {"tag": "Video1", "role": "motion | camera | pacing | blocking | source_clip | reference_video"},
    {"tag": "Audio1", "role": "voice | rhythm | ambience | music | tempo | reference_audio"}
  ],
  "characters": [],
  "production": {
    "phase": "brief | preproduction | generation | review | post | localization | delivery",
    "role": "director | dp | producer | editor | colorist | sound | localization | qc",
    "delivery_surface": "web | broadcast | social | theatrical | client_review | archive",
    "approval_owner": ""
  },
  "shot_list": [
    {
      "shot_id": "S01_SH01",
      "purpose": "establish | reveal | demonstrate | emotional_turn | end_card",
      "shot_contract": "shot size, angle, lens feel, camera move, endpoint",
      "start_frame": "",
      "end_frame": "",
      "risks": []
    }
  ],
  "continuity_anchors": {
    "character": [],
    "product": [],
    "wardrobe": [],
    "props": [],
    "location": "",
    "screen_direction": "",
    "eyeline": "",
    "lighting_state": "",
    "audio_state": ""
  },
  "scene": "",
  "camera": "",
  "motion": "",
  "lighting": "",
  "style": "",
  "audio": "",
  "color_pipeline": {
    "look_intent": "",
    "working_assumption": "",
    "output_transform": "SDR Rec.709 | HDR PQ | theatrical | social",
    "show_lut_or_cdl_notes": "",
    "qc_notes": []
  },
  "subtitle_plan": {
    "subtitles": false,
    "sdh": false,
    "forced_narrative": false,
    "dubbing": false,
    "textless_required": false,
    "languages": []
  },
  "audio_deliverables": {
    "full_mix": true,
    "stems": [],
    "m_and_e": false,
    "loudness_target": "",
    "sync_cues": []
  },
  "delivery": {
    "frame_rate": "",
    "resolution": "",
    "aspect_ratio": "",
    "safe_area": "",
    "version_name": "",
    "qc_checks": []
  },
  "safety_notes": [],
  "final_prompt": ""
}
```

JSON 包装用于规划。最终提示词仍然需要读起来自然。对于专业工作，把 production、shot-list、continuity、localization、audio、color 和 delivery 字段当作交接元数据；不要把它们全部塞进提示词。

## 序列状态 Schema（Sequence-State Schemas）

版本 6 在 `schemas/` 下新增了机器可校验的状态固件（fixtures）：

- `project-state.schema.json`：用于项目状态、故事、节拍、片段血缘、拍摄历史、规范修订和参考注册表。
- `clip-contract.schema.json`：用于当前片段的生产任务。
- `take-review.schema.json`：用于观察到的起始/结束状态、已接受的偏差、已完成节拍，以及拒绝/修复裁定。
- `prompt-spec.schema.json`：用于内部提示词编译元数据。
- `generation-run.schema.json`：用于合成基准测试与本地运行记录。

这些 schema 是规划产物。除非用户明确请求结构化输出，最终的 Seedance 提示词仍保持自然语言。
