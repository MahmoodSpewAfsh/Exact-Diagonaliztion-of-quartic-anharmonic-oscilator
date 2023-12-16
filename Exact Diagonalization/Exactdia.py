import numpy as np
from numpy.linalg import eig


# Here I define my Function that generates the matrix


def Hamiltonian(D, g):

    H = np.zeros((D,D))

    for i in range(0, D):
        for j in range(0, D):
            if i == j:
                H[i][j] = g/16 * (3 + 6*i + 6 * i**2) + i + 0.5
            if i == j-2:
                H[i][j] = g/16 * 2 * (2 * j - 1) * np.sqrt(j * (j-1))
            if i == j-4:
                H[i][j] = g/16 * np.sqrt(j * (j-1) * (j-2) *(j-3))
            if i == j+2:
                H[i][j] = g/16 * 2 * (3 + 2 * j) * np.sqrt((j+1)*(j+2))
            if i == j+4:
                H[i][j] = g * np.sqrt(((j+1)*(j+2)*(j+3)*(j+4)))/16
    return H

# print(Hamiltonian(10,4))