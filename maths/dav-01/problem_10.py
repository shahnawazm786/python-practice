import numpy as np

def get_array_properties(arr):
    '''
    INPUT: arr -> A nD array
    OUTPUT: result -> tuple consisting of shape and dimension
    '''
    
    ## STEP 1. Get the shape of array
    shape = arr.shape
    
    ## STEP 2. Get the dimension of array
    dim = arr.ndim
    
    return shape, dim