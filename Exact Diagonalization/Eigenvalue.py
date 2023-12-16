from Exactdia import *
import pandas as pd


# H1 = Hamiltonian(5, 1)
# E, V = eig(H1)
# E = np.sort(E)
# print(E)
Dimension = [5, 10, 15, 20, 25, 30]
G = np.array([1,2,3])
Dimension = np.array(Dimension)
D = 1/Dimension
E = np.zeros((3,6))
c = 0
eV = []
for i in Dimension:
    H = Hamiltonian(i, 4)
    E1, V = eig(H)
    E1 = np.sort(E1)
    E[0][c] = E1[0]
    E[1][c] = E1[1]
    E[2][c] = E1[2]
    c = c + 1
    eV.append(V)


np.save('g1Eigenvalues.npy', E)
# with open("EV.txt", "w") as output:
#     output.write(str(eV))