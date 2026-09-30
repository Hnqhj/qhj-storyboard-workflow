<#
.SYNOPSIS
  注册 Windows 计划任务，定时从 GitHub 拉取并安装 QHJ-SKILL 更新。

.DESCRIPTION
  任务名 QHJ-SKILL-AutoUpdate，默认每天 03:00 运行 update.ps1。
  可在「任务计划程序」中查看 / 停用 / 删除。

.EXAMPLE
  .\setup-auto-update.ps1                    # 每天 03:00，更新 Codex + WorkBuddy
  .\setup-auto-update.ps1 -Days 7            # 每 7 天一次
  .\setup-auto-update.ps1 -Target workbuddy  # 只更新 WorkBuddy
#>
[CmdletBinding()]
param(
  [int]$Days = 1,
  [ValidateSet('codex', 'workbuddy', 'all')]
  [string]$Target = 'all',
  [string]$CodexHome = $env:CODEX_HOME,
  [string]$WorkBuddyHome = $env:WORKBUDDY_HOME
)
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($CodexHome)) { $CodexHome = Join-Path $env:USERPROFILE '.codex' }
if ([string]::IsNullOrWhiteSpace($WorkBuddyHome)) { $WorkBuddyHome = Join-Path $env:USERPROFILE '.workbuddy' }

# 优先用本脚本同目录的 update.ps1（clone 场景）；否则找宿主里已安装的那份。
$candidates = New-Object System.Collections.ArrayList
[void]$candidates.Add((Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'update.ps1'))
if ($Target -eq 'codex' -or $Target -eq 'all') { [void]$candidates.Add((Join-Path $CodexHome 'skills\qhj-skill\update.ps1')) }
if ($Target -eq 'workbuddy' -or $Target -eq 'all') { [void]$candidates.Add((Join-Path $WorkBuddyHome 'skills\qhj-skill\update.ps1')) }

$scriptPath = @($candidates | Where-Object { Test-Path -LiteralPath $_ }) | Select-Object -First 1
if ([string]::IsNullOrWhiteSpace($scriptPath)) {
  throw 'update.ps1 not found. Keep this script next to update.ps1, or run install.ps1 first.'
}

$taskName = 'QHJ-SKILL-AutoUpdate'
$argLine = "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" -Target $Target"
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument $argLine
$trigger = New-ScheduledTaskTrigger -Daily -DaysInterval $Days -At 3:00AM
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel LeastPrivilege
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Description 'Pull and install QHJ-SKILL updates from GitHub' -Force | Out-Null
Write-Host "Scheduled task '$taskName' installed. Target=$Target, every $Days day(s) at 03:00."
Write-Host "Update script: $scriptPath"
