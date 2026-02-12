import numpy as np

def filter_marks(marks):
    '''
    INPUT: marks -> 1D array
    
    OUTPUT: filtered_marks -> 1D array
    '''
    
    ### Step 1 Get the mask for marks > 40
    
    mask = marks > 40
    
    ### STEP 2 use the mask to filter the array
    
    filtered_array = marks[mask]
    
    return filtered_array