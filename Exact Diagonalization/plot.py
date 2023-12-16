import matplotlib.pyplot as plt
import numpy as np
Dimension = [5, 10, 15, 20, 25, 30]
Dimension = np.array(Dimension)
D = 1/Dimension
D = np.sort(D)

arr_loaded = np.load('g1Eigenvalues.npy')
print(arr_loaded)
print(D)
plt.plot(D, arr_loaded[0][:], label = "Ground state")
plt.plot(D, arr_loaded[1][:], label = "first state")
plt.plot(D, arr_loaded[2][:], label = "second state")
plt.xlabel("1/D")
plt.ylabel("Eigenvalues")
plt.title("Quadratic harmonic ocsilator")
plt.legend()
plt.show()