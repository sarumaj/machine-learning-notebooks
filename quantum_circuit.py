from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram, circuit_drawer

# Create a Quantum Circuit acting on a quantum register of two qubits
qc = QuantumCircuit(2)

# Applying operations as per the provided pseudo code
qc.h(0)                  # Hadamard gate on qubit 0
qc.cx(0, 1)              # CNOT gate with qubit 0 as control and qubit 1 as target
qc.y(0)                  # Y gate on qubit 0
qc.cx(0, 1)              # Another CNOT gate with qubit 0 as control and qubit 1 as target
qc.h(0)                  # Another Hadamard gate on qubit 0
qc.measure_all()         # Measure both qubits

# Textual representation
print(qc)

# Matplotlib drawing
qc.draw('mpl')

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator and get the results
job = execute(qc, simulator, shots=1000)
result = job.result()

# Get counts of outcomes
counts = result.get_counts(qc)

# Display the circuit and histogram of the result
print(counts)
