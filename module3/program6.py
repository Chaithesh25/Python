import numpy as np


def convertt(array1):
    int_arr = array1.astype(int)
    bool_arr = array1.astype(bool)


    return int_arr,bool_arr

float_arrayy = np.random.uniform(0,10,20)
print("original arraya: \n",float_arrayy)


intarray , booleanarray  = convertt(float_arrayy)

print("int array: ",intarray)
print("bolean  array: ",booleanarray)