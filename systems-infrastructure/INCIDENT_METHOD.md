# The failure-investigation method

**The purpose of incident work is not to find a command that appears to help. It is to identify the mechanism responsible and validate a safe correction.**

## Seven-step method
1. **Scope** — when did the problem start, which services/users are affected, what changed, what is the impact and safety boundary?
2. **Establish baseline** — OS/version, service state, logs, metrics, dependency and network topology, compared to known good.
3. **Generate competing hypotheses** — list at least three plausible causes, predicted signals and discriminating tests.
4. **Choose minimally invasive tests** — read-only first; capture timestamped evidence and errors; avoid premature restarts that destroy signals.
5. **Identify root cause** — distinguish symptom, trigger, contributing conditions and underlying mechanism; mark uncertainty honestly.
6. **Mitigate and recover** — apply the smallest reversible change, document approvals/permissions, observe expected behavior, validate after reboot or repeat request.
7. **Prevent recurrence** — monitoring, automation with safe rollout, tested backups, runbook, post-incident change and remaining risk.

## Example: “web application is slow”
Possible explanations: CPU saturation, memory reclaim, disk latency, DNS retries, TCP retransmissions, TLS errors, database dependency or lock contention. Do not equate all slowness with “RAM is low.”

Write: hypothesis → expected evidence → safe command → observation → update confidence. If an experiment falsifies the current favorite, update the explanation. Maintain time synchronization; it affects correlation across logs.

## What to publish
An incident case-study with synthetic or owned lab data only; anonymized timelines, command examples and a runbook. Never reveal real employer topology, secrets, customer logs, identity data or confidential incident details.

Use [incident report template](templates/incident-report.md), and link final evidence under the appropriate project.