import numpy as np
a = np.array([[6, 28], [8, 56], [7, 19]])
x = np.transpose(a).reshape(1,6)
print(x)