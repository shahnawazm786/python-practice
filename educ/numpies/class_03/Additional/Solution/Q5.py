import numpy as np

def rearrange_image(data, num_splits):
    # Split the image into equal horizontal sections
    sections = np.array_split(data, num_splits, axis=0)
    
    # Rearrange: move last section to the front
    rearranged = [sections[-1]] + sections[:-1]
    
    # Concatenate back into a single array
    return np.vstack(rearranged)