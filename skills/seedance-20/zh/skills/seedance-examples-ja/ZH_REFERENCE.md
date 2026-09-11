---
name: seedance-examples-ja
description: "This skill should be used when the user asks for Japanese Seedance 2.0 examples, Japanese prompt patterns, example rewrites, or safe versions of working Japanese video-generation prompts."
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

# seedance-examples-ja

将日文范例视为母语化的提示词范式，而非翻译过来的英文模板。引用标签务必原样保留：`[Image1]`、`[Image2]`、`[Video1]` 和 `[Audio1]` 在日文句子中保持不变。

## 意图

日文范例应当读起来像日本创作者真正会用的制作笔记：在需要时礼貌得体，在模型需要清晰度时紧凑精炼，并且足够具体，使每一种情绪都落实为取景、光线、运动、声音或后期处理手法。

## 范例标签

| 标签 | 含义 |
|---|---|
| `safe` | 原创概念，不涉及受保护身份。 |
| `needs-owned-reference` | 需要用户自有、已授权、公有领域或获得许可的素材。 |
| `surface-specific` | 取决于当前的 web、API 或工作流界面。 |
| `rewrite-required` | 提及受保护身份、品牌、名人、具体场景、歌曲或嗓音。 |

## 安全范例范式

**Product I2V:** `[Image1]を商品参照として使い、ロゴ、ラベル、形状、色を正確に維持する。変化は小さな水滴が表面を下へ流れる動きと、左から横切る柔らかい暖色光だけ。Camera: locked product close-up, slow push-in. Sound: quiet room tone, one small glass tick at the end.`

**Portrait micro-performance:** `[Image1]の人物の顔、髪型、衣装、背景構図を保持。動きは小さく、一度まばたきし、視線を少し下げ、最後に控えめに微笑む。Camera: locked medium close-up, no reframing. Lighting: soft window light from frame right. Sound: quiet room tone.`

**Sequence clip 01:** `オリジナル人物Aが夜明けの駅ホームに入ってくる。目的は「誰かを待つ」と分かる最初の手がかりだけを見せる。Aは濡れた床を二歩歩き、折りたたまれた切符を見つけて拾わずに止まる。Camera: stable lateral tracking, medium-wide. このクリップでは列車到着や再会は見せない。`

**Continuation:** `前の採用済みクリップの終点から続ける。Aは切符の二歩手前で止まっている状態から開始し、ゆっくりしゃがんで切符を拾い、遠くのアナウンスに反応して顔を上げる。前の入場動作を繰り返さない。Camera: locked medium shot, slight push-in.`

**Dialogue:** `Character A sits at a cafe table in a locked medium close-up and softly says, "もう一度だけ。" セリフ中は頭を大きく動かさず、小さな口の動きだけ。Lighting: warm interior practical, cool rain reflection on wall. Sound: clear short dialogue, no music under the line.`

**Textless localization:** `9:16の日本向けSNSカット。商品は中央、端に重要な動きなし。画面内に生成文字、字幕、広告コピーを入れない。Post note: 日本語字幕、法務文言、CTAは編集で追加する。`

## 改写范式

若提示词包含受保护名称，将其创意功能改写为原创的日文描述：`有名キャラクターそのもの`（某知名角色本身）改写为 `オリジナルの仮面をつけた屋上配達員`（戴着原创面具的屋顶送货员）；`特定作品そっくり`（与某特定作品如出一辙）改写为 `低彩度の夜景、硬いサイドライト、静かな演技、長焦点の圧縮感`（低饱和夜景、硬侧光、安静的表演、长焦压缩感）。

## 输出契约

返回日文范例、标签、风险说明，并在需要时给出更安全的日文变体。除非用户要求结构化输出，否则最终的 Seedance 提示词文本保持自然语言形式。
