# 快速参考（Quick Reference）

## 默认路由（Default route）

- 模糊创意：`seedance-interview`。
- 清晰创意：`seedance-prompt`。
- 长故事或相连片段：`seedance-sequence`。
- 延续、扩展、修复尾部或重新锚定已采纳素材：`seedance-continuation`。
- 短提示词：`seedance-prompt-short`。
- 结果不佳：`seedance-troubleshoot`。
- IP 或真人风险：`seedance-copyright`。
- 被拦截的提示词：`seedance-filter`。
- 摄影机、光、运动、风格、VFX、音频或角色特定工作：加载匹配的专家子技能。

## 提示词检查清单（Prompt checklist）

| 闸门 | 通过条件 |
|---|---|
| 模式 | T2V、I2V、V2V 或 R2V 是明确的。 |
| 参考 | 每个素材恰好有一个主要角色，除非刻意分层。 |
| 主体 | 主体出现在第一个子句，必要时有稳定标签。 |
| 动作 | 一个可见节拍有可观察的终点。 |
| 摄影机 | 一个主要运动有起点、速度、主体关系和终点。 |
| 布光 | 来源、方向、色彩、氛围或转变是物理的。 |
| 音频 | 对白、环境、SFX、音乐或静默是有意为之的。 |
| 安全 | 受保护身份、IP 和不安全措辞被改写或授权门控。 |
| 反垃圾 | 空洞的增强词被可观察的制作语言替换。 |
| 预算 | 最终提示词符合已验证的活动平台提示词预算。 |
| 序列血缘 | 序列提示词在延续时有 `project_id`、`clip_id` 和父级。 |
| 实际状态 | 延续从已采纳的观察状态开始，而非计划状态。 |
| 片段范围 | 已完成节拍被排除，预留的未来节拍留在外面。 |

## 快速修复短语（Fast repair phrases）

| 失败 | 添加或替换为 |
|---|---|
| I2V 漂移 | `preserve [Image1] subject/product exactly; only motion, light, and camera change` |
| 通用观感 | `physical light source + material behavior + specific camera endpoint` |
| 摄影机混乱 | `one controlled [move] from [start frame] to [end frame]` |
| 动作弱 | `actor + verb + timing + consequence + final state` |
| 唇形同步不稳定 | `locked medium close-up, short quoted line, no head turn during dialogue` |
| VFX 嘈杂 | `source + material + path + interaction + dissipation endpoint` |
| 风格/IP 风险 | `medium + texture + palette + composition + motion rhythm` |
| 计划结尾不匹配 | `begin from the observed final frame: [actual visible state]` |
| 未来节拍泄漏 | `this clip stops at [endpoint]; do not show [reserved future beat] yet` |
