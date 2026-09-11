param(
  [int]$Days = 1,
  [string]$CodexHome = $env:CODEX_HOME
)
$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($CodexHome)) { $CodexHome = Join-Path $env:USERPROFILE '.codex' }
$taskName = 'QHJ-SKILL-AutoUpdate'
$scriptPath = Join-Path $CodexHome 'skills\qhj-skill\update.ps1'
if (-not (Test-Path -LiteralPath $scriptPath)) { $scriptPath = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'update.ps1' }
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" -CodexHome `"$CodexHome`""
$trigger = New-ScheduledTaskTrigger -Daily -DaysInterval $Days -At 3:00AM
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel LeastPrivilege
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Description 'Pull and install QHJ-SKILL updates from GitHub' -Force | Out-Null
Write-Host "Scheduled task '$taskName' installed. It will pull updates every $Days day(s) at 03:00."
