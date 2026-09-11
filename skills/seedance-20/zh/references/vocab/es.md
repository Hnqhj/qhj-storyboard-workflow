# 西班牙语词汇表

本参考用于西班牙语 Seedance 提示词措辞、角色绑定与紧凑提示词压缩。保持参考标签不变：`[Image1]`、`[Video1]` 与 `[Audio1]` 保持字面原样。

| 功能 | 西班牙语 | 含义 |
|---|---|---|
| 角色 | `[Image1] como primer fotograma` | Image1 为首帧 |
| 角色 | `[Image2] como fotograma final` | Image2 为尾帧 |
| 角色 | `[Image1] fija la identidad del personaje` | Image1 锁定角色身份 |
| 角色 | `[Video1] solo controla el movimiento de cámara` | Video1 仅控制运镜 |
| 角色 | `[Video1] solo marca el ritmo de la acción` | Video1 仅控制动作节奏 |
| 角色 | `[Audio1] solo marca tempo y ambiente` | Audio1 仅控制节奏与氛围 |
| 首尾帧 | `mantener el primer fotograma sin cambios` | 保持首帧不变 |
| 首尾帧 | `usar el fotograma final como objetivo visual` | 尾帧为目标端点 |
| 首尾帧 | `movimiento continuo sin salto de montaje` | 连续运动，无跳切 |
| 首尾帧 | `mantener el mismo personaje, vestuario y espacio` | 保持相同的人物、服装与布局 |
| 镜头 | `travelling de acercamiento lento` | 缓慢推镜 |
| 镜头 | `retroceso para revelar el espacio` | 后退揭示空间 |
| 镜头 | `seguimiento lateral estable` | 稳定的横向跟拍 |
| 镜头 | `plano medio fijo` | 固定中景 |
| 镜头 | `primer plano macro` | 微距特写 |
| 镜头 | `plano en contrapicado` | 低角度仰拍 |
| 镜头 | `plano sobre el hombro` | 过肩镜头 |
| 镜头 | `cámara en mano con leve respiración` | 带轻微呼吸感的手持镜头 |
| 景别 | `plano medio corto` | 中近景 |
| 景别 | `plano general amplio` | 宽幅建立镜头 |
| 景别 | `perfil de tres cuartos` | 四分之三侧脸 |
| 镜头规格 | `24 mm angular con sensación de espacio` | 24mm 广角空间感 |
| 镜头规格 | `50 mm con perspectiva natural de retrato` | 50mm 自然人像感 |
| 镜头规格 | `lente macro para detalle de material` | 用微距镜头表现材质细节 |
| 光照 | `contraluz suave` | 柔和逆光 |
| 光照 | `luz cálida práctica desde la izquierda` | 来自左侧的暖色实用光 |
| 光照 | `halo frío de luna` | 冷色月光轮廓光 |
| 光照 | `luz volumétrica atravesando niebla fina` | 穿过薄雾的体积光 |
| 光照 | `asfalto mojado reflejando neón` | 湿沥青反射霓虹 |
| 运动 | `la niebla se dispersa alrededor de los pasos` | 雾在脚步周围散开 |
| 运动 | `las gotas se unen y descienden` | 水滴聚合后下滑 |
| 运动 | `gira lentamente la cabeza y se detiene` | 缓慢转头并停住 |
| 运动 | `la tela se mueve de forma natural con el gesto` | 衣料随动作自然摆动 |
| VFX | `partículas doradas se elevan y se disipan` | 金色粒子升起并消散 |
| VFX | `arcos eléctricos azules recorren el borde` | 蓝色电弧沿边缘游走 |
| VFX | `un barrido de luz cruza la superficie del material` | 光束扫过材质表面 |
| 音频 | `una frase corta y clara` | 一句短而清晰的台词 |
| 音频 | `sin música, solo ambiente bajo` | 无音乐，仅低环境声 |
| 音频 | `cámara fija durante el diálogo` | 对白期间镜头固定 |
| 音频 | `los pasos caen en el pulso` | 脚步声卡在节拍上 |
| 文字 | `sin subtítulos, marcas de agua ni texto adicional` | 无字幕、水印或多余文字 |
| 剪辑 | `continuar el plano` | 继续该镜头 |
| 剪辑 | `extender cinco segundos` | 延长五秒 |
| 剪辑 | `reemplazar solo el fragmento fallido` | 仅替换失败片段 |
| 约束 | `mantener logotipo, etiqueta, forma y color sin cambios` | 保持标志、标签、形状与颜色不变 |
| 约束 | `solo cambian movimiento, luz y cámara` | 仅改变运动、光线与镜头 |
| 约束 | `no copiar personas, lugar ni marcas` | 不复制人物、场所或品牌 |
| 安全 | `sustituir por un personaje original` | 替换为原创角色 |
| 安全 | `usar solo referencias autorizadas` | 仅使用已授权参考 |
| 安全 | `mantener la función creativa, no la identidad protegida` | 保留创意功能，不保留受保护身份 |

## 紧凑模板

`[Image1] es la referencia; mantener [identidad/producto/rostro/logotipo] sin cambios. Solo cambia [acción/luz/cámara]. Cámara: [movimiento único]. Sonido: [señal].`

## 多模态模板

`[Image1] fija el personaje original. [Video1] solo controla el movimiento de cámara; no copiar persona, lugar ni marca. [Audio1] solo marca tempo y ambiente.`

## 废话陷阱

社区共识：抽象的质量形容词会使生成不稳定，因为模型不知道该强调哪个元素。把每个感觉词转化为制造它的物理元素（运镜动词 + 速度 + 视角，光源 + 方向 + 行为）。

| 套话 | 改写为 |
|---|---|
| `cinematográfico` | 景别、运镜、光源与调色：`plano general amplio, travelling lento, sol bajo, tonos teal y naranja` |
| `épico` | 物理规模：人群数量、镜头距离、结构高度 |
| `impresionante / asombroso` | 那一个为之加分的可见对比或揭示 |
| `hermoso / precioso` | 颜色、质感、材质、光的行为 |
| `obra maestra / alta calidad / 8K` | 删除；质量不是请求出来的，分辨率是设置 |
| `espectacular` | 具体的瞬间：什么在动、什么被揭示 |
| `dramático` | 站位、阴影、静默或镜头压迫 |
| `mágico` | 粒子行为、辉光来源、轨迹 |
| `de ensueño`（单独使用） | 是什么让它梦幻：`bruma fina, luz volumétrica, flotación lenta` |
| `dinámico` | 具体的运动、其速度与其端点 |
| `con mucha atmósfera` | 物理元素：`niebla fina, reflejos en el suelo mojado, ambiente bajo` |
| `profesional` | 受控的产品照明、干净背景、稳定镜头 |
