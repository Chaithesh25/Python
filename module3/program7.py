# Create a 2D NumPy array
original_array = np.array([[1, 2, 3],
                           [4, 5, 6]])

print("Original Array:")
print(original_array)

# Flatten the array
flat_array = flatten_array(original_array)
print("\nFlattened Array:")
print(flat_array)

# Reshape back to original shape
reshaped_array = flat_array.reshape(original_array.shape)
print("\nReshaped Back to Original:")
print(reshaped_array)
