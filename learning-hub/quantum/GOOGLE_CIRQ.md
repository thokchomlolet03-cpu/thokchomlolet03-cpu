# Q3/Q4 — Google Quantum AI and Cirq

[← Quantum path](README.md) · [Qiskit first](QISKIT.md) · [Experiments](EXPERIMENTS.md)

**Google's toolchain is useful—especially for understanding real hardware constraints and circuit compilation.** The official path is primarily documentation, Colab tutorials, simulators and research examples, rather than the same kind of packaged beginner-to-advanced curriculum offered by IBM. Google [says Cirq basics assumes prior quantum knowledge](https://quantumai.google/cirq/start/basics): take Q0/Q1 first.

## One-click practical sequence

| Order | Direct official resource | Target understanding |
|---|---|---|
| 1 | [Cirq overview](https://quantumai.google/cirq) | What gates, operations, moments, device targets and circuit transformers mean |
| 2 | [Introduction to Cirq](https://quantumai.google/cirq/start/intro) | Write a simple circuit, simulator or variational ansatz in Python |
| 3 | [Cirq basics notebook](https://quantumai.google/cirq/start/basics) | Qubits, gates, simulation, parameter sweeps; runnable Colab link |
| 4 | [Cirq simulation](https://quantumai.google/cirq/simulate/simulation) | Ideal state vector, density-matrix noise and shot-based sampling |
| 5 | [Quantum Virtual Machine (QVM)](https://quantumai.google/cirq/simulate/quantum_virtual_machine) | Virtual device constraints and realistic simulated noise |
| 6 | [Textbook algorithms in Cirq](https://quantumai.google/cirq/experiments/textbook_algorithms) | Teleportation, QFT, phase estimation and Grover |
| 7 | [Cirq source code](https://github.com/quantumlib/Cirq) | Inspect API behavior, issues, tests and actual compilation logic |

## Things to reason about rather than memorize

- **Topology:** a 2-qubit interaction may not be physically native between arbitrary qubits.
- **Native gates:** circuit decomposition can raise depth or gate count.
- **Moments and scheduling:** concurrent vs sequential operation constraints.
- **Noise:** coherent errors, incoherent channels, readout errors; don't collapse all noise into a single number.
- **Cost:** classical simulations consume memory and time. Large state-vector sizes can be prohibitively expensive.
- **Quantum error correction:** requires significant extra physical resources, decoding and control—not just toggling a software switch.

## First Google-flavored experiment

Recreate the Bell state from Qiskit, then simulate with Cirq; compare ideal distributions, qubit order, measurement keys, shot count and random seeds. Next introduce a supported noise model **in the simulator only**. Write down which differences come from API conventions, sampling or actual noise.

**Do not assume Google Quantum AI hardware access.** Google's [official access policy](https://quantumai.google/cirq/google/access) says use of its quantum hardware is restricted to approved groups, normally requiring a Google sponsor. The Cirq code and simulators are accessible without a hardware grant. A simulator/QVM result must be labeled accordingly.

## How this connects with past quantum compilation work

When examining a quantum circuit-optimization task, define the objective (such as two-qubit gate count, native depth, fidelity proxy or compile time), specify all allowed transformations and constraints, and compare with a valid reproducible baseline. Good compiler improvements must preserve the circuit's intended semantics within appropriate equivalence (including phase and measurement conventions). A leaderboard result or simulator metric is not automatically real-hardware superiority.

See [Q03 compilation and noise experiments](EXPERIMENTS.md) and [Quantum–AI research](QUANTUM_AI_RESEARCH.md).
