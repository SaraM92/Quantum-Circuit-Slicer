#This file defines a new object based on the Qiksit Barrier object.

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.circuit.barrier import Barrier
from qcs.gatefinder import startCount

class BreakPoint(Barrier):
    def __init__(self, ints):
        self.inst = ints
        Barrier.__init__(self,ints)


def breakbarrier(self, *qargs):
        """Apply :class:`~qiskit.circuit.Barrier`. If qargs is None, applies to all."""
        #from .barrier import Barrier
        qubits = []

        if not qargs:  # None
            for qreg in self.qregs:
                for j in range(qreg.size):
                    qubits.append(qreg[j])

        for qarg in qargs:
            if isinstance(qarg, QuantumRegister):
                qubits.extend([qarg[j] for j in range(qarg.size)])
            elif isinstance(qarg, list):
                qubits.extend(qarg)
            elif isinstance(qarg, range):
                qubits.extend(list(qarg))
            elif isinstance(qarg, slice):
                qubits.extend(self.qubits[qarg])
            else:
                qubits.append(qarg)

        return self.append(BreakPoint(len(qubits)), qubits, [])


def startDebug():
	setattr(QuantumCircuit, 'breakbarrier', breakbarrier)
	startCount(QuantumCircuit)
#    return QuantumCircuit

