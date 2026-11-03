# Quality assurance

This portfolio keeps the difference between authored code, local tests, verified CI, completed personal labs, and employment experience explicit.

For practical projects, run syntax checks, failure-path tests, credential scanning, and reproducibility checks before marking them complete. CI status must be inspected in the GitHub Actions interface rather than assumed from a workflow file.

## Automated jobs
The workflow at [.github/workflows/systems-infrastructure-ci.yml](../.github/workflows/systems-infrastructure-ci.yml) runs P01 smoke/failure tests, P03 synthetic loopback tests, link-checker unit tests and local Markdown link target validation. **Workflow creation is not a pass**; inspect [GitHub Actions](https://github.com/thokchomlolet03-cpu/thokchomlolet03-cpu/actions) before claiming a green CI run.

External course links, credentials, lab safety, accuracy and actual systemd/enterprise environments still require human review.
