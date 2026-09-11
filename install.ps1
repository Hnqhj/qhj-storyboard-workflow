param([string]$CodexHome = $env:CODEX_HOME)
$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($CodexHome)) { $CodexHome = Join-Path $env:USERPROFILE '.codex' }
$target = Join-Path $CodexHome 'skills'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Get-ChildItem -LiteralPath (Join-Path $here 'skills') -Directory | ForEach-Object { Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force }
Write-Host "Installed QHJ skill bundle to $target"
