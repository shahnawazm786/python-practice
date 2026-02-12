import numpy as np

def specific_elements(mat1, mat2, r1, r2, c1, c2):
    '''mat1, mat2 are the two 2d numpy arrays
       r1, r2 are the start and end of rows indices
       c1, c2 are the start and end of columns indices
       Output -> Return a numpy array according to indices'''
    
    # STEP 1: Check whether matrix multiplication is possible
    if mat1.shape[1] != mat2.shape[0]:
        return -1
    
    # STEP 2: Perform matrix multiplication
    matmul_array = np.matmul(mat1, mat2)
    
    # STEP 3: Slice the array based on given ranges (end index excluded)
    result = matmul_array[r1:r2, c1:c2]
    
    return result