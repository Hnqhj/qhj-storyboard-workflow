# Image Prompt Workflow

Use this reference when the user wants an image prompt, cover prompt, first-frame prompt, or "刺猬星球superi风格" image.

## Interaction Modes

Use Quick Mode when the user wants speed or gives a simple theme. Use Step Mode when the user is a fan who wants guided choices.

Do not ask repeated questions for information the user already provided. If the user says "随机", choose a coherent option and continue.

## Step Mode Questions

Ask one question at a time unless the user asks for a full form.

Question 1:

```text
第 1 个问题：你想生成人物的性别是什么？
A. 女性
B. 男性
C. 一男一女
D. 随机
```

Question 2:

```text
第 2 个问题：人物年龄段是多少？
A. 16-18 岁
B. 18-22 岁
C. 22-28 岁
D. 28-35 岁
E. 随机
```

Question 3:

```text
第 3 个问题：人物身份是什么？

你可以直接输入任何身份，例如：卖花女、绣娘、茶馆老板娘、赶考书生、江湖女侠、医女、船娘、画师、账房先生。

也可以从下面选一个方向：
A. 宫廷贵女 / 妃子 / 公主
B. 宫女 / 侍女 / 女官
C. 平民少女 / 农家女 / 渔女
D. 市井人物：卖花女 / 茶馆老板娘 / 酒肆女子
E. 手艺人：绣娘 / 医女 / 画师 / 伞匠
F. 书香人物：书生 / 教书先生 / 女先生
G. 江湖人物：侠女 / 女将 / 刺客 / 镖师
H. 权贵男性：皇帝 / 权臣 / 贵公子
I. 我自己输入一个身份
J. 随机
```

Question 4:

```text
第 4 个问题：人物此刻的情绪是什么？
A. 克制
B. 隐忍
C. 警觉
D. 失落
E. 不甘
F. 冷淡
G. 温柔
H. 随机
```

Question 5:

```text
第 5 个问题：服装主色想要什么？
A. 黑金
B. 红金
C. 青绿
D. 紫色
E. 白色
F. 浅蓝
G. 随机
```

Question 6:

```text
第 6 个问题：服装想要什么质感？
A. 宫廷华服
B. 清冷素雅
C. 权贵压迫感
D. 温柔贵女感
E. 少女轻盈感
F. 生活化布衣
G. 江湖利落感
H. 随机
```

Question 7:

```text
第 7 个问题：场景在哪里？
A. 宫殿内室
B. 烛火厅堂
C. 窗前
D. 书房
E. 长廊
F. 庭院
G. 市集/茶馆/酒肆
H. 江湖客栈/竹林/雪街
I. 随机
```

Question 8:

```text
第 8 个问题：光影想要什么感觉？
A. 暖色烛光
B. 柔和窗光
C. 侧逆光
D. 金色宫廷光
E. 暗调电影光
F. 雨后/雾气自然光
G. 随机
```

Question 9:

```text
第 9 个问题：你想要什么构图？
A. 半身近景
B. 胸像特写
C. 全身中景
D. 双人对峙
E. 侧脸特写
F. 随机
```

Question 10:

```text
第 10 个问题：这张图主要用来做什么？
A. 图生视频首帧
B. 短视频封面
C. 教学案例
D. 作品发布
E. 随机
```

After all required answers, summarize:

```text
你的设定我已经整理好了：

人物：[性别]，[年龄段]，[身份]
情绪：[情绪]
服装：[服装颜色]，[服装质感]
场景：[场景]
光影：[光影]
构图：[构图]
用途：[用途]

是否直接生成图片提示词？
A. 直接生成
B. 我想修改一个选项
```

## Quick Mode

When the user gives a broad request, fill missing details coherently:

- gender: female unless theme says otherwise
- age: 22-28
- identity: choose from theme; default to historical-drama noblewoman
- emotion: restrained or hidden sorrow
- clothing: match identity and color mood
- scene: grounded ancient interior or identity-specific location
- light: warm candle/window side light
- composition: vertical 9:16 half-body close shot
- purpose: video first frame

## Image Prompt Output Template

```text
【你的画面设定】
人物：[性别]，[年龄段]，[身份]
情绪：[情绪]
服装：[服装]
场景：[场景]
光影：[光影]
构图：[构图]
用途：[用途]

【图片生成提示词】
请生成一张竖屏 9:16 的真实古装剧电影感画面。人物是[人物设定]，身处[身份适配的场景]，穿着[服装颜色与质感]。[加入身份适配的道具、空间和服化道细节]。人物气质[情绪与身份气质]，像是[一句具体剧情动机]，表面克制，但眼神里有情绪。

人物面部为真实自然的东方面部，五官比例自然，皮肤干净细腻但不油腻、不塑料、不玻璃皮，妆容清透克制，眼神清澈有情绪，脸部光影自然融入场景。

画面采用[构图]，浅景深，[光影]照亮人物脸部，背景具有真实古装剧空间层次。[根据身份加入环境细节]。整体效果像真实古装剧中的剧情帧，而不是古装写真、角色展示、AI 模特摆拍或影楼照。

画面重点：[3-6 个关键词]。

【负面提示词】
[从 style-card 选择紧凑负面词]

【使用建议】
如果平台支持参考图，可以上传合法授权的面部参考图或角色参考图，并说明“参考脸部气质和真实质感，不照搬姿势、服装和背景”。
```

## Next Menu After Image Prompt

```text
下一步你想做什么？

A. 我去生成图片，生成好后上传回来做可灵 O3 视频提示词
B. 修改这张图的设定
C. 换一个人物重新生成
D. 保持同样风格，再生成一个不同版本
E. 生成一组 3 张同风格图片提示词

你直接回复选项字母即可。
```

## Three Image Variants

When the user chooses E or asks for 3 variants, keep the same identity/style but vary:

- Variant 1: emotion close-up
- Variant 2: scene/story action
- Variant 3: stronger cover composition

Each variant should have its own short prompt and shared negative prompt.

