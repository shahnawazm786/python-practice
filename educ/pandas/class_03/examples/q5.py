import pandas as pd

def generate_pivot_table(data):
    '''
    input:
    data -> the dataframe provided to the function
    
    output:
    result -> the pivoted data required by question
    '''
    result = None
    
    # Your Code Starts here
    result = pd.pivot_table(
        data,
        index='Region',
        values='Sales',
        aggfunc='sum',
        fill_value=0
    )
    
    # Sort rows and columns alphabetically
    result = result.sort_index(axis=0).sort_index(axis=1)
    return result


    

