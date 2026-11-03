# Automation — from shell convenience to safe systems operations

## Why automate?
Avoid repeatable human mistakes and eliminate repetitive toil *without making errors faster*. Production-grade automation must have predictable inputs, bounded scope, meaningful feedback, tests, monitoring, least privilege and recovery.

## Suggested learning order and proof
| Stage | Tool | Learn | Proof |
|---|---|---|---|
| 1 | Bash | Quotes, globs, pipes, exit codes, traps, signals, heredocs, shell portability | P01 with meaningful failures and ShellCheck/Bats |
| 2 | PowerShell | Object pipeline, Get-Help, modules, CIM/WMI, remoting, structured errors | Windows service and update inventory with Pester tests |
| 3 | Python | argparse, pathlib, subprocess (list args), JSON, logging, exceptions, packaging | Cross-platform inventory CLI with pytest |
| 4 | Ansible | Inventory, SSH privilege escalation, playbooks, roles, check mode, vault, idempotence | P06 drift and convergent second run |
| 5 | APIs/IaC | Microsoft Graph least privilege, Jamf APIs (when authorized), Terraform plan/state | Audited low-risk endpoint/cloud workflows |
| 6 | Controlled remediation | Canary, dry-run, blast radius, rollback, rate limits, observability | Mini-enterprise incident management |

## Safety checklist for every script
- [ ] State exactly what it reads, changes and sends over network.
- [ ] Reject unsafe user inputs; avoid command injection and unsafe shell eval.
- [ ] Require explicit authorization/confirmation for destructive operations.
- [ ] No hardcoded secrets; redact credentials/PII in logs; separate test fixtures.
- [ ] Use meaningful exit codes; do not hide error output.
- [ ] Have a rollback strategy and test for idempotence where applicable.
- [ ] Limit privileges and scope; avoid wildcards across remote fleets.
- [ ] Test an empty dataset, missing dependency, permission denied, interrupted operation and partial failure.
- [ ] Include a documentation section for prerequisites, supported OS and limits.
- [ ] Use AI as reviewer/hypothesis generator; personally verify behavior and results.

## Bash knowledge that distinguishes advanced practitioners
Pipelines and pipefail semantics, quoting/word splitting, file descriptors and redirects, signals, traps, race conditions, subprocess effects, POSIX vs Bash-specific syntax, shellcheck, external command failures, version-sensitive GNU vs BSD utilities.

## PowerShell knowledge
Pipelines contain **objects**, not text lines; properties/methods; error actions vs exception handling, CIM, remoting permissions, ExecutionPolicy limitations, Pester tests, careful use of Microsoft Graph with least-privilege delegated/app permissions.

## Ansible knowledge
Desired state vs imperative scripts; modules and idempotence; check mode limitations; templating and variables; handlers and changed/failed conditions; secure secrets management; no indiscriminate root commands.

## AI and programming
Use Python to build small, diagnosable systems utilities, not to divert into generic app development. AI can propose root causes or scripts, but acceptance requires reproducible local measurements, tests, manual review and a safe rollback.

## References
[GNU Bash manual](https://www.gnu.org/software/bash/manual/) · [PowerShell docs](https://learn.microsoft.com/en-us/powershell/) · [Python docs](https://docs.python.org/3/) · [Ansible docs](https://docs.ansible.com/) · [Pester](https://pester.dev/) · [Bats-core](https://bats-core.readthedocs.io/) · [ShellCheck](https://www.shellcheck.net/).
