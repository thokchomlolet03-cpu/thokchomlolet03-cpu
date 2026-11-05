# Computer and mathematical foundations — from logic gates to operating systems

[← University learning](README.md) · [Finnish courses/ECTS opportunities](FINNISH_CREDIT_OPPORTUNITIES.md) · [Systems engineering portfolio](../../systems-infrastructure/README.md) · [Quantum learning](../quantum/README.md)

The goal is **deep engineering understanding**, not simply additional programming credentials. These independent public courses fill conceptual gaps a business degree may not cover, while connecting to real systems troubleshooting.

## A deliberate first-principles ladder

| Step | Source — click to study | What it explains | An original evidence exercise |
|---|---|---|---|
| **0. Learn to reason precisely** | **[MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)** | Logic, proof, induction, graphs, recurrences, discrete probability and algorithmic complexity | Prove an invariant and test it on a graph-search toy problem |
| **1. Construct a computer** | **[Nand2Tetris — official free learning materials](https://www.nand2tetris.org/)** | NAND gates → Boolean logic → ALU → CPU and memory → assembly → OS abstractions | Build and test the provided logic components; explain each interface |
| **2. Study computer architecture** | [MIT 6.004 — Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) | ISA, processor datapath, pipelining, memory hierarchy, caches and coordination | Explain how an instruction changes hardware state and where stalls arise |
| **3. Study systems programming** | [Carnegie Mellon 15-213 — Introduction to Computer Systems](https://www.cs.cmu.edu/~213/) | Machine-level programs, memory, processes, caching and networking | Reproduce a safe C program's memory behavior on a local sandbox |
| **4. Inspect an OS** | [MIT 6.1810 — Operating System Engineering](https://pdos.csail.mit.edu/6.1810/2026/) | xv6 kernel, syscalls, scheduling, page tables, filesystems, concurrency | Implement a carefully bounded, course-permitted kernel exercise; log tests |
| **5. Connect machines and handle failures** | [Stanford CS144 — Computer Networking](https://web.stanford.edu/class/cs144/) · [MIT 6.5840 — Distributed Systems](https://pdos.csail.mit.edu/6.5840/) | TCP, protocols, reliability, distributed replication and recovery | Explain or safely reproduce a realistic network/service failure |

**Free and academic status:** MIT OpenCourseWare, public university labs and the Nand2Tetris self-study materials are accessible online, **without a Harvard/MIT/CMU/Stanford degree or free university completion credential**. The Nand2Tetris publisher states that self-study materials/tools are free for non-profit use; **its Coursera certificate is paid**. Check integrity/licensing policies before publishing class solution code. [Nand2Tetris official explanation](https://www.nand2tetris.org/).

## How to choose without rushing

- Already competent in Python? **Skip repetitive beginner drills** unless the formal credited course fills a genuine admission/credential requirement.
- Lost in computer architecture? Work on Nand2Tetris until you can explain CPU, instruction decode, registers and memory without a diagram in front of you.
- Interested in *thinking* rather than writing syntax? Work through MIT 6.042J proofs and graph problems; explain why an approach must work, not just a successful test.
- Pursuing real systems competence? Alternate a physical/software mechanism with an [existing lab](../../systems-infrastructure/PROJECT_BACKLOG.md) and [production engineering postmortem](../engineering-incidents/README.md).
- Interested in AI/quantum discovery? Mathematical reasoning and simple algorithms transfer into [quantum foundations](../quantum/FOUNDATIONS.md); an actual quantum advantage is **not presumed**.

## A single integrated exercise

Take a real published engineering incident, for example from [Cloudflare's official postmortems](https://blog.cloudflare.com/tag/post-mortem/) or [Netflix Tech Blog](https://netflixtechblog.com/):

1. Identify the important **hardware, OS, networking or distributed system** mechanism.
2. Draw the smallest accurate mechanism you can defend mathematically.
3. Make a prediction or causal hypothesis from an original primary source.
4. Simulate an authorized analogous failure in a private VM/container (never in an employer environment).
5. Keep the exact observation, alternative explanations, recovery and limitations.
6. Present the result in two minutes to a technical or nontechnical audience using the [communication track](../personal-skills/PROFESSIONAL_COMMUNICATION.md).

This is how breadth and depth can reinforce each other without making the learning journey a race.
