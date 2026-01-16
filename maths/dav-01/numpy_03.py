import numpy as np
arr=np.arange(1,10,2)
print(arr)
print('🌟 Converting array into 1D array')
array_1D=np.array(arr)
print(array_1D)
print('🚨 Details of 1D array')
print(f'📌 Dimension of array->\t{array_1D.ndim}')
print(f'📌 Element of array ->\t{array_1D.size}')
print(f'📌 Shape of array ->\t {array_1D.shape}')
print('🌟 Creating array 2D array from 1D array')
array_2D= np.array(array_1D)
print('🚨 Details of 2D array')
print(f'📌 Dimension of array->\t{array_2D.ndim}')
print(f'📌 Element of array ->\t{array_2D.size}')
print(f'📌 Shape of array ->\t {array_2D.shape}')


