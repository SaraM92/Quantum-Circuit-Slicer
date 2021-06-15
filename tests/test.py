from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qcs import startDebug
from slicer import Vslicer, Hslicer
from  gatefinder import gateLoc

def Quan_full_adder(qc, in_qbits,zero_qubit): # a function to build a simple full-adder circuit
    #in_qbits = QuantumRegister(3,name='input')
    print(len(in_qbits))
    #zero_qubit = QuantumRegister(1,name='zero')
    #qc = QuantumCircuit(in_qbits,zero_qubit)
    qc.ccx(in_qbits[0],in_qbits[1],zero_qubit)
    qc.cx(in_qbits[0],in_qbits[1])
    qc.breakbarrier() #insert breaks into the circuit
    qc.ccx(in_qbits[1],in_qbits[2],zero_qubit)
    qc.cx(in_qbits[1],in_qbits[2])
    qc.cx(in_qbits[0],in_qbits[1])
    qc.breakbarrier() #insert breaks into the circuit
    qc.ccx(in_qbits[1],in_qbits[2],zero_qubit)
    qc.cx(in_qbits[1],in_qbits[2])
    qc.cx(in_qbits[0],in_qbits[1])
    qc.breakbarrier() #insert breaks into the circuit
    qc.ccx(in_qbits[1],in_qbits[2],zero_qubit)
    qc.cx(in_qbits[1],in_qbits[2])
    qc.cx(in_qbits[0],in_qbits[1])
    return qc


#start debug mode of the quantum circuit
QuantumCircuit = startDebug()

#Create the circuit
in_qbits = QuantumRegister(3,name='input')
zero_qubit = QuantumRegister(1,name='zero')
qc = QuantumCircuit(in_qbits,zero_qubit)
out_full = Quan_full_adder(qc,in_qbits,zero_qubit)
out_full.draw(output='mpl')


#test the slicer
slices = Vslicer(out_full)

#get information about the control-not gates in circuit
gateLoc(qc,'cx')