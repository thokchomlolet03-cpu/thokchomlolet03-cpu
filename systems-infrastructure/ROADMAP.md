# 24-month curriculum with career checkpoints

**Planning horizon:** November 2026–October 2028, at ~8–10 focused hours/week. **Not a guarantee of proficiency, sponsorship or employment.** Each stage ends with a reproducible demonstration rather than a course-completion screenshot.

| Months | Core competency | Deliverables | Employment checkpoint |
|---|---|---|---|
| 1–3 | Linux shell, VMs, logs, boot, storage, Windows PowerShell, TCP/DNS fundamentals | P01 diagnostics; P03 service triage; begin P04 PowerShell | Apply to matched L2/IT support roles using existing professional evidence |
| 4–6 | Linux services/SELinux/filesystems; Windows Server AD DS/GPO/DNS; virtual networks and backups | P04 Windows domain; begin P13 recovery | Choose RHCSA or MD-102 according to interviews/job descriptions |
| 7–9 | Bash, PowerShell, Python for administration, testing, Ansible | P05 inventory; P06 Linux fleet; finish P13 restore | Explore endpoint/sysadmin roles with hands-on proof |
| 10–12 | Routing, VLANs, DNS, DHCP, TLS and packet analysis | P07 network incident atlas | Decide whether CCNA has strong ROI |
| 13–15 | Intune, Jamf, Apple platform management, patch/remediation policies | P08 enterprise endpoint runbooks | Target workplace/endpoint engineers |
| 16–18 | Scheduling, virtual memory, locks, filesystem internals, tracing, optional xv6 | P09 performance case study | Distinguish measured mechanisms from guesses |
| 19–21 | Observability, backups/restore, security hardening, incident response, change controls | P10 monitoring and restoration | Infrastructure/cloud operations path |
| 22–24 | Integration, automated provisioning, operating documentation | P11 mini-enterprise; P12 cost-bounded cloud/hybrid lab | Polish top 3 deep case studies and apply systematically |

### First 90 days: make three things *real*
1. Repair GitHub CI, then personally reproduce P01 diagnostics and P03 systemd failures in an owned VM.
2. Begin [P04 Windows + PowerShell](projects/p04-windows-infrastructure/README.md) with a legal Windows test environment or read-only Windows client observations if server licensing/hardware is not available.
3. Document an isolated virtual machine backup and **independent** restore using [P13](projects/p13-virtualization-recovery/README.md); do not confuse snapshots with backups.

For a recruiter, lead with finished evidence, not a 24-month aspirational schedule. See [career evidence](CAREER_EVIDENCE_SYSTEM.md).

### Two paths after the shared foundation
**Track A — Workplace Technology / Endpoint Engineering:** Windows, PowerShell, Active Directory, Microsoft Entra, Intune, Jamf, macOS, Apple enrollment, endpoint security. This path has immediate relevance to prior experience.

**Track B — Linux Systems / Infrastructure Engineering:** RHCSA-level administration, networking, configuration management with Ansible, monitoring, Terraform, cloud operations, reliability. Deeper systems specialization.

**Initial learning split:** 50% Linux + OS internals, 30% Windows + endpoint, 20% network + automation practice. Rebalance from actual job descriptions at months 3, 6, 12 and 18. Avoid simultaneously pursuing every cloud provider or multiple expensive exams.

### International employment considerations
- **UAE:** IT support, endpoint engineer, desktop support, system administrator and infrastructure operations opportunities.
- **Ireland:** workplace technology, internal IT, endpoint management, data-center/infrastructure operations. Check each employer's **actual sponsorship/work authorization** requirements.
- **Germany:** system administration, support and infrastructure roles. Parallel German learning (B1/B2 then higher as needed) matters for many customer-facing roles; some international roles operate in English.
- No certification automatically confers eligibility for a job, visa or country-specific professional qualification.

### Stage-exit gate
1. Fresh VM/tenant lab rebuilt by following version-controlled instructions.
2. Fault reproduced, predicted outcome and actual outcome compared.
3. Automation is tested and documented, including failure behavior.
4. Data are sanitized and lawful to publish.
5. One-page incident or technical case study explains root cause, alternatives and limitations.
6. Interview-grade explanation in own words with no live AI guidance.

This plan is reviewed quarterly against job ads and time available, not treated as an unchangeable calendar.
