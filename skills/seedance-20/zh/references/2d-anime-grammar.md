# 2D / 动漫语法 —— 执导媒介，而非相机机位

*Seedance 2.0 能很好地渲染风格化的 2D 与动漫运动，但实拍语法会让它退化：镜头、景深和传感器词汇会把输出拉向照片级真实感或假的移轴效果。改用动画制作语言来执导 2D 作品。标签：[field] = 从业者反馈 · [heuristic] = 待测试的默认值。工艺指引编纂于 2026-06-11；不包含任何平台可用性主张。*

## 核心规则 [field]

先点名媒介，并让每个句子都处于动画制作流程之内："hand-drawn 2D animation, cel-shaded characters over a painted background."（手绘 2D 动画，赛璐珞着色角色叠在绘景背景上。）在 2D 提示词中绝不使用镜头、散景、景深、焦距或机身词汇——它会召唤照片级真实的渲染。

## 图层语法 [field]

2D 场景读作堆叠的美术图层，模型对图层语言有反应：

- **赛璐珞叠绘景背景：** 清晰的赛璐珞着色主体叠在柔和的水粉或水彩绘景背景上。
- **背景滚动 / 多平面纵深：** 用 "the painted background scrolls past"（绘景背景滚动而过）或 "foreground silhouettes slide faster than the distant skyline"（前景剪影比远处天际线滑动得更快）来制造视差。
- **背景保持、主体动画：** 声明什么保持静止——保持帧是这门媒介的特性，而非失败。

## 运动语法 [field]

- **爆发式作画（作画／sakuga）与保持帧：** 让高投入的全动画爆发与保持姿势交替："a burst of fluid full animation as she turns, then a held frame on her expression."（她转身时一段流畅全动画的爆发，然后在她的表情上停一个保持帧。）
- **定时：** "animated on twos"（一拍二）用于经典赛璐珞节奏；"on ones"（一拍一）只用于展示性动作。[heuristic]
- **冲击帧：** "a single high-contrast impact frame on the hit."（命中时一个高对比的冲击帧。）
- **速度线与拖影：** "speed lines streak the background during the dash,"（冲刺时速度线划过背景，）"her arm smears across the swing."（她的手臂在挥动中拉出拖影。）
- **跟随动作：** 头发、布料和外套下摆在身体停下后仍继续安顿。

## 2D 中的相机 [field]

"相机"是美术作品之上的台车：横摇扫过绘景背景，在一张保持的脸上缓慢推进，沿着高塔美术作品垂直俯仰。每镜头一个有动机的运动仍然适用。避免推轨、手持抖动和镜头呼吸的真实感措辞。

## 光与色 [field]

光是画出来的，不是渲染出来的："hard two-tone cel shadow,"（硬质双调赛璐珞阴影，）"rim light as a clean shape along the jaw,"（沿下颌画成干净形状的轮廓光，）"specular drawn as a white wedge in the eye."（眼中画作白色楔形的镜面高光。）点名调色板和质感："limited palette, warm paper texture,"（有限调色板、温暖的纸纹，）"flat color with painted light bloom."（平涂色彩配绘制的光晕。）

## 2D 的声音 [heuristic]

风格化的声音比真实拟音读起来更好：拖影上的一声呼啸，冲击帧上的一记尖锐刺音，保持帧上环境音的骤然消失。

## 风格安全 [field]

描述技法、年代和调色板——绝不描述某个工作室、系列或在世艺术家。"1990s hand-painted TV-anime look with grainy film texture"（带颗粒胶片质感的 1990 年代手绘电视动漫风）是安全的语法；具名工作室或系列风格请求要经由 `[skill:seedance-copyright]` 和 `[skill:seedance-style]` 路由。

## 失败 → 修复 [field]

| 症状 | 修复 |
|---|---|
| 输出漂向照片级或 3D-CG | 移除镜头和景深词；以 "hand-drawn 2D cel animation" 起头；点名绘景背景 |
| 运动显得飘忽或转描感 | 要求干脆的"一拍二"爆发、节拍间的保持帧、快速弧线上的拖影 |
| 快速动作中面孔融化 | 把速度放进线条、拖影和背景滚动里，而非面部细节；切到一个保持的冲击帧 |
| 风格在镜头间闪烁 | 在多镜头提示词的每个镜头里重复完全相同的媒介句；保持一个调色板短语不变 |

## 序列边界 [heuristic]

对于相连的 2D 片段，保留角色设定表、调色板、线条粗细、图层角色、画面方向和未完成的运动。把被采用片段中已观察到的最终布局用作下一段的开场布局。在写续接提示词时，不要切换到摄影镜头或传感器语言。
