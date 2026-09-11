param(
  [switch]$AuditOnly,
  [switch]$CleanSafe,
  [switch]$IncludeModelCaches,
  [switch]$ScanWallpaper,
  [string]$WallpaperRoot = "E:\SteamLibrary\steamapps\workshop\content\431960",
  [int]$Top = 30,
  [int]$MinDuplicateMB = 100
)

$ErrorActionPreference = "Continue"

function Write-Block {
  param([string]$Name, [object[]]$Rows)
  Write-Output $Name
  if ($Rows -and $Rows.Count -gt 0) {
    $Rows | ConvertTo-Csv -NoTypeInformation
  } else {
    Write-Output "EMPTY"
  }
}

function Get-DriveSnapshot {
  Get-PSDrive -PSProvider FileSystem |
    Select-Object Name, Root,
      @{Name="UsedGB"; Expression = { [math]::Round($_.Used / 1GB, 2) }},
      @{Name="FreeGB"; Expression = { [math]::Round($_.Free / 1GB, 2) }},
      @{Name="TotalGB"; Expression = { [math]::Round(($_.Used + $_.Free) / 1GB, 2) }},
      @{Name="FreePercent"; Expression = {
        if (($_.Used + $_.Free) -gt 0) {
          [math]::Round(100 * $_.Free / ($_.Used + $_.Free), 1)
        } else {
          $null
        }
      }}
}

function Get-SizeGB {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return 0 }
  $sum = (Get-ChildItem -LiteralPath $Path -Force -Recurse -File -ErrorAction SilentlyContinue |
    Measure-Object -Property Length -Sum).Sum
  if ($null -eq $sum) { $sum = 0 }
  [math]::Round($sum / 1GB, 3)
}

function Get-FolderStat {
  param([string]$Name, [string]$Path)
  $exists = Test-Path -LiteralPath $Path
  if (-not $exists) {
    return [pscustomobject]@{ Name = $Name; Path = $Path; SizeGB = 0; Files = 0; Exists = $false }
  }
  $files = Get-ChildItem -LiteralPath $Path -Force -Recurse -File -ErrorAction SilentlyContinue
  $sum = ($files | Measure-Object -Property Length -Sum).Sum
  if ($null -eq $sum) { $sum = 0 }
  [pscustomobject]@{
    Name = $Name
    Path = $Path
    SizeGB = [math]::Round($sum / 1GB, 3)
    Files = ($files | Measure-Object).Count
    Exists = $true
  }
}

