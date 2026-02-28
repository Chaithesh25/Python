import numpy as np

arr = np.random.randint(1,21,size=(4,4))
print("orignial array: \n",arr)

#accesing the element
print("element at (1,2)",arr[0,0])

#accesing the first row
print("element at first row: ",arr[0])

#changing the element
arr[0,0] = 120
print(arr)


#slicing 
sliced_array = arr[0:3,0:4]
print("sliced array\n",sliced_array)