#This file includes the gatefinder functions, these functions track where every gate was added to the circuit in order

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import inspect
import traceback

def startCount(Cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.decorated_obj = Cls(*args, **kwargs)
            self.gateInfo = dict()
        def __getattribute__(self, s):
            #print("here", s)
            #print("========")
            try:
                x = super().__getattribute__(s)
                return x
            except AttributeError:
                pass
            x = self.decorated_obj.__getattribute__(s)
            #print("x is", x)
            #print("======")
            #s is the name of the method
            #print(s)
            if type(x) == type(self.__init__) and str(x).find("method") != -1: #s==gate2check:  # it is an instance method
                if s not in self.gateInfo.keys():
                    self.gateInfo[s] = [traceback.extract_stack()[-3:-1]]
                else:
                    self.gateInfo[s].append(traceback.extract_stack()[-3:-1])  
                #print(traceback.extract_stack()[-3:])
                #print(self.gateInfo)
                return x  # this is equivalent of just decorating the method with print_method         
            else:
                return x
    return Wrapper 


def gateLoc(qc, gateName):
    #print(gateInfo)
    gateOccur = len(qc.gateInfo[gateName])
    l = qc.gateInfo[gateName][0]
    print("--------------------------")
    print("There are", gateOccur, "occurances of gate", gateName, ".\nThey were added to the circuit in the following locations:")
    print(*traceback.format_list(l), sep='\n')
    print("--------------------------")
    #return qc.gateInfo
