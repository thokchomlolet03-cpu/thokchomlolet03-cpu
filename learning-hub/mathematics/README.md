# Mathematics — foundations, applications and open-ended discovery

[← Learning Hub](../README.md) · [World-class free courses](../WORLD_CLASS_FREE_COURSES.md) · [Computer foundations](../university/COMPUTER_FOUNDATIONS.md)

**Updated: 16 November 2026.** A welcoming, problem-driven entrance to mathematics: repair Grade 11–12 foundations where helpful and freely explore the larger landscape beyond what any job requires. It assumes roughly comfortable arithmetic and Grade 10 material, but potentially missing links in higher-school algebra and functions. Start with diagnostic exercises, not an age-based label.

> **Method:** *intuition → worked derivation → independent exercises → practical application → explain from memory*. A beautiful video develops intuition, but mastery also requires problems solved without hints.

## What mathematics is actually worth learning?

| Order | Topic | Depth needed | Direct career / research use |
|---|---|---|---|
| 0 | Arithmetic, ratios, percentages, scientific notation and units | Fluency; review only if stuck | Cloud bills, bandwidth, capacity, exchange rates, finance |
| 1 | **Algebra and functions**: equations, inequalities, graphs, exponentials, logarithms, systems | **Essential foundation** | Growth, algorithms, performance graphs, model outputs, interest |
| 2 | **Discrete mathematics**: binary, hexadecimal, powers of two, Boolean logic, sets, modular arithmetic, basic graphs | **Essential for infrastructure** | CIDR/subnetting, addressing, permissions, logic, dependency networks |
| 3 | **Statistics and probability**: averages, variability, conditional probability, Bayes, sampling, confidence intervals and hypothesis testing | **Essential for evidence-based work** | Incident rates, A/B tests, model evaluation, data science, Kaggle |
| 4 | **Linear algebra**: vectors, dot products, matrices, transformations, projections, eigenvector intuition | **Important for AI** | Embeddings, least squares, ranking and models |
| 5 | **Calculus essentials**: limits, derivatives, rates of change, integrals, gradients | **Important for deeper AI/science** | Optimization, learning curves, continuous physical models |
| 6 | **Financial mathematics**: compound growth, inflation, discounting, NPV, risk and expected value | **Practical essential** | Savings/investing, startup unit economics, valuations |
| Optional | Trigonometry, differential equations, numerical methods, optimization | Only when a project demands them | Engineering simulation, physics, scientific ML, quantum |

You need not wait for every later topic to learn networking, cloud administration or programming. For those fields, algebra, units and discrete math already unlock most everyday calculations.

## Stage 0 — Diagnose and patch gaps (selectively)

