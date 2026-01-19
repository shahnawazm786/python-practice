import numpy as np
def reverse_columns(arr):
    return np.flip(arr, axis=1)
arr = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
print(reverse_columns(arr))