---
name: seedance-audio
description: "This skill should be used when the user asks for native audio, dialogue, lip-sync, voice, sound effects, music timing, beat sync, ambient sound, audio references, or audio-video synchronization in Seedance 2.0."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - audio
  - lip-sync
  - sound-design
metadata:
  version: "5.1.0"
  updated: "2026-04-27"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: ""
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-audio

使用本 skill 来进行对白、唇音同步、音乐时序、音效、环境声及音频参考的规划。

返回：音频目标、说话人/音源分配、可直接用于提示词的措辞、同步约束、风险说明，以及一个重试变体。

规则：
- 台词保持简短，并将每句台词分配给特定角色。
- 将对白、环境声、音效（SFX）与音乐分开。
- 按角色映射参考：`[Audio1] rhythm`、`[Audio2] voice tone`、`[Audio3] ambience`。
- 不要声称支持万能语言、任意时长或声音克隆。请查阅 `[ref:api-status]`。
- 真人嗓音与肖像工作流需要授权及平台专属支持。

提示词范式：`[Character A] says: "short line." Quiet [environment ambience], [specific SFX], [music/rhythm cue]. Lip movement synchronized to the spoken line; camera and body motion remain simple enough to preserve sync.`

遗留细节已移至 `references/migrated/seedance-audio-original.md`。
