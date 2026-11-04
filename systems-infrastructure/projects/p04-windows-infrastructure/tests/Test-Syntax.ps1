# Static parse test only; runs under PowerShell Core on Linux CI or Windows.
# This does not execute Get-EndpointHealth.ps1 or validate Windows CIM results.
Set-StrictMode -Version Latest
$path = Join-Path $PSScriptRoot '..' 'Get-EndpointHealth.ps1'
$tokens = $null
$parseErrors = $null
[void][System.Management.Automation.Language.Parser]::ParseFile(
    (Resolve-Path $path).Path, [ref]$tokens, [ref]$parseErrors
)
if ($parseErrors.Count -gt 0) {
    foreach ($item in $parseErrors) { Write-Error $item.Message }
    exit 1
}
Write-Output 'PASS: PowerShell syntax parse (Windows runtime untested).'
