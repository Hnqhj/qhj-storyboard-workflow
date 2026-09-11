---
name: seedance-vocab-ja
description: "This skill should be used when the user asks for Japanese Seedance 2.0 prompt wording, Japanese cinematic vocabulary, or translation of camera, lighting, action, VFX, audio, and production terms into Japanese."
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

# seedance-vocab-ja

当用户要求日语提示词措辞、双语交付、紧凑翻译，或相机、光线、运动、视效和音频的制作词汇时，使用日语电影词汇。引用标签务必原样保留：`[Image1]`、`[Video1]` 和 `[Audio1]` 保持在英文方括号内。

## 意图

用日语工作的用户往往最贴近这个模型钟爱渲染的动漫传统。同时服务两种语域——礼貌语气塑造的自然句子，以及制作术语——并让词汇感觉是母语化的，绝非翻译出来的。

## 使用规则

宁可选用简洁的制作日语，而非直译。让结构保持可读：主体、动作、相机、光线、声音和保留约束。

| 功能 | 日语措辞 |
|---|---|
| Camera | `ゆっくりドリーイン`, `横移動のトラッキング`, `固定の中景`, `低いアングル`, `クローズアップ` |
| Lighting | `逆光`, `柔らかい窓光`, `暖かい実用照明`, `冷たい月明かり`, `輪郭光` |
| Motion | `ゆっくり振り返る`, `画面を素早く横切る`, `水滴が下へ流れる`, `煙が薄く広がる` |
| Audio | `静かな環境音`, `短い台詞`, `金属音`, `音楽なし` |
| Constraints | `ロゴ、ラベル、形状を正確に維持する` |

## 紧凑范式

`[Image1]を参照として、被写体の顔/商品形状/ロゴを正確に維持する。変化は[動き/光/カメラ]のみ。カメラ：[一つの動き]。音：[音声指示]。`

## 去套话规则

当提示词依赖 `映画のような`、`エモい`、`雰囲気のある`、`壮大な` 或 `高画質` 时，加载 `../../../references/vocab/ja.md` 中的套话陷阱表，把每个词分解为产生它的物理要素——動作動詞＋速度＋視点、光源＋方向＋挙動。

## 输出契约

返回日语提示词措辞、有用时可选的英语注释，以及未改动的引用标签。
