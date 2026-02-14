import pandas as pd
def solve(string):
    """
    returns a series object with word count as values and words as the indices.
    """
    # store the frequency of the strings in a series
    words = string.split()
    freq = pd.Series(words).value_counts()
    # sort the indices
    res = freq.sort_index()
    
    return res