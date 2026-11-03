# Detailed first 12 weeks: a working schedule

**Assumption:** 8–10 weekly focused hours and an isolated Linux VM. Lab-first; don't memorize commands without a falsifiable expectation. Allocate 60% doing, 25% reading, 15% documenting/reviewing. Use a lower pace during exhausting shifts without treating that as failure.

| Week | Reading / course modules | Hands-on deliverable | How you prove it |
|---|---|---|---|
| 1 | LFS101 basics; MIT Missing Semester shell | Install Linux VM, snapshot, inventory | Fresh rebuild notes, `uname`, `lsblk`, `ss` |
| 2 | Files, permissions, users/groups | Ownership/ACL/permission fault lab | Before/after evidence, lowest permission fix |
| 3 | Processes, services and logs | Failed systemd service diagnosis | Hypotheses + `journalctl` + repeatable repair |
| 4 | Network interfaces, DNS, TCP | Isolated DNS misconfiguration | Distinguish DNS failure from routing/port failure |
| 5 | Bash manual: quoting, redirection, exit codes | Improve P01 with safe error handling | Script run and real tests |
| 6 | PowerShell basics and object pipeline | Windows services/process inventory | Structured output and explain objects vs text |
| 7 | OSTEP process virtualization chapters | Compare CPU-bound and I/O-bound behaviors | Measured process timing/CPU state |
| 8 | OSTEP memory virtualization | Inspect RSS, faults, swap | VM-safe bounded experiment and explanation |
| 9 | Disk, mounts, ext4/XFS and journaling | Disposable disk and filesystem lab | Recover a safe mount mistake; persistence |
| 10 | Network traces / Wireshark | TCP + DNS packet inspection | Redacted traces, command-to-packet explanation |
| 11 | Git workflows; tests, ShellCheck, Pester intro | Unit-test a diagnostic script | Reproducible test output, failure-path check |
| 12 | Review and first mini-capstone | Repair unknown fault from snapshot | 10-minute walkthrough, case study and accurate limitations |

## Weekly allocation
- **Session A (90 min):** Read just enough to predict what you will observe; sketch model.
- **Session B (90 min):** Build/reproduce/fix in lab without copy-pasting answers.
- **Session C (90 min):** Investigate one misleading symptom or competing hypothesis.
- **Sessions D/E (45 min each):** Short book/doc study and review.
- **Session F (60–90 min):** Write evidence, add code/tests and explain it as if to a colleague.

## Checkpoint questions (every fourth week)
- Could I recover the lab from a fresh VM without screenshots or tutorials?
- Did I learn a causal mechanism or only remember a command?
- Can I distinguish three plausible causes of the same symptom?
- Does my automation show its failures and operate on least privilege?
- Is the published result real and reproducible rather than AI-generated prose?

## When changing plans
If MD-102/Intune job interviews rise, increase Windows/PowerShell in weeks 6–12. If Linux/sysadmin hiring rises, prioritize RHCSA-style timed labs. Keep Linux and networking shared fundamentals either way.

## Monthly reflection (copy into PROGRESS)
Time actually studied; working artifacts; failed attempts; blind spots; changes in job requirements; spent money vs acquired skill; next month's one primary deliverable.
