---
name: codex-asset-console
description: 安装、验证、修复或适配 Windows Codex 资产控制台：任务关联的本地素材审阅、待确认、音视频浏览、受管单副本存储、逻辑移动、分类与恢复。只负责资产控制台这一部件本身；工作区整体增强（侧边栏、任务回溯、用量状态）请用 codex-workspace-enhancer。 Install, verify, repair, or adapt the Windows Codex Asset Console for task-linked local asset review, pending confirmation, audio/video browsing, managed single-copy storage, logical moves, classification, and recovery. This skill owns the Asset Console component only; use codex-workspace-enhancer for whole-workspace enhancement.
---

# Codex Asset Console

Use the bundled Windows runtime as a local reference implementation. Keep user assets and state outside the Skill package.

## Install or update

1. Inspect the current state with `scripts/inspect.ps1`.
2. Preview all mutations with `scripts/install-bundled.ps1 -WhatIf`.
3. After the user approves installation, run `scripts/install-bundled.ps1`.
4. Run `scripts/verify.ps1`; use `-BundleOnly` when validating a package without touching a machine.

The installer owns only:

- `%LOCALAPPDATA%\Programs\Codex Asset Console`
- `%LOCALAPPDATA%\CodexAssetConsole`
- `%LOCALAPPDATA%\CodexAssetConsoleService`

Do not redirect installation or deletion outside these roots. Preserve existing configuration, ledgers, recovery records, and managed media across updates and rollback.

## Asset behavior

- Bind imported/generated assets to their originating task when the evidence is exact; otherwise place them in Pending Confirmation.
- Browse image, audio, and video without copying them into a second managed location.
- Treat moves between projects, folders, or categories as logical organization changes over one managed file whenever the backend supports it.
- Keep classification reversible and show recovery/undo results explicitly.
- Add selected absolute local paths to the current composer without sending the task.
- Never claim ownership from “the next download”; require an exact asset ID, exact filename, or direct file binding.

For runtime boundaries, read [references/architecture.md](references/architecture.md). For a release or repair, also read [references/acceptance-checklist.md](references/acceptance-checklist.md).

## Release boundary

Never package tokens, local configuration, state files, ledgers, task history, UUID-bearing private records, or user media. The release build must pass its deterministic privacy scan before hashes are published.
