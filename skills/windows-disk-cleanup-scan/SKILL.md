---
name: windows-disk-cleanup-scan
description: 磁盘扫描与分级清理清单。当用户问「某盘哪些文件能删」「磁盘快满了」「分析空间占用」「找出大文件」时使用；只读扫描产出 A/B/C 三级清单与根因，绝不擅自删除。需直接执行清理请用 windows-safe-cleanup。
agent_created: true
---

# Windows 磁盘空间扫描与清理分析

## 与 windows-safe-cleanup 的分工

本仓库有两个磁盘相关技能，职责不重叠，**同一任务只用其中一个的入口**：

| 技能 | 职责 | 何时用 |
|---|---|---|
| **本技能** | **只读**扫描指定盘符/目录，产出 A/B/C 三级可删除清单与根因分析 | 用户想知道「什么能删」，要一份能逐项核对的报告 |
| `windows-safe-cleanup` | 审计 + **执行**清理（带 `scripts/windows_cleanup.ps1`），覆盖 C/D/E 盘、浏览器与开发者缓存、NVIDIA 着色器、Wallpaper Engine/Steam | 范围已明确，直接动手清理 |

两者可串联：本技能出清单 → 用户逐项确认 → 按本技能第 5 步的安全流程执行。

## 目的与安全原则

对指定盘符/目录做只读扫描，产出分级可删除清单。铁律：

1. 扫描阶段绝不移动/重命名/删除任何文件，只生成报告
2. 删除必须等用户明确确认具体范围后才执行
3. 执行删除时：单批 ≤10 项、优先回收站机制或先备份、每批验证
4. 疑似重复文件删除前先做哈希校验（同名同大小同时间戳只是强线索）

## 本机环境坑（重要）

- **Bash 可用，但必须先显式补 PATH**（2026-09-23 实测更正）：
  本环境默认 PATH 不完整，直接跑 `find` / `head` / `dirname` 会报
  `command not found`，**很容易误判成「Bash 工具坏了」而改道 PowerShell**。
  实际只需在每条命令开头加一行：
  ```bash
  export PATH="/usr/bin:/bin:/mingw64/bin:$PATH"
  ```
  之后 `find` / `grep` / `awk` / `md5sum` / `sort` / `comm` 全部正常。
  批量文本统计和逐文件比对，Bash 比 PowerShell 快得多，优先用它。

- **PowerShell 工具的 stdout 不回显**：所有输出必须
  `Set-Content -LiteralPath ... -Value ... -Encoding UTF8` 写入文件，
  再用 Read 工具读取。控制台中文会乱码，但写进文件的内容正常。

- **大目录递归枚举很慢**（100 万文件约 14 分钟）：用
  `run_in_background=true` 启动，再用 TaskOutput `block=true` 等待；
  一次 TaskOutput 超时后可以再次阻塞等待。

- **PowerShell 5.1 语法**：不用 `&&` / `||` / `?.`；中文或含空格路径一律用
  `-LiteralPath`；长脚本尽量保持纯 ASCII（目录名靠枚举动态获得，不硬编码）。
  含中文的 `.ps1` 必须存为 **UTF-8 with BOM**，否则按 GBK 解码会变乱码报语法错。

- ⚠️ **删除有守卫，先算「条目数」而不是「体积」**：
  非 Temp 路径的 `rm` 会被送系统回收站，本机回收站不可用 → fail-closed
  直接拒绝（报 `safe-delete ... trash-failed`），**换语言、换工具都一样**。
  且存在会话级累计配额（阈值 50 个条目，按递归展开后的文件数计），
  一旦超限，本轮后续所有删除请求都会被拒。
  → 单个文件可用 .NET 直接删（`[System.IO.File]::Delete()`，不需批准）；
    整个目录要提权批准。
  → **海量小文件的缓存目录不适合脚本删**，优先挑 >20MB 的单文件，
    少量条目就能换 GB 级空间。

## 工作流

### 第 1 步：盘符与根目录总览

