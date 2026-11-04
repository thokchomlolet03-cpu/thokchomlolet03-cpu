# Quantum + AI: a research roadmap, not a marketing claim

[← Quantum path](README.md) · [Experiments](EXPERIMENTS.md) · [NotebookLM](../notebooklm/README.md)

## Long-term direction

My future discovery intelligence system may combine classical computing, statistical/ML models, scientific evidence and **quantum methods when a specific computational subproblem justifies them**. The integration question is not "Can I attach Qiskit to AI?" It is:

> **Which exactly defined calculation is difficult for a strong classical method, expressible as a quantum algorithm, executable within hardware and data-access constraints, and shown to yield an independently verified benefit?**

A working quantum SDK integration alone does **not** imply faster model inference, better scientific truth finding, new physical laws or quantum advantage.

## Main research families — with skepticism built in

| Candidate subproblem | Why it might be worth studying | Classical baseline required | Main risk |
|---|---|---|---|
| **Quantum chemistry / Hamiltonian simulation** | Electronic structure and molecules are naturally quantum-mechanical | Classical eigensolver, small exact diagonalization, established chemistry approximation | Hardware/noise/resource overhead and classically tractable small problems |
| **Combinatorial optimization** | Some real search/constraint tasks can be expressed using quantum optimization approaches | Classical mixed-integer solver / heuristics / local search, with matched budgets | Encoding overhead and no proven general practical speedup |
| **Quantum machine learning** | Quantum kernels or variational circuits may provide useful inductive biases for selected datasets | Logistic regression, SVM/kernel methods, random forest/modern ML | Data-loading overhead, small/noisy circuits, overfitting, unfair comparisons |
| **Sampling/simulation research** | Certain quantum distributions and simulation tasks have interesting complexity properties | Best known exact/approximate classical sampler and resource estimate | A contrived benchmark may not solve a meaningful scientific task |
| **Compilation and error correction** | Better circuit mapping, decoder/controls can help use constrained hardware | Compiler's existing valid baseline, exact unitary or distribution check, cost model | Optimizing a proxy without improving real output fidelity |
| **AI for quantum hardware engineering** | Classical ML might help calibration, noise modeling, compilation or fault diagnosis | Rules, conventional optimization and established control methods | Improvement on synthetic simulation may not transfer to hardware |

There is **no default or universal quantum advantage for AI**. IBM's [Quantum Machine Learning introductory lesson](https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning/introduction) explicitly warns that most ML problems already have highly effective classical solutions.

## Suggested future system architecture — conditional, unimplemented

```text
SCIENCE QUESTION
     |
Evidence ingestion, provenance, contradiction checks, hypotheses
     |
     v
Problem specification and classical baseline (required)
     |
     +--> No justified quantum approach -> classical result or experiment request
     |
     +--> Candidate quantum subproblem (requires justification)
                     |
              Problem encoding and error/resource budget
                     |
              Local quantum simulation (first)
                     |
              Optional approved hardware execution (if warranted)
                     |
              Classical post-processing and independent comparison
                     |
              Claim-evidence audit and uncertainty report
```

The epistemic layer must be able to say **"insufficient evidence," "quantum did not help"** or **"request a real experiment"** instead of manufacturing success.

## Advancement gates — each must pass

1. **Scientific motivation:** articulate the actual physical/algorithmic problem and why quantum methods are relevant.
2. **Problem encoding:** specify input representation, encoding depth, qubit count, target connectivity and how classical data reaches the circuit.
3. **Classical baseline:** choose at least one strong baseline; no favorable choice of dataset or hardware that hides classical strengths.
4. **Simulation baseline:** ideal and noisy circuit estimates, random seeds, uncertainty, runtime and classical simulation resource cost.
5. **Hardware feasibility:** circuit depth, native gates, qubit count, error model, readout overhead, number of repetitions, queue time, monetary cost and access constraints.
6. **Fair comparison:** same problem definition, quality metric, reporting of training/tuning effort, data access and wall-clock/cost. Isolate any overhead.
7. **External reproducibility:** code, environment, versions, source data licensing, results, confidence intervals, failure cases and independent checks.
8. **Claim discipline:** report only task-specific results, not broad or speculative "quantum beats AI" statements.

**Red flags:** improvement over intentionally weak classical baselines; ignoring feature-map/data-loading cost; leakage across ML folds; optimizing a circuit gate count without verifying semantics; treating a cloud simulator as a real QPU; conflating a result on a few qubits with scalable advantage; claiming discovery without independent scientific validation.

## Where to begin, concretely

Start at **chemistry and compilation** rather than a full LLM/quantum integration. These are narrow enough to support honest comparison:
- **Quantum chemistry (Q05):** a minimal Hamiltonian, exact diagonalization baseline and a tiny VQE circuit. The [IBM VQE chemistry course](https://quantum.cloud.ibm.com/learning/en/courses/quantum-chem-with-vqe/index) explains the components and limitations.
- **Circuit compilation (Q03):** circuit equivalence, gate counts and hardware connectivity in Cirq/Qiskit. This aligns with quantum compilation as a reproducible engineering problem.
- **QML critique (Q04):** a toy dataset, fixed train/test splits, realistic sklearn baseline and quantum kernel/variational alternative. Cite [IBM QML](https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning) and [PennyLane demos](https://pennylane.ai/demonstrations).

Only connect this to a discovery system once multiple experiments identify a real benefit or a clearly valuable research question.

## Learn the adjacent infrastructure

Your systems-engineering career foundation helps: quantum workflows still depend on Linux, Python environments, container/scheduler tools, distributed computing and reproducible experiments. IBM explicitly offers a course on [integrating quantum and high-performance computing](https://quantum.cloud.ibm.com/learning/en/courses/integrating-quantum-and-high-performance-computing/introduction). Quantum services are **not simply CPU or GPU resources**; hardware scheduling, no-cloning, measurement and control make them operationally different.

## Research reference shelf

- [IBM Quantum Learning course catalog](https://quantum.cloud.ibm.com/learning/en/courses)
- [IBM Quantum Machine Learning — limitations](https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning/introduction)
- [Google Quantum AI Cirq documentation](https://quantumai.google/cirq)
- [Google hardware access rules](https://quantumai.google/cirq/google/access)
- [IBM Foundations of Quantum Error Correction](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/index)
- [PennyLane quantum chemistry and resource estimation demos](https://pennylane.ai/demonstrations)
- [Quantum course and research progress](PROGRESS.csv)

**Scientific humility:** simulation results can test implementations and models; claims about molecular, biological, or real-world effects need independent physical experiments or relevant ground-truth evidence.
