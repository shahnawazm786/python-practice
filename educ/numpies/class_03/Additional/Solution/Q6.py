import numpy as np

def add_padding(mat):
    '''mat-> NumPy array
       output-> NumPy array is expected to be returned'''
    
    # Add a layer of zeros on all sides
    res = np.pad(mat, pad_width=1, mode='constant', constant_values=0)
    
    return res