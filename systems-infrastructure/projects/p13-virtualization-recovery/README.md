# P13 — Virtualization, Storage and Disaster Recovery Lab

**Status: planned. This document is a reproducible exercise specification, not evidence of a working hypervisor, VMware administrator experience, tested backups or production disaster recovery.**

## Why this is a flagship project
A Systems Engineer must understand more than creating a virtual machine. You should distinguish VM host vs guest, CPU/memory overcommit, virtual NIC vs network bridge, storage latency and capacity, snapshot chains, backup consistency, restore processes, and the blast radius of failed infrastructure.

**Business scenario:** A synthetic internal application runs in a VM. A storage failure or configuration mistake makes it unavailable. The recovery objective is to rebuild or restore it reliably while measuring data loss and recovery time.

## Select one low-cost, legally usable platform
- **Existing Windows host:** Hyper-V if your Windows edition and hardware support it; use official Hyper-V docs.
- **Existing Intel/AMD Linux host:** KVM/QEMU with libvirt, using distro-supported packages. Avoid privileged network exposure.
- **Existing Apple Silicon Mac:** use an ARM64 guest with UTM or another supported hypervisor; document host/guest architecture differences and unsupported nested virtualization.
- **Dedicated owned lab hardware (optional):** Proxmox VE only when you can isolate it, accept its licensing/subscription terms, and safely install on a nonessential disk.

**Do not install a bare-metal hypervisor on your only working computer or company hardware.** No cloud spending is required. Do not expose SSH, RDP, web admin panels or management interfaces to the public internet.

## Isolated topology
~~~text
Owned computer / hypervisor
   |
   +-- VM-A: synthetic service and synthetic dataset
   |      isolated virtual disk + internal virtual NIC
   +-- VM-B: monitoring/backup verification (optional)
   |
   +-- Independent backup destination
          NOT merely a snapshot of VM-A on the same virtual disk
~~~

## Six staged experiments
**E01: provision and inspect.** Record host CPU architecture, hypervisor, guest OS/kernel, allocated CPU/RAM/disk, virtual NIC mode, storage backend and utilization. Explain the hypervisor and I/O path.

**E02: resource pressure.** Apply a bounded synthetic CPU or disk workload to the guest in a disposable snapshot-backed VM. Compare guest metrics with host metrics and explain contention/limits. Never fill the host disk intentionally.

**E03: network failure.** Introduce a guest-only DNS or virtual firewall misconfiguration. Prove where the failure occurs using link, route, DNS, TCP and application-level tests.

**E04: snapshot vs independent backup.** Create a VM snapshot and separately back up a synthetic dataset to another permitted storage location. Explain why snapshots alone are usually not a sufficient recovery plan, particularly when disk/host storage is lost.

**E05: verified restore.** Generate synthetic records and a hash manifest, make an independent backup, corrupt a disposable copy, then recover into a **fresh, isolated recovery VM**. Verify integrity by SHA-256 or equivalent hashes and an application health check; do not overwrite the sole remaining copy.

**E06: recovery game day.** Start a timer at the simulated incident declaration, diagnose and restore the application, record actual detection/restore intervals, confirm data state and explain measured RPO/RTO instead of fictional numbers.

## Evidence table (fill only after executing)
| Test | Prediction | Actual measurement | Evidence | Recovery status |
|---|---|---|---|---|
| E01 inventory | — | Not executed | — | Planned |
| E02 contention | — | Not executed | — | Planned |
| E03 network fault | — | Not executed | — | Planned |
| E04 snapshot + separate backup | — | Not executed | — | Planned |
| E05 clean restore + hash verification | — | Not executed | — | Planned |
| E06 timed recovery | — | Not executed | — | Planned |

## Required technical write-up
- Architecture diagram and exact versions, license/cost limitations, host vs guest boundaries.
- Data model and **synthetic** baseline manifest, restore steps and independently verified hashes.
- Which faults snapshot recovery can address vs disk loss, host failure or logical corruption.
- Observed changes from host pressure, memory ballooning or disk latency (if platform supports them).
- Security boundaries: snapshot/backup confidentiality, key management, least privilege, backup access.
- A documented **failed** attempt and revised hypothesis, not only a successful happy path.
- A concise post-incident report with a genuine recorded recovery duration.

## Role alignment
Windows/Linux Systems Administrator; Infrastructure Engineer; Virtualization Engineer; Cloud Operations and Data Center Operations. VMware-specific operations should only be claimed if actually practiced on a properly licensed VMware environment.

## References
[Microsoft Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-overview) · [libvirt](https://libvirt.org/docs.html) · [QEMU](https://www.qemu.org/docs/master/) · [Proxmox VE](https://pve.proxmox.com/pve-docs/) · [Google SRE Workbook](https://sre.google/workbook/table-of-contents/).
