# P03 — initial synthetic test evidence

**Date:** 2026-11-03  
**Scope:** Assistant-controlled isolated Debian GNU/Linux 13 (trixie) container, Python 3.13.5. The code was tested as a local copy before publication. This is **not** the owner's VM, **not** a systemd runtime test and **not** production operation.

## Tests observed
Command executed: `python3 -m unittest discover -s p03/tests -v`

| Test | Observed |
|---|---|
| Missing JSON configuration | PASS — process exited 2 with CONFIG_ERROR |
| Malformed JSON configuration | PASS — process exited 2 |
| Loopback endpoint on ephemeral port | PASS — HTTP 200 and expected synthetic response |
| Same-port second process | PASS — second process exited 3 with BIND_ERROR |

**Result:** 4 tests passed locally. The tests involve only loopback networking and temporary synthetic files. GitHub Actions has been configured, but an actual successful run **has not been independently verified**.

## Still unverified
- Behavior under the user's hypervisor, Ubuntu/RHEL distributions or a constrained systemd user session
- Journal logs, unit working-directory failures, service account and permission failures
- Rollback/reboot persistence, fault-injection incident reconstruction and peer review
- Any scalability, uptime, performance, security or production readiness claims

See [the lab runbook](README.md) and [P03 owner-lab issue](https://github.com/thokchomlolet03-cpu/thokchomlolet03-cpu/issues/5). Only promote to “demonstrated in lab” after the owner captures sanitized real observations on a rebuildable VM.
