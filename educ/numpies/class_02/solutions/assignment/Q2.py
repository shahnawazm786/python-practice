import numpy as np

def extract_subarray(arr):
    '''
    INPUT: arr -> 2D array
    OUTPUT: result -> 2D array
    '''
    
    arr = np.array(arr)
    
    ### STEP 1: Get the rows (2nd to 4th row)
    row_array = arr[1:4]
    
    #### STEP 2: Get the last 3 columns from the row array
    cols_array = row_array[:, -3:]
    
    #### STEP 3: Reverse the rows in cols array
    result = cols_array[::-1]
    
    return result

arr = [
    [ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11],
    [12, 13, 14, 15],
    [16, 17, 18, 19]
]
print(extract_subarray(arr))