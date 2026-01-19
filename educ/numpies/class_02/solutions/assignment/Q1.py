import numpy as np

def check_conditions(arr, k):
    '''
    INPUT: arr, k
    OUTPUT: result -> bool
    '''
    
    ## STEP 1 : Create mask for the given condition
    mask = (arr % 2 == 0) & (arr > k)
    
    ## STEP 2: Use logical function on mask
    result = np.all(mask)
    
    return result

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
k = 3
print(check_conditions(arr, k))

arr = np.array([8, 12, 16, 20])
k = 4
print(check_conditions(arr, k))