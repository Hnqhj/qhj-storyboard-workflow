# V6 序列提示词编译器清单（Manifest）

## 当前补丁

- 有效包版本：`6.1.0`。
- 补丁范围：导演引擎（有动机的场景导演、统一的导演嗓音、长篇视觉脊线）接入访谈、提示词、镜头、灯光、运动、角色、序列和续接；延续的 provider/router、Seedance 2.0 Mini 命名和 Runway 来源维护。
- 当前期望的有效子技能数：28。
- 当前期望的 eval 用例数：114。

## 基线（Baseline）

本节记录原始 v6 迁移所检查的历史基线。它不是当前的有效发布编号。

- 仓库：`Emily2040/seedance-2.0`
- 检查的基线提交：`94906cd`
- 基线版本：`5.5.2`
- 基线子技能：24
- 基线参考：47
- 基线 eval 用例：61
- 基线验证器：`validate_skills.py`、`content_audit.py`、`eval_schema_check.py`、`design_audit.py`、`source_registry_check.py`、`vocab_schema_check.py`
- 基线 CI：六个本地 Python 验证器
- Frontmatter 约定：YAML 块，含 `name`、第三人称 `description`、`license`、`user-invocable`、`tags` 和 `metadata.version`；子技能还要求 `metadata.parent: "seedance-20"`

## 新增的文件

- `skills/seedance-sequence/ZH_REFERENCE.md`
- `skills/seedance-continuation/ZH_REFERENCE.md`
- `references/sequence-project-state.md`
- `references/continuation-handoff.md`
- `references/prompt-compiler.md`
- `references/reference-transfer-contract.md`
- `references/dense-storyboard-mode.md`
- `references/surface-prompt-profiles.md`
- `references/event-density.md`
- `references/continuity-qc.md`
- `references/failure-atlas.md`
- `schemas/project-state.schema.json`
- `schemas/clip-contract.schema.json`
- `schemas/take-review.schema.json`
- `schemas/prompt-spec.schema.json`
- `schemas/generation-run.schema.json`
- `scripts/prompt_lint.py`
- `scripts/project_state_check.py`
- `scripts/continuity_chain_check.py`
- `scripts/behavior_contract_check.py`
- `scripts/sequence_eval_check.py`
- `scripts/generation_run_check.py`
- `tests/test_prompt_lint.py`
- `tests/test_project_state.py`
- `tests/test_continuity_chain.py`
- `tests/test_behavior_contract.py`
- `tests/test_sequence_eval.py`
- `tests/test_generation_run_check.py`
- `evals/generation-benchmark.json`
- `data/generation-runs.example.jsonl`
- `examples/sequence-airport-arrival/*`
- `examples/sequence-observed-deviation/*`
- `examples/standalone-clip/*`
- `examples/golden-prompts/*`

## 修改的文件

- `ZH_REFERENCE.md`
- `README.md`
- `CHANGELOG.md`
- `agents/openai.yaml`
- `.github/workflows/validate-skills.yml`
- `evals/evals.json`
- `scripts/validate_skills.py`
- `scripts/eval_schema_check.py`
- 现有技能路由器：interview、interview-short、prompt、prompt-short、troubleshoot、camera、motion、characters、audio、lighting、style、recipes，以及所有有效子技能的版本元数据。
- 现有参考：storytelling framework、shot-list continuity、reference workflow、JSON schema、retake protocol、eval rubric、quick reference、examples by mode、multishot grammar、2D anime grammar、model mechanics、allocation model、capability map、progressive disclosure、agent compatibility、field-observed tips、community-source methodology 和 prompt examples。

## 行为变更

- 在模式关卡之前新增了根序列关卡。
- 将请求分类为 `standalone_clip` 或 `sequence_project`。
- 在 Clip 01 之前要求：故事目标、故事最终结局、有序节拍、平台配置、片段预算、当前片段任务和当前片段端点。
- 在续接提示词之前要求：被接受的上一段素材或被接受的末帧，外加 `observed_end_state`。
- 将正典参考与瞬态的被接受素材区分开。
- 让被接受的观察素材覆盖计划状态。
- 防止被拒绝的素材更新正典。
- 防止后续提示词重播已完成节拍或泄露预留的未来节拍。
- 在前一个被接受的镜头被复核之前，保持后续提示词为临时性。
- 逐字节精确保留参考标签。
- 除非用户请求结构化输出，否则保持最终 Seedance 提示词为自然语言。
- 新增一个可移植的项目状态胶囊（Project State Capsule），用于跨会话续接。

## 迁移

- 版本从 `5.5.2` 迁移到有效的 v6 线，覆盖有效技能元数据、README、eval 元数据和验证器期望值。
- 期望子技能数从 24 增加到 26。
- 必需参考从 47 增加到 56。
- Eval 从 61 增加到 108。
- CI 从六项检查扩展为完整的 v6 验证套件。

## 验证命令

```bash
python scripts/validate_skills.py --strict
python scripts/content_audit.py --strict
python scripts/eval_schema_check.py --strict
python scripts/design_audit.py --strict
python scripts/source_registry_check.py --strict
python scripts/vocab_schema_check.py --strict
python scripts/project_state_check.py --strict
python scripts/continuity_chain_check.py --strict
python scripts/behavior_contract_check.py --strict
python scripts/sequence_eval_check.py --strict
python scripts/generation_run_check.py --strict
python scripts/prompt_lint.py --self-test --strict
python -m unittest discover -s tests -v
python -m compileall scripts tests
git diff --check
```

## 发布验收结果

2026-06-22 的最终全套件运行（v6.1.0 导演引擎发布）：

- `python scripts/validate_skills.py --strict`：通过；根加 28 个子技能和必需的 v6.1.0 文件。
- `python scripts/content_audit.py --strict`：通过；有效内容干净，已迁移的归档警告仍为仅警告。
- `python scripts/eval_schema_check.py --strict`：通过；114 个 eval 用例。
- `python scripts/design_audit.py --strict`：通过。
- `python scripts/source_registry_check.py --strict`：通过。
- `python scripts/vocab_schema_check.py --strict`：通过。
- `python scripts/project_state_check.py --strict`：通过；4 个项目状态。
- `python scripts/continuity_chain_check.py --strict`：通过。
- `python scripts/behavior_contract_check.py --strict`：通过。
- `python scripts/sequence_eval_check.py --strict`：通过；47 个序列用例。
- `python scripts/generation_run_check.py --strict`：通过。
- `python scripts/prompt_lint.py --self-test --strict`：通过。
- `python -m unittest discover -s tests -v`：通过；6 个测试。
- `python -m compileall scripts tests`：通过。
- `git diff --check`：通过。

标记为启发式的假设：序列漂移风险、延长深度警告、事件密度拆分和未知平台保守配置。没有断言任何新的易变平台限制、定价、模型 ID、地区、端点名或授权规则。
