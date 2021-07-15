# Quantum Circuit Slicer (QCS)


This repo contains files to add a quantum circuit slicer to Qiskit. The slicer provides some useful functions for debugging quantum circuits.

The circuit slicer includes:
1. The addition of the "breakbarrier" object, which acts as a breakpoint for quantum circuits.
2. Vslicer function to divide the circuit vertically.
3. Hslicer to remove unused qubits in a particular slice.
4. Gate tracking when you enter debugging mode by calling the startDebug function.
5. Perform queries on a specific gate within a circuit.


Instructions
---
### Installation
To use the circuit slicer, you need to have a working version of Qiskit (version 0.19.6 or higher)

`pip install quantum-circuit-slicer`

### Test
Once the package is installed, try running the file test.py to make sure eveything is installed and working properly, and how to use the slicer.
