---
name: seedance-recipes
description: "This skill should be used when the user asks for a Seedance 2.0 template, genre recipe, product ad, lifestyle video, drama scene, music video, landscape shot, commercial, animation scene, or reusable production pattern."
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

# seedance-recipes

把配方当作起始范式，而非僵硬的提示词模板。挑选与用户结果相匹配的配方，然后定制主体、动作、相机、光线、音频和约束。配方应保留短镜头的"一节拍"纪律。

加载 `[ref:genre-guides]` 获取类型范式，当用户需要可直接复制的范例时加载 `[ref:examples-by-mode]`，为专业的多镜头序列或商业广告加载 `[ref:shot-list-continuity]`，当配方应反映中文/俄文/日文/韩文/西班牙文社区风格结构时加载 `[ref:multilingual-community-examples]`。

## 意图

配方是一个起跑优势，绝非一个模具。用户想要的，是一个被验证过的形态所带来的信心，里面装着他们自己的故事。每一次都把配方弯折去贴合故事；一个感到自己被模板化的用户，即便输出尚算合格，也已经被辜负了。

## 配方家族

| 家族 | 最佳用途 | 核心范式 |
|---|---|---|
| Product | 广告、电商、英雄镜头、材质揭示。 | `product anchor + one material change + controlled camera + logo preservation` |
| Lifestyle | 人物使用、食物、旅行、社交片段。 | `simple action + lived environment + handheld or natural light + ambient sound` |
| Drama | 情绪、对白、简短叙事节拍。 | `character tag + gesture + motivated camera + silence or sparse sound` |
| Music video | 节拍同步、舞蹈、风格化剪辑。 | `rhythm reference + visible beat changes + light pulses + clear character blocking` |
| Landscape | 建立镜头、自然、氛围。 | `slow camera + weather motion + layered depth + natural sound` |
| Commercial | 品牌安全的精致感与功能性。 | `problem/use/result beat + precise product constraint + clean light` |
| Animation | 原创角色与风格化运动。 | `medium + shape language + palette + elastic or weighted motion` |
| VFX | 变换、粒子、天气、能量。 | `source + material behavior + interaction + dissipation endpoint` |
| First/last frame | 中间过渡、产品状态变化、角色姿势目标。 | `first frame + last frame + continuous transition + identity locks` |
| Commercial campaign | 6/10/15/30 秒变体、竖屏/社交剪短版、无字版/本地化母版。 | `hook + product proof + end state + cutdown matrix + delivery notes` |
| Short drama (短剧) | 快剪竖屏迷你剧节拍：铺垫、反转、悬念。 | `two or three labeled shots + one emotional reversal + held reaction close + cut on the sting` |
| Talking head (口播) | 主持人、讲解、直播式对镜推销。 | `locked medium close-up + short quoted lines + minimal head motion + caption-safe framing + room tone` |
| Home / space tour | 房间、场地或房产的漫步导览。 | `single continuous take + steady forward path + light changes per zone + ambient sound only` |

## 提示词骨架

**Product I2V:** `[Image1] is the product reference; preserve logo, label, shape, and materials exactly. [One material or light change]. Camera: [single move]. Lighting: [physical source]. Sound: [ambient/SFX].`

**Drama T2V:** `Character A [visible emotional action] in [specific setting]. Camera: [motivated framing]. Lighting: [motivated source]. Sound: [ambient or short dialogue]. End state: [changed expression/action].`

**Reference Motion:** `[Video1] provides only [camera/action/timing] reference; do not transfer identity, costume, logo, or environment. New subject: [authorized/original subject]. [Action and endpoint].`

**First/Last Frame:** `[Image1] is the first frame. [Image2] is the last frame. Preserve [identity/product/scene anchors]. Generate a continuous transition from [start state] to [end state]. Camera: [locked or one controlled move]. Sound: [ambient/SFX].`

**Animation:** `Original [character archetype] [action] in [environment]. Style: [medium, line quality, texture, palette]. Motion: [rhythm]. Camera and sound: [simple support].`

## 选择规则

若用户给出许多目标，选择那个能保护最脆弱需求的配方。产品身份胜过相机奇观；对口型胜过大幅头部运动；角色一致性胜过复杂编排；首/末帧目标准确性胜过额外的风格变化；安全与授权胜过风格模仿。

## 序列状态

当存在序列状态时，配方必须继承故事主线、当前镜头范围、连续性锁定项、精确的引用标签、已完成节拍，以及预留的未来节拍。配方可以提出一份镜头图，但它必须只敲定当前未解决的提示词，并在审阅被采用的素材之前让后续提示词保持暂定。

## 输出契约

返回一个选定的配方、它为何契合、定制后的提示词骨架、紧凑的最终提示词，以及相关时的项目/交付说明。
