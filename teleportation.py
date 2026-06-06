from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity
import numpy as np

sim = AerSimulator()

def quantum_teleportation(state_to_send):
    qc = QuantumCircuit(3, 3)
    # state_to_send هو الزاوية بالـ radians
    qc.ry(state_to_send, 0)
    qc.barrier()

    # Bell pair بين Alice و Bob
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    # Alice تقيس
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()
    qc.measure([0, 1], [0, 1])
    qc.barrier()

    # Bob يصحح
    qc.cx(1, 2)
    qc.cz(0, 2)
    qc.measure(2, 2)

    return qc

def run_teleportation():
    angles = [0, np.pi/4, np.pi/2, np.pi]
    labels = ["0°", "45°", "90°", "180°"]

    print("Quantum Teleportation Results")
    print("=" * 40)
    print(f"{'State':<10} {'|0> prob':<12} {'|1> prob':<12} {'Success'}")
    print("-" * 40)

    for angle, label in zip(angles, labels):
        qc = quantum_teleportation(angle)
        compiled = transpile(qc, sim)
        result = sim.run(compiled, shots=1024).result()
        counts = result.get_counts()

        total = sum(counts.values())
        success_0 = sum(v for k, v in counts.items() if k[0] == '0')
        success_1 = sum(v for k, v in counts.items() if k[0] == '1')

        prob_0 = success_0 / total
        prob_1 = success_1 / total

        expected_0 = np.cos(angle/2)**2
        success = "✓" if abs(prob_0 - expected_0) < 0.1 else "✗"

        print(f"{label:<10} {prob_0:<12.3f} {prob_1:<12.3f} {success}")

    print("=" * 40)
    print("Teleportation complete!")

if __name__ == "__main__":
    run_teleportation()