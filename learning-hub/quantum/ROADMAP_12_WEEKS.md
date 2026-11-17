# First 12 study weeks — flexible on-ramp for a long-term quantum track

[← Quantum path](README.md) · [Experiments](EXPERIMENTS.md)

This is a *suggested order*, not an expectation to finish in exactly 12 calendar weeks. It is intentionally small (roughly two to three hours each week), alongside German and professional infrastructure study. Extend weeks for mathematical gaps.

| Week | Topic | Main learning link | Evidence to create |
|---|---|---|---|
| 1 | What quantum computing does and doesn't promise | [IBM beginner course](https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today) | Two-column note: possible algorithms vs unsupported claims |
| 2 | Complex numbers, vectors and normalization | [MIT linear algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | 2-element state normalized by hand |
| 3 | Unitary gates, H/X/Z, phase | [PennyLane foundations](https://pennylane.ai/codebook/learning-paths/foundations-of-quantum-computing/) | Manual gate action checked with NumPy |
| 4 | Tensor products and entanglement | [IBM quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information) | Derive Bell state without SDK |
| 5 | Qiskit current setup and local simulation | [IBM Qiskit quickstart](https://quantum.cloud.ibm.com/docs/en/guides/quick-start) | Q01 source + seed/shot run with version log |
| 6 | Probability, measurement and noise | [Google simulation guide](https://quantumai.google/cirq/simulate/simulation) | Exact vs finite-shot vs noisy results explained |
| 7 | Circuit semantics and common algorithms | [IBM algorithms](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms) | Explain a toy algorithm's cost model |
| 8 | Cirq operations and simulation | [Google Cirq basics](https://quantumai.google/cirq/start/basics) | Q02 Qiskit ↔ Cirq equivalent circuit |
| 9 | Transpilation, topology and error models | [Google Cirq overview](https://quantumai.google/cirq) | Q03 experiment plan; compare native vs abstract circuit |
| 10 | Density matrices, noisy channels, measurement | [IBM general formulation](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/index) | Small mixed-state calculation and limitations |
| 11 | Error correction and resource overhead | [IBM QEC course](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/index) | Distinguish physical/logical qubits and explain error thresholds qualitatively |
| 12 | Choose next research branch | [Quantum–AI roadmap](QUANTUM_AI_RESEARCH.md) | Select Q04 or Q05; write fair classical baseline and no-spend plan |

### After week 12 — choose one line of inquiry, not everything
- **A. Compilation/noise engineering:** finish Q03, then revisit published hardware constraints and error correction.
- **B. Quantum chemistry:** work through [IBM's VQE chemistry course](https://quantum.cloud.ibm.com/learning/en/courses/quantum-chem-with-vqe/index) and Q05, beginning with exact classical energies.
- **C. Quantum machine learning:** work through [IBM QML](https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning) and Q04 with strong sklearn baselines.
- **D. Quantum systems/HPC:** follow [IBM's quantum-HPC course](https://quantum.cloud.ibm.com/learning/en/courses/integrating-quantum-and-high-performance-computing/introduction) and analyze how control and scheduling differ from ordinary servers.

Once a month, ask: "What did I independently predict, implement and verify?" If the answer is only "watched a course," repeat an experiment rather than accumulating badges.
