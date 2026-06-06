from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity
from qiskit_aer.noise import NoiseModel, depolarizing_error
import numpy as np
import matplotlib.pyplot as plt

sim = AerSimulator()

def bell_state():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def compute_fidelity(qc):
    state = Statevector.from_instruction(qc)
    ideal = (Statevector.from_label("00") + Statevector.from_label("11")) / np.sqrt(2)
    return state_fidelity(state, ideal)

def noisy_bell_fidelity(noise_level):
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    noise_model = NoiseModel()
    error_1q = depolarizing_error(noise_level, 1)
    error_2q = depolarizing_error(noise_level, 2)
    noise_model.add_all_qubit_quantum_error(error_1q, ["h"])
    noise_model.add_all_qubit_quantum_error(error_2q, ["cx"])
    qc_sv = qc.copy()
    qc_sv.save_statevector()
    compiled = transpile(qc_sv, sim)
    result = sim.run(compiled, noise_model=noise_model, shots=1).result()
    state = result.get_statevector()
    ideal = (Statevector.from_label("00") + Statevector.from_label("11")) / np.sqrt(2)
    return state_fidelity(state, ideal)

def sweep_noise():
    noises = np.linspace(0, 0.3, 10)
    fidelities = [noisy_bell_fidelity(n) for n in noises]
    print("\nNoise\t\tFidelity")
    print("-" * 25)
    for n, f in zip(noises, fidelities):
        print(f"{n*100:.1f}%\t\t{f:.4f}")
    plt.figure(figsize=(8, 5))
    plt.plot(noises * 100, fidelities, marker='o', color='#185FA5', linewidth=2)
    plt.xlabel("Noise Level (%)")
    plt.ylabel("Fidelity")
    plt.title("Bell State - Fidelity vs Noise")
    plt.ylim(0, 1.05)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("fidelity_vs_noise.png", dpi=150)
    print("\nGraph saved: fidelity_vs_noise.png")
    plt.show()

if __name__ == "__main__":
    qc = bell_state()
    f = compute_fidelity(qc)
    print(f"Bell State Fidelity (no noise): {f:.4f}")
    sweep_noise()