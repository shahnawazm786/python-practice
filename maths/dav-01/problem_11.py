import numpy as np

def create_seq(start, end, step):
    '''
    INPUT: start, end, step 
    OUTPUT: arr -> 1D numpy array
    '''
    
    arr = np.round(np.arange(start, end, step), 2)
    
    return arr