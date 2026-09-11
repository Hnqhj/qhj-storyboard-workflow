# MOKE V11 方法数据库

这是 V11 原包的**旁路知识数据库**，不是默认执行规则。它保留值得查询、尚需条件化、具有版本时效、或不适合作为硬门的内容。

## 调用原则

1. 主 Skill 足以完成任务时，不加载数据库。
2. 用户明确问“V11 原包怎么写”“把固定模板也带上”“给我平台版本”“需要更强制的九图变化”时才读取。
3. 每条记录必须保留 `source / status / owner / conditions / caution`。
4. `time-sensitive` 平台条目必须交当前 adapter 或官方资料复核后才进入最终副本。
5. `optional-heuristic` 只能作为诊断或探索候选，不能替代具体叙事理由。
6. `archive-only` 仅用于追溯，不自动进入提示词。

## 文件

- `methods.json`：机器可检索的完整方法索引；
- `platform-renderers-dated.md`：V11 原包的平台写法快照；
- `shot-variation-heuristics.md`：固定配额与镜头变化启发式；
- `output-template-database.md`：Compact / Production / Planning-only 历史模板；
- `source-file-ledger.json`：原包 7 个有效文件与 10 个 macOS 元数据文件的覆盖信息。

## 状态词

| status | 含义 |
|---|---|
| `active-candidate` | 方法本身有用，但只有当前任务需要时才加载 |
| `optional-heuristic` | 可用作检查/探索，不作为固定要求 |
| `time-sensitive` | 含平台版本、参数或能力，执行前必须复核 |
| `covered-by-owner` | 已由现有专业 Skill 更强地拥有 |
| `archive-only` | 仅保留来源和审计价值 |

