# Learning resource catalog — official-first and lab-linked

**Last researched: 2026-11-03; university study addendum verified 2026-11-05.** Free means content access is free, **not** necessarily a free exam, included lab/cloud tenant, perpetual access or optional instruction. Verify region-specific price, version and availability before paying.

An editable [40-entry learning tracker](LEARNING_TRACKER.csv) is available for dated, evidence-linked progress. **Not started** in the tracker means *not yet recorded as completed in this portfolio*; it does not assert the user never studied the material elsewhere.

## Added university foundations and possible ECTS opportunities

For independent computer-engineering depth: [Nand2Tetris, MIT 6.042J mathematics, architecture and OS](../learning-hub/university/COMPUTER_FOUNDATIONS.md).

For optional formally assessed studies with free-access offerings: [Helsinki Python and cybersecurity, Turku AI/cybersecurity, KAMK cloud and other current offerings](../learning-hub/university/FINNISH_CREDIT_OPPORTUNITIES.md). **Credit is conditional, not automatically awarded by completing a MOOC.** The current [Metropolia enrollment restriction](https://www.metropolia.fi/en/study-at-metropolia/open-university) applies to people without the required Finnish personal identity code, unless an applicable exception is confirmed.

These university studies **supplement**, not replace, the Linux and network lab evidence tracked below.

## How to use this catalog
Pick **one primary** resource per topic, then use the reference material to answer questions raised by a lab. Record actual exercise evidence in [PROGRESS](PROGRESS.md). For each module, ask: (1) what mechanism did I learn? (2) can I predict an outcome? (3) can I provoke and diagnose a failure? (4) can I automate and test recovery?

### Track 1: Linux and shell — months 1–6
| Resource | Access | Primary practical outcome |
|---|---|---|
| **[Linux Foundation — LFS101 Introduction to Linux](https://training.linuxfoundation.org/training/introduction-to-linux/)** | Free course | Files, processes, services, permissions, shell and networking |
| **[MIT Missing Semester (2026)](https://missing.csail.mit.edu/2026/)** | Free | Shell, debugging/profiling, Git, development tools and code quality |
| [GNU Bash manual](https://www.gnu.org/software/bash/manual/) | Free official reference | Quoting, expansions, exit statuses, redirection, signals |
| [Linux man-pages](https://man7.org/linux/man-pages/) | Free | Kernel/user APIs, syscalls and details of tools |
| [Ubuntu Server documentation](https://documentation.ubuntu.com/server/) | Free | Networking, systemd, security and package-management labs |
| [Red Hat RHEL docs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/) | Free manuals | RHEL-specific SELinux, systemd, LVM, storage and networking |
| [ArchWiki](https://wiki.archlinux.org/) | Free community reference | Troubleshooting, boot and system concepts; check distro applicability |
| [RHCSA EX200 objective outline](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam) | Free objectives; exam paid | Practical administrator self-assessment |

**Lab requirement:** create, inspect and recover services; permissions; logical volumes (only on virtual disks); scheduled jobs; troubleshooting after reboot. Distinguish Ubuntu, RHEL and other distributions where commands differ.

### Track 2: OS architecture, firmware and internals — months 4–18
| Resource | Access | Practical outcome |
|---|---|---|
| **[Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/)** | Free textbook PDFs | CPU scheduling, virtual memory, concurrency, persistence |
| **[MIT 6.1810 Operating System Engineering, Fall 2026](https://pdos.csail.mit.edu/6.1810/2026/)** | Free materials | xv6 and kernel mechanisms; obey class code-sharing policies |
| [Linux kernel documentation](https://docs.kernel.org/) | Free | Kernel APIs, subsystems and tracing |
| [Linux tracing with bpftrace](https://bpftrace.org/docs/release_024/one-liners) | Free docs; platform dependent | Inspect actual process/kernel events in an isolated Linux VM |
| [Intel Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) | Free | x86 architecture, privilege, memory (advanced) |
| [UEFI specifications](https://uefi.org/specifications) | Free | Boot firmware architecture |
| [CS:APP book site](https://csapp.cs.cmu.edu/) | Site free; textbook normally paid | C, assembly, caches, memory, process model |
| [The Linux Programming Interface — publisher](https://nostarch.com/tlpi) | Paid book | Mature Linux system-call and process reference |

**Lab requirement:** measure scheduling effects, reproduce memory pressure, trace files/syscalls, explain boot chain; advanced xv6 work should be original and compliant with MIT's public-sharing restrictions.

### Track 3: Windows and enterprise identity — months 1–15
| Resource | Access | Practical outcome |
|---|---|---|
| **[Microsoft Learn — Get started with Windows PowerShell](https://learn.microsoft.com/en-us/training/paths/get-started-windows-powershell/)** | Free | Cmdlets, pipelines, objects and scripts |
| [PowerShell documentation](https://learn.microsoft.com/en-us/powershell/) | Free | Native help, remoting, error handling and modules |
| **[Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/)** | Free utilities/docs | Process Explorer, ProcMon, Autoruns, TCPView |
| [Windows Performance Toolkit](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/) | Free docs; tool install required | ETW/WPR/WPA performance evidence |
| [Windows Server documentation](https://learn.microsoft.com/en-us/windows-server/) | Free | AD DS, Group Policy, DNS, Windows Server internals |
| [Microsoft Entra docs](https://learn.microsoft.com/en-us/entra/) | Free | Cloud identity, groups, auth and hybrid identity |
| [Microsoft Intune docs](https://learn.microsoft.com/en-us/intune/) | Free | Provisioning, policy, applications, compliance and remediation |
| [Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/overview) | Free | Scoped and auditable API automation |
| [Windows Server Administrator AZ-802 exam study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) | Free guide; exam paid | AD, hybrid Windows management and troubleshooting |
| [MD-102 Endpoint Administrator study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102) | Free guide; exam paid | Windows and cross-platform device administration |
| [Windows Internals book, Part 1](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals) | Book paid; reference page free | Windows kernel, processes, memory and security |

**Lab requirement:** inspect Windows process trees and handles; repair a deliberately failing scheduled task or service; create a small domain/Group Policy lab only with legitimate OS licenses; use synthetic account names and never publish tenant IDs or user records.

### Track 4: macOS, Jamf, Apple endpoint management — months 7–15
| Resource | Access | Practical outcome |
|---|---|---|
| **[Jamf 100](https://www.jamf.com/training/100-course/)** | **25 free lessons**; exam **USD 100** currently | Mac/iOS/iPadOS, Jamf Pro, profiles, app/software management |
| [Jamf training catalog](https://trainingcatalog.jamf.com/) | Self-paced selection and paid tracks | Jamf Pro, Protect, device management |
| **[Jamf 170 — Jamf Protect](https://www.jamf.com/training/170-course/)** | **14 free lessons and a free certification exam** per Jamf's 2025 announcement; verify current exam terms before registering | Apple endpoint security, compliance, Jamf Protect and Jamf Security Cloud |
| [Jamf 200](https://www.jamf.com/training/200-course/) | Paid instructor-led | Advanced hands-on Jamf administration |
| **[Apple IT Training](https://training.apple.com/)** | Self-paced learning; certification exams paid | Apple Device Support, Deployment and Management |
| [Apple Platform Deployment](https://support.apple.com/guide/deployment/welcome/web) | Free Apple reference | Enrollment, identity, platform management |
| [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) | Free Apple reference | Secure boot, identity, FileVault, platform trust |
| [Apple Developer — Device Management](https://developer.apple.com/documentation/devicemanagement) | Free reference | MDM protocol and declarative management |
| [macOS command-line admin guide](https://support.apple.com/guide/terminal/welcome/mac) | Free | Shell-level OS observation |

**Lab requirement:** describe the full managed-device lifecycle; conduct authorized tests only on personally owned devices and legitimate tenants. A Jamf 100 simulation is **not** equivalent to deploying a 500-device fleet.

### Track 5: networking and protocol troubleshooting — months 2–12
| Resource | Access | Practical outcome |
|---|---|---|
| **[Cisco Networking Academy](https://www.netacad.com/)** | Many free courses | Network fundamentals, switching/routing and labs |
| [CCNA 200-301 official exam page](https://www.cisco.com/web/go/ccna/) | Free objectives; exam paid | Structured networking competency |
| [CCNA v2.0 topics PDF](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf) | Free official PDF | Prepare for **Feb 3, 2027** new exam |
| [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer) | Free for qualifying learners | Simulate routers, switches, VLANs, routes |
| **[Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)** | Free | Packet capture and protocol analysis |
| [TCP/IP Illustrated, Vol. 1](https://www.pearson.com/en-us/subject-catalog/p/tcpip-illustrated-volume-1-the-protocols/P200000003320) | Paid book | Deep protocol mechanics, supplement to Wireshark |
| [Cloudflare Learning Center](https://www.cloudflare.com/learning/) | Free vendor explanations | HTTP, DNS, TLS, certificates and edge |

**Lab requirement:** packet-level evidence distinguishing DNS, route, TCP, TLS and application failure; recreate a topology and explain packet flow hop by hop.

### Track 6: Bash, PowerShell, Python, Ansible and Terraform — months 4–21
| Resource | Access | Practical outcome |
|---|---|---|
| **[Ansible getting started](https://docs.ansible.com/projects/ansible/latest/getting_started/get_started_ansible.html)** | Free | Inventories, playbooks, idempotent configuration |
| [Python tutorial](https://docs.python.org/3/tutorial/) | Free | CLI tools, exception handling, structured data |
| [pytest docs](https://docs.pytest.org/en/stable/) | Free | Executable behavior checks |
| [ShellCheck](https://www.shellcheck.net/) | Free open-source linting | Bash scripting quality |
| [Bats-core](https://bats-core.readthedocs.io/) | Free | Shell tests |
| [Pester](https://pester.dev/) | Free | PowerShell tests |
| [Git book — Pro Git](https://git-scm.com/book/en/v2) | Free | Version control, auditability and review |
| **[Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)** | Free content; infrastructure may cost | IaC, state, planning and drift |
| [Existing Terraform Mastery project](https://github.com/thokchomlolet03-cpu/terraform-mastery) | Existing personal work | Deepen state, planning, reconciliation and failure labs |
| [GitHub Actions docs](https://docs.github.com/en/actions) | Free docs; usage quotas depend on account | Automated lint, tests and checks |

**Lab requirement:** every remediation script provides an explicit dry-run or inspection-only mode where practical, least-privilege assumptions, tests, meaningful error status and recovery instructions.

### Track 7: cloud operations, observability and resilience — months 16–24
| Resource | Access | Practical outcome |
|---|---|---|
| [Google SRE book](https://sre.google/sre-book/table-of-contents/) | Free | SLOs, toil, incident response, reliability |
| [Google SRE workbook](https://sre.google/workbook/table-of-contents/) | Free | Applied incident practice and SLOs |
| [Prometheus docs](https://prometheus.io/docs/introduction/overview/) | Free | Metrics collection, alerting |
| [Grafana tutorials](https://grafana.com/tutorials/) | Free materials; hosting may cost | Dashboards and analysis |
| [AWS Skill Builder](https://skillbuilder.aws/) | Free + paid tiers | Intro to AWS operations |
| [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) | Free | Recovery, failure domains, resilience |
| [Azure architecture center](https://learn.microsoft.com/en-us/azure/architecture/) | Free | Infrastructure patterns |
| [Google Cloud training](https://cloud.google.com/learn/training) | Free + paid programs | Google Cloud ops and infrastructure |

**Lab requirement:** inject failure, alert on it, identify root cause, recover from backup and demonstrate budget cleanup. Keep cloud spending near zero until lab skills are established.

## In-person programs: pay only for differentiated value
- **Red Hat RH124/RH134/RH199** hands-on administration if a reputable authorized provider offers a real lab environment and practice exam.
- **Cisco CCNA instructor-led** only if there are physical networking labs and instructor feedback.
- **Jamf 200** instructor-led after free Jamf 100, preferably employer-funded.
- **Structured cabling / fiber** short hands-on labs if targeting data-center or field network hardware roles.
- Vendor/learning-hub courses may have access limits; **verify an employer catalog and learning rights privately**, do not republish proprietary materials.

### Study tracking template
For each resource: URL, why chosen, free/paid, prerequisites, current version, start/finish dates, one lab artifact, failure examined, and next action. The checkpoint is *what can I reproduce?*, not the number of videos watched.

### Additional virtualization and recovery sources (P13)
| Resource | Access | Practical outcome |
|---|---|---|
| [Microsoft Hyper-V overview](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-overview) | Free documentation; supported Windows license/hardware required | Virtual switches, VM lifecycle and recovery |
| [libvirt documentation](https://libvirt.org/docs.html) | Free documentation | KVM/QEMU virtual machines on Linux |
| [QEMU documentation](https://www.qemu.org/docs/master/) | Free documentation | Guest architecture, virtual disk and emulation models |
| [Proxmox VE documentation](https://pve.proxmox.com/pve-docs/) | Free documentation; assess licenses/support | Enterprise-style hypervisor and backup architecture |
| [Microsoft Windows evaluation center](https://www.microsoft.com/en-us/evalcenter/) | Evaluation under product terms | Licensed Windows lab images, where available |

Use [P13](projects/p13-virtualization-recovery/README.md) to demonstrate **verified independent restoration** rather than purchasing hardware or accumulating more tutorials. Do not treat backup software installation as proof of recovery capability.
