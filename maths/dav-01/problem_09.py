import numpy as np
def seq(start, length, step):
    ''' start, length and step are in form of integers all representing the attributes as their names suggest
        output -> A numpy array is expected to be returned'''

    # YOUR CODE GOES HERE
    
    sequence =np.arange(start, start + length * step, step)
    
    return sequence