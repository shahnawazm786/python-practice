import numpy as np

def split(arr, k):
    '''
    INPUT: arr, k
    OUTPUT: split_arr -> list of arrays
    '''
    
    # Convert input to NumPy array (if not already)
    arr = np.array(arr)
    
    # Split array into k equal parts
    split_arr = list(np.split(arr, k))
    
    return split_arr