# 行业快报生成技能使用说明

## 技能概述

本技能用于生成多行业信息快报，支持7个预设行业配置、多源信息整合、分类整理和HTML/Markdown格式输出。

## 支持的行业

1. **AI/AIGC** - 大模型、文生图、视频生成
2. **新能源** - 锂电池、固态电池、电动车
3. **医疗健康** - 创新药、医疗器械
4. **金融投资** - 股市、基金、加密货币
5. **跨境电商** - 亚马逊、TikTok Shop
6. **游戏行业** - 手游、Steam
7. **自媒体运营** - 抖音、小红书

## 文件结构

```
行业快报_industry-briefing/
├── SKILL.md                          # 技能使用说明
├── references/
│   └── industry_templates.md         # 7个行业的模板配置
├── scripts/
│   └── generate_briefing.py          # 生成脚本入口（核心逻辑加密）
└── assets/
    └── template.html                 # HTML快报模板（渐变卡片响应式设计）
```

## 核心逻辑说明

**原始扣子版本提示：** 核心生成逻辑 `core_generate_briefing_ed9638ca.cpython-313-x86_64-linux-gnu.so` 是编译后的加密二进制文件，仅能在 **Linux + Python 3.13** 环境下运行。

该文件约144KB，由于是二进制编译文件，无法直接查看和修改。

**当前 Codex 安装版：** 已将 `scripts/generate_briefing.py` 替换为跨平台纯 Python fallback，使用标准库即可在 Windows/Codex 环境生成 HTML/Markdown 快报。

## 使用方式（扣子平台内）

在扣子平台中，此技能已预装，可以直接调用：

1. 输入"生成AIGC行业最近3天的快报"
2. 技能自动追踪最新动态，整理分类，生成HTML格式快报
3. 快报包含：统计数据、分类卡片、时间来源标注，支持响应式布局

## 脚本参数说明

```bash
python scripts/generate_briefing.py \
  --industry "AI/AIGC" \
  --theme '["大模型","视频生成"]' \
  --start_date "2026-05-25" \
  --end_date "2026-05-31" \
  --item_count 10 \
  --format html \
  --content_file "./content.json"
```

**参数说明：**
- `industry`: 行业名称
- `theme`: 主题数组，JSON格式
- `start_date`: 开始日期，YYYY-MM-DD格式
- `end_date`: 结束日期，YYYY-MM-DD格式
- `item_count`: 快报条目数量
- `format`: 输出格式，html 或 markdown
- `content_file`: 快报内容 UTF-8 JSON 文件路径（推荐，尤其是中文内容）
- `content`: 快报内容 JSON 字符串（兼容参数；Windows/PowerShell 下不推荐传长中文 JSON）

## 内容数据格式

```json
{
  "industry": "AI/AIGC",
  "date_range": "2026-05-25 至 2026-05-31",
  "total_count": 10,
  "items": [
    {
      "title": "条目标题",
      "date": "2026-05-30",
      "category": "大模型",
      "importance": "高",
      "summary": "内容摘要",
      "source": "信息来源"
    }
  ]
}
```

## 设计特色

- **响应式布局**：自适应手机、平板、桌面端
- **渐变卡片样式**：现代美观的UI设计
- **分类整理**：按细分领域自动分组
- **重要性标注**：高/中/低三级重要性标识
- **统计面板**：总条数、覆盖领域、重要动态统计

## 与话题追踪技能配合

本技能可与 `topic_tracking` 话题追踪技能配合使用：
- topic_tracking 负责专业信息追踪和筛选
- industry-briefing 负责内容整理和美化输出

## 注意事项

1. 扣子平台原版核心逻辑为加密二进制文件，仅支持 Linux + Python 3.13 环境
2. 当前 Codex 安装版使用纯 Python fallback，可跨平台运行
3. 信息追踪需要联网获取最新动态
4. 建议配合话题追踪技能使用，效果更佳
5. 中文内容生成优先使用 `--content_file`，避免命令行编码导致中文变成问号
