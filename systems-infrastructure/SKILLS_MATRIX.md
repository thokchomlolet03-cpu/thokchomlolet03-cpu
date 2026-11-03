# Competency matrix: what “very good” means

**Definitions:** Familiar = explain key concepts. Functional = independently perform routine tasks. Strong = troubleshoot unfamiliar failures under constraints and explain mechanism. Advanced = design secure, repeatable, measured recovery/automation and teach or review others' work. **Target** is a future goal; this matrix does not assert the skill is already held.

| Competency | Suggested target | Proof required | Projects |
|---|---|---|---|
| Hardware and boot | Strong | Explain firmware/UEFI, CPU privilege, RAM/storage; fix three safe boot faults | P02 |
| Linux daily administration | Strong | Install, secure, monitor, manage users/storage/services and recover after reboot | P01/P03 |
| Linux internals | Strong | Explain system call, context switch, scheduler, page fault, caching; observe with tools | P09 |
| Windows administration | Strong | AD DS/DNS/GPO, service diagnostics, Process Monitor and Event Viewer evidence | P04/P05 |
| macOS and Apple deployment | Functional → Strong | Show platform security and compliant enrollment in an authorized lab | P08 |
| TCP/IP networking | Strong | Distinguish routing/DNS/TCP/TLS/HTTP with packet traces and repairs | P07 |
| Endpoint fleet administration | Strong | Identity, packaging, policy, patching, inventory, compliant remediation | P05/P08 |
| Bash | Strong | Defensive scripts, traps/exit codes, tests, review, documented failure semantics | P01/P05 |
| PowerShell | Strong | Structured objects, modules, remote admin when permitted, Pester tests | P05 |
| Python for systems | Functional → Strong | Robust CLI, subprocess safety, structured logs, tests, packaging | P05 |
| Ansible | Strong | Safe roles, repeat convergence, drift recovery, vault/secret discipline | P06 |
| Infrastructure as code | Functional → Strong | State/diff, drift, lifecycle, cleanup, documented risk | Terraform Mastery/P12 |
| Storage/backup | Strong | Restore checks, disaster-recovery game day, data integrity demonstration | P10 |
| Incident response | Strong | Hypothesis-driven evidence, timeline, root cause vs symptom, follow-up actions | P03/P07/P10 |
| Cloud operations | Functional | One provider's IAM, cost controls, logs, monitoring, basic recovery | P12 |
| Communication & documentation | Strong | Crisp runbook, case study, architecture explanation and measurable trade-offs | All |

## Honest baseline
Prior enterprise support includes AD, Microsoft 365, Intune, Jamf, SCCM, ServiceNow, remote networking and customer-facing incident work. **Do not infer expert-level skills merely from tool exposure**. Track each area against concrete tasks and reproducible evidence, not a self-rating.

## Deep-understanding questions
For every subsystem ask:
1. What hardware/kernel/userland mechanism creates the observed behavior?
2. What competing hypotheses predict similar symptoms?
3. What single safe measurement most efficiently distinguishes them?
4. Which corrective action changes the necessary mechanism, and what could it break?
5. How would I detect recurrence across hundreds of machines?
6. How would I test and safely revert an automated intervention?
7. Could I explain this without relying on a tutorial or AI?

Quarterly reevaluate the target based on observed deficiencies and job-market requirements.