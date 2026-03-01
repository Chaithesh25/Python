import numpy as np
def calculate(arr1,arr2):
    sum  = arr1 + arr2
    diff = arr1 - arr2
    mul = arr1 * arr2

    return sum , diff , mul




array1 =np.array([[19,12],
          [24,65]
          ])

array2 =np.array([[93,45],
          [65,32]])

sum , diff , mul = calculate(array1,array2)

print("sum: ",sum)
print("diff: ",diff)
print("multiplication :",mul)