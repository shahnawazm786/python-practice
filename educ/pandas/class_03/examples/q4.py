import pandas as pd
def healthExp(df):
    # Define bins and labels
    bins = [1969, 1980, 1990, 2000, 2010, 2021]

    # Create year bins
    df['Year'] = pd.cut(df['Year'], bins=bins)

    # Group and calculate average expenditure
    result = (
        df.groupby('Year')['Spending_USD']
          .mean()
          .round(3)
          .to_frame(name='avg_expenditure')
    )

    return result