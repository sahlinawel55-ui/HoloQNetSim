# HoloQNetSim

**Quantum Network Simulation Platform**  
Simulating entanglement distribution and noise effects in quantum communication networks.

---

## Modules

| File | Description |
|------|-------------|
| `holoqnetsim.py` | Bell State, Fidelity calculation, Noise sweep |
| `teleportation.py` | Quantum Teleportation (Alice → Bob) |
| `quantum_simulation.py` | Initial 3-case simulation |

---

## Results

### Bell State — Fidelity vs Noise

![Fidelity vs Noise](fidelity_vs_noise.png)

| Noise | Fidelity |
|-------|----------|
| 0.0%  | 1.0000   |
| 10.0% | 1.0000   |
| 26.7% | 1.0000   |
| 30.0% | 0.0000   |

> Critical threshold detected between 26.7% and 30%

---

### Quantum Teleportation — Alice → Bob

| State | \|0⟩ Prob | \|1⟩ Prob | Success |
|-------|-----------|-----------|---------|
| 0°    | 1.000     | 0.000     | ✓       |
| 45°   | 0.855     | 0.145     | ✓       |
| 90°   | 0.523     | 0.477     | ✓       |
| 180°  | 0.000     | 1.000     | ✓       |

---

## Installation

```bash
pip install qiskit qiskit-aer matplotlib numpy
```

## Run

```bash
python holoqnetsim.py
python teleportation.py
```

---

## Author

GitHub: [sahlinawel55-ui](https://github.com/sahlinawel55-ui)