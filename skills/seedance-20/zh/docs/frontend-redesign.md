# V6 首页设计

本仓库目前不包含独立的 Web 应用。公开前端是 GitHub README、生成的位图 hero/信息图资源，以及 SVG 支撑图。

## V6 设计目标

- 以 v6 序列状态承诺打头：一个故事状态、一个当前片段合同、一条编译后的 Seedance 提示词。
- 让 README 在读者到达安装章节之前就对英语、中文、日文和韩文母语读者有用，包括完整的母语读者文档和有效的范例技能。
- 展示 Seedance 的实用范围：参考、首/末帧连续性、续接、产品揭示、时间线控制、音频和镜头导演。
- 为操作系统概览、技能映射、技能能力图、CDN 交付图、参考角色图、制作交付图和 QC 栈使用生成的电影级信息图。
- 当文字大、经过校正、视觉平衡，并在邻近的可搜索 Markdown 中重复时，允许使用文字密集型信息图。
- 让 SVG 资源作为支撑图，而非主要的情感表面。
- 用 `scripts/design_audit.py` 验证 README 完整性、画廊覆盖、PNG 尺寸和资源存在性。

## 母语读者要求

- 第一屏必须说明该项目是当前的 v6 工作。
- README 必须包含可见的中文、日文和韩文文案，而不仅仅是声称这些语言存在的英文标签。
- 母语行必须链接到有效的技能文件和有效的词汇参考，而非已迁移的遗留文件。
- 日文和韩文必须拥有与中文范例地位对等的有效范例技能路由。
- 诸如 `[Image1]`、`[Video1]`、`[Audio1]`、`@图1` 和 `@视频1` 之类的参考标签必须原样展示，使读者不会把它们翻译掉。
- 本地化指引必须把字幕、法务文案和市场文案保留在后期制作中，除非用户明确要求简单的屏上生成文字。

## 资源

- `assets/hero-command-center.png`
- `assets/hero-global-filmmaker-mode.png`
- `assets/infographic-skill-capabilities.png`
- `assets/infographic-cdn-delivery-map.png`
- `assets/infographic-reference-role-map.png`
- `assets/infographic-production-delivery.png`
- `assets/infographic-professional-qc-stack.png`
- `assets/hero-cinematic.png`
- `assets/skill-os-infographic.png`
- `assets/skill-map-cinematic.png`
- `assets/hero-dark.svg`
- `assets/hero-light.svg`
- `assets/skill-map.svg`

## 设计规则

- SVG 中不使用外部字体或脚本。
- 每个 SVG 都需要 `<title>` 和 `<desc>`。
- README 应在移动端和暗色模式下保持可读。
- 避免密集的徽章墙和嘈杂的装饰性文字。
- 仅对在 README 宽度下仍清晰可读的大而短的标签使用文字密集型生成信息图。
- 检查每一张生成的文字图；在提交前拒绝乱码词、丑陋排版、对比度差或看起来像占位符的面板。
- 在每张文字密集型图旁保留对等的 Markdown 说明，使仓库保持可访问、可搜索。

## V6 编辑型系统

报头从生成的位图艺术转向手工构建的编辑型系统：衬线展示字体压过等宽规格标签、暖色墨/纸主题搭配单一琥珀强调色、电影齿孔与取景器线条，以及零渐变。`assets/hero-dark.svg` 和 `assets/hero-light.svg` 通过 `prefers-color-scheme` picture 元素提供，使 hero 匹配观看者的 GitHub 主题；`assets/skill-map.svg` 被重建为一张规格图（关卡 -> 根 -> 集群 -> 参考库 -> 验证）。徽章统一为扁平方形墨/琥珀。生成的位图——hero 镜头和文字密集型信息图，包括 assets/infographic-cdn-delivery-map.png——仍保留在精选视觉画廊中，带可搜索的替代文本，外加从正文迁移过来的操作系统艺术。Token 见 `references/frontend-design-system.md`。
