import copy
import numpy as np
arr=np.array([1,2,3,4,5],dtype='object')
print(arr)
new_copy=copy.deepcopy(arr)
new_copy[0]=100
print(new_copy)
print('original array')
print(arr)