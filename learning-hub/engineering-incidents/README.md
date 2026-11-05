# Engineering incident library — learn from real failures

[← Learning Hub](../README.md) · [Systems Engineering portfolio](../../systems-infrastructure/README.md) · [NotebookLM technical deep dives](../notebooklm/INDEX.md)

A curated one-click library of first-party incident reports, postmortems and engineering deep dives. **Sources are the companies' own published accounts**, not proof that their system design is universally correct. Reports can be incomplete; actively test alternative explanations.

**[Why this belongs in the lifelong learning system](../LEARNING_PHILOSOPHY.md):** studying how expert organizations solve production problems is a continuing practice. Read a primary account, test competing mechanisms, and connect a safe experiment to the [systems labs](../../systems-infrastructure/PROJECT_BACKLOG.md) or discuss insights with people at [events](../participation/README.md).

**Purpose:** build causal understanding of operating systems, DNS/BGP/TCP, dependencies, scaling, monitoring, recovery, automation and human response. These are the skills a Systems Engineer needs when unexpected infrastructure problems appear.

## Live source libraries — bookmark these, not individual search results

| Engineering organization | Open the official publication | Strong areas | How to use it |
|---|---|---|---|
| **Cloudflare** | **[Cloudflare Post Mortems](https://blog.cloudflare.com/tag/post-mortem/)** | DNS, BGP, routing, infrastructure incidents, config rollouts | Best starting point for concrete network root causes |
| **Netflix** | **[Netflix Technology Blog](https://netflixtechblog.com/)** | Linux/CPU behavior, observability, containers, distributed operations | Read design trade-offs and operational mechanisms |
| **GitHub** | **[GitHub Availability Reports](https://github.blog/tag/github-availability-report/)** | Infrastructure reliability, database/load balancer issues, incident follow-ups | Compare customer impact with technical cause |
| **Spotify** | **[Spotify Engineering](https://engineering.atspotify.com/)** | Infrastructure, capacity, observability, queues and reliability | Trace a failure across services and recovery steps |
| **Google SRE** | **[Incident Response Case Studies](https://sre.google/workbook/incident-response/)** | Incident command, remediation, communications, recovery and postmortems | Learn the engineering and human operating model |
| **Discord** | **[Discord Engineering & Developers posts](https://discord.com/blog)** | Real-time systems, scale, latency and production engineering | Filter for Engineering & Developers |
| **AWS** | **[2012 AWS US-East Service Event](https://aws.amazon.com/message/67457//)** | Data-center power, multi-AZ dependencies, resiliency | Historical case: observe physical faults and failure domains |

These are publication feeds, not a guarantee that every new post is an incident report. Read originals. Do not copy full third-party articles into GitHub or NotebookLM without respecting site/source terms.

## Start with these real investigations

| Suggested order | Report to read | Systems question | Linked personal exercise |
|---|---|---|---|
| 1 | [Cloudflare — June 12, 2025 service outage](https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/) | How does a critical storage/config dependency cause multiple services to fail? | [P03 service fault lab](../../systems-infrastructure/projects/p03-service-failure-lab/README.md) |
| 2 | [Cloudflare — December 5, 2025 outage](https://blog.cloudflare.com/5-december-2025-outage) | How can an emergency security change create a new availability problem? | [P07 network fault atlas](../../systems-infrastructure/PROJECT_BACKLOG.md) |
| 3 | [Netflix — Mount Mayhem: modern CPUs and containers](https://netflixtechblog.com/mount-mayhem-at-netflix-scaling-containers-on-modern-cpus-f3b09b68beac) | Which CPU/OS mechanism explains unexpectedly poor container scaling? | [OS internals](../../systems-infrastructure/OPERATING_SYSTEMS.md) |
| 4 | [Netflix — Failure diagnosis with Pensive AI](https://netflixtechblog.com/making-failure-diagnosis-reliable-with-pensive-ai-6b0811a1c015) | When should diagnostics be deterministic, and how are unknown failures handled? | [P01 diagnostics](../../systems-infrastructure/projects/p01-linux-diagnostics/README.md) |
| 5 | [Netflix — Real-time service topology](https://netflixtechblog.com/from-silos-to-service-topology-why-netflix-built-a-real-time-service-map-0165ba13a7bc) | How do service maps aid root-cause investigation? | [Cloud & Reliability](../../systems-infrastructure/CLOUD_AND_RELIABILITY.md) |
| 6 | [Spotify — July 2026 podcast video incident report](https://engineering.atspotify.com/2026/7/content-ingestion-and-podcast-video-incident-report) | How do capacity limits, batch load and queue backlogs interact? | [P09 performance](../../systems-infrastructure/PROJECT_BACKLOG.md) |
| 7 | [GitHub — September 2026 availability report](https://github.blog/news-insights/company-news/github-availability-report-september-2026/) | How can retries/shared dependencies compound outages? | [P10 monitoring & incident response](../../systems-infrastructure/PROJECT_BACKLOG.md) |
| 8 | [Google SRE — Incident response case studies](https://sre.google/workbook/incident-response/) | What distinguishes ad-hoc recovery from well-run incident management? | [Incident method](../../systems-infrastructure/INCIDENT_METHOD.md) |

**Date notice:** reports are historical examples; dates above are *publication or incident context*, not a claim that these outages are ongoing.

## Read like a Systems Engineer

For every real outage write down:

1. **User-visible symptoms and blast radius.** What did users see and which services degraded?
2. **Architecture and dependencies.** Draw a small diagram (DNS, config store, database, gateway, host, cache).
3. **Timeline.** What was observed first, what changed and when was the incident declared?
4. **Trigger versus root cause.** Why was the trigger capable of causing such a large failure?
5. **Discriminating tests.** What metric/log/packet trace would help distinguish competing causes?
6. **Mitigation versus long-term fix.** Was traffic drained, configuration rolled back, caches cleared, a service restarted? What prevented recurrence?
7. **Uncertainty and alternatives.** What is not documented or still unclear?
8. **Small-scale safe experiment.** Can you test one of the mechanisms in an authorized isolated VM?

Copy the [reading note template](READING_TEMPLATE.md) for your own original analysis and add the source to [READING_QUEUE.csv](READING_QUEUE.csv). Optionally build a public [NotebookLM deep dive](../notebooklm/README.md) referencing permitted URLs. Do not represent a company's incident as something you personally resolved.

## One-hour reading ritual

- 15 minutes: read the incident *before* consulting summaries.
- 15 minutes: write your predicted mechanisms and a dependency diagram.
- 15 minutes: revisit the report and compare actual findings with your predictions.
- 15 minutes: write one question to investigate in a personal VM or textbook.

At least once a month, translate a reading note into a reproducible experiment in the [Systems Engineering project backlog](../../systems-infrastructure/PROJECT_BACKLOG.md).
