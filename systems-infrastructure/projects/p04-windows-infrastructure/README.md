# P04 — Enterprise Windows Infrastructure and PowerShell

**Status: planned lab, with read-only script source authored. No owner-executed Windows Server, Active Directory, Group Policy or Microsoft Entra deployment is claimed.**

## Recruiter brief
**Scenario:** A small company reports intermittent domain logons, Group Policy failures and slow devices. Recreate an isolated Windows environment; use DNS, identity, event logs, PowerShell and first-principles troubleshooting to distinguish causes.

**What this will eventually demonstrate:** Windows Server installation, AD DS and DNS, client domain joining, least-privilege accounts/OU design, Group Policy, Kerberos concepts, endpoint diagnostics, and repeatable recovery. Document real outcomes after executing the lab.

## Architecture

~~~text
Physical host / hypervisor (licensed OS and isolated host-only network)
  |
  +-- win-dc-01  : Windows Server evaluation/licensed VM
  |                 AD DS, DNS for corp.example.test (synthetic domain)
  +-- win-client-01 : Windows client evaluation/licensed VM
  |                   domain member with synthetic test user
  +-- linux-admin-01: optional diagnostics-only Linux machine
~~~

**Do not use an employer tenant, work-issued device, live user directory or any organization's DNS zone.** The reserved `.test` suffix denotes a fictional lab. Do not publish IP addresses tied to your personal or employer network.

## Stage 0: licensing, isolation and baseline
- Obtain Windows Server and Windows client media from Microsoft under the applicable evaluation or license terms. Record exact edition, version, license conditions and expiration in a private local environment manifest.
- Create a host-only virtual network with no exposed RDP/WinRM ports. Use snapshots for experiments and a separate independent backup.
- Establish a baseline of Windows Update state, hostname, firewall profile, event logs, time sync and disk health. Keep credentials only in approved local password handling; never commit.
- If current hardware cannot support two Windows VMs, **do not fabricate evidence**. Perform the free PowerShell and Sysinternals observation exercises on a personal Windows computer first.

## Stage 1: build and diagnose
1. Install an isolated Windows Server and promote it to a *new lab forest* only after confirming the domain name and network isolation.
2. Record the purpose of AD DS, DNS, Kerberos, NTLM legacy compatibility, Group Policy, LDAP and time synchronization.
3. Create fictional departmental OUs, synthetic users, security groups and minimal GPOs; explain scope, precedence and least-privilege delegation.
4. Join the lab client and verify logon with a synthetic account.
5. Inspect domain DNS with `Resolve-DnsName`, AD-related logs with Event Viewer, domain policy using `gpresult /r`, effective identity with `whoami /all`, and client domain join with `Get-CimInstance Win32_ComputerSystem`.
6. Document a controlled safe change to an OU-linked policy and expected/actual effect.
7. Reboot each VM and verify behavior; restore a snapshot only after collecting evidence.

## Stage 2: reversible failure investigations
| Fault | Predicted symptom to test | Primary evidence | Verification |
|---|---|---|---|
| Incorrect client DNS pointing away from DC | Domain discovery or logon issues | Resolver config, DNS lookup, domain events | Restore DC DNS, verify lookup and logon |
| Unlinked test GPO | Intended restriction does not apply | GPResult, OU path, GPO link/scope | Relink correctly, verify policy |
| Stopped noncritical demo service | Application unavailable but domain intact | Service state, Event Viewer, dependency state | Restore service, verify without reboot |
| Restricted synthetic file permissions | Access denied despite valid identity | NTFS ACL, identity/group, event log | Apply minimum correct ACL, verify |
| Incorrect time on a disposable client (optional) | Potential Kerberos authentication errors | Time skew and authentication evidence | Restore safe time sync; do not modify host/real network |

Do not intentionally disable security on a networked machine. Do not publish private domain inventories, account names, sensitive screenshots or full authentication logs.

## Stage 3: PowerShell read-only diagnostic starter
Review [Get-EndpointHealth.ps1](Get-EndpointHealth.ps1) before using it on a personally owned, authorized Windows test machine. The script performs **local observations only**, collects no file content, calls no network endpoints and writes no files. Process names and service states can still be sensitive: redact outputs before publication.

~~~powershell
Get-Help ./Get-EndpointHealth.ps1 -Detailed
./Get-EndpointHealth.ps1 -TopProcesses 5
./Get-EndpointHealth.ps1 -TopProcesses 5 -AsJson
~~~

A PowerShell script is not proof of a working AD domain. Further lab validation and Pester testing must be recorded separately.

## Evidence and exit criteria
- Environment manifest and diagram, with costs/licensing assumptions and rebuild instructions.
- Three independent hypotheses per simulated incident; time-stamped actual observations.
- A functioning synthetic domain logon, a demonstrably applied test GPO, and a failed-and-recovered scenario.
- Sanitized screenshots or transcripts, issue numbers, rollback, and a repeatability check after reboot.
- PowerShell source reviewed, tested, and documented for unsupported versions.
- An original [incident report](../../templates/incident-report.md) that separates mechanism from symptom.
- Independent owner-lab verification before promoting to **demonstrated**.

## Primary references
[Windows Server documentation](https://learn.microsoft.com/en-us/windows-server/) · [Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) · [Microsoft Windows PowerShell](https://learn.microsoft.com/en-us/powershell/) · [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) · [Windows evaluation center](https://www.microsoft.com/en-us/evalcenter/).