function Assert-SafeDirectoryTarget {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return $false }
  $resolved = (Resolve-Path -LiteralPath $Path -ErrorAction Stop).Path
  $blocked = @(
    "C:\", "D:\", "E:\",
    $env:USERPROFILE, $env:LOCALAPPDATA, $env:APPDATA, $env:SystemRoot,
    "C:\Users", "C:\Windows", "C:\Program Files", "C:\Program Files (x86)"
  )
  foreach ($item in $blocked) {
    if ($item -and $resolved.TrimEnd("\") -ieq $item.TrimEnd("\")) { return $false }
  }
  return $true
}

function Clear-DirectoryContentsSafely {
  param([string]$Label, [string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) {
    return [pscustomobject]@{ Label = $Label; Path = $Path; BeforeGB = 0; AfterGB = 0; FreedGB = 0; Status = "Missing" }
  }
  if (-not (Assert-SafeDirectoryTarget -Path $Path)) {
    $size = Get-SizeGB -Path $Path
    return [pscustomobject]@{ Label = $Label; Path = $Path; BeforeGB = $size; AfterGB = $size; FreedGB = 0; Status = "Skipped unsafe target" }
  }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $before = Get-SizeGB -Path $resolved
  Get-ChildItem -LiteralPath $resolved -Force -ErrorAction SilentlyContinue |
    ForEach-Object { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction SilentlyContinue }
  $after = Get-SizeGB -Path $resolved
  [pscustomobject]@{
    Label = $Label
    Path = $resolved
    BeforeGB = $before
    AfterGB = $after
    FreedGB = [math]::Round($before - $after, 3)
    Status = "Cleaned"
  }
}

function Clear-RecycleBinsSafely {
  $rows = New-Object System.Collections.Generic.List[object]
  foreach ($drive in Get-PSDrive -PSProvider FileSystem) {
    $path = Join-Path $drive.Root '$Recycle.Bin'
    if (-not (Test-Path -LiteralPath $path)) {
      $rows.Add([pscustomobject]@{ Label = "Recycle Bin"; Path = $path; BeforeGB = 0; AfterGB = 0; FreedGB = 0; Status = "Missing" })
      continue
    }
    $before = Get-SizeGB -Path $path
    Get-ChildItem -LiteralPath $path -Force -ErrorAction SilentlyContinue |
      ForEach-Object { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction SilentlyContinue }
    $after = Get-SizeGB -Path $path
    $rows.Add([pscustomobject]@{
      Label = "Recycle Bin"
      Path = $path
      BeforeGB = $before
      AfterGB = $after
      FreedGB = [math]::Round($before - $after, 3)
      Status = "Cleaned"
    })
  }
  return $rows
}

function Invoke-Audit {
  $targets = @(
    @{ Name = "User Downloads"; Path = "$env:USERPROFILE\Downloads" },
    @{ Name = "User Desktop"; Path = "$env:USERPROFILE\Desktop" },
    @{ Name = "User Documents"; Path = "$env:USERPROFILE\Documents" },
    @{ Name = "User Videos"; Path = "$env:USERPROFILE\Videos" },
    @{ Name = "User Temp"; Path = "$env:TEMP" },
    @{ Name = "Windows Update Download Cache"; Path = "$env:SystemRoot\SoftwareDistribution\Download" },
    @{ Name = "NVIDIA DXCache"; Path = "$env:LOCALAPPDATA\NVIDIA\DXCache" },
    @{ Name = "Chrome Cache"; Path = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cache" },
    @{ Name = "Chrome Code Cache"; Path = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Code Cache" },
    @{ Name = "Chrome Service Worker Cache"; Path = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Service Worker\CacheStorage" },
    @{ Name = "Edge Cache"; Path = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Cache" },
    @{ Name = "Edge Code Cache"; Path = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Code Cache" },
    @{ Name = "Edge Service Worker Cache"; Path = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Service Worker\CacheStorage" },
    @{ Name = "npm Cache"; Path = "$env:LOCALAPPDATA\npm-cache" },
    @{ Name = "pip Cache"; Path = "$env:LOCALAPPDATA\pip\Cache" },
    @{ Name = "pnpm Store"; Path = "$env:LOCALAPPDATA\pnpm\store" },
    @{ Name = "HuggingFace Cache"; Path = "$env:USERPROFILE\.cache\huggingface" },
    @{ Name = "Codex Workspaces"; Path = "$env:USERPROFILE\Documents\Codex" },
    @{ Name = "QoderWork Workspace"; Path = "$env:USERPROFILE\.qoderwork\workspace" }
  )

  $recycleTargets = foreach ($drive in Get-PSDrive -PSProvider FileSystem) {
    @{ Name = "$($drive.Name) Recycle Bin"; Path = (Join-Path $drive.Root '$Recycle.Bin') }
  }

  Write-Block "DRIVES" @(Get-DriveSnapshot)
  Write-Block "CLEANUP_CANDIDATES" @(($targets + $recycleTargets) | ForEach-Object {
    Get-FolderStat -Name $_.Name -Path $_.Path
  } | Sort-Object SizeGB -Descending)
}

function Invoke-CleanSafe {
  $before = @(Get-DriveSnapshot)
  $rows = New-Object System.Collections.Generic.List[object]

  foreach ($row in Clear-RecycleBinsSafely) { $rows.Add($row) }

  $targets = @(
    @{ Label = "NVIDIA DXCache"; Path = "$env:LOCALAPPDATA\NVIDIA\DXCache" },
    @{ Label = "Chrome Cache"; Path = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cache" },
    @{ Label = "Chrome Code Cache"; Path = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Code Cache" },
    @{ Label = "Chrome Service Worker Cache"; Path = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Service Worker\CacheStorage" },
    @{ Label = "Edge Cache"; Path = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Cache" },
    @{ Label = "Edge Code Cache"; Path = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Code Cache" },
    @{ Label = "Edge Service Worker Cache"; Path = "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Service Worker\CacheStorage" },
    @{ Label = "User Temp"; Path = "$env:TEMP" },
    @{ Label = "Windows Update Download Cache"; Path = "$env:SystemRoot\SoftwareDistribution\Download" }
  )

  if ($IncludeModelCaches) {
    $targets += @{ Label = "HuggingFace Cache"; Path = "$env:USERPROFILE\.cache\huggingface" }
  }

  foreach ($target in $targets) {
    $rows.Add((Clear-DirectoryContentsSafely -Label $target.Label -Path $target.Path))
  }

  $pipPath = "$env:LOCALAPPDATA\pip\Cache"
  $beforePip = Get-SizeGB -Path $pipPath
  try {
    if (Get-Command pip -ErrorAction SilentlyContinue) {
      & pip cache purge | Out-Null
    } else {
      $rows.Add((Clear-DirectoryContentsSafely -Label "pip Cache fallback" -Path $pipPath))
    }
  } catch {}
  $afterPip = Get-SizeGB -Path $pipPath
  $rows.Add([pscustomobject]@{ Label = "pip Cache"; Path = $pipPath; BeforeGB = $beforePip; AfterGB = $afterPip; FreedGB = [math]::Round($beforePip - $afterPip, 3); Status = "Purged if available" })

  $npmPath = "$env:LOCALAPPDATA\npm-cache"
  $beforeNpm = Get-SizeGB -Path $npmPath
  try {
    if (Get-Command npm -ErrorAction SilentlyContinue) {
      & npm cache clean --force | Out-Null
    } else {
      $rows.Add((Clear-DirectoryContentsSafely -Label "npm Cache fallback" -Path $npmPath))
    }
  } catch {}
  $afterNpm = Get-SizeGB -Path $npmPath
  $rows.Add([pscustomobject]@{ Label = "npm Cache"; Path = $npmPath; BeforeGB = $beforeNpm; AfterGB = $afterNpm; FreedGB = [math]::Round($beforeNpm - $afterNpm, 3); Status = "Cleaned if available" })

  $pnpmPath = "$env:LOCALAPPDATA\pnpm\store"
  $beforePnpm = Get-SizeGB -Path $pnpmPath
  try {
    if (Get-Command pnpm -ErrorAction SilentlyContinue) {
      & pnpm store prune | Out-Null
    }
  } catch {}
  $afterPnpm = Get-SizeGB -Path $pnpmPath
  $rows.Add([pscustomobject]@{ Label = "pnpm Store"; Path = $pnpmPath; BeforeGB = $beforePnpm; AfterGB = $afterPnpm; FreedGB = [math]::Round($beforePnpm - $afterPnpm, 3); Status = "Pruned only" })

  Write-Block "DRIVES_BEFORE" $before
  Write-Block "CLEAN_RESULTS" $rows
  Write-Block "DRIVES_AFTER" @(Get-DriveSnapshot)
}

function Invoke-WallpaperScan {
  if (-not (Test-Path -LiteralPath $WallpaperRoot)) {
    Write-Block "WALLPAPER_STATUS" @([pscustomobject]@{ Path = $WallpaperRoot; Status = "Missing" })
    return
  }

  $topItems = Get-ChildItem -LiteralPath $WallpaperRoot -Force -Directory -ErrorAction SilentlyContinue |
    ForEach-Object {
      $files = Get-ChildItem -LiteralPath $_.FullName -Force -Recurse -File -ErrorAction SilentlyContinue
      $sum = ($files | Measure-Object -Property Length -Sum).Sum
      if ($null -eq $sum) { $sum = 0 }
      $largest = $files | Sort-Object Length -Descending | Select-Object -First 1
      [pscustomobject]@{
        WorkshopId = $_.Name
        SizeGB = [math]::Round($sum / 1GB, 3)
        FileCount = ($files | Measure-Object).Count
        LargestFileGB = $(if ($largest) { [math]::Round($largest.Length / 1GB, 3) } else { 0 })
        LargestFileName = $(if ($largest) { $largest.Name } else { "-" })
        Path = $_.FullName
      }
    } | Sort-Object SizeGB -Descending | Select-Object -First $Top

  Write-Block "WALLPAPER_TOP_ITEMS" @($topItems)

  $minBytes = [int64]$MinDuplicateMB * 1MB
  $files = Get-ChildItem -LiteralPath $WallpaperRoot -Force -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object {
      $_.Length -ge $minBytes -and
      $_.Name -notmatch "\.7z\.\d{3}$" -and
      $_.Name -notmatch "\.zip\.\d{3}(\.exe)?$"
    }

  $sameSize = $files | Group-Object Length | Where-Object { $_.Count -gt 1 }
  $hashRows = foreach ($group in $sameSize) {
    foreach ($file in $group.Group) {
      try {
        $hash = Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256 -ErrorAction Stop
        [pscustomobject]@{
          SizeGB = [math]::Round($file.Length / 1GB, 3)
          Hash = $hash.Hash
          WorkshopId = ($file.FullName -replace "^.*content\\431960\\([^\\]+).*$", '$1')
          Name = $file.Name
          Path = $file.FullName
        }
      } catch {}
    }
  }

  $dupes = $hashRows |
    Group-Object Hash |
    Where-Object { $_.Count -gt 1 } |
    ForEach-Object {
      [pscustomobject]@{
        Count = $_.Count
        SizeEachGB = $_.Group[0].SizeGB
        DuplicateWasteGB = [math]::Round(($_.Count - 1) * $_.Group[0].SizeGB, 3)
        Items = ($_.Group | ForEach-Object { $_.WorkshopId + " :: " + $_.Name }) -join " | "
        Paths = ($_.Group | ForEach-Object { $_.Path }) -join " | "
      }
    } | Sort-Object DuplicateWasteGB -Descending

  Write-Block "WALLPAPER_EXACT_DUPLICATES" @($dupes)
}

if (-not $AuditOnly -and -not $CleanSafe -and -not $ScanWallpaper) {
  $AuditOnly = $true
}

if ($AuditOnly) { Invoke-Audit }
if ($CleanSafe) { Invoke-CleanSafe }
if ($ScanWallpaper) { Invoke-WallpaperScan }
