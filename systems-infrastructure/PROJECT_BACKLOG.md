# Portfolio project backlog — 12 real engineering demonstrations

**State of this file:** specifications, not finished projects. A project can be featured for recruiters only after reproducible implementation and written evidence exist. Prioritize quality over count: three deep, credible studies beat twelve shallow scripts.

## Shared acceptance rubric (each scored 0–2, target ≥ 12/14)
1. Problem, stakeholder constraints and observable success condition
2. Reproducible environment manifest and clean setup
3. Architecture/mechanism explanation, not just command recipes
4. Deliberate, safe failure and hypothesis-driven diagnosis
5. Working implementation or actionable, tested runbook
6. Verification artifacts: real sanitized output, tests, change/rollback
7. Security, privacy, limitations, cost and honest status disclosure

Use [project template](templates/project-readme.md), [incident report template](templates/incident-report.md), and the [progress register](PROGRESS.md). Never commit customer data, employer procedures, credentials, secrets or course assignment solutions in violation of license/policy.

| ID | Priority | Project | Competencies | Status |
|---|---|---|---|---|
| P01 | Immediate | [Linux System Diagnostics](projects/p01-linux-diagnostics/README.md) | Bash, Linux observations, safe CLI | **Starter authored; not yet validated on a real user lab** |
| P02 | First quarter | Boot-to-login and Linux recovery atlas | Firmware, bootloader, kernel, systemd | Planned |
| P03 | First half-year | Linux service failure investigation suite | Systemd, permissions, logs, processes | Planned |
| P04 | First half-year | Isolated Windows AD DS / Group Policy lab | Windows Server, DNS, GPO, identity | Planned |
| P05 | Months 7–9 | Cross-platform system inventory and remediation | PowerShell, Python/Bash, schema, tests | Planned |
| P06 | Months 7–9 | Idempotent three-node Linux fleet | Ansible, security, configuration drift | Planned |
| P07 | Months 10–12 | Network failure and packet-evidence atlas | DNS, routing, TCP, TLS, Wireshark | Planned |
| P08 | Months 13–15 | Apple / Intune endpoint lifecycle laboratory | Jamf, MDM, Intune, compliance | Planned; tenant/device access-gated |
| P09 | Months 16–18 | OS performance investigation | Scheduling, memory, disk, locks | Planned |
| P10 | Months 19–21 | Observability and disaster recovery game day | Metrics, alerting, SLOs, backups | Planned |
| P11 | Months 22–24 | Mini-enterprise IT operations capstone | Identity, endpoints, networks, automation | Planned |
| P12 | Optional | Cost-bounded cloud/hybrid infrastructure | Terraform, cloud ops, IAM, spending | Planned |

## P01 — Linux System Diagnostics (start now)
**User story:** A support engineer needs a non-destructive first view of a slow Linux workstation or server. Build a **read-only**, locally executable Bash script that reports kernel/uptime, load, memory, disk and process/network summaries. Initial source and limitations are in [P01](projects/p01-linux-diagnostics/README.md).

**Prove:** unprivileged execution, no network calls, no persistent writes, well-labelled missing commands, real captured outputs with redaction, checks across two OS environments or clearly documented narrower support. Compare collected observations with source utilities. Add shell tests and ShellCheck and a documented induced low-disk test on an isolated disposable virtual disk.

**Failure modes:** missing tool, nonzero exit, zero/missing mounts, constrained permissions, full scratch disk, concurrent processes. Do not invent outcomes.

## P02 — Boot and Recovery Atlas
**Problem:** A Linux VM becomes unbootable or fails to reach expected services after a configuration change.

**Build:** firmware/UEFI → bootloader → kernel/initramfs → PID 1/systemd → login diagram; controlled breakage of a noncritical boot service and a sandbox mount configuration; use snapshot or recovery media for safe restoration.

**Prove:** 3 different failure signatures, before/after logs, accurate cause, working rollback, successful reboot, a decision tree linking each signal to a hypothesis.

**Risk:** boot/partition experiments only on disposable local VMs, not an everyday laptop.

## P03 — Linux Service Reliability
**Problem:** Service stops after deployment and support must restore it without guessing.

**Build:** simple local demo service plus systemd unit; faults for wrong service account, missing working directory, unsuitable permission, bad environment and port conflict.

**Prove:** service state, journal entries, process and listening-socket analysis, root-cause chain, fix and reboot test for at least four independent faults. Include unit hardening trade-offs.

