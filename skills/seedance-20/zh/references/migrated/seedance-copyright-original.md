# `seedance-copyright` 的遗留正文

迁移于 2026-04-27 的 v5.1.0 期间。除非在 `references/api-status.md` 或 `references/source-registry.md` 中得到确认，否则将此处的平台、政策、API 与安全声明视为遗留内容。

---

# seedance-copyright

Seedance 2.0 的内容政策与 IP 保护规则。
每次生成在提交前都必须通过此检查清单。

---

## ⚠️ 2026 年 2 月执行背景

> **发生了什么（2026 年 2 月 12–25 日）：**
> ByteDance 于 2 月 12 日发布 Seedance 2.0。几天内，迪士尼、派拉蒙 Skydance、Netflix、美国电影协会（MPA）及 SAG-AFTRA 都发出了停止侵权函。迪士尼的信件称其为对 IP 的"虚拟暴力抢夺"。Netflix 称其为"高速盗版引擎"。日本政府启动了监管调查。
>
> ByteDance 的回应（2 月 15 日）："我们正采取措施加强当前的保护机制，努力防止用户未经授权使用知识产权与相似性。"
>
> **API 状态是平台特定的，必须对照当前官方文档核查**，自原计划的 2 月 24 日起。未设定新的发布日期（截至 2 月 25 日）。
>
> **这对提示词意味着什么：** 硬性拦截比 v3.0 更严格。许多角色/相似性过滤器已被收紧。假定任何被命名的特许经营角色、演员或流媒体原创内容都会被拒绝或被静默降级。

---

## 核心原则

Seedance 拦截引用特定受保护知识产权的内容。
模型不拦截*概念*、*美学*或*原型*——只拦截被命名的、有所有者的身份。
你的任务：描述这个想法，而不指明其所有者。

---

## 硬性拦截（高风险，应重写）

无论如何框定，这些都会触发内容拒绝：

| 类别 | 示例 | 为何被拦截 |
|---|---|---|
| 指名道姓的真人面孔 | "Elon Musk", "Taylor Swift", "Obama", "Tom Cruise" | 公开权 / 相似性权利 |
| 被命名的特许经营角色 | "Iron Man", "an original masked acrobat hero", "Darth Vader", "Deadpool" | 迪士尼/漫威 IP（停止侵权函生效中） |
| 被命名的皮克斯 / 迪士尼动画 | "Elsa", "Woody", "Wall-E", "Simba" | 迪士尼 IP |
| 被命名的动漫角色 | "Naruto", "Goku", "Luffy", "Levi", "Demon Slayer" | 工作室/出版商 IP + 日本政府调查 |
| 被命名的游戏角色 | "Mario", "Master Chief", "Geralt", "Kratos" | 任天堂/微软/索尼/CD Projekt IP |
| 被命名的流媒体原创 | "Stranger Things characters", "Squid Game guard", "Bridgerton" | Netflix IP（停止侵权函生效中） |
| 派拉蒙 IP | "Shrek", "SpongeBob", "Dora", "Mission Impossible" | 派拉蒙 Skydance 停止侵权函生效中 |
| 被命名的 DC 角色 | "Batman", "Superman", "Wonder Woman", "Joker" | WB/DC IP |
| 可见的品牌标志 | Nike swoosh, Apple logo, Coca-Cola script | 商标侵权 |
| 受版权保护的场景再现 | 来自被命名影片的精确镜头 | 电影工作室版权 |
| 被命名的音乐作品 | "Play Bohemian Rhapsody as the score" | 音乐出版权 |
| 深度伪造 / 换脸请求 | "Replace @Image1's face with [celeb]" | 深度伪造政策 + ByteDance 上传拦截 |
| 军队 / 政府徽章 | 带单位徽章的特定武装部队制服 | 法规 + 潜在政策 |

---

## 实时执行示例（2026 年 2 月）

这些在 MPA 与迪士尼法律函件中被具体引用为被拦截示例：

| 提示词类型 | 触发拦截的原因 |
|---|---|
| "an original masked acrobat hero fighting Captain America on the streets of New York" | 被命名的漫威角色 |
| "Anakin Skywalker and Rey battling with lightsabres" | 被命名的星球大战角色 |
| "Stranger Things characters in a new scene" | 被命名的 Netflix 原创 |
| "Deadpool and Wolverine fight sequence" | 被命名的漫威角色 |
| "Shrek walks through a swamp" | 被命名的派拉蒙角色 |
| "Tom Cruise and Brad Pitt fight scene" | 被命名的真实演员（2 月 15 日后引发热议的拒绝） |

> **注意：** 引发争议的 Tom Cruise / Brad Pitt 打斗片段是在 2 月 15 日收紧之前生成的。2 月 15 日之后，被命名的真人请求会静默失败或返回通用的拒绝消息。

---

## 软性拦截（依语境而定）

这些可能通过或失败，取决于框定方式与视觉具体程度：

