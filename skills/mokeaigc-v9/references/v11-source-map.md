# V11 蒸馏来源图

来源包：`mokeaigc-worldbuilder- V11(1).zip`，审计日期 2026-07-19。

## 保留并增强

- `SKILL.md`：清晰边界、指令优先级、低问卷默认、内部连续性 Bible、方面矩阵、平台中性优先、静默验证；
- `world-aspects.md`：九个方面按叙事功能区分；
- `continuity-and-shot-planning.md`：参考图证据边界、`forbidden_drift`、逐帧矩阵和连续性锚点；
- `camera-and-style-adaptation.md`：相机位置/距离优先、景深多变量、数字采集与胶片模拟分开、皮肤细节条件化；
- `output-formats.md`：Planning-only / Compact / Production 三档和严格子集行为；
- `platform-renderers.md`：只保留“平台中性语义先冻结、语法最后交 adapter”的架构原则。

## 已由现有体系覆盖

- 文化/生产设计、空间/光学/材料证据、最终介质打包：`world-visual-development-director`；
- 一般单帧和同场景多构图：`cinematic-ai-image-prompt-library`；
- 当前平台语法：各 platform adapter；
- 视频运动、分镜和实体连续性：对应现有 owner。

## 不进入默认硬规则、但保留在 V11 数据库

- 同一焦段区间最多三次；
- 九张中必须恰好两张安静、一张高压；
- 默认永远输出完整九张，即使上游已选择六张或用户要子集；
- 把 Midjourney 当前参数写入世界观永久方法；
- 对所有平台统一英文优先；
- 把颗粒、雾、泥、腐朽和皮肤微细节当作普遍高级感。

这些内容没有删除，已单独存入 `references/v11-database/`，按 `active-candidate`、`optional-heuristic`、`time-sensitive` 或 `archive-only` 标记。只有用户明确调用或当前任务确实需要时才读取；平台事实必须经过当前 adapter 复核。

## 旧能力迁移

原 `mokeaigc-v9` 内“同一场景九种构图”没有丢弃，已迁至 `cinematic-ai-image-prompt-library/references/same-scene-composition-exploration.md`，因为它控制的是单场景观看方式，不是世界功能发现。

