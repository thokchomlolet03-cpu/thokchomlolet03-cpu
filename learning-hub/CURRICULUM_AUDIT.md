# Curriculum audit — reduce obligations, preserve discovery

[← Learning Hub](README.md) · [Current free-course directory](WORLD_CLASS_FREE_COURSES.md)

**Audit date:** 16 November 2026. **Scope:** the public GitHub profile repository's `learning-hub/` (42 tracked files at review), with cross-checks against `systems-infrastructure/` career roadmap, resource library and career-evidence framework. Other software projects, research evidence and private records were not edited.

## What was wrong with the former organization?

1. **Many entry points, no single decision:** the 31-entry university CSV, ~30-entry free-course list, systems resources, 12-week schedules and mathematics queue all appeared actionable at once.
2. **Duplicate fundamentals:** introductory Python, multiple general programming curricula, multiple Linux entry points, cloud platforms, maths references and German alternatives. Choice was masquerading as progress.
3. **Priorities did not match the career roadmap:** some advanced architecture, Kubernetes, MIT kernel/distributed-systems and academic-credit campaigns were labeled near-term despite a stated emphasis on Windows/Linux administration, endpoint, networking and cloud support.
4. **Deadlines mixed with life planning:** dated 2026/27 Finnish registration and ECTS possibilities could tempt a rush toward credentials unrelated to a current hiring gap.
5. **Reference vs. commitment was unclear:** scientific curiosity, quantum research, human skills and practical engineering are all valuable, but they do not need identical weekly schedules.

## Decisions and rationale

| Decision | Why | Where the valuable content remains |
|---|---|---|
| **One visible active queue** | Prioritize one lab/course, German habit, targeted mathematics and optional exploration | [Learning Hub home](README.md) |
| **Shrink 31 academic course entries to 9** | Remove duplicate beginner Python/DevOps choices, nonessential electives and date-driven enrollment targets from the active reference list; preserve IDs of survivors | [Curated university CSV](university/COURSE_CATALOG.csv) and [matched tracker](university/EVIDENCE_TRACKER.csv) |
| **Replace the 30-link "take everything" directory with a choice-based source shelf** | Preserve exceptional original teaching without requiring 30 certificates | [World-class courses](WORLD_CLASS_FREE_COURSES.md) |
| **One mathematics dependency chain** | Math is needed for specific mechanisms, not as a full Class 11–12 repeat | [Career math](mathematics/README.md) |
| **One principal German course** | DW Nicos Weg is already chosen and practiced; duplicate full A1 tracks cause avoidable switching | [German](german/README.md) |
| **Keep specialist research, remove mandatory framing** | Quantum, MIT engineering depth, biology, entrepreneurship and visual thinking are exploratory, not necessary for an IT support role | [Quantum](quantum/README.md), [University](university/README.md), [Human skills](personal-skills/README.md) |
| **Archive instead of pretending time-sensitive research is current** | Preserve past source research and links while making clear it is not current enrollment guidance | [Finnish credit research](university/FINNISH_CREDIT_OPPORTUNITIES.md), [retired sequence](university/SIX_MONTH_SEQUENCE.md) |

### Courses removed from the *active academic register*

Original IDs removed: **U001, U002, U004, U005, U006, U007, U008, U011, U012, U013, U016, U017, U018, U019, U020, U023, U024, U025, U026, U027, U030, U031.**

These were **all listed as not started** in the academic tracker at audit time; no earned university credits or evidence records were discarded. This is **not** a judgment that the institutions or subjects are mediocre. Some remain available in subject-specific references or original provider sites; they simply do not belong in an actionable core curriculum.

**Retained IDs:** U003, U009, U010, U014, U015, U021, U022, U028, U029. Most retained entries are optional, with one or two useful immediately if a genuine gap exists.

## What the restructure deliberately did not do

- It did **not** erase personal research projects, existing experiment designs, GitHub issues, evidence logs, the long German-learning essay, the quantum experiment plan or the systems portfolio.
- It did **not** claim that completing a course earns CCNA/RHCSA, university admission, ECTS, a job or professional experience.
- It did **not** promise that course prices, registration windows or curricula never change.
- It did **not** narrow curiosity to IT: the [discovery shelf](WORLD_CLASS_FREE_COURSES.md#3-discovery-shelf-not-a-checklist) explicitly invites science, biology, finance, food systems, physical engineering and entrepreneurship.

## Quarterly maintenance rubric

For each resource, record the intended skill, direct official URL, access terms and a practical exit test. Then ask:

1. What currently unsolved problem or job qualification does this resource address?
2. Does a stronger original-source course already teach the same thing?
3. Is it actually fully free, or are labs, access, exams or verified certificates paid?
4. Will this be practiced, or is it simply an interesting reference? Label that honestly.
5. Is it time-sensitive, and has the claimed enrollment/credential status been checked this term?

If no skill gap or concrete curiosity supports an entry, **remove it from the active queue**. Keep historically interesting research in reference pages or Git history rather than treating all ideas as failed commitments.
