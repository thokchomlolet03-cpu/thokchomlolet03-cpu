# Sequence and weekly syllabus

[← MIS home](README.md) · [Resources by module](RESOURCES.md) · [Assessment](ASSESSMENT.md)

Independent expanded syllabus, not UNO's private weekly syllabus. Week ranges are active study weeks, not rigid calendar dates. Each semicolon-separated numbered theme is a week. Read the primary resource and complete its relevant exercises, not every optional class.

## 0 — Fundamentals readiness (weeks 1–2, 30h)
- W1: systems, business value, information quality, Python/Git/tests and technical writing.
- W2: web request lifecycle, API/authentication, SQL joins, ER models and normalization; probability/algebra diagnostic.
- Gate: independently build a small CRUD application with relational constraints and tests; explain HTTP, Git, SQL and a business metric. Remediate only failed areas via R0 and linked hub tracks.

## 1 — ISQA 8210 Systems analysis and design (weeks 3–10, 120h)
- W3: stakeholders, system boundary, objectives, information flows and problem framing.
- W4: interviews, functional/nonfunctional requirements, acceptance criteria, traceability.
- W5: as-is/to-be process, BPMN gateways, bottlenecks, cycle time, process controls.
- W6: feasibility, make/buy, cost-benefit, agile versus waterfall and scope risk.
- W7: UML use case/class/sequence diagrams, logical architecture, data models.
- W8: interface contracts, accessibility, prototype, human-centered design.
- W9: SDLC, estimation, backlog, testing, deployment and change management.
- W10: integrated design defense and timed case.
- Deliverable: requirements traceability matrix, BPMN models, UML, architecture, tested prototype, economic justification.
- Primary R1. Mastery: independently turn ambiguous objectives into testable requirements and compare two designs.

## 2 — ISQA 8310 IT infrastructure and cloud (weeks 11–18, 120h)
- W11: CPU, memory, storage, processes, virtualization and OS abstractions.
- W12: TCP/IP, subnetting, switching, routing and DNS.
- W13: HTTP/TLS, network segmentation, firewalls and packet diagnostics.
- W14: identity, RBAC, least privilege, endpoint security.
- W15: virtual networks, VMs, containers, storage and cloud shared responsibility.
- W16: automation/IaC, configuration, reproducible environments.
- W17: monitoring, incident response, SLOs, backup/restore, capacity.
- W18: fault injection, cost/availability trade-offs and exam.
- Deliverable: a local lab with network diagram, measured service latency, reproducible configuration and witnessed restore. Reuse existing systems workbench only after independent demonstration.
- Primary R2. Mastery: trace a request across layers and diagnose an unfamiliar outage.

## 3 — ISQA 8410 Data management (weeks 19–28, 150h)
- W19: conceptual/logical/physical modeling, entities, keys and constraints.
- W20: relational algebra and SQL semantics.
- W21: dependencies, anomalies, normalization to 3NF/BCNF.
- W22: joins, subqueries, windows, aggregates and NULL semantics.
- W23: storage pages, indexes, B-trees and hashing.
- W24: EXPLAIN, query plans and cost/optimization.
- W25: ACID, isolation, locking, MVCC and deadlocks.
- W26: recovery, logging, permissions and data integrity.
- W27: warehouse/OLTP boundaries, quality, stewardship, lineage and privacy.
- W28: practical + written exam.
- Deliverable: generate up to one million synthetic rows; constraints, migration, reproducible queries, performance before/after, concurrent transaction tests. Scale to available hardware.
- Primary R3. Mastery: explain why queries and transactions behave as measured; no unqualified speed claims.

## 4 — ISQA 8380 Enterprise architecture and integration (weeks 29–38, 150h)
- W29: business capability maps, architecture viewpoints and trade-offs.
- W30: ERP/CRM/HRIS and process integration; data ownership.
- W31: REST/SOAP, contracts, schema versioning and API gateways.
- W32: messaging, queues, pub/sub, idempotency and replay.
- W33: distributed systems failure modes, replication, consistency and partitions.
- W34: monolith vs services, containers and orchestration fundamentals.
- W35: IAM, network boundaries, threat modeling, security controls.
- W36: availability, SLOs, observability, retry/backoff, disaster recovery.
- W37: cost model, scaling, capacity and migration plan.
- W38: failure drills, architecture decision record, case defense.
- Deliverable: two services, queue, database, duplicate delivery test, failure recovery and measured SLOs; compare monolith with distributed alternative.
- Primary R4. MIT distributed systems papers/labs are selected extensions, not compulsory full systems programming course.