**Source:** [Khan Academy — Get ready for Algebra 2](https://www.khanacademy.org/math/get-ready-for-algebra-ii) or [Khan Academy — Algebra 2](https://www.khanacademy.org/math/algebra2). Use the course challenge and unit tests, then study **only** weak units: equations, functions, polynomials, exponentials, logarithms and needed trigonometry. Use [OpenStax College Algebra / Precalculus](https://openstax.org/subjects/math) when you need a careful textbook explanation.

**Exit checks (without a calculator first, then verify):**
- Rearrange `C = n × p` to solve for `n`; explain why units matter.
- Plot what `y = 2^x` means and reverse it with a logarithm.
- Solve two linear equations and explain the crossing point.
- Describe how a 20% increase followed by a 20% decrease affects an original value (it does not return to the original).

## Stage 1 — Discrete math for actual computer systems

**Start with concrete problems:** convert 42 between decimal and binary; explain why a `/27` IPv4 network contains 32 total addresses; simulate permission rules with AND/OR/NOT; trace a dependency graph and a shortest path.

**Primary sources:**
- [Cisco Networking Academy](https://www.netacad.com/) and [Packet Tracer](https://www.netacad.com/cisco-packet-tracer) for real subnetting and packet-flow exercises.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) for proof, sets, relations, graph theory, counting and probability (**select chapters**, not every assignment).

**Prerequisite warning:** MIT 6.042J formally assumes some single-variable calculus. Start with accessible early topics and return to its harder proofs/probability after Stage 4; do not treat the full MIT course as beginner material.

**Evidence project:** Plan a small multi-subnet lab and justify every subnet address range; independently explain a least-privilege Boolean policy.

## Stage 2 — Statistics and probability for evidence

**Start with:** [Khan Academy — Statistics and probability](https://www.khanacademy.org/math/statistics-probability). Cover distributions, conditional probability, random variables, sampling, confidence intervals, and the difference between association and causation. Then move to [MIT 18.05 — Introduction to Probability and Statistics](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/) for depth.

**Later, not first:** [Harvard — Statistics 110: Probability](https://stat110.hsites.harvard.edu/). It is excellent but assumes calculus and matrix familiarity, so defer until those foundations are comfortable.

**Evidence project:** Analyze a small open dataset. Compare means vs medians, document missing data, compute a confidence interval, and explain what the sample **cannot** establish. Apply calibration and class imbalance reasoning to model evaluation.

## Stage 3 — Linear algebra for machine learning

**Intuition first:** [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) (visual explanation). **Then real exercises:** [MIT 18.06SC — Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) (self-study course). The videos **do not substitute** for independently computing matrix operations and solving systems.

**Must understand:** vectors, norms and similarity; dot products; matrix multiplication; solving linear systems; projections; eigenvectors at conceptual level.

**Evidence project:** Calculate vector similarities on paper and in a notebook, and explain why embedding similarity can be misleading for uncertain classes.

## Stage 4 — Calculus, only to required depth

**Start:** [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/lessons/essence-of-calculus/) to see why limits, derivatives and integrals exist. **Practice and depth:** [MIT 18.01SC — Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) or [Khan Academy Calculus 1](https://www.khanacademy.org/math/calculus-1).

**Learn first:** function limits; slopes and derivatives; derivatives of powers/exponentials/logs; optimization of a one-variable function; integration as accumulation. For AI, add the meaning of partial derivatives and gradients, not advanced proofs initially.

**Evidence project:** Build a simple gradient-descent example, plot the loss function, predict each step and identify where optimization fails.

**Optional next steps:** MIT multivariable calculus, differential equations and numerical optimization only if a specific physics, simulation or research project requires them.

## Stage 5 — Financial math for practical decisions

Use [Khan Academy — Finance and capital markets](https://www.khanacademy.org/economics-finance-domain/core-finance) for core ideas, then [NYU Stern — Aswath Damodaran, Corporate Finance / Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/onlineclass.htm) for serious business reasoning.

Understand percentages vs percentage points, compounding, annualized returns, inflation, discount factors, NPV and expected value. Do not confuse nominal profits with risk-adjusted returns.

**Evidence project:** Compare two savings/investment scenarios with transparent contribution amounts and assumptions, then stress-test lower returns and higher inflation. Do not present hypothetical market returns as forecasts.

## A light, sustainable study sequence

**Use checkpoints rather than arbitrary deadlines**—progress can be faster on familiar material and slower where conceptual gaps exist.

1. **Check algebra.** Work a Khan course challenge; redo only weak units and explain exponential/logarithmic models.
2. **Study one real networking question.** Use binary, powers of two and CIDR with a Packet Tracer lab.
3. **Learn statistics early.** It pays dividends in Kaggle competitions, experiments, investments and business decisions.
4. **Learn vectors and matrices.** Make a small numerical notebook tied to a real ML question.
5. **Add calculus when needed.** Use visual intuition plus independently solved derivatives and optimization problems.
6. **Apply financial mathematics continually.** Make a transparent spreadsheet and analyze alternative assumptions.
7. **Sample harder science only when invited by a real problem.** Preserve curiosity, but keep claims backed by computations.

**Suggested session (35–50 min):** 10 min concept + 20–30 min solving 3–5 problems unaided + 5–10 min explaining or using the idea in a lab. Keep a concise error log: *what I predicted; where the reasoning failed; what observation corrected it; next independent test*.

## Foundational source index

All course materials below offer free access to the cited content. Degree credit and formal certificates are not implied.

| Need | Free original-source resource | Why |
|---|---|---|
| Targeted higher-school repair | [Khan Academy Algebra 2](https://www.khanacademy.org/math/algebra2) | Guided lessons, mastery exercises and feedback |
| Rigorous reference | [OpenStax Mathematics library](https://openstax.org/subjects/math) | Free full textbooks, including algebra, precalculus, statistics and calculus |
| Discrete mathematical thinking | [MIT 6.042J Mathematics for CS](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | University lectures, open textbook, problem sets |
| Statistics and inference | [Khan Academy Statistics](https://www.khanacademy.org/math/statistics-probability) | Self-paced fundamentals |
| Deeper probability | [Harvard Stat 110](https://stat110.hsites.harvard.edu/) | University lectures and free online text; advanced prerequisites |
| Linear-algebra visual intuition | [3Blue1Brown Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) | Visual transformations and geometric explanations |
| Rigorous linear algebra | [MIT 18.06SC](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | Lecture series, exercises and exams |
| Calculus intuition | [3Blue1Brown Essence of Calculus](https://www.3blue1brown.com/lessons/essence-of-calculus/) | Understand the mechanisms before memorizing formulas |
| Calculus practice | [MIT 18.01SC](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | Complete independent-learning course |
| Applied finance | [NYU Damodaran online classes](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/onlineclass.htm) | Free, rigorous, practical finance |

**Quality standard:** A course is a tool for acquiring capability; completing the video playlist is not a mathematical proficiency claim. One independently explained subnetting problem or sound probabilistic analysis is more useful than five incomplete courses.


## Beyond career relevance: mathematics as an intellectual world

You do **not** need to justify a mathematical interest by employment value. The earlier stages above offer a comfortable practical entrance, but this library also invites deeper exploration without a fixed sequence: [MIT mathematics on OpenCourseWare](https://ocw.mit.edu/search/?d=Mathematics) for number theory, combinatorics, geometry, topology, differential equations and proof-based courses; [Santa Fe Institute Complexity Explorer](https://www.complexityexplorer.org/courses) for chaos, networks, information theory, complexity and dynamical systems; [3Blue1Brown](https://www.3blue1brown.com/) for elegant geometric intuition; [OpenStax Mathematics](https://openstax.org/subjects/math) for open textbooks. Pick a mathematical question because it is beautiful, surprising, or useful—not because a job description demands it. [Browse the wider Knowledge Atlas](../KNOWLEDGE_ATLAS.md).
