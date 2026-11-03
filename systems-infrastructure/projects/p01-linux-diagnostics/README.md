# P01 — Linux System Diagnostics (read-only starter)

**Status: source authored; passed a narrow assistant-side isolated-Linux smoke test; NOT yet validated in the owner's Linux lab.** This is an original Bash starter for learning, not an enterprise monitoring/remote-management agent.

## Problem
A support engineer needs immediate, **non-invasive**, local observations for a Linux performance or service problem. The wrong action (e.g., blindly restarting a process) can erase evidence and mask root cause.

## Tool
[diagnose.sh](diagnose.sh) prints:
- UTC time and kernel/architecture
- uptime and load
- current memory use
- mounted filesystem capacity
- leading CPU-consuming processes (process names can be sensitive)
- aggregate socket statistics

It uses Linux/GNU commands found on many distributions; some commands may not be installed. Missing dependencies and nonzero command exits are visible, and cause a nonzero script exit. It accepts only `--help` and does not read files beyond what invoked system utilities naturally inspect. **It does not collect or write diagnostics to a file, open network connections, modify settings, require sudo, or install tools.** However, system diagnostics can reveal machine/user/process information; inspect and redact before sharing output.

## Usage — isolated personal VM only
```bash
bash diagnose.sh --help
bash -n diagnose.sh
bash diagnose.sh
```
Review the code before running. Do **not** run it on employer devices without authorization. Logs/outputs should not be committed unredacted.

## What the observations do NOT tell you
- Load average is not equal to CPU utilization.
- High resident memory alone does not prove a leak.
- Free disk space is not the same as inode availability, quotas or underlying latency.
- Socket counts do not prove application health.
- The highest instantaneous CPU consumer need not be root cause.
- A single snapshot does not establish a trend or service-level objective.

## Initial narrow smoke evidence
A separate isolated Linux container executed a reproduced copy of the script: Bash syntax passed, help printed, invalid-argument exit was 2, and read-only output completed with exit code 0 and zero section warnings. [Evidence and limitations](EVIDENCE.md). This is **not independent validation and not a test on the owner's machine**. CI has been configured, but its successful execution is not claimed here.

## Planned owner-lab validation (not yet executed)
1. Run `bash -n diagnose.sh` and `shellcheck diagnose.sh` when installed.
2. Compare each printed section with direct source commands.
3. Run as non-root in Ubuntu Server and at least one other Linux version, logging exact versions.
4. Temporarily hide `ss` or `free` using a restricted test PATH and verify clear missing-tool failures.
5. Use a disposable virtual disk to reproduce a low-space condition without modifying the physical host disk.
6. Redact any machine/process identifiers in the final evidence.
7. Add Bats-core tests for success and failure behavior; capture an actual test transcript.
8. Publish an original incident report using the [template](../../templates/incident-report.md) and update [progress](../../PROGRESS.md).

## Next milestones
- Structured JSON output with explicit opt-in, schema and tests.
- Cross-platform Windows equivalent in P05 with PowerShell.
- Sampling and alerting only after proving reliable, bounded and privacy-conscious operation.

## Recruiter interpretation
This starter shows the intended design and initial source only. There is **no claim** of production use, complete tests or a benchmark result.