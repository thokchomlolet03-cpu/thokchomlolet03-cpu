# Quantum computing — first principles to trustworthy quantum–AI research

[← Learning Hub](../README.md) · [Start Here](../../START_HERE.md) · [Systems & Infrastructure](../../systems-infrastructure/README.md) · [NotebookLM](../notebooklm/README.md)

> **Status: a research learning roadmap, not a deployed AI–quantum system or a claim of quantum advantage.** Last source review: **4 November 2026**.

## Why this track exists

My long-term ambition is a discovery system that reasons about scientific evidence and can eventually evaluate quantum computing as **one possible computational resource**. I am studying quantum computing to understand the actual physics, mathematical capabilities, constraints and interfaces—not to assume that a quantum processor improves every AI workflow. This track is **independent of my near-term infrastructure career**: it is a patient, long-term area of study with real experiments and strict classical baselines.

**Core research principle:** use the simplest well-supported classical solution unless a well-defined quantum algorithm, independent comparison and resource model justify a quantum approach.

## First click — choose your present level

| Starting point | Direct resource | What to do |
|---|---|---|
| **New to quantum theory** | **[IBM — Use a quantum computer today](https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today)** | Run a small Bell-state circuit; don't worry about full theory on the first day |
| **Refresh mathematics** | **[MIT OCW 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)** | Vectors, complex numbers, eigenvalues, tensor products |
| **Understand the foundations** | **[IBM — Basics of quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information)** | Work through John Watrous's quantum states, gates, entanglement and measurement |
| **Return to Qiskit** | **[IBM Qiskit current quickstart](https://quantum.cloud.ibm.com/docs/en/guides/quick-start)** | Use modern primitives; don't copy old `execute`/`Aer` tutorials blindly |
| **Learn Google's approach** | **[Google Quantum AI — Cirq](https://quantumai.google/cirq)** | Follow Cirq basics and noise/compilation tutorials after quantum circuits are familiar |
| **Explore hybrid quantum + ML** | **[IBM — Quantum machine learning](https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning)** | Read the limitations before testing a quantum kernel |
| **Prepare future discovery experiments** | **[Quantum–AI research integration](QUANTUM_AI_RESEARCH.md)** | Identify candidate problems and specify honest quantum-vs-classical tests |

## Qiskit versus Google Cirq — the practical decision

**Qiskit remains current**: IBM's learning platform has a maintained collection of quantum-information, algorithm, hardware, error-mitigation and QML courses. The current installation guide describes the **Qiskit 2.x** series. Start with Qiskit if you've used it before; carry your physics/mathematics understanding across tooling changes.

**Google's quantum programming path is Cirq**, with tutorials for gates, circuits, device constraints, simulations, noisy channels and circuit transformations. Unlike IBM's structured course catalog, Google's site is more **documentation/tutorial oriented**. The [Cirq basics tutorial](https://quantumai.google/cirq/start/basics) explicitly assumes existing quantum computing knowledge.

**Hardware access distinction:** Cirq simulators are open source, but **Google quantum hardware access is restricted to approved groups**, usually with a Google sponsor. Don't mistake simulator results for Google quantum-processor runs. IBM hardware access, quotas and prices depend on its current service plans; start locally before spending.

**Optional third toolkit:** [PennyLane Codebook](https://pennylane.ai/codebook/learning-paths) and [PennyLane demos](https://pennylane.ai/demonstrations) are useful for differentiable programming, quantum machine learning, quantum chemistry and cross-checking approaches. Learn it **after** understanding one primary SDK, not concurrently with two new languages.

## A staged path — learning gates, not calendar promises

| Stage | Topic | Official first click | A personally demonstrated exit condition |
|---|---|---|---|
| **Q0** | Linear algebra, probability, complex numbers, Python/NumPy | [MIT linear algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) · [PennyLane basics](https://pennylane.ai/codebook/learning-paths/foundations-of-quantum-computing/) | Independently compute and verify a 1–2 qubit state and measurement probabilities |
| **Q1** | Superposition, interference, entanglement, gates, measurement | [IBM Basics of quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information) | Predict Bell circuit outputs analytically and verify in a simulator |
| **Q2** | Current Qiskit SDK and algorithm basics | [Qiskit quickstart](https://quantum.cloud.ibm.com/docs/en/guides/quick-start) · [IBM quantum algorithms](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms) | Implement at least two circuits; check exact/noisy outcomes and sample counts |
| **Q3** | Cirq, compilation, target topology, noise and simulators | [Google Cirq](https://quantumai.google/cirq) · [simulation guide](https://quantumai.google/cirq/simulate/simulation) | Translate the same circuit from Qiskit into Cirq and explain discrepancies |
| **Q4** | Error correction, fault tolerance and resource constraints | [IBM error correction](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/index) · [Cirq QVM](https://quantumai.google/cirq/simulate/quantum_virtual_machine) | Compare ideal/noisy simulated results and describe logical vs physical qubits |
| **Q5** | Variational algorithms, quantum chemistry and ML with baselines | [IBM variational algorithms](https://quantum.cloud.ibm.com/learning/en/courses/variational-algorithm-design) · [QML](https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning) | Reproduce a tiny VQE/QML example and benchmark against a serious classical method |
| **Q6** | Quantum computing in a discovery system | [Research integration roadmap](QUANTUM_AI_RESEARCH.md) | A reproducible decision record documenting where quantum helps, fails or is unnecessary |

Detailed prerequisite map: [Foundations](FOUNDATIONS.md). SDK-specific guided routes: [Qiskit](QISKIT.md) and [Google Cirq](GOOGLE_CIRQ.md).

## First four practical experiments

Open the complete specification in [Experiments & Evidence](EXPERIMENTS.md). Do them in order:

1. **Q01 — Bell-state truth check**: expected ideal probabilities vs finite-shot sampling, with seeds and tolerances.
2. **Q02 — Qiskit ↔ Cirq translation**: same 2-qubit circuit; compare probability distributions and gate semantics.
3. **Q03 — Noise and circuit compilation**: show how connectivity, gate counts and noise assumptions affect results.
4. **Q04 — Quantum-vs-classical benchmark**: compare a small hybrid/quantum algorithm against a competitive classical baseline, including data loading and runtime costs.

These are **proposed tests**, not completed artifacts. Any previous competition work must be linked and independently audited before promotion to `owner-executed` evidence.

## What will matter to the eventual AI–quantum system?

```text
Question + scientific evidence
          |
          v
   Classical reasoning/retrieval/verification
          |
          v
  Define a narrow computational subproblem
          |
          v
Classical baseline + cost/error budget + test design
          |
       if justified
          v
 Quantum simulator / approved quantum service
          |
          v
  Reproducible comparison & uncertainty record
          |
          v
 Update claims only if supported by evidence
```

**Not an architecture promise:** quantum processors today are not drop-in LLM accelerators, do not provide arbitrary database-like quantum RAM, and cannot generally turn a classical learning system into a superior one simply by being added to its infrastructure. More in [Quantum–AI research integration](QUANTUM_AI_RESEARCH.md).

## Low-cost weekly routine (alongside the infrastructure career)

- One session: **theory** (derive one identity or prediction without software).
- One session: **laboratory** (one small simulator run and a reproducible output).
- One short review: **critique** (read a primary source, identify a limitation and write the next hypothesis).
- Keep expenditures at **zero** initially using docs, free course pages, local simulation and permissibly available Colab sessions. Don't buy cloud-QPU time without a falsifiable question and a budget cap.

**A 2–3 hour weekly allocation is a suggestion, not a deadline.** OS, networking and enterprise-infrastructure proficiency remain the priority for near-term employment.

## Navigation and evidence

[Foundations](FOUNDATIONS.md) · [Qiskit](QISKIT.md) · [Google Cirq](GOOGLE_CIRQ.md) · [Experiments](EXPERIMENTS.md) · [Quantum–AI research](QUANTUM_AI_RESEARCH.md) · [Resource directory](RESOURCES.csv) · [Progress register](PROGRESS.csv) · [NotebookLM source notes](../notebooklm/INDEX.md).

All research and SDK details should be checked against vendor documentation before execution; packages and cloud access evolve. Do not store API credentials, employer data or restricted paper PDFs in public GitHub or NotebookLM.
