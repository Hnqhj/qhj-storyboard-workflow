# 实地观察技巧（Field-Observed Tips）

last_verified: 2026-05-30

这些是从公开社区材料中收集的从业者模式。请把它们当作实地观察，而非官方平台保证。

## 稳定工作流（Stable Workflow）

1. 先短后长起草：在花费于 10–15 秒片段之前，先测试 3–5 秒。
2. 每次重试只改一个变量：摄影机、布光、运动或参考角色。
3. 把每个参考素材绑定到一项工作上。
4. 对脆弱的身份、产品标识、可读文字、唇形同步、手部或复杂 VFX，使用锁定构图。
5. 把视频参考用于运动节律或摄影机行为，而非未经授权的身份转移。
6. 把音频参考用于节奏、情绪或氛围，除非该配音/音乐是自有、已授权或经授权的。
7. 当只有一个节拍失败时，优先用剪辑、扩展或片段替换，而非重新生成整个片段。
8. 对于延续，当平台支持时保存返回的尾帧，并将其用作下一个首帧锚点。
9. 如果一个音频参考应当控制时序，则在上传前将相互竞争的参考视频静音，或明确将它们的角色降为仅摄影机/运动。
10. 对于序列，在请求下一条提示词之前，先写下观察到的最终状态；不要假设计划中的终点已经发生。

## 提示词纪律（Prompt Discipline）

| 弱模式 | 更强模式 |
|---|---|
| `cinematic, epic, beautiful` | `soft side backlight, wet asphalt reflections, locked medium shot, quiet room tone` |
| `make it move naturally` | `shoulders rise once with breathing, hand releases the cup, final pose holds for one second` |
| `use this video as style` | `[Video1] provides only side-tracking camera rhythm; do not transfer performer identity or background` |
| `make product luxury` | `narrow warm light sweep across the label, black acrylic table reflection, no label redesign` |

## 高风险区域（High-Risk Areas）

- 快速手势。
- 小字、标牌、标识、标签和字幕。
- 无标签的多角色动作。
- 多个同时进行的摄影机运动。
- 身份必须保持固定时的产品转化。
- 真人面孔、声音、名人肖像和受保护角色。
- 在一次生成里要求过多切镜、地点和角色转折的、类似剧本的长提示词。
- 没有尾帧锚点的扩展链；质量与连续性可能在多次重试中退化。
- 没有记录已完成节拍、预留节拍或精确参考标签的序列链。

## 安全的隐藏技巧（Safe Hidden Trick）

最好的"技巧"不是绕过过滤器，而是让意图可读：来源、角色、动作路径、摄影机终点、光源、声音提示和约束。