## P04 — Windows Identity and Group Policy
**Problem:** Securely provision a small office and diagnose a configuration problem.

**Build:** legally licensed/evaluation AD DS server and Windows client on isolated network; OU/group model, DNS integration, GPO, least-privilege delegation. Introduce broken DNS or GPO link deliberately.

**Prove:** real gpresult, Windows event logs and AD/PowerShell diagnostic output **with synthetic identities**; verify restored policy, secure teardown, licensed software.

## P05 — Cross-Platform Endpoint Inventory
**Problem:** A support team needs OS, update, health and service inventories across Windows/Linux without intrusive agents.

**Build:** PowerShell and Python/Bash collectors to a documented JSON schema, offline aggregation, controlled elevation, schema validation, fixtures and automated tests.

**Prove:** correct outputs for distinct environments, error behavior when access is restricted, privacy/redaction tests, no collection of keys, personal files or secrets. macOS support is optional.

## P06 — Ansible Reconciliation Fleet
**Problem:** Configure three isolated Linux VMs predictably.

**Build:** inventory, minimal roles, desired package/service/user/firewall state, verification checks, change log, no inline secrets, explicit rollback and topology diagram.

**Prove:** first apply changes expected state; second apply makes no unintended changes; drift introduction is detected and corrected; clean rebuild succeeds. Compare check/diff mode limitations.

## P07 — Network Failure Atlas
**Problem:** A user reports “the application is down” but symptoms may originate from name resolution, routing, TCP, TLS or application service.

**Build:** local multi-VM path with DNS and web service; deliberately create 5 faults, capture safe packet evidence with Wireshark/tcpdump.

**Prove:** each incident has hypothesis, observed packets, tests, root cause, remedy, verification and one misconception corrected. No scanning external systems.

## P08 — Endpoint Lifecycle: Windows, macOS and MDM
**Problem:** Deploy and secure managed endpoints with policy consistency.

**Build:** documented enrollment → policy → app install → patch → compliance → retirement lifecycle; Windows/Intune and Apple/Jamf variants when authorized test tenants/hardware exist.

**Prove:** actual configuration, results and remediation with redaction and compliance. If no access, publish **architecture/runbooks only** and label untested areas. A Jamf course simulation is **not** production fleet evidence.

## P09 — OS Performance Lab
**Problem:** Slow process with similar user symptoms but radically different root causes.

**Build:** synthetic CPU-bound, I/O-bound, memory-pressure and lock-contention workloads in a VM with safe resource limits.

**Prove:** measurements for load vs CPU use, RSS vs virtual memory, page faults, disk latency/throughput and contention; record false hypotheses and corrected diagnosis. Use measured data, not arbitrary charts.

## P10 — Monitoring and Restore Exercise
**Problem:** Critical internal service must be detected and restored after corruption/failure.

**Build:** small service, Prometheus metrics, actionable alert, synthetic incident, backup schedule and restore playbook.

**Prove:** alert triggered, incident timeline, estimated detection/restore time, restored data integrity, game-day report and known RPO/RTO limitations. Separate lab promises from real SLOs.

## P11 — Reproducible Mini-Enterprise
**Problem:** Manage 10 simulated users and 3–5 mixed machines using identity, endpoint configuration, support tickets, monitoring, backup and changes.

**Build:** isolated architecture using existing smaller labs; synthetic ticket data; provisioning, joining, access controls, policy, monitoring and rollback.

**Prove:** end-to-end onboarding, intentionally broken login/network/update case and working recovery. Must be reproducible using authorized licenses and modest hardware. Explain what is simulated.

## P12 — Cost-Bounded Hybrid/Cloud Operations
**Problem:** Operations need a cloud deployment with reliable teardown and spending controls.

**Build:** minimal single-provider deployment with Terraform, IAM, monitoring and teardown, only if budget and permissions allow.

**Prove:** IaC code review, actual provider costs, zero unnecessary resources after teardown, backup/restore check, incident model, key/secret scanning. Never publish credentials or promise free usage.

## Capstone selection
For endpoint/IT Support Engineer interviews, lead with **P04 + P05 + P08**. For Linux/system engineering, lead with **P03 + P06 + P09**. For infrastructure/cloud ops, lead with **P06 + P10 + P12**. P07 is an excellent cross-role demonstration.

Projects should not get a green “complete” badge until their acceptance tests and evidence are linked.