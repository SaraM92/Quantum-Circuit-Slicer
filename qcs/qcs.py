import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

from qiskit.circuit.barrier import Barrier
from gatefinder import startCount
from breakbarrier import breakbarrier


def startDebug():
	from qiskit import QuantumCircuit
	setattr(QuantumCircuit, 'breakbarrier', breakbarrier)
	QuantumCircuit = startCount(QuantumCircuit)
	return QuantumCircuit
'''

def startDebug(qc):
	from breakbarrier import breakbarrier
#	from qiskit import QuantumCircuit
	setattr(qc, 'breakbarrier', breakbarrier)
	qc = startCount(qc)
	return qc
#    return QuantumCircuit
'''