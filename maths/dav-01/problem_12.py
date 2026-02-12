import numpy as np
def get_elements(arr):
    '''
    INPUT: arr -> 1D numpy array
    
    OUTPUT elements -> tuple of first and last element.
    '''
    
    first_element = arr[0]
    
    last_element = arr[-1]
    
    return (first_element, last_element)