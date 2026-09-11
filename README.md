# QHJ-SKILL

可迁移的剧本拆分镜工作流技能包，覆盖路由、镜头组、动作、VFX、表演、连续性、Seedance、平台编译、预检和输出复盘。

## 安装

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

## 手动更新

```powershell
powershell -ExecutionPolicy Bypass -File .\update.ps1
```

更新机制按时从公开 GitHub 仓库拉取最新 `main` 分支，将 `skills` 同步到本机 Codex 技能目录。可用 Windows 任务计划程序定期运行 `update.ps1`，例如每天一次。脚本只更新技能文件，不修改 Codex 系统目录。

版本以 `manifest.json` 为准。发布新版本时更新版本号、提交并推送；用户下次定时拉取即可同步。