## 5 — ISQA 8420 IS management and strategy (weeks 39–46, 120h)
- W39: IS theories, sociotechnical systems, organizational structure and value.
- W40: competitive advantage, capabilities, strategy alignment and digital business.
- W41: process management, change adoption, ERP selection and stakeholder incentives.
- W42: IT investment, NPV/TCO, uncertainty, sensitivity analysis and opportunity cost.
- W43: governance, decision rights, sourcing, service management, KPIs.
- W44: cyber risk, privacy, ethics, controls and business continuity.
- W45: digital transformation, innovation, AI governance and evaluation.
- W46: executive case memo and oral defense.
- Deliverable: three alternatives including do-nothing, cost and risk register, benefits metrics, financial model with assumptions, rollout and evaluation plan.
- Primary R5. Mastery: quantify and defend technology choices from both business and technical perspectives.

## 6 — ISQA 8306 Database administration (weeks 47–52, 90h)
- W47: deployment and configuration; roles and least privilege.
- W48: monitoring, slow queries, storage and vacuum.
- W49: backup strategy, recovery point/time goals, restore verification.
- W50: replication, failover, availability and operational risks.
- W51: capacity, migrations, version upgrades and runbooks.
- W52: timed incident recovery and DBA exam.
- Deliverable: restore into a separate database, report measured recovery time/data loss, observe performance and document maintenance. Primary R6.

## 7 — ISQA 8016 Business intelligence (weeks 53–58, 90h)
- W53: decision questions, KPI definitions, data quality and sampling.
- W54: dimensional modeling, fact grain, dimensions and star schemas.
- W55: ETL/ELT, pipeline tests, lineage and incremental loads.
- W56: descriptive statistics, visual design, uncertainty and dashboard UX.
- W57: semantic models, DAX or equivalent SQL metrics, access controls.
- W58: stakeholder presentation and timed analytics case.
- Deliverable: reproducible warehouse and dashboard, reconciled metrics and decision memo; explain missingness and misleading chart risk. Primary R7.

## 8 — ISQA 8450 NoSQL/big data (weeks 59–64, 90h)
- W59: document/key-value/graph/relational trade-offs; query patterns.
- W60: MongoDB model and index experiments.
- W61: partitioning, replication, consistency and workload design.
- W62: distributed batch processing, Spark DataFrames and SQL.
- W63: streaming, windows, late events, replay and deduplication.
- W64: comparative benchmark and exam.
- Deliverable: identical synthetic workload in SQL and document store, Spark local aggregation, failure test; compare costs/latency/correctness without cherry-picking. Primary R8.

## 9 — IS research methods and quantitative analysis (weeks 65–70, 90h)
- W65: IS theories, research question, construct, literature search and critical synthesis.
- W66: probability, distributions, sampling, uncertainty and measurement reliability.
- W67: inference, effect size, confidence intervals and power.
- W68: regression, confounding, causal diagrams and limits of observational data.
- W69: experiment/quasi-experiment, qualitative interviews/coding, design science and mixed methods.
- W70: reproducibility, ethics, preregistration and proposal defense.
- Deliverable: literature matrix (10 relevant studies), reproducible analysis and planned method. No human-subject collection without appropriate approval. Primary R9.

## 10 — Independent research/capstone (weeks 71–82, 180h)
- W71: scope/refined question; W72: literature review; W73: requirements and experiment protocol; W74: data generator and reproducibility; W75–76: baseline implementation and tests; W77–78: comparison and fault/robustness studies; W79: analysis and uncertainty; W80: paper; W81: adversarial review and revision; W82: oral defense and archived reproducibility package.
- See [capstone rubric](ASSESSMENT.md#capstone). R10 is optional paper/experiment enrichment.
- Buffer (8 weeks): delayed closed-book retests, unresolved weak areas, applications and exam logistics; separate GRE/language study from MIS mastery hours.
