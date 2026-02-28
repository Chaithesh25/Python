import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Scalar value
scalar = 10

# Element-wise addition using broadcasting
result = arr + scalar

print("Original Array:\n", arr)
print("Scalar:", scalar)
print("Result after addition:\n", result)
