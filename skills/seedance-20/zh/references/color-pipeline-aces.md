# 色彩管线与 ACES 说明

当 Seedance 输出必须进入专业剪辑、调色、HDR/SDR 流程、代理审核或交付工作流时，使用本参考。

## 诚实的边界

Seedance 提示词能描述色彩意图、光线动机、对比度、调色板、材质响应和情绪。它们无法取代经测量的色彩管理、校准监看、套底、调色、合法范围检查或交付变换。让提示词语言保持创意性；把管线语言作为后期的元数据。

## 提示词级色彩意图

使用：

- 源光：钨丝实用灯、阴天日光、钠灯街光、霓虹招牌、冷月轮廓光；
- 对比度：柔和低对比、硬质黑色电影对比、干净的产品对比、高调美感；
- 调色板：克制的暖/冷分割、低饱和冬季调色板、饱和的音乐视频调色板；
- 材质响应：拉丝金属高光、肤质过渡、亮面亚克力反射、湿沥青镜面高光；
- 转变：实用灯使脸部变暖、闪电短暂地令剪影变硬。

避免：

- 不受支持的主张，如仅凭一条提示词就达到确切的 ACES 合规；
- 不可能的堆叠，如在一段短镜头里同时要 HDR 杜比视界、16mm、霓虹、漂白旁路和柔彩商业感；
- 把 LUT 名称当作魔法风格词而不描述可见的结果。

## 待跟踪的后期元数据

对于专业交接，记录：

| 字段 | 含义 |
|---|---|
| capture/source | 生成的源、参考片段、静帧、源帧 |
| 工作色彩空间 | 项目的工作假设，常为 ACEScct/ACEScg 或编辑器管理的替代方案 |
| IDT/源变换 | 源媒体如何被解释（如适用） |
| show look | 创意风格描述、LUT/CDL/LMT 说明 |
| 输出变换 | SDR Rec.709、HDR PQ、院线/DCP、社交平台转换 |
| 微调流程 | 单独的 SDR/HDR/社交审核说明 |
| QC 说明 | 削波、非法电平、色带、肤色、产品色、徽标色 |

## ACES 友好交接

当用户要求 ACES 时，用两层答案回应：

1. 提示词：Seedance 能理解的可见色彩和光线指令。
2. 交接：供剪辑师或调色师在 Seedance 之外验证的 ACES/AMF/色彩说明。

示例：

`Prompt look: cool overcast daylight with a warm practical lamp reflected in the bottle, soft contrast, clean highlight rolloff, no crushed blacks. Post note: conform generated clip into the project color pipeline, verify source interpretation, preserve product color, create SDR Rec.709 and HDR trim review if required.`

## 色彩失败修复

| 症状 | 修复 |
|---|---|
| 图像发平 | 添加有动机的主光源、轮廓/分离，以及一处材质高光 |
| 色彩过度处理 | 减少风格名称；指定自然对比度和中性的肤色/产品色 |
| 跨镜头色彩不一致 | 在每个镜头里重复光线方向、时辰、调色板和 show-look 说明 |
| 产品色错误 | 使用 I2V 产品参考、锁定相机，以及产品色保留约束 |
| HDR/社交不匹配 | 让提示词保持中性；在后期规划单独的调色/导出版本 |
