import numpy as np
arr=np.array([1,'m',[100,200,300]],dtype='object')
print(arr)
print('deep copy')
arr_copy=arr.copy()
print(arr_copy)
print('change the value at 0 index')
arr_copy[2][0]=500

print('After change')
print(arr_copy)

print('Check the original array')
print(arr)
