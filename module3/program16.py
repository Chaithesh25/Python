import numpy as np

# Create a 2D array (3 rows, 3 columns)
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


rowwise_sum = np.sum(arr, axis= 1)
colum_mean = np.mean(arr,axis=0)

print(rowwise_sum)
print(colum_mean)