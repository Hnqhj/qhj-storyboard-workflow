# 参考工作流（Reference Workflow）

## 素材角色映射（Asset Role Map）

在写提示词散文之前，给每个上传的素材指派一个角色。角色映射防止意外转移身份、标识、场景归属，或不兼容的摄影机与运动指令。

| 素材 | 好的角色 | 避免 |
|---|---|---|
| 图像 | 身份、产品、姿势、服装、环境、首帧、尾帧 | 要求它定义未见的运动 |
| 视频 | 运动、摄影机、节奏、调度、时机、手势节律 | 抄袭受保护身份、标识或场景归属 |
| 音频 | 节律、节奏、情绪、环境、播报基调、音乐质感 | 假设声音、歌曲或肖像授权 |
| 文本简报 | 动作、类型、摄影机计划、约束 | 用含糊情绪词替代具体的参考角色 |

## 规则（Rules）

- 精确保留参考标签。
- 在写风格语言之前，给每个参考一个主要角色。
- 不要要求一个参考控制不兼容的角色，除非权衡是明确的。
- 使用自有、已授权、公有领域或明确授权的参考。
- 写明哪些应转移、哪些不应转移。
- 当授权不明确时，转移宽泛的运动、节奏、情绪或制作功能，而非受保护身份。
- 把多模态参考生成、视频编辑、视频扩展和首/尾帧生成当作独立任务。它们可以共享素材，但提示词应命名当前活动的工作流。
- 如果音频和视频参考相互竞争，当音频时序必须主导时让视频静音，或声明视频只控制摄影机/运动而 `[Audio1]` 控制节奏。
- 在序列中，把规范参考与已采纳连续性来源分开：规范身份/产品参考控制不可变设计，而已采纳的先前素材控制临时开场状态。
- 绝不让运动参考覆盖连续性锁定、已完成节拍、预留节拍或精确参考标签。

## 工作流特定模式（Workflow-Specific Patterns）

| 工作流 | 使用此措辞 | 避免 |
|---|---|---|
| 多模态参考 | `[Image1] controls product identity; [Video1] controls camera rhythm; [Audio1] controls tempo only.` | `Use all references for style.` |
| 视频编辑 | `[Video1] is the source clip; preserve composition and timing, change only [lighting/background/VFX].` | 从零重新生成整个概念。 |
| 视频扩展 | `[Video1] is the previous clip; continue the same shot for [duration] and preserve last-frame continuity.` | 在没有连续性锚点的情况下开始新场景。 |
| 首/尾帧 | `[Image1] is first frame; [Image2] is final visual target; generate the continuous transition only.` | 要求尾帧只作"情绪"。 |
| 音频参考 | `[Audio1] controls tempo and energy; do not copy protected voice, song, or performance identity.` | 把音频当作授权证明。 |

## 角色示例（Role Examples）

| 情境 | 强映射 |
|---|---|
| 产品广告 | `[Image1] controls product identity; [Audio1] controls tempo only.` |
| 运动转移 | `[Video1] controls side-step choreography only; do not transfer performer, costume, room, or logo.` |
| 风格参考 | `[Image2] controls warm bar atmosphere only; product identity remains from [Image1].` |
| 首尾帧 | `[Image1] is first frame; [Image2] is target end frame; transition occurs through light sweep, not product deformation.` |
| 编辑/扩展 | `[Video1] is the source clip; preserve subject and camera path, replace only the failed lighting beat from 3s to 5s.` |

## 运动转移（Motion Transfer）

实地观察的技术；在承诺结果之前先测试。这大概是最未被充分利用的参考能力：一个捐赠视频驱动编舞或摄影机节律，而一张图像保持身份。

- 把一个捐赠 `[Video1]` 与一个身份锚点 `[Image1]` 配对，并明确写出排除项：`[Video1] controls the choreography only - nothing of its appearance, performer, costume, room, or logo transfers.`
- 选择有一个清晰动作、干净剪影和稳定摄影机的捐赠片段。忙碌的多人素材转移的是噪声，而非运动。
- 上传前把捐赠片段静音，除非它的声音应当驱动时序；如果它保留声音，说明哪个参考拥有时钟。
- 转移效果好的：编舞、手势时机、摄影机节律、调度。转移效果差的：精细手部细节、多人同步、面部表演。
- 仅使用自有、已授权、素材库、动捕、排练或自录的捐赠素材；真人捐赠者只转移一般运动，绝不转移肖像。

## 模板（Template）

`[Image1] controls product identity. [Video1] controls camera pace only. [Audio1] controls tempo only. Preserve the subject from [Image1]; do not copy characters, logos, music, voice, or environment from [Video1]/[Audio1].`

## 序列转移模板（Sequence Transfer Template）

`[Video 1] is the accepted previous clip and controls only the actual opening state, camera phase, motion phase, ambience, and environment arrangement. @Image 1 controls canonical identity. Preserve both tags exactly. Do not copy unrelated identity, costume, logo, or future action from any reference.`
