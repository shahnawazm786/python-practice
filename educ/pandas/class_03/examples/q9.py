import pandas as pd

def solve(reg_id, reg_dates):
    res_df = pd.DataFrame(zip(reg_id, reg_dates), columns=["RID", "RDate"])
    """
    input:
    reg_id -> id of the input dataframe
    reg_dates -> dates of the input dataframe
    res_df -> the input dataframe 
    
    output:
    return the resultant dataframe after performing the required operation
    """
    
    # Convert RDate to datetime
    res_df["RDate"] = pd.to_datetime(res_df["RDate"])
    
    # Extract Month, Year, and Day
    res_df["RMonth"] = res_df["RDate"].dt.month
    res_df["RYear"] = res_df["RDate"].dt.year
    res_df["RDay"] = res_df["RDate"].dt.day
    
    return res_df