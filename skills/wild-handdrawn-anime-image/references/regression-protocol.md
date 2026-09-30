# 纯文字回归记录协议

本协议用于有预算的风格调试，不包含具体画风配方。配方与量表必须来自当前任务中实际检查过的证据。

## 运行方式

```text
python scripts/regression.py init <manifest.json> --plan <plan.json>
python scripts/regression.py validate <manifest.json> --phase ready
python scripts/regression.py validate <manifest.json> --phase complete
python scripts/regression.py report <manifest.json> --output <report.md>
```

`init` 不覆盖已有文件。输入 plan 包括 `cases`、`budget`、`rubric`、`stability`；审美量表未定时可建 draft，但不能通过 ready。所有相对文件路径按 manifest 所在目录解析；可使用本任务的绝对路径。

## 最小数据模型

- `cases`：`id`、`label`、`design_contract`。角色设计模块在重复批次中固定。
- `budget`：`batch_output_cap`、`total_output_cap`、`max_batches`、`authorized_scope`；所有数值为正整数。
- `rubric`：`hard_gates`（字符串列表）、`dimensions`（`id / weight / max_score / observable`）、`pass_score_100`、`minimum_dimension_scores`、`tie_break`。权重合计1，评分按加权满分归一到100。空量表不算检查通过。
- `stability`：`required_passing_batches`、`max_batch_mean_delta`、`max_case_score_delta`、`minimum_gain`、`plateau_comparisons`。停止包括达到稳定规则、预算耗尽、连续指定次数低于最小增益、或已判断文字能力/任务范围需重新界定。
- `recipes`：每版的 `id / path / sha256 / status / frozen_at_utc`；`path` 是完整的实际配方文件，`status` 为 `approved` 或 `draft`。`active_recipe_id` 绑定当前已审阅版。配方文件改变即新版本或重新冻结哈希。
- `batches`：`id / index / recipe_id / purpose / hypothesis / status`；`purpose` 为 `baseline / revision / repeat`。完整回归批次每个角色恰好一张；下一批开启前前批全部已评分。
- `attempts`：见下例。一次返回一张可读原图为一条记录；一次调用返回多张时每张各记一条、共享 invocation ID。
- `decisions`：`after_batch / decision / reason / evidence / next_single_gap`。每个完成批次有停止判断；`CONTINUE` 仅在剩余预算内有效。

```json
{
  "id": "b1-acheron",
  "invocation_id": "recorded-tool-call-id",
  "batch_id": "b1",
  "case_id": "acheron",
  "recipe_id": "v1",
  "status": "returned_image",
  "tool": "actual callable tool name",
  "model_version": null,
  "seed": null,
  "created_utc": "actual UTC time",
  "request_path": "requests/b1-acheron.json",
  "prompt_path": "prompts/b1-acheron.txt",
  "prompt_sha256": "actual SHA256",
  "output_path": "originals/b1-acheron.png",
  "output_sha256": "actual SHA256",
  "review": {
    "reviewer": "named reviewer",
    "inspected_original": true,
    "hard_gates": {"example_gate": true},
    "scores": {"example_dimension": 4},
    "evidence": [{"dimension": "example_dimension", "region": "face / hand / silhouette", "observation": "visible finding"}],
    "verdict": "accepted",
    "reason": "specific reason",
    "rejection_codes": []
  }
}
```

`request_path` 的 JSON 是实际图像工具输入对象，包含完整 `prompt`。在纯文字协议中，任何 `referenced_image_paths`、`num_last_images_to_include`、`image`、`image_url`、`input_image`、`mask`、`reference_images` 键均失败，即使值为空；如另一个工具使用其他图像参数，须扩充显式禁止键。保存记录本身不证明工具服务内部行为，校验器只能检查可见的调用记录。

`tool_failed` 记录保存请求和错误证据，`output_path` 为 null；不伪造原图或审美评分。返回原图而画得不好仍是 `returned_image`，保留并计数。

生成时间不可得时 `created_utc` 为 null，`time_evidence` 记录实际可得的归档时间及其性质；不能把归档时间改称生成时间。若量表在首图出现之后、独立审阅之前才冻结，须记录实际冻结阶段和谁已看过预览；该批为部分预注册开发样本，不能倒填成完整预注册。后续同词回归继续沿用已冻结门槛。

## 稳定性与停止口径

一个完整批次先过所有硬门槛和分项下限，再过总分；任一项失败即该样本不通过。完成度或漂亮程度不能冲抵硬门槛。

连续两批在同配方版本下全用例通过，且每个用例完整提示词哈希相同，才可检验均分差、逐用例分差等预设重复条件。每个角色各一张只是覆盖检查。首批与改词后第二批即使都通过，也不是同词重现证据。

数据量、评分者及工具控制条件决定结论边界：报告 `n` 张中 `k` 张通过、哪些角色/维度未通过、是否满足本轮预设规则。分数是带证据的审美判断，不是测量到的真实概率；不要写“稳定性99%”。没有固定种子时如实写未知；不同调用不能自动假定为统计独立样本。

每次变更只回灌一个被证据支持的缺口。两次连续比较低于 `minimum_gain` 时停止随机扩量，回到配方假设或目标定义；纯文字要求仍有效，不可自行转成参考图编辑。预算耗尽时即使未稳定也保留全部输出并报告实际状态。工具故障可修复，但不会恢复已消耗的可读原图槽位。
