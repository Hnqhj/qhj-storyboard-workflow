---
name: seedance-antislop
description: "This skill should be used when a Seedance 2.0 prompt contains generic AI filler, hollow superlatives, vague cinematic language, bloated adjectives, weak verbs, or needs sharper production-specific wording."
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

# seedance-antislop

移除那些掩盖了缺失视觉决策的填充词。一条强 Seedance 提示词使用可观察的名词、动词、镜头运动、光源、声音提示和约束。一条弱提示词索要卓越，却不说卓越看起来或听起来是什么样。

## 意图

用户之所以伸手去抓那些巨大而空洞的词，恰恰是因为他们极度在乎、却不知道把这份在乎放在哪里。去套话的灵魂是「守恒」：每删掉一个「epic」，都必须以一个承载同样在乎之情的可见选择回来。剥离一条提示词时若不尊重那份把它撑胖的感情，用户听到的就是「你的兴奋是错的」。

## 可见性测试

每个主要短语都应当能被镜头看见、被测光表测量、在混音中听见，或作为运动被观察到。如果一个短语无法通过这个测试，就用制作语言替换它。

| 填充词 | 追问它意味着什么 | 强替换模式 |
|---|---|---|
| cinematic（电影感） | 什么镜头和光让它有电影感？ | `locked close-up, warm practical key, cool rim light` |
| epic（史诗） | 尺度或赌注是什么？ | `wide low-angle shot, tiny figure against storm wall` |
| beautiful（美） | 什么颜色、材质或光的行为？ | `pearl highlights on wet ceramic, soft window bounce` |
| dynamic（动感） | 什么在动、多快、在哪里结束？ | `fast lateral track ending on the hero label` |
| professional（专业） | 什么样的制作设置？ | `clean commercial tabletop, controlled reflection, no clutter` |

## 六类套话

在改写前先分类——每一类都有不同的修复方法：

1. **空洞评价词**（`cinematic, epic, stunning`）——把每一个都转化为配得上它的那一个可观察细节。
2. **借来的图像模型 token**（`8K, masterpiece, trending on ArtStation`）——删除；质量和分辨率是设置，不是文案。
3. **标签沙拉**（从图像提示移植来的逗号关键词堆）——改写为拍摄简报式文案：每个元素一句话，带一个动作和一条时间轴。
4. **否定套话**（`no blur, no artifacts, no extra fingers`）——否定会「召唤」；改为描述存在的东西，并只在约束槽位保留否定。
5. **形容词堆叠**（一个品质用三个同义词）——挑出那个真正重要的细节。
6. **「感觉后缀」词**（`电影感, 雰囲気のある, 감성적인, atmosférico, атмосферный, vibey`）——说出那种感觉的物理成因；`../../../references/vocab/` 中的每个语言文件都有针对其自身社区空洞词的「套话陷阱」表。

## 改写流程

第一，划出所有最高级词和含糊的风格标签，并按套话类别给每个分类。第二，决定每个词应当变成镜头、灯光、运动、材质、声音还是约束语言。第三，减少重复。第四，让提示词保持在字符预算内并保留参考标签。

## 不要过度纠正

当有用的类型语言与具体的导演指令搭配时，不要移除它。`Noir hallway with hard venetian-blind shadows` 是有用的；`dramatic cinematic noir vibes` 不是。保留传达媒介、年代、调色板或镜头行为的术语。

加载 `[ref:anti-slop-lexicon]` 以获取套话类别分类法和扩展替换表，加载 `[skill:seedance-vocab-en]` 与 `../../../references/vocab/en.md` 以获取完整的按功能组织的英语精度词汇。对于非英语提示词，加载匹配的词汇文件的「套话陷阱」表（`../../../references/vocab/zh.md`、`ja.md`、`ko.md`、`es.md`、`ru.md`）——每个语言社区都有其自己的空洞质量词和分解方式。

## 输出合同

返回：被移除的词、按镜头/灯光/运动/声音/约束分组的替换，以及收紧后的提示词。
