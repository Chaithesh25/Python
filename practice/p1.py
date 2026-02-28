import numpy as np
# array  = np.arange(1,17).reshape(4,4)

# print(array)

# splite_array = np.array_split(array,2)

# print("\n",splite_array)


# for i , splite_array in enumerate(splite_array,start=1):

#     print(f"Array{i}",splite_array)

x = np.array([[1],[2],[3]])
y = np.array([10,20,30])
print(x)
print(y)

print("broadcasted result = ",x+y)