# P01 initial smoke execution — narrow evidence

**Date:** 2026-11-03  
**Where:** an isolated Linux container controlled by the assisting environment, **not** the owner's machine.  
**Purpose:** sanity-check the authored shell script.  
**Privacy:** actual process listings, host identifiers and network details are intentionally not published.

## Commands and observed outcomes
| Command / test | Observed result |
|---|---|
| `bash -n diagnose.sh` | Syntax check passed |
| `bash diagnose.sh --help` | Help printed |
| `bash diagnose.sh --nope` | Exit status 2 |
| `bash diagnose.sh` | Exit status 0; all 7 diagnostic sections printed |
| Diagnostic warnings | 0 reported in this environment |

This verifies **only a narrow smoke path** against a reproduced copy of the committed script. No ShellCheck execution, unit-test harness result, second distribution, independent review, resource-fault simulation, permission boundary or deployment has been verified.

## What would justify saying this project is “demonstrated”?
A learner-owned VM with documented OS/kernel/architecture, unprivileged run, measured output validation, tests for missing/failing tools, lint results, controlled incident capture and repeatability after rebuild. See [P01 backlog](../../PROJECT_BACKLOG.md) and [validation issue](https://github.com/thokchomlolet03-cpu/thokchomlolet03-cpu/issues/2).

**No employer/customer system was accessed or modified.**
## Additional execution on 2026-11-03
In an isolated Debian GNU/Linux 13 container (Bash 5.2.37), the diagnostic script and a matching extended local test harness were executed. Observed checks passed for help, an invalid argument, normal read-only execution, a synthetic failing `ss` command (exit code 23) and an absent `ss` executable. The committed [failure-path test](tests/failure_cases.sh) separately passed locally. **These results do not establish performance, safety on an employer system, owner-machine compatibility, or a successful GitHub Actions run.**
