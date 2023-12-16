# values = ['1', '2', '3']

# with open("file.txt", "w") as output:
#     output.write(str(values))

import numpy as np
import pandas as pd

# # Create a 2D NumPy array
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# # Convert the array to a DataFrame
# df = pd.DataFrame(arr)

# # Save the DataFrame to a CSV file
# df.to_csv('myarray.csv', index=False, header=False)

# Create a NumPy array
# arr = np.array([1, 2, 3, 4, 5])

# Save the array to a binary file
# np.save('myarray.npy', arr)

# Load the saved array
arr_loaded = np.load('g1Eigenvalues.npy')
print(arr_loaded)