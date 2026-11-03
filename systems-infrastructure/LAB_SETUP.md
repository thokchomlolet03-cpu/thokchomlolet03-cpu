# Lab setup: minimal cost, controlled failure, real understanding

## Start with one VM
Use an existing computer and 1 Ubuntu Server VM. Add a second Linux VM for Ansible after the first is reproducible. Windows and macOS enterprise labs come later, only with properly licensed hardware and tenant access.

### Architecture and hypervisor warning
- **Apple Silicon (ARM64) Macs:** use an ARM64-compatible guest image and virtualization software (e.g., UTM or other ARM-aware hypervisor). Do not assume x86 ISO images run natively at full speed. For x86-specific OS exercises, use actual x86 hardware, appropriately configured emulation with trade-offs, or permitted lab infrastructure.
- **Windows Server/Windows client:** obey evaluation/licensing terms. Windows Server AD DS labs require more resources.
- **macOS/Jamf:** some MDM workflows require Apple hardware, Jamf tenant, Apple Business Manager/School Manager eligibility and organization enrollment. Document prerequisites and **never claim simulated diagrams are real enrollments**.
- **Cloud:** free tiers are not guaranteed to remain free. Set budgets/alerts and explicit teardown; never rely on a budget alert to automatically stop charges.

```text
Physical computer (hypervisor)
   |
   +-- Isolated NAT / host-only virtual network
       +-- ubuntu-admin-01 (month 1)
       +-- linux-managed-02 (month 4+)
       +-- win-client-01 (optional)
       +-- win-dc-01 (optional, evaluation/licensed)
```

## Minimum documented manifest
Host architecture, RAM, disk, hypervisor/version, each VM OS/kernel/release, network mode, snapshots, tools installed, resource estimates and rollback steps.

## Safety requirements
- No enterprise or employer network connections; no unauthorized scanning, credential testing or monitoring.
- No public SSH/RDP, port forwarding, unprotected cloud VMs or insecure “tutorial defaults.”
- Snapshot before each destructive experiment. Keep backup data synthetic.
- Never publish personal IP addresses, access keys, credentials, enrollment tokens, customers or proprietary screenshots.
- Explicitly distinguish a reproducible simulation from real operations.

## Rebuild/recovery checklist
From a fresh image: install, configure secure access, recreate the fault, run diagnostic commands, demonstrate root cause, fix it, reboot and verify expected state. Record exact commands and versions. Remove lab resources safely afterward.

## Upgrades
1. One Linux VM + shell.
2. Two Linux VMs + Ansible.
3. Optional Windows/AD/PowerShell or legitimate managed Apple device.
4. Networking topologies with Packet Tracer/virtual routers.
5. One cloud provider only when local competence and target roles justify it.
