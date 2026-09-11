---
name: seedance-vocab-ko
description: "This skill should be used when the user asks for Korean Seedance 2.0 prompt wording, Korean cinematic vocabulary, or translation of camera, lighting, action, VFX, audio, and production terms into Korean."
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

# seedance-vocab-ko

当用户要求韩语提示词措辞、双语交付、紧凑翻译，或相机、光线、动作、视效、音频和约束的制作词汇时，使用韩语电影词汇。引用标签务必原样保留：`[Image1]`、`[Video1]` 和 `[Audio1]` 不得被翻译。

## 意图

韩语用户带来"감성"——一种带着严苛视觉品味的情感文化。这里的灵魂是把"감성"物理化：用户给出的每个情绪词，都以他们能辨认为"正是我所感受到的"那种光线、取景和定时返回。

## 使用规则

翻译制作意图，而非每个英语单词。让韩语提示词保持紧凑而具体：主体、动作、相机、光线、声音和保留约束。

| 功能 | 韩语措辞 |
|---|---|
| Camera | `천천히 돌리 인`, `측면 트래킹 샷`, `고정된 중간 샷`, `로우 앵글`, `클로즈업` |
| Lighting | `역광`, `부드러운 창문 빛`, `따뜻한 실용 조명`, `차가운 달빛`, `림 라이트` |
| Motion | `천천히 돌아선다`, `프레임을 빠르게 가로지른다`, `물방울이 아래로 흐른다`, `연기가 얇게 퍼진다` |
| Audio | `조용한 환경음`, `짧은 대사`, `부드러운 금속음`, `음악 없음` |
| Constraints | `로고, 라벨, 형태를 정확히 유지한다` |

## 紧凑范式

`[Image1]은 참조 이미지이며 얼굴/제품 형태/로고를 정확히 유지한다. 변화는 [동작/조명/카메라]만 적용한다. 카메라: [한 가지 움직임]. 사운드: [음향 지시].`

## 去套话规则

当提示词依赖 `영화같은`、`감성적인`、`분위기 있는`、`웅장한` 或 `고퀄리티` 时，加载 `../../../references/vocab/ko.md` 中的套话陷阱表，把每个词分解为产生它的物理要素——카메라 동사+속도+시점、광원+방향+행동。

## 输出契约

返回韩语提示词措辞、有用时可选的英语注释，以及未改动的引用标签。
