import numpy as np
import time
a=[1,2,3,4,5]
res= [i**2 for i in a]
print(res)
arr=np.array(a)
print(arr**2)
l=range(100000)
start=time.time()
res1=[i**2 for i in a]
print(res1)
end=time.time()
print(end-start,'seconds')
