import numpy as np

def reverse_columns(arr):
    arr = np.array(arr)
    return arr[:, ::-1]

arr = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
print(reverse_columns(arr))