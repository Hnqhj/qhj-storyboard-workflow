---
name: seedance-lighting
description: "This skill should be used when the user asks for lighting design, atmosphere, time of day, color temperature, shadow, reflections, weather light, practical lights, or mood transitions in Seedance 2.0."
license: MIT
metadata:
  version: "6.1.0"
  updated: "2026-06-22"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-lighting

光线应描述物理光源与转变，而非抽象的美感。一条有用的光线提示词会告诉模型光从何处来、它的色温、阴影如何表现、什么样的氛围介质承接了光线，以及光线在镜头过程中是否变化。

当用户要求 ACES、HDR/SDR、节目风格、调色、LUT、CDL、产品色彩或专业色彩交接时，加载 `[ref:color-pipeline-aces]`。要把光线作为情绪来处理时——比率、主光方向、色温、动机，以及随戏剧转折而变化的光——加载 `[ref:directing-engine]`，使光线表达场景的意图，而不只是照亮它。

## 意图

当用户说出情绪词时，他们几乎总是在要求光线。本技能的目的，是把"温馨""孤独"或"带电"这类词，用一轮太阳、一盏灯或一扇窗来回应——因为那正是情感在画面中物理栖身之处。把他们的情绪作为一个他们能指给你看的光源还给他们。

## 光线契约

陈述：主光源、方向、色温、氛围介质、阴影表现、反射表现，以及任何转变。

| 情绪或任务 | 可直接用于提示词的光线 | 为何有效 |
|---|---|---|
| 产品奢华感 | `narrow warm strip light sweeps across brushed metal, black acrylic reflection remains clean` | 材质与反射受到控制。 |
| 夜间剧情 | `warm practical lamp from frame left, blue moonlight rim on shoulders, soft hallway shadows` | 使用有动机的光源。 |
| 发现/揭示 | `door crack opens and a thin white beam widens across dust in the air` | 光随动作而变化。 |
| 食物真实感 | `large soft window light from the right, gentle bounce on the plate, no harsh specular glare` | 保持质感清晰可辨。 |
| 风暴氛围 | `cool overcast daylight, intermittent lightning flashes briefly sharpen the silhouette` | 天气影响对比度。 |

## 光源选择

室内、亲密感与可见动机用**实用灯具（practical lamps）**。自然主义以及食物或生活方式场景用**窗光（window light）**。当需要分离时用**轮廓光（rim light）**。黑色电影、刺眼阳光或图形化阴影用**硬光（hard light）**。美感、肤质、产品精致度，以及儿童或家庭场景用**柔光（soft light）**。当场景需要可见的变化时用**移动光（moving light）**。

## 色彩与氛围

仅在重要时点明色温：暖钨丝光、冷月光、绿色荧光、钠灯街光、中性阴天日光。氛围介质要克制地添加：薄雾、灰尘、雨丝、烟雾或凝结的水汽，应与光线和主体相互作用，而不只是装点画面。

## 失败修复

若输出看起来发平，加入一个有动机的主光源、轮廓分离，以及一处针对材质的高光。若看起来过度处理，去掉宽泛的风格主张并指定更柔和的对比度。若出现闪烁或光线跳变，让光源保持稳定并移除相互竞争的转变。

## 序列状态

当存在序列状态时，继承持续的实用光源、主光方向、光线阶段、当前镜头范围、连续性锁定项、精确的引用标签，以及预留的未来节拍。除非转变或允许变化明确许可，否则不要重置昼/夜、实用灯具或天气光。

## 输出契约

返回一个紧凑的光线块、必要时的转变说明，以及一句可直接用于提示词的整合句。
