[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $PackwizArguments
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$localPackwiz = Join-Path $repositoryRoot '.build/tools/packwiz/packwiz.exe'
$packwizCommand = if (Test-Path -LiteralPath $localPackwiz) {
    $localPackwiz
} else {
    (Get-Command packwiz -ErrorAction Stop).Source
}

$cachePath = Join-Path $repositoryRoot '.build/packwiz-cache'
$configPath = Join-Path $repositoryRoot '.build/packwiz-config.toml'
$packPath = Join-Path $repositoryRoot 'pack'

New-Item -ItemType Directory -Path $cachePath -Force | Out-Null
Push-Location $packPath
try {
    & $packwizCommand --cache $cachePath --config $configPath @PackwizArguments
    exit $LASTEXITCODE
} finally {
    Pop-Location
}
