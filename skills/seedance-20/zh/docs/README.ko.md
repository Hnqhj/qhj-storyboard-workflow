# Seedance 2.0 Skill OS 한국어 가이드（中文版）

> 注：本文件是 `docs/README.ko.md`（韩文母语指南）的中文翻译版本。

这是 v6.1.0 的韩语起点。它不是英文 README 的逐字翻译，而是给以韩语处理 Seedance 提示词、连续片段、参考素材、字幕与交付的用户使用的实务指南。

## 先看的地方

| 想做的事 | 先打开 |
|---|---|
| 写韩语提示词 | `skills/seedance-vocab-ko/ZH_REFERENCE.md` 和 `references/vocab/ko.md` |
| 查看韩语范例 | `skills/seedance-examples-ko/ZH_REFERENCE.md` |
| 把长故事分成多个片段 | `skills/seedance-sequence/ZH_REFERENCE.md` |
| 制作已批准视频的下一部分 | `skills/seedance-continuation/ZH_REFERENCE.md` |
| 使用图像、视频、音频参考 | `references/reference-workflow.md` |
| 固定首帧和末帧 | `references/first-last-frame-guide.md` |

## 韩语提示词基础

- `[Image1]`、`[Video1]`、`[Audio1]` 参考标签不翻译，原样保留。
- 先确定人物固定、服装、空间结构、动作终点、镜头运动。
- 不要只用「感性的」「有氛围的」「电影般的」这类词，要分解为镜头、灯光、材质、空气、声音。
- 最终字幕、广告文案、法律文字不交给影像生成，应在编辑阶段加入。
- 在连续故事中，记录上一个已批准片段的实际末态后，再写下一条提示词。

## 连续片段模板

```text
이야기의 최종 목표: [마지막에 도달해야 하는 상태]
승인된 사실: [이전 영상에서 실제로 일어난 일]
이번 클립만: [이번에 보여줄 하나의 시각적 작업]
아직 보여주지 않을 것: [뒤 클립에 남겨둘 내용]
참조: [Image1]은 인물 고정, [Video1]은 카메라만, [Audio1]은 템포만
프롬프트: [한 가지 동작 + 한 가지 카메라 + 실제 조명 + 소리]
```

## 韩语范例

```text
[Image1]은 제품 참조이며 로고, 라벨, 병 모양, 색상을 정확히 유지한다.
변화는 작은 물방울이 표면을 따라 내려가는 움직임과 왼쪽에서 지나가는 따뜻한 실용 조명만 적용한다.
Camera: locked product close-up, slow push-in.
Sound: 낮은 실내 환경음, 마지막에 작은 유리 소리.
자막, 워터마크, 불필요한 글자 추가 금지.
```

## 安全改写

不要用另一种语言隐藏受保护的角色、真实人物、品牌、歌曲、声音。保留创作功能，替换为原创人物、原创世界、已授权参考，或后期制作的替代方案。
