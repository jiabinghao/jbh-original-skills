# Copies only selected skills. Does not overwrite an existing directory.
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Low')]
param(
    [string[]]$Skill = @(),
    [string]$Destination = ''
)

$ErrorActionPreference = 'Stop'
$packageRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$catalog = Get-Content -LiteralPath (Join-Path $packageRoot 'catalog.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$knownNames = @($catalog.skills | ForEach-Object { $_.name })
if ($Skill.Count -eq 0) { $Skill = $knownNames }
$selectedNames = @($Skill | Select-Object -Unique)
foreach ($name in $selectedNames) {
    if ($name -notmatch '^jbh-[a-z0-9]+(-[a-z0-9]+)*$' -or $knownNames -notcontains $name) {
        throw "Unknown skill: $name"
    }
}
if ([string]::IsNullOrWhiteSpace($Destination)) {
    if ($env:CODEX_HOME) {
        $Destination = Join-Path $env:CODEX_HOME 'skills'
    } else {
        $Destination = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex/skills'
    }
}
$destinationRoot = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Destination)
$destinationRoot = [IO.Path]::GetFullPath($destinationRoot)
$sourceRoot = [IO.Path]::GetFullPath((Join-Path $packageRoot 'skills'))
$separator = [IO.Path]::DirectorySeparatorChar
if ($destinationRoot.TrimEnd($separator) -eq $sourceRoot.TrimEnd($separator) -or
    $destinationRoot.StartsWith($sourceRoot.TrimEnd($separator) + $separator, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Destination must be outside the source skills directory.'
}
if ((Test-Path -LiteralPath $destinationRoot) -and -not (Test-Path -LiteralPath $destinationRoot -PathType Container)) {
    throw 'Destination exists and is not a directory.'
}
# Preflight the entire selection before any write, preventing partial conflict installs.
foreach ($name in $selectedNames) {
    $source = Join-Path $sourceRoot $name
    $target = Join-Path $destinationRoot $name
    if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf) -or
        -not (Test-Path -LiteralPath (Join-Path $source 'LICENSE') -PathType Leaf)) {
        throw "Incomplete source skill: $name"
    }
    if (Test-Path -LiteralPath $target) {
        throw "Destination already exists; nothing overwritten: $target"
    }
}
foreach ($name in $selectedNames) {
    $source = Join-Path $sourceRoot $name
    $target = Join-Path $destinationRoot $name
    if ($PSCmdlet.ShouldProcess($target, 'Install skill')) {
        if (-not (Test-Path -LiteralPath $destinationRoot)) {
            New-Item -ItemType Directory -Path $destinationRoot -Force | Out-Null
        }
        Copy-Item -LiteralPath $source -Destination $target -Recurse -ErrorAction Stop
        Write-Output "Installed: $target"
    }
}
