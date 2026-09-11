# 渐进式披露方案（Progressive Disclosure Plan）

根技能应当路由。子技能应当决策。参考文档应当承载密集的表格和易变的事实。

| 内容 | 位置 | 加载条件 |
|---|---|---|
| 路由、高层规则 | `ZH_REFERENCE.md` | 总是 |
| 提示词构建 | `skills/seedance-prompt/ZH_REFERENCE.md` | 写提示词任务 |
| 平台/API 事实 | `references/api-status.md` | 平台或 API 任务 |
| 词汇表 | 语言技能 + 参考文档 | 翻译/压缩任务 |
| 安全与 IP | `seedance-copyright` + `platform-constraints` | 受保护身份或安全敏感任务 |
| 长示例 | `seedance-examples-zh` 或未来的 `examples/` | 用户请求示例 |

不要把大型数据库挪回活动子技能正文中。

## V6 序列披露（V6 Sequence Disclosure）

根 `ZH_REFERENCE.md` 只拥有序列闸门（Sequence Gate）和不变式。`skills/seedance-sequence` 拥有全局规划和当前片段编译。`skills/seedance-continuation` 拥有已采纳素材的延续和重新锚定。密集的状态细节存在于 `references/sequence-project-state.md`、`references/continuation-handoff.md` 和 `references/prompt-compiler.md` 中。
