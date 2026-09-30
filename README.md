# qhj-storyboard-workflow

可迁移的剧本拆分镜工作流技能包：覆盖路由、镜头组、动作、VFX、表演、连续性、Seedance、平台编译、预检和输出复盘。

> 旧仓库名 `QHJ-SKILL` 会由 GitHub 自动重定向到本地址，已安装的用户无需改动。

当前版本见 `manifest.json`，共 98 个技能。

## 安装

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

默认同时装到 Codex 和 WorkBuddy：

| `-Target` | 安装位置 |
|---|---|
| `all`（默认） | `%USERPROFILE%\.codex\skills` + `%USERPROFILE%\.workbuddy\skills` |
| `codex` | `%USERPROFILE%\.codex\skills` |
| `workbuddy` | `%USERPROFILE%\.workbuddy\skills` |

自定义宿主数据目录：

```powershell
.\install.ps1 -CodexHome D:\codex -WorkBuddyHome D:\workbuddy
```

## 手动更新

```powershell
powershell -ExecutionPolicy Bypass -File .\update.ps1
```

同样支持 `-Target codex | workbuddy | all`，例如只更新 WorkBuddy：

```powershell
.\update.ps1 -Target workbuddy
```

## 开启定时自动更新

在 Windows 上运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-auto-update.ps1
```

默认每天凌晨 3:00 从公开 GitHub 仓库拉取最新版本，同时更新 Codex 与 WorkBuddy。修改频率与目标：

```powershell
.\setup-auto-update.ps1 -Days 7
.\setup-auto-update.ps1 -Target workbuddy
```

任务名称为 `QHJ-SKILL-AutoUpdate`，可在 Windows「任务计划程序」中查看、停用或删除。

## 更新机制

定时任务调用 `update.ps1`：`git clone --depth 1` 拉取公开仓库最新 `main`，把 `skills\` 平铺复制到各目标宿主技能目录，并把 `manifest.json` 写到目标目录下的 `qhj-manifest.json`。

- **不是实时推送**，而是**轮询**：其他 agent 会在下一次定时任务运行时拿到更新；想立刻生效就手动跑一次 `update.ps1`。
- 脚本只新增/覆盖技能文件，**不删除**任何内容，也不修改宿主系统目录。
- 版本以 `manifest.json` 为准。发布新版本时更新版本号、提交并推送，用户下次拉取即可同步。

### 注意

WorkBuddy 与 Codex 的技能清单在**会话启动时**加载。更新完成后需要**新开一个会话**才能看到新技能。
