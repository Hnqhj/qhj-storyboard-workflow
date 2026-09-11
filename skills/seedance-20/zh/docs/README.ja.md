# Seedance 2.0 Skill OS 日本語ガイド（中文版）

> 注：本文件是 `docs/README.ja.md`（日文母语指南）的中文翻译版本。

这是 v6.1.0 的日语入口。它不是英文 README 的逐字翻译，而是给以日语处理 Seedance 提示词、连续片段、参考素材、字幕与交付的用户使用的实用指南。

## 先打开什么

| 想做的事 | 先看的位置 |
|---|---|
| 写日语提示词 | `skills/seedance-vocab-ja/ZH_REFERENCE.md` 和 `references/vocab/ja.md` |
| 看日语范例 | `skills/seedance-examples-ja/ZH_REFERENCE.md` |
| 把长故事分成多个片段 | `skills/seedance-sequence/ZH_REFERENCE.md` |
| 制作已采用视频的续接 | `skills/seedance-continuation/ZH_REFERENCE.md` |
| 使用图像/视频/音频参考 | `references/reference-workflow.md` |
| 固定首帧和末帧 | `references/first-last-frame-guide.md` |

## 日语提示词基础

- `[Image1]`、`[Video1]`、`[Audio1]` 不翻译，原样保留。
- 先固定人物的同一性、服装、构图、动作的终点。
- 不要止步于「电影感」「emo」「有氛围」，要分解为镜头、光源、材质、空气、声音。
- 不要让最终字幕、广告文案、法务文字被烧录进生成影像，应在后期处理中加入。
- 在连续故事中，确认上一个已采用片段的实际终点后，再写下一条提示词。

## 连续片段模板

```text
物語の最終目標：[最後に到達したい状態]
採用済み事実：[前の動画で実際に起きたこと]
このクリップだけ：[今回見せる一つの可視タスク]
まだ見せないこと：[後のクリップに残す内容]
参照：[Image1]で人物を固定、[Video1]はカメラだけ、[Audio1]はテンポだけ
プロンプト：[一つの動き + 一つのカメラ + 具体的な光 + 音]
```

## 日语范例

```text
[Image1]の商品を参照し、ロゴ、ラベル、形状、色を正確に維持する。
変化は小さな水滴が表面を下へ流れる動きと、左から横切る柔らかい暖色光だけ。
Camera: locked product close-up, slow push-in.
Sound: quiet room tone, one small glass tick at the end.
字幕、透かし、余計な文字を追加しない。
```

## 安全改写

不要用另一种语言隐藏受保护的角色、真实人物、品牌、歌曲、声音。保留创作上的功能，替换为原创人物、原创世界、已授权参考，或后期处理方案。
