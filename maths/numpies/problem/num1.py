import numpy as np
x = np.array([-5, 9 , 20 , 25, -3, 5, 16, 10])
x[(x >= -5) & (x <= 15)] *= -1
print(x)