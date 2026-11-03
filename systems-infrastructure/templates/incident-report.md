# Incident: [short technical title]

**Case ID:** LAB-YYYY-NNN  
**Date / time zone:**  
**Evidence status:** Planned / Captured / Independently reproduced  
**Environment:** Isolated personal lab; synthetic data only  
**Impact:** What actually failed and what users/systems would experience  
**Safety boundary:** Which systems may be modified; snapshot and recovery plan

## 1. Initial symptom
What was observable? What changed? Which facts are directly measured and which are assumptions? Include time-synchronized evidence where possible.

## 2. Environment and baseline
OS, kernel/build, hardware/VM architecture, virtual networking, service version, baseline metrics and known-good comparison (redact sensitive identifiers).

## 3. Hypotheses
| Competing explanation | Predicted observation | Least invasive test | Result | Keep/reject |
|---|---|---|---|---|
| H1 | | | | |
| H2 | | | | |
| H3 | | | | |

## 4. Experiment and command evidence
Include exact non-secret commands, relevant error codes, timestamped outputs and interpreted meaning. Link to sanitized logs. Avoid claiming a result until actually executed.

## 5. Root cause and mechanism
What failed at the hardware/OS/process/network/application layer? Separate **trigger, contributing factors and root cause**. If uncertain, state alternatives that remain open.

## 6. Correction and validation
What was changed? Why should the fix work? Did it pass **before/after**, reboot and negative-path tests? What happened when attempting to reproduce it again?

## 7. Rollback and risks
How was the snapshot/backup verified? What could the intervention damage? What permissions or change approvals would be needed in a real enterprise?

## 8. Prevention and follow-up
Monitoring, automatic tests, patch/design improvements, open risks, next hypothesis and related project.

## 9. Authenticity declaration
Test environment: [real personal lab / simulated only / professional under permission]. Synthetic data? [yes/no]. Independently validated? [yes/no]. Never include employer/customer proprietary material.
