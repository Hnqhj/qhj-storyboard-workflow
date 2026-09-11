---
name: industry-briefing
description: 多行业信息追踪与精美快报生成；当用户需要获取AI、新能源、医疗、金融、电商等行业的最新动态并生成HTML/Markdown快报时使用
---

# 行业快报生成

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## 任务目标
- 本 Skill 用于：生成多行业信息快报，支持信息追踪、分类整理和格式化输出
- 能力包含：7个预设行业配置、多源信息整合、分类整理、HTML/Markdown格式输出
- 触发条件：用户要求生成某行业的最新动态、行业快报、信息汇总或趋势分析

## 前置准备
- 依赖说明：无外部依赖（Codex 安装版脚本使用 Python 标准库）
- 非标准文件/文件夹准备：无（当前路径视为相对于 Skill 目录的父目录）
- 环境说明：原扣子版本依赖 Linux + Python 3.13 加密核心；当前 Codex 安装版已替换为跨平台纯 Python fallback，可在 Windows/Codex 环境生成 HTML/Markdown

## 操作步骤

### 标准流程

1. 识别行业并加载配置
   - 从 [references/industry_templates.md](references/industry_templates.md) 读取行业配置
   - 匹配用户指定的行业名称（支持模糊匹配）
   - 加载该行业的细分领域、行业特色和关注点
   - 如果用户未指定行业，引导用户从预设7个行业中选择

2. 信息追踪与收集（智能体完成）
   - 优先方式：如果存在 `topic_tracking` 技能，调用该技能进行专业信息追踪
   - 备选方式：由智能体根据行业配置，通过网络搜索和知识库，收集指定日期范围内的行业动态
   - 收集范围：行业细分领域内的最新动态、重要事件、技术进展、市场变化
   - 收集数量：根据用户要求的快报条数（默认10条）

3. 分类整理内容（智能体完成）
   - 按细分领域对收集的信息进行分类
   - 提炼每个条目的核心信息：标题、时间、分类、摘要、来源
   - 标注重要性级别（高/中/低）
   - 确保内容准确、时效性强、覆盖全面

4. 生成快报（脚本处理）
   - 将整理好的内容转换为JSON格式
   - 推荐调用方式：先将整理好的内容保存为 UTF-8 JSON 文件，再调用 `python scripts/generate_briefing.py --industry "行业名称" --theme '["主题1","主题2"]' --start_date "YYYY-MM-DD" --end_date "YYYY-MM-DD" --item_count 10 --format html --content_file "content.json"`
   - 兼容调用方式：`--content 'JSON内容'` 仍可使用；但在 Windows/PowerShell 环境遇到中文内容时优先使用 `--content_file`，避免编码被命令行吞成问号
   - 脚本读取模板，生成HTML或Markdown快报
   - 如用户主要在手机端阅读，可额外调用 `python scripts/render_mobile_image.py --content_file "content.json" --output "briefing_mobile.png"` 输出手机长图
   - 快报保存为文件，路径由脚本返回

### 可选分支

- 当 用户未指定日期范围：默认使用最近7天
- 当 用户未指定条数：默认使用10条
- 当 用户未指定格式：默认生成HTML格式
- 当 行业不在预设列表中：引导用户自定义行业配置，或使用通用模板

## 使用示例

### 示例1：AI行业周报
- 场景/输入：用户需要生成AI行业最近一周的快报，包含大模型和文生图主题
- 预期产出：HTML格式的AI行业快报，包含10条动态，按细分领域分类
- 关键要点：
  - 加载AI行业配置（细分领域：大模型、文生图、视频生成）
  - 收集最近7天的AI动态
  - 按大模型、文生图、视频生成分类
  - 生成带渐变卡片样式的HTML快报

### 示例2：新能源月度报告
- 场景/输入：用户需要生成新能源行业月度报告，包含锂电池和电动车主题，20条动态
- 预期产出：Markdown格式的新能源行业月报，20条动态
- 关键要点：
  - 加载新能源行业配置（细分领域：锂电池、固态电池、电动车）
  - 收集最近30天的新能源动态
  - 重点聚焦锂电池和电动车领域
  - 生成结构清晰的Markdown报告

### 示例3：医疗健康最新动态
- 场景/输入：用户需要医疗健康行业的最新动态，关注创新药领域
- 预期产出：HTML格式的医疗快报，5条动态
- 关键要点：
  - 加载医疗健康行业配置
  - 重点关注创新药领域
  - 收集最近3天的动态
  - 生成简洁的HTML快报

## 资源索引

- 脚本：见 [scripts/generate_briefing.py](scripts/generate_briefing.py)（用途：接收整理好的内容数据，生成HTML或Markdown快报文件；参数：industry、theme、start_date、end_date、item_count、format、content_file/content）
- 长图脚本：见 [scripts/render_mobile_image.py](scripts/render_mobile_image.py)（用途：将同一份 UTF-8 JSON 内容渲染为适合手机阅读的 PNG 长图）
- 参考：见 [references/industry_templates.md](references/industry_templates.md)（何时读取：在步骤1识别行业时，读取该文件获取行业配置、细分领域和关注点）
- 资产：
  - 见 [assets/template.html](assets/template.html)（直接用于生成/修饰输出：HTML模板，包含响应式布局和渐变卡片样式）
  - 见 [assets/template.md](assets/template.md)（直接用于生成/修饰输出：Markdown模板，定义清晰的文档结构）

## 注意事项

- 智能体负责信息追踪和内容整理，脚本负责格式化输出，职责清晰
- 生成的快报文件保存在当前工作目录，文件名格式：`{行业}_快报_{日期}.{format}`
- HTML模板支持动态主题色，可根据行业类型调整配色方案
- 如果 `topic_tracking` 技能不可用，智能体应基于网络搜索和领域知识完成信息收集
- 保持内容时效性，优先选择最新、最权威的信息源
- 快报应包含时间、来源、分类等元数据，便于追溯和验证
- 为主人生成 AIGC 快报时，优先聚焦 AI 创作工具、前沿技术、创作实战、开源社区和重大产品发布；避免泛政策、融资、算力基建等低相关宏观内容
- 中文快报内容必须优先走 UTF-8 JSON 文件 + `--content_file`，不要把长中文 JSON 直接塞进 PowerShell 参数
- 主人日常偏手机阅读，正式 AIGC 快报优先同时产出 HTML 和手机长图；长图采用窄版日报流、左侧蓝紫竖线、摘要 + 影响解读结构
