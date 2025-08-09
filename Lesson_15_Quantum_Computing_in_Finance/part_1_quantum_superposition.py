from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate to put the qubit in superposition
qc.h(0)

# Measure the qubit
qc.measure_all()

# Execute the circuit on a simulator
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1024).result()
counts = result.get_counts()

print("Superposition results:", counts)
