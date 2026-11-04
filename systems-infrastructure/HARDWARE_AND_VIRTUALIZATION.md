# Hardware, firmware, virtualization and storage — the missing physical layer

**Scope:** first-principles understanding needed for Systems Engineers, Infrastructure Engineers and Data Center Technicians. This complements [OS internals](OPERATING_SYSTEMS.md) and [P13 recovery lab](projects/p13-virtualization-recovery/README.md).

## Hardware to OS causal chain
Power delivery and firmware → CPU privilege, microcode and memory controller → DRAM and storage controllers → PCIe buses and device discovery → boot configuration and secure boot → kernel drivers → block/network device abstraction → filesystem and application I/O.

Learn to explain **which layer owns an error** and what evidence differentiates a physical fault from an OS/driver/virtualization issue.

| Subsystem | What to learn | A safe observation exercise |
|---|---|---|
| CPU | core vs thread, cache, turbo, thermal limits, hardware virtualization | Compare guest allocated vCPU with actual host capacity; document scheduling contention |
| Memory | DRAM, ECC, OOM vs hardware faults, page tables, swap | Use bounded VM-only memory pressure; inspect page faults and resource limits |
| Storage | SSD/NVMe, SMART, RAID redundancy, filesystem vs backup | Inspect a disposable virtual disk and restore synthetic files from independent backup |
| Firmware | BIOS/UEFI, boot order, TPM, secure boot, driver handoff | Photograph or describe a permitted firmware setup; never change risky host settings without recovery |
| Networking hardware | NIC, PHY, link lights, speeds/duplex, VLANs, cables/fiber | Isolated packet captures, link-level fault reasoning, no third-party scanning |
| Server management | BMC, IPMI, Redfish, out-of-band management, remote console | Read vendor docs or use a legally available simulator; never expose a BMC to internet |
| Virtualization | type-1 vs type-2, virtual switches, virtual disks, guest agents, snapshots | Explain host/guest boundary and run [P13](projects/p13-virtualization-recovery/README.md) |

## Essential distinctions
- RAID improves availability under certain drive faults. **RAID is not backup.**
- A VM snapshot helps reverse some changes but cannot replace an independently recoverable backup.
- A disk being nearly full differs from filesystem inode exhaustion, quota restrictions and slow I/O.
- High load average does not necessarily mean CPU saturation.
- A remote management network is a separate security boundary; isolate it.
- An application error may arise from firmware/hardware drivers or a hypervisor resource issue; test competing hypotheses before swapping parts.

## Data-center skills — optional branch
Physical cabling and labeling, rack elevation and load, power distribution, redundant supplies, ESD precautions, parts inventory, hardware fault isolation, firmware/BIOS upgrades, drive replacement policies, secure erasure and ticket documentation. Actual high-voltage, facility-power or fiber safety procedures require supervised, authorized hands-on instruction.

## Reproducibility requirements
A lab write-up should include host architecture, RAM, disk controller/storage backend, hypervisor version, guest image and kernel, networking mode, fault injection boundary, observed metrics, cost, restore method and limitations. **Never claim production server/BMC experience solely from reading a vendor manual.**

## References
[Linux kernel documentation](https://docs.kernel.org/) · [Intel SDM](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) · [UEFI specifications](https://uefi.org/specifications) · [QEMU](https://www.qemu.org/docs/master/) · [libvirt](https://libvirt.org/docs.html) · [Microsoft Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-overview).
