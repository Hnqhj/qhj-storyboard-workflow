---
name: seedance-vocab-en
description: "This skill should be used when an English Seedance 2.0 prompt is slop-heavy, generic, padded with empty quality words, tripping false-positive filters, or needs precise English production vocabulary for camera, lighting, motion, VFX, audio, and constraints."
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

# seedance-vocab-en

英语是默认的提示语言，它会同时以两种方式失败：套话（增加 token 却毫无信号的空洞评价词）和误报（含糊的、近似威胁的措辞会触发最严苛的审核界面）。两者的解药相同：具体的制作英语。引用标签务必原样保留：`[Image1]`、`[Video1]`、`[Audio1]` 绝不能被改写。

## 意图

英语是大多数用户思考之处，也是大多数提示词悄然腐烂之处。本词汇的灵魂是"精确即善意"：给人们精确的词，让他们的兴奋在接触模型后得以存活，并让诚实的提示词不再被误认作危险之物。

## 使用规则

若相机、麦克风、测光表或秒表无法探测到它，就重写它。每个句子都应点名某个可见、可闻或可测量的东西：主体、可见动作、相机、光源、声音、约束。

| 功能 | 英语措辞 |
|---|---|
| Camera | `slow push-in`, `locked medium shot`, `stable lateral tracking`, `pull back to reveal`, `macro close-up` |
| Lighting | `soft backlight`, `warm practical light from the left`, `cool moonlight rim`, `wet asphalt reflecting neon` |
| Motion | `a slow head turn that stops`, `droplets merge and slide down`, `fabric settles after the gesture` |
| Audio | `quiet room tone`, `one clear spoken line in quotes`, `no music until after the line` |
| Constraints | `keep the logo, label, and shape unchanged`, `one action, one camera move`, `nothing else moves` |

## 去套话检查

在添加任何东西之前先剥离质量形容词：`cinematic`、`epic`、`stunning`、`masterpiece`、`8K`、`ultra-realistic`、`award-winning`、`hyper-detailed`，全都删除，或各自转换为一个可观察的细节。一条配得上"epic"的提示词，会点名人群规模、镜头距离或建筑高度，而非那个词本身。

## 滤镜感知措辞

英语同音/多义词在滤镜看来像威胁：`shoot the scene`、`kill the lights`、`gun it`、`dead silence`、`blow up the image`。使用制作同义词（`film the take`、`cut the lights to black`、`accelerate hard`、`held silence`、`enlarge to full frame`）。这仅仅是为了安全提示词的清晰度——绝非规避。任何真正有风险的内容（未成年人、真实人物肖像、性或露骨内容）应路由到 `[skill:seedance-filter]` 走它的边界规则，而非改写措辞。

## 紧凑范式

`[Image1] is the reference; keep identity, color, and shape unchanged. Only [motion/light/camera] changes. Camera: [one move]. Sound: [one cue]. Constraints: [lock].`

加载 `../../../references/vocab/en.md` 获取按功能组织的完整词汇、套话陷阱和滤镜误触修复。加载 `[ref:anti-slop-lexicon]` 获取核心替换规则，加载 `[ref:filter-vocab]` 获取完整的误报修复表。

## 输出契约

返回去套话后的英语提示词、所做的每处替换（套话 → 可观察细节）、所应用的任何滤镜误触修复，以及未改动的引用标签。
