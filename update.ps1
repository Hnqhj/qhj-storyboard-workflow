<#
.SYNOPSIS
  从 GitHub 拉取 QHJ-SKILL 最新版本并安装到本机技能目录。

.DESCRIPTION
  git clone --depth 1 公开仓库 -> 把 skills\ 平铺复制到目标宿主 -> 写入 manifest。
  只更新技能文件，不修改宿主系统目录。

.EXAMPLE
  .\update.ps1                     # 更新 Codex + WorkBuddy
  .\update.ps1 -Target workbuddy   # 只更新 WorkBuddy
  .\update.ps1 -Repo <url>         # 用自定义仓库地址（fork 场景）
#>
[CmdletBinding()]
param(
  [ValidateSet('codex', 'workbuddy', 'all')]
  [string]$Target = 'all',
  [string]$CodexHome = $env:CODEX_HOME,
  [string]$WorkBuddyHome = $env:WORKBUDDY_HOME,
  [string]$Repo = 'https://github.com/Hnqhj/QHJ-SKILL.git'
)
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($CodexHome)) { $CodexHome = Join-Path $env:USERPROFILE '.codex' }
if ([string]::IsNullOrWhiteSpace($WorkBuddyHome)) { $WorkBuddyHome = Join-Path $env:USERPROFILE '.workbuddy' }

$targets = New-Object System.Collections.ArrayList
if ($Target -eq 'codex' -or $Target -eq 'all') {
  [void]$targets.Add(@{ Name = 'Codex'; Root = (Join-Path $CodexHome 'skills') })
}
if ($Target -eq 'workbuddy' -or $Target -eq 'all') {
  [void]$targets.Add(@{ Name = 'WorkBuddy'; Root = (Join-Path $WorkBuddyHome 'skills') })
}

# 唯一临时目录：避免并发/残留导致 clone 失败。
$tmp = Join-Path $env:TEMP ('qhj-skill-update-' + [Guid]::NewGuid().ToString('N').Substring(0, 8))
try {
  # Windows PowerShell 5.1 会把原生命令写到 stderr 的内容（git 的 "Cloning into ..."、
  # 进度条等）当成 ErrorRecord；上层一旦把错误流重定向（*>&1 / 2>&1），
  # 配合 $ErrorActionPreference = 'Stop' 就会被误判成终止错误。
  # 所以这里局部降级为 Continue，只以 $LASTEXITCODE 为准。
  $eap = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  $gitOut = @(git clone --depth 1 $Repo $tmp 2>&1)
  $cloneExit = $LASTEXITCODE
  $ErrorActionPreference = $eap
  if ($cloneExit -ne 0) {
    $detail = ($gitOut | ForEach-Object { $_.ToString() }) -join "`n"
    throw "git clone failed (exit $cloneExit): $Repo`n$detail"
  }

  $src = Join-Path $tmp 'skills'
  if (-not (Test-Path -LiteralPath $src)) { throw "skills directory not found in clone: $src" }

  foreach ($t in $targets) {
    $dest = $t.Root
    if (-not (Test-Path -LiteralPath $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
    $count = 0
    foreach ($s in Get-ChildItem -LiteralPath $src -Directory) {
      Copy-Item -LiteralPath $s.FullName -Destination $dest -Recurse -Force
      $count++
    }
    Copy-Item -LiteralPath (Join-Path $tmp 'manifest.json') -Destination (Join-Path $dest 'qhj-manifest.json') -Force -ErrorAction SilentlyContinue
    Write-Host ("[{0}] updated {1} skills -> {2}" -f $t.Name, $count, $dest)
  }
  Write-Host "QHJ skills updated from GitHub."
} finally {
  if (Test-Path -LiteralPath $tmp) { Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue }
}
