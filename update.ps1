param([string]$CodexHome = $env:CODEX_HOME)
$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($CodexHome)) { $CodexHome = Join-Path $env:USERPROFILE '.codex' }
$target = Join-Path $CodexHome 'skills'
$repo = 'https://github.com/Hnqhj/QHJ-SKILL.git'
$tmp = Join-Path $env:TEMP 'qhj-skill-update'
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
git clone --depth 1 $repo $tmp
Get-ChildItem -LiteralPath (Join-Path $tmp 'skills') -Directory | ForEach-Object { Copy-Item $_.FullName -Destination $target -Recurse -Force }
Copy-Item (Join-Path $tmp 'manifest.json') -Destination (Join-Path $target 'qhj-manifest.json') -Force -ErrorAction SilentlyContinue
Remove-Item $tmp -Recurse -Force
Write-Host "QHJ skills updated from GitHub."