```powershell
$out = @()
Get-PSDrive -PSProvider FileSystem | ForEach-Object {
  $out += ("{0}: Used={1:N2}GB Free={2:N2}GB" -f $_.Name, ($_.Used/1GB), ($_.Free/1GB))
}
Get-ChildItem X:\ -Force -ErrorAction SilentlyContinue | ForEach-Object {
  $out += ("{0}`t{1}`t{2}" -f ($(if($_.PSIsContainer){'DIR'}else{'FILE'})), $_.Name, $_.LastWriteTime)
}
$out | Out-File -FilePath "<工作区>\scan_report.txt" -Encoding UTF8
```

### 第 2 步：全盘逐目录统计（后台运行）

对每个顶层目录递归枚举，同时收集：目录总大小/文件数、2GB 以上大文件全路径、
垃圾模式统计（`*.tmp`、`~$*`、`*.bak`/`*.old`、`*.chk`、`thumbs.db`）。
参考实现（单次遍历同时收集全部指标，X: 为目标盘）：

```powershell
$dirs = Get-ChildItem X:\ -Force -ErrorAction SilentlyContinue | Where-Object { $_.PSIsContainer }
foreach ($d in $dirs) {
  $size = 0L; $count = 0
  $files = Get-ChildItem -LiteralPath $d.FullName -Recurse -File -Force -ErrorAction SilentlyContinue
  foreach ($f in $files) {
    $size += $f.Length; $count++
    if ($f.Length -gt 2GB) { <加入大文件列表> }
    <按扩展名/文件名模式累计垃圾统计>
  }
  <记录 目录名/SizeGB/Files/LastWrite>
}
<全部结果 Out-File UTF8 写入 scan_report2.txt>
```

### 第 3 步：重点疑点精确复扫

对第 2 步暴露的可疑目录（backup、test-extract、安装包、模型目录、缓存）
单独递归统计精确大小，并展开其一级子目录。同名同大小同时间戳的大文件
（尤其 AI 模型 `.safetensors`/`.pth`/`.ckpt`、`app.asar`）跨目录出现
→ 标记为疑似重复。

### 第 4 步：分级报告

按风险分三级，用结构化表格呈现（路径、大小、根因），并给汇总数字：

- **A 级（基本无风险）**：回收站 `$RECYCLE.BIN`、chkdsk 的 `found.00x`、
  Adobe Media Cache、同目录已解压的安装包压缩包、已被新版替代的旧版安装包、
  `*.tmp` 等
- **B 级（疑似重复/测试副本，确认后可删）**：`backup`/`test-extract` 目录、
  跨目录重复的 AI 模型与开发环境副本、`uv_cache`/`hf_cache` 等可再生缓存
- **C 级（需用户决策）**：测试目录整目录、老项目素材、安装包目录整体、
  长期未动的个人文件

可搭配 show_widget 横向条形图（Chart.js）展示清理候选项大小，
**按 A/B/C 三色区分**。

### 第 5 步：用户确认后执行删除

- 逐项列出将删除的完整路径与总大小，**加粗警告不可逆风险**，取得明确确认
- B 级重复项先哈希校验（`Get-FileHash`）证明完全一致再删
- 单批 ≤10 项；优先移入回收站或先 `robocopy` 备份；每批完成后验证并汇报释放量
- 系统/开发环境相关目录（运行中环境的 `node_modules`、
  `System Volume Information`）删除前再次与用户确认是否在用

## 常见垃圾特征速查

| 特征 | 典型路径 | 处理 |
|------|---------|------|
| 回收站 | `X:\$RECYCLE.BIN` | 清空即释放 |
| chkdsk 恢复 | `X:\found.000/001/002` | 通常可删，常为空 |
| Adobe 缓存 | `...\Media Cache\*.cfa`/`*.pek` | 可删，自动重建 |
| 安装包双份 | 同目录 `.rar` + 解压文件夹 | 二选一 |
| 旧版安装包 | 安装包目录内老版本 zip | 已有新版即可删 |
| 测试/备份副本 | `backup`、`test-extract`、`ceshi`（测试） | 确认后删 |
| AI 模型多副本 | `.safetensors`/`.pth` 同名同大小跨目录 | 哈希校验后删一份 |
| 可再生缓存 | `uv_cache`、`hf_cache`、`.pnpm-store` | 确认后删 |
| 空目录 | 0 文件的文件夹 | 删除仅整洁，不释放空间 |
