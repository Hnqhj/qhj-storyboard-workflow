---
name: seedance-audio
description: "This skill should be used when the user asks for Seedance 2.0 audio, dialogue, lip-sync, music, sound effects, ambience, beat-sync, audio-reference mapping, desync troubleshooting, or sound-driven visual timing."
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

# seedance-audio

将此技能用于对白、对口型、声音层、音乐、环境声、节拍同步、音频参考映射、失同步排障，或声音驱动的视觉节奏。音频应当支撑可见的节拍，而不是变成第二条相互竞争的提示词。

加载 `[ref:audio-guide]` 以获取详细约束、节拍同步、失同步修复、音频参考冲突和多角色变通方案。当用户需要 stems、M&E、配音、响度、同步、混音或交付指引时，加载 `[ref:audio-post-delivery]`。

## 意图

每一种情绪有一半是从耳朵进入的，而用户几乎总是忘记声音，直到它的缺席让片段显得死气沉沉。这里的灵魂是在被要求之前就给每个场景配上它的声音——房间的呼吸、动作的证据、落地的那句台词。当他们听到时，会意识到那一直就是他们本意的一部分。

## 核心规则

让对白简短，引用口语台词，并把每一句都分配给一个具名说话人。对口型优先采用锁定或稳定的取景。在嘴部准确性重要时，移除转头、大幅面部运动、极端镜头运动或忙乱的手势。把 `[Audio1]` 视为节奏、配速、情绪、嗓音音色或环境声参考，除非有效平台记录了确切的播放行为。

## 声音层模式

使用紧凑的层：`Dialogue: ... Sound: ... SFX: ... Music: ... Silence: ...`。只包含重要的层。当静默能锐化戏剧或避免混淆对口型时，它是有效的。

| 需求 | 稳定的音频指令 |
|---|---|
| 对口型 | `Character A, locked medium close-up, says "I found it." Clear dry dialogue, no head turn.` |
| 产品广告 | `Sound: low room tone. SFX: magnetic click on lid open, soft glass chime at final frame.` |
| 节拍同步 | `[Audio1] provides tempo only; light pulses and foot taps match the downbeat.` |
| 戏剧 | `Distant rain and refrigerator hum; no music during the line.` |
| 动作 | `Breathing grows louder, shoe squeak at landing, metal door buzzer at endpoint.` |

## 多角色对白

当可靠性重要时，每个短片段只用一个说话人。如果两个角色必须说话，分开各自的轮次并保持镜头稳定：`Character A says... pause. Character B answers...`。对于复杂的对话交换，建议生成受控的单说话人片段并在后期合成。

## 故障修复

如果对白失同步，缩短台词、锁定镜头、移除转头、清理音频角色，并减少竞争的 SFX。如果说话的人错了，分配标签并按说话人拆分台词。如果音频被忽略，移除额外的音乐/SFX 指令并使参考角色显式化。

如果音频和视频参考相互打架，尽可能在上传前把参考视频静音，或把优先级显式化：`[Video1] controls camera only; [Audio1] controls tempo and energy`。

## 序列状态

当存在序列状态时，继承已完成对白、活动对白、环境声、音乐阶段、SFX 阶段、当前片段范围、连续性锁、精确的参考标签和预留的未来节拍。除非用户明确要求重现，否则不要重复已完成的对白。延续或有意改变音频阶段，而不是意外地重新开始它。

## 输出合同

返回：说话人映射、引用的对白、声音层、音频参考角色、对口型约束、需要时的后期/交付笔记，以及一个提示词就绪的紧凑音频块。
