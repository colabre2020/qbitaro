from .gates import H, X, Z, CNOT
from .register import QuantumRegister
from .utils import pretty_print_statevector, sample_measurements

def teleport():
    print("Quantum Teleportation Protocol\n")
    
    # Step 1: Prepare 3-qubit register
    qr = QuantumRegister(3)

    # Step 2: Encode Alice's qubit (qubit 0) — let's say |ψ⟩ = (|0⟩ + |1⟩)/√2
    qr.apply_single_qubit_gate(H, 0)
    print("Alice's qubit initialized:")
    pretty_print_statevector(qr.get_state())

    # Step 3: Create Bell pair between qubit 1 and qubit 2
    qr.apply_single_qubit_gate(H, 1)
    qr.apply_two_qubit_gate(CNOT, control=1, target=2)
    print("\n Bell pair between Q1 and Q2:")
    pretty_print_statevector(qr.get_state())

    # Step 4: Alice applies CNOT (Q0→Q1) and H on Q0
    qr.apply_two_qubit_gate(CNOT, control=0, target=1)
    qr.apply_single_qubit_gate(H, 0)

    # Step 5: Alice measures Q0 and Q1
    m0, _ = qr.measure_qubit(0)
    m1, _ = qr.measure_qubit(1)
    print(f"\n Alice measures Q0 = {m0}, Q1 = {m1}")

    # Step 6: Bob applies corrections to Q2
    if m1 == 1:
        qr.apply_single_qubit_gate(X, 2)
    if m0 == 1:
        qr.apply_single_qubit_gate(Z, 2)

    # Result: Qubit 2 has the teleported state
    print("\n Final State (Bob's Q2):")
    pretty_print_statevector(qr.get_state())

    # Optional: Sample and display probabilities
    print("\n Sampled Measurement (1000 shots):")
    dist = sample_measurements(qr.get_state(), 1000)
    for state, prob in dist.items():
        print(f"{state}: {prob:.3f}")


if __name__ == "__main__":
    teleport()
