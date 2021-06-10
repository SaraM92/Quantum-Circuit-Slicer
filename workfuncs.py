#This file includes some functions that help cleanup the gates list before slicing
import warnings
#from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
warnings.filterwarnings("ignore", category=UserWarning)



#Function to obtain barrier locations
def get_barrier_locs(getesList):
    barrier_locs = {}
    count = 1
    for i in range(len(getesList)):
        if "BreakPoint" in str(getesList[i][0]):
            #print(str(gates_list[i][0]))
            key = "BreakPoint" + str(count)
            #print(key)
            barrier_locs[key] = i
            count += 1
    return barrier_locs  

#Create sub-circuits based on carrier locations
def slice_list_with_indeces(targetList, indecesList):
    size = len(targetList) 
    res = [targetList[i: j] for i, j in
        zip([0] + indecesList, indecesList + ([size] if indecesList[-1] != size else []))] 
    return res

#Remove "BreakPoint" for sub-circuits
def remove_barrier(subCirList):
    cleanList = []
    for cir in subCirList:
        temp = []
        for j in cir:
            if "BreakPoint" not in str(j):
                temp.append(j)
        cleanList.append(temp)
    return cleanList