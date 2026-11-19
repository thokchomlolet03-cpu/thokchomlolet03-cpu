# Mastery assessment, cases and research

[← MIS home](README.md) · [Curriculum](CURRICULUM.md) · [Progress](PROGRESS.md)

## Baseline diagnostic
Do closed book and without AI; maximum 150 minutes. 10 points per item, score each on correctness 6, reasoning 3, caveat 1. Do tasks on synthetic data. Record time and missed concepts.
1. Define MIS vs IT vs decision support; map input/processing/output/control and people in a hospital appointment system.
2. Given a 20-minute appointment queue and repeated missing records, identify stakeholder requirements and draw as-is/to-be flow.
3. Draw ERD for customers, orders, items and payments with keys and constraints; explain 3NF.
4. Create tables, insert sample rows and query total revenue per month including zero-order customers. Explain NULL and join cardinality.
5. Write a Python function with tests to validate and group records; explain error cases and Git workflow.
6. Trace browser-to-API request from DNS through TLS, application, database and response; locate likely failures.
7. Compare synchronous API vs queue for unreliable downstream service; describe duplicate processing prevention.
8. Evaluate two fictional software alternatives (A: $10k upfront + $2k/year, B: $4k upfront + $4k/year; 3 years); compute undiscounted total and discuss risk.
9. Explain why correlation between overtime and errors cannot establish causation; propose measurement and comparison.
10. Design a permission model, backup/restore check and two metrics for a small service; discuss privacy.

90+ overall with >=8/10 each prerequisite and independent CRUD lab pass: skip only corresponding foundation units. 70–89: remediate specific gaps; below 70: complete foundations. Retest with altered scenarios after 2 weeks. Familiarity is not proof.

## Module assessment (100)
- 30 timed closed-book conceptual/quantitative exam (correctness plus reasoning).
- 35 hands-on lab (reproducible 10, correctness 15, adverse cases 10).
- 20 written case memo (alternatives 8, evidence and uncertainty 8, clarity 4).
- 15 oral defense/teach-back (mechanism 6, tradeoffs 6, limitations 3).
Pass mastery >=90 with no component below 75% and all security/privacy/correctness gates met; otherwise remediate and retest different problems. Repeat delayed recall at 2 and 6 weeks; target >=85. Scores self-assessed unless independently reviewed, not official grades.

## Original final-exam bank (start here, extend with new cases)
Each module: 40-minute problem set + 20-minute written case + live lab/defense.
- 8210: payroll errors despite automated approvals. Separate root causes from requirements; BPMN exception flow; choose buy/build with testable acceptance and change plan.
- 8310: site resolves DNS but HTTPS fails from one subnet; design diagnostic sequence, explain network evidence, prove recovery. Compare 99.9% vs 99.99% monthly availability using 30 days.
- 8410: normalized order schema; write top-three product query per region, explain execution plan, demonstrate lost-update prevention and design constraints.
- 8380: event bus duplicates messages during outage; design idempotency and replay; justify consistency/service boundaries, recovery and cost.
- 8420: three-year ERP options including retain legacy; calculate TCO and NPV using explicitly chosen discount rate, propose outcome measures and risk ownership.
- 8306: recover deleted records from backup to separate instance without corrupting originals; report RPO/RTO and test evidence.
- 8016: two dashboards disagree on revenue; reconcile grain, time zones, returns, joins, permissions and uncertainty; demonstrate reproducible metrics.
- 8450: select storage for transactional payments vs event analytics; compare two workflows; handle late or duplicate events.
- Research: proposed AI improves analyst throughput; define construct and outcomes, confounders, baselines, adverse effects, credible method and limitations.

## Capstone
Build a simulated enterprise decision-support and operations information system (sector-neutral synthetic organization). Integrate ticketing, staffing, operational events, role-based access, relational warehouse, tested APIs and an optional event stream. Study a falsifiable question such as whether a decision-support workflow improves accuracy or time under controlled synthetic workloads, relative to a deterministic baseline. Scope down to one workflow if necessary; no real employer data or human-subject experimentation without appropriate approval. A simulation cannot establish real-world organizational effect.

Predefine success metrics, workloads, assumptions, sample sizes or repeat counts, failure conditions, and analysis before experiments. Include a non-AI baseline if evaluating AI. Report null or negative findings, uncertainty, compute cost, and limitations.

Rubric: problem/business value 10; literature and theory 10; requirements/process 10; architecture and data model 15; reproducible implementation/tests 15; security/privacy/reliability 10; design/analysis and evidence 15; paper and limitations 10; defense 5. Target >=90 and mandatory safe data handling. Outputs: design report, repository code and synthetic generator, run instructions, tests, results, paper (suggested 6–10 pages), 10-minute defense slides. Publication is optional and not guaranteed.

## Study evidence template
Date | Module | source and unit | independent question | hypothesis/prediction | artifact/command | observed result | mistake and correction | score | retest date. Preserve failed hypotheses as learning. Keep personal scores and sensitive notes local if desired; do not post private admissions documents.
