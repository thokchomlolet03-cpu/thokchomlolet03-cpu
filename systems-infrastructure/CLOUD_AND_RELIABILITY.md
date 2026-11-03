# Infrastructure and reliability — beyond deploying a VM

## What systems roles require
Reliable delivery of OS/network/identity services, patching, backups, logging, access boundaries, cost awareness and a provable recovery path. Cloud resources are just another operating environment; do not start by treating a cloud certificate as a substitute for OS/network skills.

## Progression
1. **Virtualization:** hypervisor, guest vs host resources, virtual networks, snapshots and clean recovery.
2. **Configuration management:** Ansible desired state, controlled changes, diff/rollback, drift detection.
3. **Infrastructure as code:** Terraform graph, providers, state, locking, drift and teardown. Existing related study: [Terraform Mastery](https://github.com/thokchomlolet03-cpu/terraform-mastery).
4. **Monitoring:** system metrics, process/application metrics, logs, structured events, meaningful alerts, signal vs noise.
5. **Backups:** encryption, retention, restore testing, RPO and RTO with real measured outcomes.
6. **Access control:** IAM, MFA, short-lived credentials, security groups/firewalls, secrets, audit logs.
7. **Failure domains:** VM, zone, region, network, dependency and human configuration error.
8. **Incident response:** on-call handoff, timelines, hypotheses, safe mitigations, postmortem and preventive action.

## Avoid expensive distractions
Do not study AWS, Azure and GCP equally in year one. Choose one based on real hiring feedback. Local Linux/Windows/Ansible labs are cheaper and more transferable. Before any cloud experiment, enable billing alerts, least privilege, resource tags and a cleanup plan; **billing alerts do not cap actual spending**.

## SLO reasoning exercise
For a synthetic service, define how success is measured (e.g., correct HTTP response and latency), a target and a window. Inject a failure and measure detection/restore **in that test lab**, not as an implied production SLA.

## Reliability portfolio
P06 configuration convergence, P10 metric alert + verified restore, P11 mini-enterprise, and P12 minimal cloud/hybrid case.

References: [Google SRE book](https://sre.google/sre-book/table-of-contents/) · [SRE Workbook](https://sre.google/workbook/table-of-contents/) · [Prometheus](https://prometheus.io/docs/introduction/overview/) · [AWS Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) · [Terraform](https://developer.hashicorp.com/terraform/tutorials).
