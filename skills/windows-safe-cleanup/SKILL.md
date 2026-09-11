---
name: windows-safe-cleanup
description: Audit and safely clean a Windows PC, especially disk pressure on C/D/E drives, user temp files, browser caches, developer package caches, recycle bins, NVIDIA shader caches, and Wallpaper Engine/Steam Workshop storage. Use when the user asks to inspect their computer, find what can be cleaned, free disk space, run a safe cleanup, review Windows storage, delete explicitly approved large files, or check Wallpaper Engine for large or duplicate workshop items.
---

# Windows Safe Cleanup

## Bottom-Layer Reasoning

Apply the `think-one-step-further` mechanism as a lightweight check:

- Confirm this skill is solving the user's real intent, not only the surface request.
- Make the output immediately usable and name any unavoidable next action.
- Extract the reusable structure and, when aligned, propagate it to adjacent prompts, skills, checklists, or workflows.
- Add one guardrail for the most likely next failure while preserving this skill's primary workflow.

## Operating Rules

Default to read-only audit. Do not delete anything until the user explicitly approves a cleanup scope.

Use plain user-facing language: "checking disk space", "cleaning safe caches", "Wallpaper subscriptions", not raw command details unless helpful.

Treat these as protected unless the user names an exact path and clearly approves deletion:
- personal projects, footage, photos, videos, documents, downloads, desktop files
- creative app drafts such as Jianying/CapCut, Adobe, Topaz, and editor cache locations
- Steam game installs, app installs, model folders, and chat app data
- credentials, config folders, databases, and hidden app state

Never bulk-delete a drive root, profile root, `AppData`, `Program Files`, `Windows`, or a whole Steam library. For explicitly approved deletes, verify the resolved path first and prefer leaf files or clearly named folders.

## Workflow

1. Run an audit first.
2. Summarize current free space per drive and top cleanup candidates.
3. Split recommendations into:
   - safe cleanup: recycle bins, temp files, browser caches, NVIDIA shader cache, npm/pip/pnpm cache pruning
   - needs confirmation: model caches, old workspaces, app-specific caches
   - manual review: user files, creative drafts, Steam/Wallpaper subscriptions, installed apps
4. Ask for explicit approval before any deletion or cleanup.
5. After cleanup, rerun the audit and report before/after free space.

## Script

Use `scripts/windows_cleanup.ps1` for repeatable checks:

```powershell
# Audit only; default safe starting point.
powershell -ExecutionPolicy Bypass -File C:\Users\liu1\.codex\skills\windows-safe-cleanup\scripts\windows_cleanup.ps1 -AuditOnly

# Safe cleanup after explicit approval.
powershell -ExecutionPolicy Bypass -File C:\Users\liu1\.codex\skills\windows-safe-cleanup\scripts\windows_cleanup.ps1 -CleanSafe

# Include redownloadable model caches only when explicitly approved.
powershell -ExecutionPolicy Bypass -File C:\Users\liu1\.codex\skills\windows-safe-cleanup\scripts\windows_cleanup.ps1 -CleanSafe -IncludeModelCaches

# Scan Wallpaper Engine / Steam Workshop large items and exact duplicate files.
powershell -ExecutionPolicy Bypass -File C:\Users\liu1\.codex\skills\windows-safe-cleanup\scripts\windows_cleanup.ps1 -ScanWallpaper -WallpaperRoot E:\SteamLibrary\steamapps\workshop\content\431960
```

The script prints labeled CSV blocks so the result is easy to summarize.

## Wallpaper Engine

Wallpaper Engine app id is commonly `431960`; workshop content usually lives under:

`<SteamLibrary>\steamapps\workshop\content\431960`

Do not directly delete workshop folders as the first move. Prefer reporting:
- total workshop size
- top largest workshop IDs and largest file names
- exact duplicate files confirmed by hash
- same-name candidates that are not proven duplicates

Recommend unsubscribing or deleting through Steam/Wallpaper Engine for large subscribed items. Direct filesystem deletion is acceptable only after explicit user approval and with the understanding Steam may redownload subscribed content.

## Deletion Checklist

Before deleting an explicitly approved file or folder:

1. Resolve the path and confirm it is not a protected root.
2. Show or internally verify size and type.
3. Use `Remove-Item -LiteralPath` with the exact resolved path.
4. Do not compose deletion commands by piping paths into another shell.
5. Rerun drive-space checks afterward.
