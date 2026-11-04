# Q2 — Qiskit remains relevant: the IBM-first hands-on track

[← Quantum path](README.md) · [Foundations](FOUNDATIONS.md) · [Experiments](EXPERIMENTS.md)

**Decision as of November 2026:** continue with **modern Qiskit** rather than discarding what you previously studied. IBM actively maintains its Qiskit 2.x SDK and official Quantum Learning material. Concepts learned in older Qiskit—gates, state preparation, transpilation, measurement, noise—remain valuable, **but API examples can be outdated**.

## One-click sequence

1. **[Use a quantum computer today](https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today)** — gentle 5-hour introduction; start with **[build and run your first program](https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today/build-and-run-your-first-quantum-program)**. It includes an optional simulator route.
2. **[Install Qiskit](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)** — use an isolated virtual environment; check Python and OS support for your machine.
3. **[IBM Quickstart](https://quantum.cloud.ibm.com/docs/en/guides/quick-start)** — build a Bell circuit with `QuantumCircuit` and sample using `StatevectorSampler`.
4. **[Basics of quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information)** — mathematically explain the circuit instead of following a notebook blindly.
5. **[Fundamentals of quantum algorithms](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms)** — understand the black-box/query model, Grover, phase estimation and Shor rather than equating theoretical query improvements with real-world speedup.
6. **[Qiskit tutorials](https://quantum.cloud.ibm.com/docs/en/tutorials)** — compare your solution to an official maintained implementation.
7. **[General formulation of quantum information](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/index)** — density matrices, channels, measurements.
8. **[Foundations of quantum error correction](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/index)** — logical qubits, syndrome concepts and fault tolerance.
9. **[Variational algorithm design](https://quantum.cloud.ibm.com/learning/en/courses/variational-algorithm-design)** — classical optimizer + quantum circuit + careful cost/error accounting.
10. **[Quantum chemistry with VQE](https://quantum.cloud.ibm.com/learning/en/courses/quantum-chem-with-vqe/index)** or **[Quantum machine learning](https://quantum.cloud.ibm.com/learning/en/courses/quantum-machine-learning)** — only after you can construct fair classical baselines.

## Qiskit API migration trap

Tutorials from previous years may use deprecated or removed `Aer`, `execute`, `Backend.run` or old primitive interfaces. **Never copy old code without checking versions.** IBM's [current quickstart](https://quantum.cloud.ibm.com/docs/en/guides/quick-start) uses `StatevectorSampler` for a simple simulator-based Bell experiment. Use IBM's maintained [tutorials](https://quantum.cloud.ibm.com/docs/en/tutorials) as the primary reference.

### Reference pattern, not claimed as executed here

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result()
print(result[0].data.meas.get_counts())
```

Expected counts cluster around `00` and `11`; actual values depend on sampling and randomness. Re-run in a clean environment, pin versions and use a safe tolerance for stochastic tests. This code is adapted from the public IBM quickstart; record the installed version when you execute it yourself.

## Your first six tasks

- [ ] Create a fresh Python virtual environment and record Python/Qiskit version, machine architecture and OS.
- [ ] Derive the Bell state with NumPy (no Qiskit) and compare results.
- [ ] Run the circuit in a current local simulator and log seeds/shots.
- [ ] Explain `StatevectorSampler` outputs and why you cannot read state amplitudes from hardware measurements directly.
- [ ] Explore transpilation/basis-gate changes and verify semantic equivalence.
- [ ] Translate the same experiment into [Google Cirq](GOOGLE_CIRQ.md), avoiding framework-specific false differences.

## Access and cost

- Read public IBM learning and SDK docs without QPU hardware spending.
- Local simulation is the default; QPU access uses IBM Quantum's current account/service rules and may require registration, quotas, available plans and/or payment. [IBM Compute client](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit-runtime) is distinct from installing the local SDK.
- Do not save credentials or access tokens in a notebook committed to GitHub.

**Output:** pass Q01/Q02 in [Experiments & Evidence](EXPERIMENTS.md) before declaring Qiskit competency; a course badge alone is not equivalent to independent algorithm analysis.
