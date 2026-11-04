#Requires -Version 5.1
<#
.SYNOPSIS
  Read-only local Windows endpoint observation for isolated labs.
.DESCRIPTION
  Returns an object with OS build, memory, fixed disk utilization and a
  bounded list of processes. Never writes files or makes network calls.
  Process names and system information may be sensitive; redact before sharing.
.PARAMETER TopProcesses
  Number of processes by cumulative CPU time to show (not instantaneous load).
.PARAMETER AsJson
  Emit JSON instead of a PowerShell object for review.
.EXAMPLE
  ./Get-EndpointHealth.ps1 -TopProcesses 5 -AsJson
#>
[CmdletBinding()]
param(
    [ValidateRange(1, 25)]
    [int]$TopProcesses = 5,
    [switch]$AsJson
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSEdition -eq 'Core' -and -not $IsWindows) {
    throw 'This script is intentionally Windows-only.'
}

$os = Get-CimInstance -ClassName Win32_OperatingSystem
$disks = @(Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3" |
    ForEach-Object {
        [pscustomobject]@{
            Drive = $_.DeviceID
            SizeGiB = [math]::Round($_.Size / 1GB, 2)
            FreeGiB = [math]::Round($_.FreeSpace / 1GB, 2)
        }
    })
$processes = @(Get-Process |
    Sort-Object -Property CPU -Descending |
    Select-Object -First $TopProcesses -Property Name, Id, CPU, WorkingSet64)

$result = [pscustomobject]@{
    CapturedUtc = [DateTimeOffset]::UtcNow.ToString('o')
    Platform = 'Windows'
    OsCaption = $os.Caption
    OsVersion = $os.Version
    OsBuild = $os.BuildNumber
    TotalPhysicalMemoryGiB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
    FreePhysicalMemoryGiB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
    FixedDisks = $disks
    TopProcessesByCumulativeCpu = $processes
    InterpretationWarning = 'CPU is cumulative process time, not instantaneous utilization.'
}

if ($AsJson) {
    $result | ConvertTo-Json -Depth 5
} else {
    $result
}
