# 音频指南

将本参考用于详细的音频、对白、节拍同步、环境音和对口型工作流。让音频角色保持明确，除非当前界面有文档说明，否则避免承诺确切的平台行为。

对于专业音频后期、分轨、M&E（音乐与效果）、配音、响度或交付检查，还需加载 `audio-post-delivery.md`。

## 对白

- 让台词简短，最好每个说话者轮次一句。
- 把口语对白放进引号。
- 用标签分配说话者。
- 对口型时使用稳定取景。
- 当口型准确性重要时，避免头部转动、大幅面部移动、极端相机运动或繁忙的手部动作。
- 若台词比环境更重要，则在台词期间减少音乐和音效。
- 非英语对白：让台词更短——长的非英语短语是现场反馈的薄弱点。对于完全配音的非英语片段，改为计划后期配音，并查阅该语言词汇文件中的对白说明。

## 音频参考映射

`[Audio1]` 可用于节奏、节拍、情绪、嗓音音色、环境音、音乐质感或节拍定时。除非当前平台有文档说明确切的播放行为，否则不要承诺确切的音频播放。若来源含有真实嗓音或可辨识歌曲，把它视为对授权敏感，并在版权不明时把它转换为宽泛的声音描述词。

当音频参考与视频参考冲突时，若音频应控制定时，则在上传前对视频参考静音或消音。若视频必须保留声音，陈述优先级：`[Video1] controls only camera/motion; [Audio1] controls tempo and energy`。

| 角色 | 好的措辞 | 避免 |
|---|---|---|
| 节奏 | `[Audio1] provides tempo only; foot taps match the downbeat` | 复制受保护的表演 |
| 情绪 | `[Audio1] provides calm sparse atmosphere` | 确切回放主张 |
| 嗓音音色 | `soft, breathy, close-mic delivery` | 模仿某个具名的真实嗓音 |
| 环境音 | `rainy street room tone, distant traffic bed` | 密集相互竞争的声音层 |
| 冲突修复 | `[Video1] is muted and controls camera only; [Audio1] controls beat timing` | 两个来源都控制节奏 |

## 多角色对白

当可靠性重要时，使用独立的说话者轮次。对于两人对话，生成受控的单说话者片段，并在必要时于后期合成。若两个说话者仍在一条提示词中，写：`Character A says... pause. Character B answers...`，并让相机锁定或轻度受动机驱动。

## 声音分层语法

`Dialogue: Character A says "I found it." Sound: low room tone + distant rain. SFX: cup lands on table at 2s. Music: no music until after the line.`

## 节拍同步语法

`[Audio1] provides tempo only. On each downbeat: back wall light pulses once, dancer hits one pose, camera remains locked wide.` 使用可见的节拍变化，而非要求模型理解一个抽象的律动。

## 音频作为时钟

现场观察到的技法；在承诺结果前先测试。除了情绪和节奏，`[Audio1]` 还能充当剪辑的主时钟：`cut on the beat of [Audio1]; the turn lands on the drop; the door slams on the final hit.`

- 把每个音乐地标恰好绑定到一个可见事件——一次剪切、一个姿势、一次光线变化、一个物体落地。每节拍一个事件；堆叠的事件会糊掉。
- 它与单一的强节奏（干净的鼓点、节拍器般的脉冲）配合最佳。密集的混音或自由速度的素材给不了模型可遵循的时钟。
- 当音频是时钟时，让它成为唯一的时钟：对视频参考静音，并避免在同一提示词里出现第二套定时系统，如时间戳列表。
- 时钟仅在一次生成内有效；音频跨调用不连续，所以多片段作品在后期获得其统一配乐。

## 排障

- 失同步：缩短对白、稳定相机、移除头部运动、减少相互竞争的声音、清理来源音频角色。
- 说话者错误：按说话者拆分台词并使用明确的角色标签。
- 音频被忽略：移除相互竞争的音乐/音效指令，并使 `[Audio1]` 角色明确。
- 混音过繁：选择环境音加一个关键音效；若对白重要则移除音乐。
- 对口型漂移：使用锁定的中近景、无头部转动、简短的引号台词，以及简单表情。
- 音频参考冲突：对视频参考静音、移除相互竞争的音效/音乐，并每节拍描述一个可见事件。

## 后期交接边界

提示词音频可以塑造表演和可见定时，但最终混音需要后期制作审阅。对于付费或交付工作，将口语语言、字幕/配音需求、M&E/分轨需求、同步提示和买方响度目标与提示词分开记录。
