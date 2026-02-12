import numpy as np

def split(arr):
    '''
    INPUT: arr -> 2D array
    OUTPUT: subarrays -> list of 2D arrays
    '''
    
    arr = np.array(arr)
    
    # Split column-wise using slicing
    first = arr[:, :2]     # first 2 columns
    second = arr[:, 2:3]   # 3rd column
    third = arr[:, 3:]     # remaining columns
    
    subarrays = [first, second, third]
    
    return subarrays