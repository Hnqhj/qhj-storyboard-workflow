<#
.SYNOPSIS
  安装 QHJ-SKILL 技能包到本机 Codex / WorkBuddy 技能目录。

.DESCRIPTION
  把本仓库 skills\ 下的技能平铺复制到目标宿主的 skills 目录。
  只新增 / 覆盖，绝不删除任何已有内容。

.EXAMPLE
  .\install.ps1                    # 装到 Codex + WorkBuddy（默认 -Target all）
  .\install.ps1 -Target codex      # 只装 Codex  ->  %USERPROFILE%\.codex\skills
  .\install.ps1 -Target workbuddy  # 只装 WorkBuddy -> %USERPROFILE%\.workbuddy\skills
  .\install.ps1 -CodexHome D:\codex -WorkBuddyHome D:\wb
#>
[CmdletBinding()]
param(
  [ValidateSet('codex', 'workbuddy', 'all')]
  [string]$Target = 'all',
  [string]$CodexHome = $env:CODEX_HOME,
  [string]$WorkBuddyHome = $env:WORKBUDDY_HOME
)
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($CodexHome)) { $CodexHome = Join-Path $env:USERPROFILE '.codex' }
if ([string]::IsNullOrWhiteSpace($WorkBuddyHome)) { $WorkBuddyHome = Join-Path $env:USERPROFILE '.workbuddy' }

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$src = Join-Path $here 'skills'
if (-not (Test-Path -LiteralPath $src)) { throw "skills directory not found: $src" }

# 用显式列表而不是 switch 输出，避免 PowerShell 对单元素结果的展开歧义。
$targets = New-Object System.Collections.ArrayList
if ($Target -eq 'codex' -or $Target -eq 'all') {
  [void]$targets.Add(@{ Name = 'Codex'; Root = (Join-Path $CodexHome 'skills') })
}
if ($Target -eq 'workbuddy' -or $Target -eq 'all') {
  [void]$targets.Add(@{ Name = 'WorkBuddy'; Root = (Join-Path $WorkBuddyHome 'skills') })
}

foreach ($t in $targets) {
  # 注意：变量不能叫 $target —— PowerShell 变量名不区分大小写，
  # 会撞上 [ValidateSet] 的 $Target 参数，赋值时直接触发校验失败。
  $dest = $t.Root
  if (-not (Test-Path -LiteralPath $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
  $count = 0
  foreach ($s in Get-ChildItem -LiteralPath $src -Directory) {
    Copy-Item -LiteralPath $s.FullName -Destination $dest -Recurse -Force
    $count++
  }
  Write-Host ("[{0}] installed {1} skills -> {2}" -f $t.Name, $count, $dest)
}
