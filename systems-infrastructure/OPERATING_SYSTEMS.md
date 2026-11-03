# Operating systems — mechanism-first study plan

**Main question:** What precisely happens between a user action and hardware state change? Can I observe it, predict failure, and troubleshoot without relying on a memorized fix?

## Progression
### Layer 0 — hardware and firmware
Study CPU privilege levels, registers and caches, RAM vs persistence, PCIe, NVMe/SATA, UEFI, Secure Boot, TPM, interrupts and DMA. **Experiment:** inventory components and trace BIOS/UEFI → bootloader → kernel, within safe VM boundaries. Explain how boot disks and file systems are discovered.

### Layer 1 — CPU, processes and concurrency
Read OSTEP virtualization and concurrency chapters. Explain user/kernel modes, system calls, process state, thread state, preemption, context switching, CPU scheduling, interrupt handling and locking. **Experiment:** create CPU-bound versus I/O-bound processes, inspect process tree/load/scheduling; reproduce and diagnose a simple race condition in a disposable program.

### Layer 2 — memory
Study physical vs virtual addresses, paging, TLBs, caches, allocation, RSS, swap, page faults, copy-on-write and OOM recovery. **Experiment:** bounded memory allocation; compare virtual memory with RSS; observe major/minor faults, swap, and OOM conditions safely inside an isolated small VM.

### Layer 3 — filesystems, block I/O and persistence
Understand inodes, file descriptors, page cache, buffering, journaling, SSD behavior, filesystem mounts, permissions, LVM and backups. **Experiment:** mount a disposable virtual disk, provoke a low-space condition, trace errors, restore from snapshot; never experiment on host partitions.

### Layer 4 — OS startup and service lifecycle
Trace firmware → bootloader → kernel/initramfs → init/systemd → user services. Explain units/dependencies, targets, log channels and failure modes. **Experiment:** P02/P03; use snapshots before breakage.

### Layer 5 — Windows internals and macOS architecture
Compare NT kernel/user processes, Windows Service Control Manager, registry, ETW, security tokens, handles, NTFS vs Linux processes/permissions; compare macOS XNU launchd, APFS, unified logs, code signing and system extensions. **Experiment:** inspect Windows Process Explorer/ProcMon and macOS Activity Monitor/log without altering corporate endpoints.

### Layer 6 — observability tools
Linux: ps, top/htop, vmstat, iostat, ss, strace, perf/eBPF (after fundamentals), journalctl, procfs. Windows: Task Manager, Resource Monitor, Sysinternals, Event Viewer, Performance Monitor, ETW/WPR/WPA. macOS: log, launchctl, sysdiagnose only on authorized devices.

## Explanation tests
Can I distinguish:
- high load average vs CPU saturated?
- total virtual allocation vs physical memory actually resident?
- open socket vs established application-level readiness?
- filesystem full vs inode exhaustion vs quota?
- permission denied vs file missing vs SELinux/AppArmor denial?
- executable not found vs library missing vs service dependency failure?
- a system call boundary vs a userspace library call?
- OS kernel fault vs failing peripheral vs network service fault?

## Original study references
[OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) · [MIT Operating Systems 6.1810](https://pdos.csail.mit.edu/6.1810/2026/) · [Linux Kernel](https://docs.kernel.org/) · [Windows Internals resources](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals) · [Apple Platform Security](https://support.apple.com/guide/security/welcome/web).

**No copying MIT assignment solutions publicly.** Publish original measurements, diagrams and explanations, respecting course terms.