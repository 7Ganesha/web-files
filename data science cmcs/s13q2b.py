import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Flatten the array
flat_arr = arr.flatten()

# Find the maximum and minimum values
max = np.max(flat_arr)
min = np.min(flat_arr)

# Print the results
print(arr)
print(flat_arr)
print(max)
print(min)
