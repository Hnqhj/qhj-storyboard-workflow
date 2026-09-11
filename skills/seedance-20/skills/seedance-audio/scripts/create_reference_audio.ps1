param(
    [Parameter(Mandatory = $true)]
    [string]$PayloadFile,
    [string]$ApiUrl = "http://127.0.0.1:5177"
)

$ErrorActionPreference = "Stop"
$install = Join-Path $env:LOCALAPPDATA "AssetBrowser"
$configPath = Join-Path $install "asset-browser.config.json"
$serverPath = Join-Path $install "server.js"

function Test-Workbench {
    try {
        $response = Invoke-RestMethod -Uri "$ApiUrl/api/config" -TimeoutSec 2
        return $null -ne $response
    } catch {
        return $false
    }
}

if (-not (Test-Workbench)) {
    if (-not (Test-Path -LiteralPath $serverPath)) {
        throw "生成资产工作台未安装：$serverPath"
    }
    $node = (Get-Command node -ErrorAction Stop).Source
    Start-Process -FilePath $node -ArgumentList "server.js" -WorkingDirectory $install -WindowStyle Hidden
    $ready = $false
    for ($index = 0; $index -lt 80; $index += 1) {
        Start-Sleep -Milliseconds 250
        if (Test-Workbench) {
            $ready = $true
            break
        }
    }
    if (-not $ready) {
        throw "生成资产工作台没有正常启动"
    }
}

$resolvedPayload = (Resolve-Path -LiteralPath $PayloadFile).Path
$payload = Get-Content -LiteralPath $resolvedPayload -Raw -Encoding utf8 | ConvertFrom-Json
$config = Get-Content -LiteralPath $configPath -Raw -Encoding utf8 | ConvertFrom-Json

if (-not $payload.projectId) {
    $activeProfile = $config.automation.routing.profiles |
        Where-Object { $_.id -eq $config.automation.routing.activeProfileId } |
        Select-Object -First 1
    if ($activeProfile) {
        $payload | Add-Member -NotePropertyName projectId -NotePropertyValue $activeProfile.projectId -Force
        $payload | Add-Member -NotePropertyName profileId -NotePropertyValue $activeProfile.id -Force
    } else {
        $payload | Add-Member -NotePropertyName projectId -NotePropertyValue "pending-review" -Force
        $payload | Add-Member -NotePropertyName profileId -NotePropertyValue "pending-review" -Force
    }
}

$body = $payload | ConvertTo-Json -Depth 20
$result = Invoke-RestMethod `
    -Uri "$ApiUrl/api/rhythm-control/create" `
    -Method Post `
    -ContentType "application/json; charset=utf-8" `
    -Body ([Text.Encoding]::UTF8.GetBytes($body)) `
    -TimeoutSec 900

if (-not $result.ok -or -not $result.track.absolutePath) {
    throw "参考音频没有返回有效文件"
}

$trackPath = $result.track.absolutePath
$promptPath = $result.track.promptPath
$metaPath = $result.track.metaPath
foreach ($required in @($trackPath, $promptPath, $metaPath)) {
    if (-not (Test-Path -LiteralPath $required)) {
        throw "参考音频归档不完整：$required"
    }
}

$actualHash = (Get-FileHash -LiteralPath $trackPath -Algorithm SHA256).Hash.ToLowerInvariant()
if ($actualHash -ne ([string]$result.track.sha256).ToLowerInvariant()) {
    throw "参考音频 SHA-256 校验失败"
}

$result | ConvertTo-Json -Depth 20 -Compress
