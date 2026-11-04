# Quality assurance

This portfolio keeps the difference between authored code, local tests, verified CI, completed personal labs, and employment experience explicit.

For practical projects, run syntax checks, failure-path tests, credential scanning, and reproducibility checks before marking them complete. CI status must be inspected in the GitHub Actions interface rather than assumed from a workflow file.

## Automated jobs
The workflow at [.github/workflows/systems-infrastructure-ci.yml](../.github/workflows/systems-infrastructure-ci.yml) runs P01 smoke/failure tests, P03 synthetic loopback tests, link-checker unit tests and local Markdown link target validation. **Workflow creation is not a pass**; inspect [GitHub Actions](https://github.com/thokchomlolet03-cpu/thokchomlolet03-cpu/actions) before claiming a green CI run.

External course links, credentials, lab safety, accuracy and actual systemd/enterprise environments still require human review.

## Current static audit
On 2026-11-03 a read-only check of **26 repository Markdown documents** found **69 local Markdown links** and no unresolved local targets. This was a connector-side audit, *not a successful GitHub Actions run*. The automated checker and its unit tests are committed for repeatable verification.

The first P01 error test and four P03 Python tests passed in a separate isolated Debian GNU/Linux 13 environment; [P03 evidence](projects/p03-service-failure-lab/EVIDENCE.md) gives the scope. Future CI outcomes must be checked separately.

## CI audit and remediation plan — 2026-11-04
The last examined main-branch run at [Actions run 41709552945](https://github.com/thokchomlolet03-cpu/thokchomlolet03-cpu/actions/runs/41709552945) **failed** in `linux-diagnostics`. Its ShellCheck step reported **SC2317** for an indirectly invoked process-listing function. The `service-failure-lab` and `documentation` jobs passed. The new change calls the process-listing pipeline directly so the analyzer can see it; this repair remains **unverified until an actual new CI result is observed**. It also proposes moving from checkout@v4 to checkout@v5 to avoid the deprecated runtime warning. Do not display a green CI badge before confirmation.

### Additional maintenance gates
- Read-only PowerShell source gets static parse validation on GitHub CI, but Windows CIM behavior **must** be tested in a permitted Windows environment.
- After each change, inspect the actual pull request's failing job logs; do not assume fixing one lint finding guarantees all jobs pass.
- No secrets, proprietary employer data, or actual user identity dumps in evidence artifacts.
