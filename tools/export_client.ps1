[CmdletBinding()]
param(
    [string] $OutputDirectory = "dist",
    [switch] $PlayableProfile,
    [switch] $RequirePublishableModrinth
)

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$sourcePack = Join-Path $repositoryRoot "pack"
$packDirectory = $sourcePack
if ($PlayableProfile) {
    $buildRoot = [System.IO.Path]::GetFullPath((Join-Path $repositoryRoot ".build"))
    $stageParent = Join-Path $buildRoot "export-source"
    $packDirectory = Join-Path $stageParent "playable-beta"
    $resolvedStage = [System.IO.Path]::GetFullPath($packDirectory)
    if (-not $resolvedStage.StartsWith($buildRoot + [System.IO.Path]::DirectorySeparatorChar)) {
        throw "Playable export stage escapes the repository build directory."
    }
    if (Test-Path -LiteralPath $resolvedStage) {
        Remove-Item -LiteralPath $resolvedStage -Recurse -Force
    }
    New-Item -ItemType Directory -Path $stageParent -Force | Out-Null
    Copy-Item -LiteralPath $sourcePack -Destination $resolvedStage -Recurse

    $blockedMetadata = @(
        "mods/grieflogger.pw.toml",
        "mods/tensura-grief-logger.pw.toml",
        "mods/iceandfire-ce.pw.toml",
        "mods/tensura-compat-ice-fire.pw.toml"
    )
    foreach ($relative in $blockedMetadata) {
        $blockedPath = Join-Path $resolvedStage $relative
        if (-not (Test-Path -LiteralPath $blockedPath)) {
            throw "Expected playable-profile blocker metadata is missing: $relative"
        }
        Remove-Item -LiteralPath $blockedPath -Force
    }
    $diagnosticJar = Join-Path $resolvedStage "mods/tsr-unique-monsters-compat-1.0.0.jar"
    if (Test-Path -LiteralPath $diagnosticJar) {
        Remove-Item -LiteralPath $diagnosticJar -Force
    }
}

$packMetadata = Get-Content -Raw (Join-Path $packDirectory "pack.toml")
$versionMatch = [regex]::Match($packMetadata, '(?m)^version = "([^"]+)"$')
if (-not $versionMatch.Success) {
    throw "Unable to read the pack version from pack/pack.toml."
}

$packVersion = $versionMatch.Groups[1].Value
$artifactDirectory = if ([System.IO.Path]::IsPathRooted($OutputDirectory)) {
    $OutputDirectory
} else {
    Join-Path $repositoryRoot $OutputDirectory
}
$profileLabel = if ($PlayableProfile) { "-Playable" } else { "" }
$curseForgeArtifact = Join-Path $artifactDirectory "Tensura-Sovereign-Rebirth-$packVersion$profileLabel-CurseForge.zip"
$modrinthArtifact = Join-Path $artifactDirectory "Tensura-Sovereign-Rebirth-$packVersion$profileLabel-Modrinth.mrpack"
$localPackwiz = Join-Path $repositoryRoot ".build/tools/packwiz/packwiz.exe"
$packwizCommand = if (Test-Path -LiteralPath $localPackwiz) {
    $localPackwiz
} else {
    (Get-Command packwiz -ErrorAction Stop).Source
}
$cachePath = Join-Path $repositoryRoot ".build/packwiz-cache"
$configPath = Join-Path $repositoryRoot ".build/packwiz-config.toml"
$venvPython = Join-Path $repositoryRoot ".venv/Scripts/python.exe"
$pythonCommand = if (Test-Path -LiteralPath $venvPython) {
    $venvPython
} else {
    $pythonInfo = Get-Command python -ErrorAction SilentlyContinue
    if ($null -eq $pythonInfo) {
        throw "Python 3.11 or newer is required to validate exports."
    }
    $pythonInfo.Source
}

New-Item -ItemType Directory -Path $artifactDirectory -Force | Out-Null

Push-Location $packDirectory
try {
    & $packwizCommand --cache $cachePath --config $configPath "refresh"
    if ($LASTEXITCODE -ne 0) {
        throw "Packwiz index refresh failed."
    }

    & $packwizCommand --cache $cachePath --config $configPath @(
        "curseforge", "export", "--side", "client", "--output", $curseForgeArtifact
    )
    if ($LASTEXITCODE -ne 0) {
        throw "CurseForge export failed."
    }

    & $packwizCommand --cache $cachePath --config $configPath @(
        "modrinth", "export", "--output", $modrinthArtifact
    )
    if ($LASTEXITCODE -ne 0) {
        throw "Modrinth export failed."
    }
} finally {
    Pop-Location
}

& $pythonCommand (Join-Path $repositoryRoot "tools/normalize_zip.py") `
    $curseForgeArtifact $modrinthArtifact
if ($LASTEXITCODE -ne 0) {
    throw "Archive normalization failed."
}

$validationArguments = @(
    (Join-Path $repositoryRoot "tools/validate_exports.py"),
    "--pack-dir", $packDirectory,
    "--curseforge", $curseForgeArtifact,
    "--modrinth", $modrinthArtifact
)
if ($RequirePublishableModrinth) {
    $validationArguments += "--require-publishable-modrinth"
}

& $pythonCommand @validationArguments
if ($LASTEXITCODE -ne 0) {
    throw "Export validation failed."
}

Get-FileHash -Algorithm SHA256 $curseForgeArtifact, $modrinthArtifact |
    Select-Object Path, Hash
