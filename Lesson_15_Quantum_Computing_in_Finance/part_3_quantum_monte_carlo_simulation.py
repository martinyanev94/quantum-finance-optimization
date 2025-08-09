from qiskit import QuantumCircuit, Aer, transpile

def quantum_monte_carlo_sim(num_simulations):
    qc = QuantumCircuit(3)  # Create a quantum circuit with 3 qubits
    
    # Initialize the circuit for simulations
    for i in range(num_simulations):
        qc.h([0, 1, 2])  # Apply Hadamard gate for superposition

    # Transpile circuit for efficient execution
    transpiled_qc = transpile(qc, basis_gates=['u3', 'cx'])
    return transpiled_qc
