def solve(df):
    # Split the single column into City and State
    df[['City', 'State']] = df.iloc[:, 0].str.split('\t', expand=True)
    
    # Drop the original combined column
    df = df.drop(df.columns[0], axis=1)
    
    return df