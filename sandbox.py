import numpy as np
import json
from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = QasmSimulator()

ent_reg = QuantumRegister(2)
ent = QuantumCircuit(ent_reg, name='entangler')
ent.h(ent_reg[0])
ent.cx(ent_reg[0],ent_reg[1])
ent.x(ent_reg[0])

i=-1

# Create a Quantum Circuit acting on the q register
qr = QuantumRegister(2)
cr = ClassicalRegister(8)
c = QuantumCircuit(qr,cr)

c.x(qr[1])

c.measure(qr[0],(i:=i+1))
c.measure(qr[1],(i:=i+1))
c.z(qr[0])
c.measure(qr[0],(i:=i+1))
c.measure(qr[1],(i:=i+1))
c.cy(qr[0],qr[1])
c.measure(qr[0],(i:=i+1))
c.measure(qr[1],(i:=i+1))
c.z(qr[0])
c.measure(qr[0],(i:=i+1))
c.measure(qr[1],(i:=i+1))
# c.measure(qr[1],(i:=i+1))
# c.y(qr[1])
# c.measure(qr[1],(i:=i+1))

# c.measure(qr[2],(i:=i+1))
# c.x(qr[2])
# c.measure(qr[2],(i:=i+1))

# c.h(qr[0])
# c.cy(qr[0],qr[1])

# c.measure(qr[0],(i:=i+1))
# c.measure(qr[1],(i:=i+1))

# c.z(qr[0])

# c.measure(qr[0],(i:=i+1))
# c.measure(qr[1],(i:=i+1))

# circuit.append(ent,[qr[0],qr[1]])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(c, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print(c)
for key in counts.keys():
    registers=list(key[::-1])
    iters=[]
    for i in range(0,len(registers)):
        iters+=str(i)
    print("+-"*(len(registers)+1)+"+")
    print("|c|"+"|".join(iters),end="")
    print("|")
    print("+-"*(len(registers)+1)+"+")
    print("|v|"+"|".join(registers),end="")
    print("|")
    print("+-"*(len(registers)+1)+"+")
