from qiskit import QuantumCircuit

def create_qaoa_circuit(graph, depth):
    num_qubits = len(graph.nodes)
    qc = QuantumCircuit(num_qubits)

    # Apply initial layer
    for qubit in range(num_qubits):
        qc.h(qubit)

    # Apply QAOA layers
    for _ in range(depth):
        # Problem Hamiltonian (cost operator)
        for edge in graph.edges:
            qc.cx(edge[0], edge[1])
        
        # Mixing Hamiltonian (mixing operator)
        for qubit in range(num_qubits):
            qc.rx(2 * gamma, qubit)

    return qc
