# Quantum learning experiments — predict, implement, measure, challenge

[← Quantum path](README.md) · [Theory](FOUNDATIONS.md) · [Template](EXPERIMENT_TEMPLATE.md)

**Status:** all exercises below are **planned** until separately executed, saved and reviewed. They are not a record of executed experiments, earned badges, access to QPUs, or achieved quantum advantage.

## Project sequence

| ID | Experiment | Skills and expected output | Exit gate |
|---|---|---|---|
| Q01 | **Bell-state derivation and sampling** | Write analytic state calculation; simulate H+CNOT with Qiskit, measure 100–10000 shots | Output distribution matches the analytic prediction within a stated sampling tolerance |
| Q02 | **Qiskit–Cirq semantic translation** | Reimplement same circuit in both; specify bit order, gate definitions and measurement keys | Reproducible numerical equivalence with unit tests and caveat for global phase |
| Q03 | **Compiler and noise study** | Apply transformations under specified gate sets/topology; compare exact ideal semantics, noisy simulation and resource metrics | Show cases where fewer gates do **not necessarily** mean higher fidelity |
| Q04 | **Hybrid quantum/classical benchmark** | Small kernel/variational ML study with fixed holdout folds and classical baselines | Honest report with accuracy, uncertainty, resources, data-loading and tuning overhead |
| Q05 | **Miniature quantum chemistry / VQE** | Solve small Hamiltonian using exact classical diagonalization; compare with variational circuit | Report absolute energy error and sensitivity to optimizer, ansatz, noise and shot budget |
| Q06 | **Quantum workload admission test** | Evaluate a candidate quantum subproblem in future discovery architecture | Decision record: use simulator/QPU/not-yet-justified with evidence and cost limits |

## Q01: first experiment — Bell-state truth check

**Question:** Can I derive and predict measurement probabilities independently, then verify them with maintained Qiskit code?

**Inputs:** two ideal qubits initialized in |00⟩, Hadamard on the first, CNOT with that qubit as control, measurement of both.

**Prediction:** probabilities approximately half for `00` and half for `11`, zero ideal probability for `01` and `10`. With finite shots, counts fluctuate; choose a statistically justified tolerance based on `n` shots, not a demand for exactly half. Explain global vs relative phase.

**Controls:** implement H and CNOT using NumPy; use one seeded simulator or record independent runs; if switching to noisy simulation, explicitly identify the error channel and parameters.

**Evidence:** file with Python/SDK versions, notebook/script, command, counts, expected distribution, sampling confidence interval or analytic fluctuation model, and explanatory note.

**What it does not show:** practical quantum speedup or capability on a physical QPU.

## Q02: two toolchains, one physical meaning

**Question:** Do a Qiskit and a Cirq circuit implement the same quantum process under a clear definition?

**Controls:** normalized vector comparison up to global phase *before measurement*, and distribution comparison *after measurement*. Document differing qubit and bit ordering. Test at least 3 circuits, not just Bell.

**Evidence:** reproducible test assertions and a table of discrepancies explained by stochastic sampling, phase, ordering or actual wrong transformation.

## Q03: compilation is about semantics, hardware, and error models

**Question:** Can a compiler optimization change circuit depth or two-qubit gate counts without changing the ideal quantum computation? Does the altered circuit improve realistic noisy execution?

**Controls:** specify topology, native gate set, objective metric, parameter seeds and equivalent-circuit check. Distinguish ideal unitary equivalence from global phase equivalence and measurement distribution equivalence. Do not use a "good" gate-count reduction as proof of hardware fidelity.

**Evidence:** before/after circuits, native gate counts, depth, measured compiler runtime and documented simulated noise model. Real-QPU result is separately labeled and only included if actually obtained.

## Q04: quantum machine learning without favorable baselines

**Question:** Does a small quantum kernel or variational model perform better than appropriate classical baselines on the *same exact dataset and split*?

**Required classical methods:** e.g. logistic regression, RBF-SVM and a small tree-based model; tune each fairly and avoid data leakage. Report training/validation/test selection separately.

**Evidence:** accuracy or task metric with uncertainty over multiple seeds, full feature mapping, shots/circuit counts, actual wall-clock/time budget, data loading and optimizer cost. **A negative result is a valid scientific outcome.**

## Q05: tiny Hamiltonian and VQE

**Question:** Can a hybrid circuit estimate a tiny Hamiltonian's ground-state energy within known error?

**Controls:** exact NumPy diagonalization as ground truth; specify Hamiltonian, ansatz, optimizer, initializations, iteration/shot budget and optionally a noisy simulator.

**Evidence:** energy errors and convergence, multiple seeds, classical cost comparison, failure analysis. Do not claim chemical or physical validation for a synthetic Hamiltonian.

## Q06: conditional quantum integration

**Question:** When should a larger computational intelligence system request a quantum computation?

**Output:** a decision record with `problem_id`, `classical_baseline`, `quantum_method`, `assumptions`, `feasibility`, `error_budget`, `cost_budget`, `result`, `uncertainty` and `decision`. Use `not justified` when appropriate. No architecture or API integration is required at this stage.

## Laboratory policy

- Start with local simulators and **synthetic or openly licensed** data.
- Versions must be pinned at experiment time; modern Qiskit and Cirq APIs evolve.
- Record random seeds, precision, environments, CPU/memory, shots, metrics, code and source URLs.
- No university/competition benchmark scores are to be represented as owner-validated without the actual linked run and evidence.
- Do not store IBM/Google credentials in public repository.
- Prefer meaningful, falsifiable tests to ceremonial "hello quantum" demonstrations.

Use a copy of [EXPERIMENT_TEMPLATE.md](EXPERIMENT_TEMPLATE.md) for every completed lab. Keep [PROGRESS.csv](PROGRESS.csv) accurate about which experiments have actually been performed.
