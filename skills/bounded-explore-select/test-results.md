# bounded-explore-select 压力测试结果

- **测试日期**：2026-07-13
- **测试方式**：独立 Agent 盲路由；仅提供用户 prompt 与 11 个 Skill 的触发描述
- **最终结果**：9/9（100%）
- **判定门槛**：全部通过；包含应调用、同书兄弟 Skill 诱饵、非目标诱饵与边界场景

## 逐条结果

| 用例 | 类型 | 预期路由 | 实际路由 | 结果 | 轮次 |
|---|---|---|---|---|---|
| should-trigger-01 | 应调用 | bounded-explore-select | bounded-explore-select | 通过 | 首轮盲测 |
| should-trigger-02 | 应调用 | bounded-explore-select | bounded-explore-select | 通过 | 首轮盲测 |
| should-trigger-03 | 应调用 | bounded-explore-select | bounded-explore-select | 通过 | 首轮盲测 |
| should-not-trigger-01 | 不应调用/诱饵 | creative-north-star | creative-north-star | 通过 | 首轮盲测 |
| should-not-trigger-02 | 不应调用/诱饵 | cross-shot-consistency-audit | cross-shot-consistency-audit | 通过 | 首轮盲测 |
| edge-01 | 边界 | bounded-explore-select | bounded-explore-select | 通过 | 首轮盲测 |
| should-trigger-mj-01 | 应调用 | bounded-explore-select | bounded-mj-preference-calibration / 合并 owner | 通过 | 本轮独立盲测 |
| should-not-trigger-mj-01 | 不应调用/诱饵 | midjourney-generation-adapter | midjourney-generation-adapter | 通过 | 本轮独立盲测 |
| edge-mj-01 | 硬边界 | bounded-explore-select | bounded-mj-preference-calibration / 合并 owner | 通过 | 本轮独立盲测 |

## 失败分析与回炉记录

- 原 6 条全部通过；新增 3 条 Personalization/Moodboard 合并回归例也全部通过。平台兼容诱饵正确交给 `midjourney-generation-adapter`，数量不等于审美的硬门保持零容错。

## 审计文件

- 测试定义：`test-prompts.json`
- 原始盲测输入与输出：`../eval/`
- 测试格式与 darwin-skill 兼容。
