# [Project ID] — [Meaningful system or incident problem]

**Status:** Planned / Started / Demonstrated in lab / Independently reviewed  
**Date:** YYYY-MM-DD  
**Platform:** OS, CPU architecture, tool versions  
**Scope and security:** What may safely be changed; what is excluded

## For a hiring manager — 90-second overview
**Problem:** What went wrong or needed to be automated?  
**Solution:** What mechanism or decision process did I implement?  
**Evidence:** Link to a specific real test, output, or incident investigation.  
**Limitations:** What's untested, simulated or unsupported?

## Architecture
Text diagram or original graphical diagram. Explain control plane, dependencies and failure boundaries.

## Prerequisites and cost
Hardware, VM/OS, disk/RAM, licensing, accounts, cloud cost, setup estimate and reproducible versions.

## Reproduction
1. Start from clean, isolated environment.
2. Configure lab with documented steps.
3. Run safe baseline commands.
4. Inject an explicitly authorized reversible fault.
5. Diagnose using observable tests.
6. Apply reversible correction.
7. Verify expected state across reboot / repeated deployment.
8. Remove and confirm cleanup.

## Expected vs measured
| Experiment | Prediction | Observed | Evidence path | Pass/fail |
|---|---|---|---|---|
| | | | | |

## Automated tests / CI
Include exact commands, results, limitations and which environments were actually tested.

## Engineering decisions
Alternatives considered, why this approach, privacy and least privilege, failure behavior, observability, rollback and maintainability.

## Lessons / next experiments
What changed your mind? What still needs validation?

## Authenticity
This is an independent personal lab using synthetic/public data unless otherwise marked. No claims of production deployment without verifiable and authorized context.