| 类别 | 风险等级 | 备注 |
|---|---|---|
| 真实建筑外观 | 低–中 | 埃菲尔铁塔 = 公有领域。悉尼歌剧院 = 受版权保护至 2067 年。 |
| 历史人物 | 中 | 已故 + 70 年以上 = 通常安全。近代历史 = 风险升高。 |
| 通用超级英雄美学 | 低 | 红金装甲战衣 = OK。"Iron Man suit" = 被拦截。 |
| 时尚 / 品牌配色 | 低 | Tiffany 蓝裙 = OK。"Tiffany & Co. branding" = 被拦截。 |
| 文化 / 宗教意象 | 中 | 语境敏感。避免在商业语境中使用神圣符号。 |
| 真实地点附近的暴力 | 高 | 避免生成引用真实被命名地点的暴力内容。 |
| 动漫风格角色（未命名） | 低-中 | 原创角色设计 OK；与被命名角色的视觉相似 = 风险。 |
| Netflix / 流媒体 UI 元素 | 高 | 显示标志、剧集卡、界面 = 被拦截。 |

---

## 安全替换表

用描述性原型替换被命名的 IP。始终思考：*它看起来像什么，而非它叫什么？*

### 影视与银幕角色

| ❌ 被命名 IP | ✅ 安全描述符 |
|---|---|
| Iron Man | red-and-gold powered exoskeleton, chest reactor glow |
| Batman | dark armored vigilante, scalloped cape, bat emblem absent |
| an original masked acrobat hero | red-and-blue spandex web-shooter acrobat |
| Darth Vader | black full-helmet respirator suit, red energy blade |
| Deadpool | red-and-black tactical suit, masked mercenary, dual katanas on back |
| Terminator | chrome endoskeleton humanoid, single red eye |
| The Joker | smeared clown makeup, green hair, purple coat |
| Thanos | large purple-skinned humanoid with golden gauntlet |
| Elsa (Frozen) | platinum-haired woman in ice-blue gown, frost particles emanating from hands |
| Shrek | large green-skinned ogre, brown vest, Scottish accent implied in gesture |

### Netflix / 流媒体原创角色

| ❌ 被命名 IP | ✅ 安全描述符 |
|---|---|
| Stranger Things – Eleven | young girl, buzzed head, nosebleed, telekinetic gesture |
| Stranger Things – Demogorgon | multi-petaled faceless biped, tall, dark biomass skin |
| Squid Game guard | hot-pink coverall figure, black circle/triangle/square mask |
| Bridgerton aesthetic | Regency-era ballroom, empire-waist gowns, string quartet |

### 动漫角色

| ❌ 被命名 IP | ✅ 安全描述符 |
|---|---|
| Naruto | blond spiky-haired shinobi, orange jumpsuit, whisker scars |
| Goku | dark spiky-haired martial artist, orange gi, muscular |
| Luffy | straw-hat pirate, red vest, scar under left eye |
| Sailor Moon | blonde twin-tailed girl, white sailor uniform, crescent moon |
| Evangelion Unit-01 | purple-and-green giant mecha, single horn, four eyes |
| Totoro | large grey forest spirit, pointed ears, cat-like body |
| Demon Slayer – Tanjiro | dark-haired boy, checkered haori, box on back |
| Attack on Titan – Levi | short dark-haired soldier, vertical maneuvering gear, green cape |

### 游戏角色

| ❌ 被命名 IP | ✅ 安全描述符 |
|---|---|
| Master Chief | green full-body military power armor, golden visor |
| Link (Zelda) | green-tunic elf warrior, pointed hat, triangular shield |
| Geralt | white-haired witcher, dual swords on back, amber eyes |
| Kratos | bald grey-skinned warrior, red facial tattoo, chain blades |
| Aloy | red-haired hunter, tribal leather armor, focus device on ear |
| 2B (NieR) | blindfolded android, black gothic dress, white hair |

### 品牌与标志替换

| ❌ 品牌引用 | ✅ 安全描述符 |
|---|---|
| Nike swoosh | curved checkmark logo on athletic wear |
| Apple logo | silver bitten-fruit icon on laptop |
| McDonald's arches | golden M arches, fast food restaurant |
| Coca-Cola script | red can, white cursive brand lettering |
| Ferrari horse | rearing black horse emblem on red sports car hood |
| Louis Vuitton print | repeating tan-and-brown monogram canvas |

---

## 真人政策

### 已故公众人物（70 年以上）
对历史性描绘通常安全。使用与时代相符的服装与场景。
```
✅ Victorian-era inventor in a laboratory, period suit, white beard, working on electrical coils
```

### 在世公众人物
**绝不**按姓名或以鲜明相似性生成。（2 月 15 日的过滤收紧拦截了大多数基于姓名的请求。）
```
❌ "Elon Musk standing next to a rocket"
✅ "tech billionaire in casual black T-shirt, standing on launch pad"

❌ "Tom Cruise in a fight scene"
✅ "athletic 50s male actor type, sharp jaw, cropped brown hair, grey blazer, fighting stance"
```

