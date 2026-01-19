import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
arr[::2] = range(10,50,10)
print(arr)