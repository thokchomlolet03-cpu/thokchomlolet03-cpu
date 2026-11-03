# P03 — Linux Service Failure and Recovery Lab

**Status:** Python service and four automated tests **executed in an assistant-side isolated Debian container**; systemd, recovery runbook, and owner's VM exercise **not yet demonstrated**. This is not production service code.

## Scenario
An internal application appears unhealthy. A support engineer must differentiate a **bad configuration**, **missing file**, **port already in use**, **systemd misconfiguration**, and **network/listener** issues without making assumptions or restarting blindly.

The toy service is intentionally constrained: **Python standard library only**, **127.0.0.1 only**, **synthetic data**, no remote APIs, no authentication, no production use, no persistence, no automated privileged modification.

## Files
- [service.py](service.py) — local HTTP health endpoint using a validated JSON configuration.
- [config.json](config.json) — a synthetic healthy config, no secrets.
- [tests/test_service.py](tests/test_service.py) — missing/malformed config, port-conflict, healthy endpoint tests.
- [p03-lab.service.example](p03-lab.service.example) — **example** user-level systemd unit requiring local path edits.

## Prerequisites
Linux VM with Python 3.9+, optionally systemd user manager, curl, journalctl, ss and ps. Use only isolated personally owned/authorized hardware. Do not connect any experiment to workplace networks.

## Exercise A — establish a baseline
In one shell:
~~~bash
cd systems-infrastructure/projects/p03-service-failure-lab
python3 service.py --config config.json --port 8765
~~~
Expected **not yet owner-observed** startup line: READY http://127.0.0.1:8765/health

In a second shell, inspect rather than assume:
~~~bash
curl --fail --silent http://127.0.0.1:8765/health
ss -lnt | grep 8765
ps -eo pid,comm,args | grep service.py
~~~
Record actual output, exit status and environment; stop server with Ctrl+C.

## Exercise B — safe controlled failures
Make a prediction *before running* each experiment:
1. **Missing config:** while no server is running, invoke with a nonexistent JSON file. Which layer rejects it? Is it an HTTP error or a process startup error?
2. **Invalid JSON:** create a disposable invalid config in a temporary location. Compare exit status and stderr to the missing-file failure.
3. **Port conflict:** start one server on 8765, then attempt another on 8765. Which command reveals the port owner? Why does a restart not solve a second service that expects the same port?
4. **Missing/executable/script path:** edit a copy of the user unit's ExecStart to a path that does not exist; observe systemd status and journal; restore it.
5. **Bad working directory or permissions:** edit the **copy** of the user unit to point to an absent directory. Predict systemd failure and explain difference from app config failure.

**Safety:** inject changes only in this disposable lab, not a machine serving real users. Restore the original unit and verify successful health afterwards.

## Exercise C — optional systemd user unit
The example unit contains placeholders. Replace each with an **absolute path** to your cloned project. On a Linux desktop/VM with a running user manager:
~~~bash
mkdir -p ~/.config/systemd/user
cp p03-lab.service.example ~/.config/systemd/user/p03-lab.service
# STOP: edit every /ABSOLUTE/PATH placeholder before continuing
systemctl --user daemon-reload
systemctl --user start p03-lab.service
systemctl --user status p03-lab.service
journalctl --user -u p03-lab.service --no-pager -n 40
curl --fail http://127.0.0.1:8765/health
systemctl --user stop p03-lab.service
~~~
Do not enable the service at boot or enable user lingering. If systemctl --user is unavailable in a headless VM, **document that limitation** rather than replacing it with an unauthorized system-level service. Only remove the copied unit if it belongs to this lab.

## [Initial synthetic test evidence](EVIDENCE.md)
Four tests passed in an assistant-side Debian environment. Actual systemd faults and the owner's own VM remain untested.

## Automated tests
~~~bash
python3 -m unittest discover -s tests -v
~~~
These tests bind only to loopback with an ephemeral port and terminate their own child processes. They do **not** verify real systemd behavior, Linux journald or complete security isolation.

## Interview-level questions
- What is the distinction between server process started, TCP socket listening, HTTP healthy and user-visible application working?
- Which failure occurred *before* a socket was created?
- Which startup failure was caused by systemd vs the application itself?
- How would you safely identify the listener when the port is occupied?
- What is the minimum evidence needed before escalating?
- How would you package this check for ten servers and avoid hard-coded secrets or mass restart?

## Prove completion with evidence
Use [incident report template](../../templates/incident-report.md). Include a clean VM manifest, one known-good baseline, each predicted/actual failure signature, the journal timeline for systemd-related cases, root-cause comparison, a successful repair, and a fresh reboot/rebuild test.

**Milestone definition:** Code+unit tests authored and tested does NOT make this a completed systemd lab. The owner must execute the procedures in an authorized VM and publish sanitized observations.