### 历史人物（近代，去世不足 70 年）
风险升高。使用原型语言。
```
❌ "Martin Luther King Jr. giving a speech"
✅ "civil rights leader at a podium, crowd in Washington Mall, 1960s period dress"
```

### 虚构演员相似性
即使扮演虚构角色，也绝不使用演员的面孔。
```
❌ "Robert Downey Jr. as Tony Stark"
✅ "genius billionaire in a red-gold suit, goatee, reactor in chest"
```

### 真人上传（@Image 中的面孔）
ByteDance 自 2026 年 2 月 15 日起暂停了用户上传真人面孔图像。
```
❌ Upload photo of Tom Cruise → "Generate as action hero"
✅ Upload original character art → "Generate as action hero"
```

---

## 建筑与楼宇

部分建筑仍处于有效版权之下。

| 建筑 | 状态 | 备注 |
|---|---|---|
| 埃菲尔铁塔（白天） | 公有领域 | 安全 |
| 埃菲尔铁塔（夜间照明） | 受版权保护 | 灯光秀设计受保护 |
| 悉尼歌剧院 | 受保护至约 2067 年 | 使用 "iconic white shell-roof opera house" |
| 古根海姆毕尔巴鄂 | 受保护 | 使用 "titanium-clad curvilinear museum" |
| 卢浮宫金字塔 | 受保护至 2029 年 | 使用 "glass pyramid in courtyard of classical stone palace" |
| 帝国大厦 | 有部分限制 | 一般外观通常没问题；精确复制有风险 |
| 大多数 1900 年前的建筑 | 公有领域 | 安全 |

---

## 音乐与音频

| ❌ 被拦截 | ✅ 安全 |
|---|---|
| "Play Stairway to Heaven as the score" | "electric guitar power chord progression, rising tempo" |
| "BGM similar to Hans Zimmer's Inception theme" | "deep brass sting, slow bwaaah, building tension" |
| "Use a Drake beat" | "trap hi-hats 140 BPM, 808 bass, minimalist" |
| "Beethoven's 5th Symphony" | "dramatic orchestral opening, four-note fate motif, strings" |
| "John Williams Star Wars march" | "heroic brass fanfare, snare drum march, rising French horns" |

1928 年前的作品在美国属于公有领域。描述质地、节奏、配器——而非标题。

---

## 美学借鉴 vs. 直接复制

你**可以**借鉴一部影片的视觉语法。你**不能**再现被命名的场景。

### 安全：美学参考
```
✅ "washed-out teal-orange color grade, anamorphic lens flare, handheld shake"
   (describes the look without naming the film)
```

### 被拦截：场景再现
```
❌ "Recreate the Pulp Fiction diner scene with @Image1 as Vincent"
✅ "1970s diner, two men in black suits at a booth, morning light,
   16mm grain, conversation framing"
```

### 安全：类型语法
```
✅ "neon-drenched rain-soaked street, flying cars overhead, Asian signage,
   cyberpunk dystopia" — describes Blade Runner's world without naming it
```

### 被拦截：流媒体特定的世界构建
```
❌ "Stranger Things-style retro-80s supernatural horror with practical monsters"
✅ "1980s American suburb, flickering lights, child protagonists in Halloween
   costumes, practical rubber creature design, warm Super-8 grain"
```

---

## 2 月 15 日后的实用检查清单

每次生成前，运行全部六道关卡：

1. **姓名检查** —— 提示词是否包含任何真人姓名？→ 移除。
2. **IP 检查** —— 它是否点名某个特许经营、角色或品牌？→ 用描述符替换。
3. **场景检查** —— 它是否是某个受版权保护的特定场景或剧集的再现？→ 通用化重新框定。
4. **音频检查** —— 它是否请求被命名的歌曲或作曲家的作品？→ 用音乐方式描述。
5. **建筑检查** —— 它是否点名某个可能受保护的建筑？→ 使用建筑描述符。
6. **标志检查** —— 输出是否会包含可识别的标志？→ 不带品牌名地描述几何形态。

六项全部通过 → 可安全生成。

---

## 为何这很重要（对开发者而言）

2026 年 2 月的执行事件改变了 API 格局：
- **API 发布延迟** —— 在 ByteDance 发布新时间表之前，无法围绕某个集成日期做规划。
- **过滤收紧将持续** —— MPA 要求 2 月 27 日作出回应。预期会有进一步的内容过滤更新。
- **平台可行性模式** —— ByteDance 可能走 OpenAI/迪士尼路线：与工作室达成授权协议，作为重新启用角色内容的途径。
- **开源替代品** —— 社区讨论（r/comfyui）指向 WAN 2.2 与本地 OSS 模型作为无过滤的替代品，但输出质量较低。

---

## 路由

提示词结构 → [skill:seedance-prompt]
无 IP 的风格迁移 → [skill:seedance-style]
角色身份 → [skill:seedance-characters]
QA/被拦截的输出 → [skill:seedance-troubleshoot]
