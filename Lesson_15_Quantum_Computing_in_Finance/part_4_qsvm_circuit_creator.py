from qiskit import QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, LinearLayer

def create_qsvm_circuit(data):
    feature_map = ZZFeatureMap(feature_dimension=len(data[0]), entanglement='linear')
    qc = QuantumCircuit(feature_map.num_qubits)

    # Encode data
    for x in data:
        qc.append(feature_map.bind_parameters(x), range(len(x)))

    # Apply linear layer for classification
    linear_layer = LinearLayer(num_qubits=feature_map.num_qubits, weight=1.0)
    qc.append(linear_layer, range(feature_map.num_qubits))

    return qc
