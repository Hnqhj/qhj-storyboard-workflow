# 反套话词库

用可观察的制作语言替换空洞的评价语言。在各支持语言的提示词社区中经现场确认：抽象的质量词会使生成失稳，因为模型无法判断该强调哪个元素；把它们分解为物理元素（相机动词 + 速度 + 视点，光源 + 方向 + 行为，材质 + 质感 + 运动）会使其稳定。

## 六类套话

| 类别 | 看起来像 | 修复 |
|---|---|---|
| 空洞评价词 | `cinematic, epic, stunning, beautiful, dramatic` | 把每个词转换成配得上它的那个可观察细节 |
| 借来的图像模型 token | `8K, masterpiece, award-winning, trending on ArtStation, Unreal Engine, RAW` | 删除；分辨率和质量是设置或结果，绝非散文措辞 |
| 标签沙拉 | 从图像提示词搬来的逗号分隔关键词堆 | 重写为拍摄简报式散文：每元素一句——主体、动作、相机、光线、声音 |
| 否定套话 | `no blur, no artifacts, no distortion, no extra fingers` | 否定会召唤；以构图方式排除——改为描述存在的东西 |
| 形容词堆叠 | `gorgeous, breathtaking, mesmerizing sunset` | 三个同义词只构成一个软弱的主张；挑那个唯一重要的细节 |
| 感受后缀词 | `电影感 · 雰囲気のある · 감성적인 · atmosférico · атмосферный · vibey` | 点名那份感受的物理成因；每个词汇文件都有一张语言专属的套话陷阱表 |

## 替换表

| 弱表述 | 替换为 |
|---|---|
| cinematic | 景别、相机运动、光线、调色 |
| epic | 物理规模、利害、人群规模、镜头距离 |
| beautiful | 色彩、质感、构图、材质、光线行为 |
| stunning / breathtaking | 可见的对比、揭示、运动或细节 |
| dynamic | 具体的运动、速度和终点 |
| dramatic | 走位、阴影、静默或相机压迫感 |
| ultra-realistic | 材质行为、肤质、镜头瑕疵、自然运动 |
| cool transition | 匹配剪辑、甩镜、叠化、硬切、物体擦除 |
| magical | 粒子行为、辉光来源、运动路径、相互作用 |
| professional | 产品布光设置、干净背景、受控相机 |
| masterpiece / award-winning | 删除；质量不是一个请求 |
| 8K / ultra-HD / high quality | 删除；分辨率是渲染设置，不是散文措辞 |
| atmosphere of mystery | 什么被藏起来了、被什么藏起来：门洞、阴影、雾 |
| insanely / highly detailed | 那两个重要的、被点名的细节 |
| visually striking | 观众记住的那一帧，被描述出来 |
| trending / viral style | 实际的格式：竖屏、快速钩子、字幕安全取景 |

## 标签沙拉修复

图像模型的习惯迁移得很糟：`girl, sunset, 8K, cinematic, beautiful light, masterpiece, detailed face` 给视频模型既没有动作、没有相机，也没有时间轴。重写为简报：`A woman turns from the railing at sunset; the low sun flares behind her hair. Camera: slow push-in to a medium close-up. Sound: wind and distant surf.` 每元素一句胜过二十个逗号碎片。

## 否定规则

点名一个瑕疵就种下了它。与其写 `no blur, no extra fingers, no watermark text`，不如锁定正面：`hands rest still on the table`（双手静放桌上）、`clean unbroken label`（干净完整的标签）、`empty sky above the skyline`（天际线上方空荡的天空）。仅在平台预期的约束槽位里使用否定（`no on-screen text, no watermark`），绝不把它当作质量保险。

规则：若相机、麦克风、测光表或秒表无法探测到它，就重写它。

`references/vocab/` 中的每个语言文件都为其所属社区的空洞词携带一张套话陷阱表：英语（`vocab/en.md`）、中文（`vocab/zh.md`）、日语（`vocab/ja.md`）、韩语（`vocab/ko.md`）、西班牙语（`vocab/es.md`）、俄语（`vocab/ru.md`）。
