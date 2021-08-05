# This file includes the slicer functions
from qcs.workfuncs import get_barrier_locs, slice_list_with_indeces, remove_barrier
import warnings
import re
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
warnings.filterwarnings("ignore", category=UserWarning)

#Function for vertical slicer
def Vslicer(inputCir, mode="mini"): 
    gates_list = inputCir.data #Get circuit data (gates)
    #print(gates_list)
    barrier_locs = get_barrier_locs(gates_list) #Obtain locations of barriers
    slicedCir = slice_list_with_indeces(gates_list,list(barrier_locs.values())) #Slice circuit based on barrier locs
    cleanCir = remove_barrier(slicedCir) #Remove barrier from slices
    qubitsInCir = str(inputCir.qubits) #get quantum registers from circuit
    pattern = r"QuantumRegister\(\d+,\s*'\w+'\)"
    #Get the registers in the circuit and their sizes
    #Change to {name:[type, size]}
    result = re.findall(pattern,qubitsInCir)
    result = sorted(set(result), key=lambda x: result.index(x))
    qunRegs = {}
    for i in list(result):
        info = i[16:-1].split(', ')
        qunRegs [info[1][1:-1]] = info[0] #to remove the ''
    #Build a circuit for the debugging using the names and sizes of the original registers names
    #print(qunRegs)
    Dcir = QuantumCircuit()
    for key in qunRegs.keys():
        Dcir.add_register(QuantumRegister(qunRegs[key],name=key))
        #print(Dcir.qubits)
        cirList = []
    for cir in cleanCir:
        count = 1
        cirName = "sub circuit" + str(count)
        temp = Dcir.copy(name=cirName)
        for gate in cir:
            temp.append(gate[0],qargs=gate[1])
        cirList.append(temp)
        count += 1                 
    if mode == "mini": #This mode generates seperate mini circuits
        return cirList
    elif mode == "accom": #accomulated circuits
        cirListAcc = [cirList[0]]
        for i in range(1,len(cirList)):
            count = 2
            cirName = "sub circuit" + str(count)
            temp = cirListAcc[i-1].copy(name=cirName)
            temp.extend(cirList[i])
            cirListAcc.append(temp)
            count += 1
        return cirListAcc
    else:
        return "Invalid mode"


#Function for horizontal slicer, this slicer removes unused qubits from input circuits (it is better to use this after the Vslicer)
def Hslicer(cirSlice): #Add register name
    d = cirSlice.data #Get slice data (gates and registers)
    pattern = r"QuantumRegister\(\d+,\s*'\w+'\)"
    # Get the registers in the circuit and their sizes
    # Change to {name:[type, size]}
    result = re.findall(pattern, str(d))
    result = sorted(set(result), key=lambda x: result.index(x))
    qunRegs = {}
    for i in list(result):
        info = i[16:-1].split(', ')
        qunRegs[info[1][1:-1]] = info[0]  # to remove the ''
        # Build a circuit for the debugging using the names and sizes of the original registers names
    #print(qunRegs)
    sub_slices = []
    for reg in qunRegs.keys():
        temp_reg = QuantumRegister(int(qunRegs[reg]), name=reg)
        temp_cir = QuantumCircuit(temp_reg)
        for gate in cirSlice:   
            if str(gate[1]).find(reg) != -1:            
                temp_cir.append(gate[0], qargs=gate[1])
        sub_slices.append(temp_cir)
    return sub_slices
