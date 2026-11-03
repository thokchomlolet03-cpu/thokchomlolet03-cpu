# First 30 days — from reading to evidence

**Budget:** 8–10 focused hours/week; adjust around shift work. No need to purchase a course now. Follow [lab safety](LAB_SETUP.md).

## Week 1 — Build and observe
- [ ] Install one Ubuntu Server VM matched to host CPU architecture; document hypervisor, OS release, RAM, disk and network mode.
- [ ] Isolate the VM, create an ordinary user with sudo as appropriate, use SSH keys, create a recovery snapshot.
- [ ] Inspect CPU/processes with `ps aux` and `top`; RAM with `free -h`; disks with `lsblk` / `df -h`; services with `systemctl`; logs with `journalctl`; TCP sockets with `ss -tuna`.
- [ ] Explain a process, thread, kernel, daemon, inode and system call in original words.
- [ ] Examine and safely execute [P01 read-only diagnostics](projects/p01-linux-diagnostics/README.md) on this VM.
- [ ] Read initial [MIT Missing Semester](https://missing.csail.mit.edu/2026/) and [LFS101](https://training.linuxfoundation.org/training/introduction-to-linux/) lessons.

**Proof:** environment manifest, setup and rebuild steps, sanitized outputs, explanation of observations.

## Week 2 — Find and fix a broken service
- [ ] Create a disposable failing service: missing executable/permission/config error; document injected fault.
- [ ] Before repairing, list at least three hypotheses and tests to distinguish them.
- [ ] Use `systemctl status`, `journalctl -u`, permissions and unit file inspection.
- [ ] Repair, reboot, rerun service checks; reset snapshot and reproduce.
- [ ] Write one real lab incident report using [the template](templates/incident-report.md).

**Proof:** diagnosis chain, commands/expected observations, root cause, repeatable fix.

## Week 3 — Network failure analysis
- [ ] Explain link → address → route → DNS → TCP → TLS → HTTP.
- [ ] Inspect `ip address`, `ip route`, `getent hosts`, `ss`, `curl -v` and (if available) `dig`.
- [ ] Deliberately break DNS **only in the isolated VM**. Distinguish “no DNS” from “no route,” “port closed,” and “service down.”
- [ ] Restore the snapshot and capture a sanitized decision tree.

**Proof:** network diagram, at least three fault hypotheses, elimination evidence, recovery.

## Week 4 — Improve automation
- [ ] Add safe options to P01, collect structured output without passwords or user secrets.
- [ ] Test on multiple environments or mocked command outputs, including absent commands and failures.
- [ ] Run `shellcheck` when installed; explain unresolved findings.
- [ ] Document usage, operating assumptions, cleanup and one reproducible failure case.
- [ ] Mark progress only after tests and screenshots actually exist.

**Month-1 gate:** Can I rebuild without a tutorial, isolate an unfamiliar failure and write a script that fails visibly rather than hiding errors?

### Suggested weekly rhythm
Two 90-minute lab sessions, two 45-minute reading sessions, one 60-minute documentation and review block. If time is scarce, prioritize **lab evidence over watching videos**.
