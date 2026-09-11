[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$Query,

    [ValidateRange(1, 10)]
    [int]$Limit = 6,

    [ValidateRange(500, 12000)]
    [int]$MaxContentChars = 6000
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$skillRoot = Split-Path -Parent $PSScriptRoot
$promptsPath = Join-Path $skillRoot 'references/prompts.json'
if (-not (Test-Path -LiteralPath $promptsPath -PathType Leaf)) {
    throw "Curated prompts file not found: $promptsPath"
}

$normalizedQuery = $Query.Trim().ToLowerInvariant()
if ($normalizedQuery.Length -eq 0) {
    Write-Output '[]'
    exit 0
}

$stopWords = @(
    'a', 'an', 'and', 'are', 'art', 'create', 'for', 'from', 'image', 'in',
    'make', 'of', 'on', 'photo', 'picture', 'style', 'the', 'to', 'with'
)
$terms = @(
    [regex]::Matches($normalizedQuery, '[a-z0-9][a-z0-9-]{1,}') |
        ForEach-Object { $_.Value } |
        Where-Object { $_.Length -ge 3 -and $stopWords -notcontains $_ } |
        Sort-Object -Unique
)
if ($terms.Count -eq 0) {
    $terms = @($normalizedQuery)
}

$records = Get-Content -Raw -Encoding UTF8 -LiteralPath $promptsPath | ConvertFrom-Json
$results = [System.Collections.Generic.List[object]]::new()

foreach ($record in $records) {
    $title = [string]$record.title
    $description = [string]$record.description
    $content = [string]$record.content
    $score = 0
    $matchedTerms = [System.Collections.Generic.List[string]]::new()

    if ($normalizedQuery.Length -ge 3) {
        if ($title.ToLowerInvariant().Contains($normalizedQuery)) { $score += 30 }
        if ($description.ToLowerInvariant().Contains($normalizedQuery)) { $score += 15 }
        if ($content.ToLowerInvariant().Contains($normalizedQuery)) { $score += 6 }
    }

    foreach ($term in $terms) {
        $pattern = [regex]::Escape($term)
        $titleMatches = [regex]::Matches($title, $pattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase).Count
        $descriptionMatches = [regex]::Matches($description, $pattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase).Count
        $contentMatches = [regex]::Matches($content, $pattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase).Count
        if (($titleMatches + $descriptionMatches + $contentMatches) -gt 0) {
            $matchedTerms.Add($term)
        }
        $score += 8 * $titleMatches
        $score += 3 * $descriptionMatches
        $score += $contentMatches
    }

    $minimumTermMatches = if ($terms.Count -ge 4) { 2 } else { 1 }
    if ($score -le 0 -or $matchedTerms.Count -lt $minimumTermMatches) { continue }

    $truncated = $content.Length -gt $MaxContentChars
    if ($truncated) {
        $content = $content.Substring(0, $MaxContentChars) + '...'
    }

    $results.Add([pscustomobject]@{
        score = $score
        matchedTerms = @($matchedTerms)
        id = $record.id
        title = $title
        description = $description
        content = $content
        contentTruncated = $truncated
        sourceMedia = @($record.sourceMedia)
        needReferenceImages = [bool]$record.needReferenceImages
        sourceUrl = "https://youmind.com/nano-banana-pro-prompts?id=$($record.id)"
    })
}

$sorted = @($results | Sort-Object @{ Expression = 'score'; Descending = $true }, @{ Expression = { [int64]$_.id }; Descending = $false })
$top = @($sorted | Select-Object -First $Limit)
if ($top.Count -eq 0) {
    Write-Output '[]'
    exit 0
}

Write-Output (ConvertTo-Json -InputObject $top -Depth 6)
