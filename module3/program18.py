import numpy as np

arr1 = np.array([
    [12,23,34],
    [76,32,56]
])

arr2 = np.array([
    [34,21],
    [22,45],
    [87,43]
])


print(arr1)
print(arr2)

result = np.matmul(arr1,arr2)

print(result)