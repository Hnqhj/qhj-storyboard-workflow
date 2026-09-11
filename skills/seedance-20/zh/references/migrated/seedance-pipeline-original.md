# `seedance-pipeline` 的遗留正文

于 2026-04-27 在 v5.1.0 期间迁移。除非在 `references/api-status.md` 或 `references/source-registry.md` 中得到确认，否则请将此处的平台、政策、API 和安全声明视为遗留内容。

---

# seedance-pipeline

Seedance 2.0 的 API、ComfyUI 与后期处理。

## 平台接入

| 平台 | 端点 / 应用 | 备注 |
|---|---|---|
| Web | jimeng.jianying.com (Dreamina) | 4–15 秒，最高 1080p |
| 移动端 | CapCut / 剪映 · 小云雀 | 5–10 秒 |
| API | 火山引擎 `Doubao-Seedance-2.0` | 见下方速率限制 |
| 消费端 | 豆包 App | 标准 Web 限制 |

## 火山引擎 API

```
POST https://ark.cn-beijing.volces.com/api/v3/videos/generations
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

```json
{
  "model": "Doubao-Seedance-2.0",
  "prompt": "<compiled plain-text prompt>",
  "duration": 8,
  "aspect_ratio": "16:9",
  "resolution": "1080p",
  "seed": 42
}
```

**规则**
- 切勿发送原始 JSON schema —— 先编译为纯文本。
- `seed` 为可选项；省略以获得变化，设定以保证可复现。
- 检查响应中的 `status` 字段：`queued → processing → completed | failed`。
- 每 5 秒轮询一次；120 秒后超时。

## 文件预算（"12 之规则"）

| 类型 | 最大数量 | 单个最大尺寸 | 格式 |
|---|---|---|---|
| 图片 | 9 | 30 MB | JPG · PNG · WEBP |
| 视频 | 3 | **合计 ≤ 15 秒总时长** | MP4 · MOV |
| 音频 | 3 | 合计 ≤ 15 秒 | MP3 |
| **文件总数** | **12** | — | — |

## ComfyUI 节点工作流

```
[Load Image / Load Video] → [Seedance2 Sampler]
      ↓                           ↓
[CLIP Text Encode]          [Prompt Compiler]
      └────────────────────────→ ↓
                         [Video Output Node]
                                 ↓
                      [Frame Interpolation]
                                 ↓
                         [Upscale Node]
                                 ↓
                       [Color Grade Node]
                                 ↓
                        [Export / Mux Audio]
```

关键节点参数：`duration`、`aspect_ratio`、`resolution`、`seed`、`motion_strength`。

## 后期处理链

### 1 · 超分放大
- 工具：Topaz Video AI · Real-ESRGAN · ffmpeg `scale=iw*2:ih*2`
- 目标：720p → 1080p（标准）· 1080p → 2K（高级）

### 2 · 帧插值
- 工具：RIFE v4.x · DAIN
- 标准：24 fps → 60 fps（平滑运动）
- 打斗 / 快动作：24 fps → 120 fps

### 3 · 调色
- 工具：DaVinci Resolve · FFmpeg LUT
- 工作流：归一化曝光 → 应用 LUT → 蒙版提升暗部 → 定稿。
- LUT 槽位：Rec.709（Web）· Log-C（存档）。

### 4 · 音频复用
- 将生成的立体声音频与视频合并：`ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest out.mp4`

### 5 · 元数据清理
- 在分发前剥离生成元数据：`exiftool -all= output.mp4`
- 重命名：`{project}_{shot}_{take}_{date}.mp4`

### 6 · 合成（可选）
- 在 After Effects / DaVinci Fusion 中分层叠加生成的片段。
- 导出前匹配各剪辑之间的色温。

## 输出规格

| 用例 | 分辨率 | FPS | 容器 | 音频 |
|---|---|---|---|---|
| Web / 社交 | 1080p | 30 | MP4 H.264 | AAC 192k 立体声 |
| 电影节 | 2K | 24 | MOV ProRes | PCM 48kHz |
| 存档 | 2K | 24 | MKV H.265 | FLAC 立体声 |

## 路由

提示词问题 → [skill:seedance-prompt]
镜头/分镜 → [skill:seedance-camera]
QA / 错误 → [skill:seedance-troubleshoot]
