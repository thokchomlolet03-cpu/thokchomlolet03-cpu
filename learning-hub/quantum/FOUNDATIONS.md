# Q0/Q1 — understand the mathematics and physics first

[← Quantum path](README.md) · [Experiments](EXPERIMENTS.md) · [IBM quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information)

The objective is not to memorize quantum buzzwords. The objective is to **predict a circuit's output from mathematical rules and then challenge that prediction by experiment**.

## Prerequisites, sequenced

| Order | Topic | Why it is required | One accessible starting point | Self-check |
|---|---|---|---|---|
| 1 | Complex numbers | Probability amplitudes have magnitude *and phase* | [MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) and Python's built-in complex type | Calculate magnitude squared and normalize a 2-element vector |
| 2 | Vectors and matrices | States are vectors; basic gates act as linear maps | [MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | Multiply a 2×2 matrix by a 2-vector and interpret result |
| 3 | Inner products, adjoints and unitary operators | Preserve state norm under ideal closed-system evolution | [IBM quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information) | Show that the Hadamard operation is unitary |
| 4 | Eigenvalues and eigenvectors | Observables, Hamiltonians and energy estimation depend on them | [MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | Diagonalize a simple Hermitian matrix |
| 5 | Tensor products | Multiple qubits form a larger joint state space | [IBM quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information) | Expand `|0⟩ ⊗ |1⟩` as a 4-amplitude vector |
| 6 | Discrete probability / sampling | Shots, histograms and statistical confidence | [IBM beginner circuit](https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today) | Distinguish ideal 50/50 from finite-shot 47/53 |
| 7 | Python + NumPy | Verify calculations without relying on a quantum SDK | [NumPy documentation](https://numpy.org/doc/stable/) | Implement H and CNOT as arrays and compare to Qiskit |
| 8 | Measurement and entanglement | Quantum outputs are not just hidden deterministic bit strings | [PennyLane Codebook foundations](https://pennylane.ai/codebook/learning-paths/foundations-of-quantum-computing/) | Explain why the Bell state is not a product of single-qubit states |

**Starting example:** in the computational basis, a qubit state is represented by amplitudes `a`, `b` with `|a|² + |b|² = 1`. For an ideal 2-qubit Bell circuit, predict probabilities `P(00) = P(11) = 1/2` and `P(01) = P(10) = 0`, *before* running a simulator. Finite-shot results will vary; simulator numerical errors and hardware noise are separate issues.

## Learn these distinctions early

- **Superposition** does not mean you may read all amplitudes through one measurement.
- **Entanglement** is not merely an ordinary classical correlation.
- **Unitary evolution** of an isolated ideal circuit is distinct from noisy channels and measurement.
- **Circuit depth** affects exposure to noise, but gate count alone does not characterize all hardware errors.
- **A measured output distribution** is not the full quantum state.
- **A simulator** runs on classical hardware; its speed does not prove a quantum speedup.

## Suggested gates and algorithms

1. X, Z, H, Y and rotations: derive their action on |0⟩, |1⟩.
2. CNOT and controlled operations: build a Bell state and verify measurement.
3. Bloch sphere and phase: contrast global vs relative phase.
4. Noisy amplitude damping / depolarizing channel: contrast pure vs mixed states.
5. Deutsch(-Jozsa), Grover and phase estimation: distinguish proven query complexity from practical end-to-end advantage.
6. Error correction: stabilizers, syndromes, surface code, logical/physical qubit overhead.

**One trusted guided theory series:** [IBM Quantum Information & Computation courses](https://quantum.cloud.ibm.com/learning/en/courses), especially John Watrous's four-course sequence. For a second hands-on approach, use [PennyLane Codebook](https://pennylane.ai/codebook).

## First milestone

Prepare a one-page original note with:
- Algebraic amplitudes for a Bell state.
- Matrix calculation of H and CNOT without a quantum library.
- Expected counts for 1000 shots and a statement explaining sampling variability.
- A reproducible simulator run with version, seed, counts and observed differences.
- **What the result cannot establish** (entanglement does not imply universally faster algorithms).

Then graduate to [Qiskit practical training](QISKIT.md).
