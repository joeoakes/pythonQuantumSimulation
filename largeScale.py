#Creates a 30-qubit quantum circuit with Hadamard (superposition) and CNOT (entanglement).
#Compiles & optimizes the circuit for GPU execution (NVIDIA RTX 4090).

import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
import time

# 🚀 Define a Large-Scale Quantum Circuit (30 qubits)
num_qubits = 30
qc = QuantumCircuit(num_qubits, num_qubits)

# 🌀 Apply Hadamard gates to all qubits (Superposition)
for qubit in range(num_qubits):
    qc.h(qubit)

# 🔗 Apply CNOT gates in a chain (Creating Entanglement)
for qubit in range(num_qubits - 1):
    qc.cx(qubit, qubit + 1)

# 📏 Measure all qubits
qc.measure(range(num_qubits), range(num_qubits))

# 🎯 Optimize for GPU Execution (RTX 4090)
simulator = AerSimulator(method='statevector', device='GPU')  # Use NVIDIA GPU
compiled_circuit = transpile(qc, simulator)

# 🏎 Run the Quantum Circuit on the GPU
start_time = time.time()
result = simulator.run(compiled_circuit, shots=10_000).result()
end_time = time.time()

# 📊 Display Results
counts = result.get_counts()
print(f"Measurement Outcomes (sampled): {dict(list(counts.items())[:10])}")  # Show first 10 results
print(f"Simulation Time: {end_time - start_time:.2f} seconds")
