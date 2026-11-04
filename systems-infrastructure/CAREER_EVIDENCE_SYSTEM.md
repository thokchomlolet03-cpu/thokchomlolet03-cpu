# Career evidence system — role requirements to independently demonstrated skills

**Version:** November 4, 2026. This is an operating system for professional growth, not a collection of invented job vacancies, certificates or work-permit promises.

## Objective
At any time, be able to answer **three questions** with links and evidence:
1. What does the type of Systems Engineer job I want actually require?
2. Which requirements can I perform independently today, and how can a reviewer reproduce the result?
3. What specific next experiment or course most increases interview eligibility?

There are **two trackers** (see below). One tracks the labor market; the other tracks technical proof. Never confuse them.

## A. Job descriptions: [ROLE_REQUIREMENTS.csv](ROLE_REQUIREMENTS.csv)
Start with 10–15 **real, still-accessible** roles in the UAE, Ireland and Germany, in these families:
- Endpoint / Workplace Technology Engineer
- Windows / Linux Systems Administrator
- Infrastructure Operations / Systems Engineer
- Data Center Operations / Technician (hardware-focused)
- Cloud Support Engineer

Do not fabricate job titles, sponsorship, dates or salaries. Record source URL and date retrieved, distinguish `required` from `preferred`, and quote only short skill phrases under fair-use limits. Retain the underlying job link, not a copy of the posting.

### Recommended capture fields
- Country, city, employer and advertised job title
- Official job URL, posted date if explicit, date checked, vacancy status
- Required experience and education or allowed equivalent experience
- OS, network, endpoint/identity, storage/virtualization and automation requirements
- Language requirements, work authorization or explicit sponsorship policy **as actually stated**
- Must-have skills not yet proven, and a link to a fitting project
- Salary only when published by that employer or an explicitly named source
- Review date and notes about ambiguity

**Separate a job matching your skills from a job you can legally take.** Do not turn `not specified` into `sponsorship available`.

## B. Demonstrated technical competence: [EVIDENCE_MATRIX.csv](EVIDENCE_MATRIX.csv)
Every skill/project must record its exact maturity:
- **Not assessed:** no personal capability conclusion.
- **Planned:** architecture or proposed test, no practical result.
- **Source authored:** code/documentation exists, but user execution missing.
- **Assistant-side smoke test:** a narrow external tool executed code, not evidence of user skill.
- **Owner-lab demonstrated:** user independently completed and documented it on an authorized machine.
- **Reviewed/reproduced:** another reviewer or explicit CI job validated relevant behavior.
- **Professional experience:** genuinely performed at work and described without violating confidentiality.

Only record `Owner-lab demonstrated` after the user supplies the environment, method, test artifacts and failure analysis. Automated CI passes validate code, **not employment experience** or personal mastery.

## Prioritization method — every month
For each real target vacancy:
1. Identify **three main technical requirements** and which are absolute filters (e.g., German level, eligibility, driving license, university degree).
2. Compare with the evidence matrix.
3. Select one technical gap whose removal would improve multiple realistic opportunities.
4. Assign **one lab deliverable** and an exam only if necessary.
5. Reassess in four weeks. If the market favors endpoint skills, advance P04/P08; if it favors Linux operations, advance P03/P06/P13.

### Example reasoning — not a real job record
A hypothetical employer requires PowerShell, Active Directory, Windows Server, 2+ years of experience and permission to work locally. An AD lab can demonstrate technical readiness but does not solve an immigration eligibility issue. The job remains an uncertain or unsuitable opportunity unless the company states an acceptable sponsorship route.

## Recruiting evidence format
For each finished project, create a two-minute read:
- **Problem:** what failed or needed operating?
- **Architecture:** what services and dependencies exist?
- **Hypothesis and measured diagnosis:** what did you actually observe?
- **Automation/change:** code plus safety precautions and rollback.
- **Validation:** test/rebuild evidence.
- **Limitations:** versions, simulation vs production, costs and legal boundaries.

Follow [RECRUITER_PORTFOLIO.md](RECRUITER_PORTFOLIO.md). The first three supported case studies should eventually be **Windows identity**, **Linux service diagnosis**, and **virtualization/backup recovery**. Until then, mark them accurately as in progress.

## Country considerations
**UAE:** target enterprise helpdesk-to-endpoint/system administration transitions and record visa/employer constraints by vacancy.

**Ireland:** some employers hire internationally; others require existing right to work or particular citizenship. Record a vacancy's actual stated restriction, never presume sponsorship because a company is multinational.

**Germany:** language expectations can vary drastically; record exact German level and whether a technical degree or formally recognized qualification is required. Track German language study separately from technical certifications.

## Quarterly review
- Count genuinely **eligible** opportunities by role family, excluding unknown sponsorship status from confirmed-eligible counts.
- Compare required technical gaps, realistic interview likelihood, shift/on-site and earnings.
- Decide if RHCSA, MD-102, Jamf 100 or CCNA adds marginal value.
- Remove outdated links and explicitly date the next review.

**Do not let job research displace hands-on OS learning.** A useful budget is 1–2 hours/month reviewing vacancies after your weekly practical labs.
