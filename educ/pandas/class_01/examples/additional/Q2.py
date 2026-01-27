import pandas as pd
def select_row(df,r1,r2):
    import pandas as pd
def select_rows(df, r1, r2):
    '''
    input:
    df -> the dataframe provided to the function
    r1 -> the starting index of the rows to be selected
    r2 -> the ending index of the rows to be selected
    
    output:
    df_new -> the selected rows of the dataframe
    '''
    
    # Select the rows r1 to r2
    df_selected = df.iloc[r1:r2]
    
    # Select the columns "name" and "amt"
    #df_new = df_selected[['name', 'amt']].reset_index(drop=True)
    df_new = df_selected[['name', 'amt']]
    
    return df_new

