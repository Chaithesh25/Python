import numpy as np

# Create two NumPy arrays
A = np.array([10, 20, 30, 40])
B = np.array([25, 15, 35, 5])

# Element-wise maximum
max_array = np.maximum(A, B)

# Element-wise minimum
min_array = np.minimum(A, B)

# Print results
print("Array A:", A)
print("Array B:", B)
print("Element-wise Maximum:", max_array)
print("Element-wise Minimum:", min_array)
