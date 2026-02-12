import pandas as pd
def lifeExp(df):
    #Your Code Goes Here
    melted_df = df.melt(
    id_vars=['Country'],
    var_name='Year',
    value_name='Life_Expectancy'
)

# Calculate average life expectancy per year
    avg_life = (
        melted_df
        .groupby('Year')['Life_Expectancy']
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

# Convert to dataframe with required format
    result = avg_life.to_frame()


    return result # a dataframe containing 5 rows with Year as index and Life Expectancy as a column, sorted in descending order of average life expectancy.
    # Note that the Life Expectancy column in the output represents the avarage life expectencies for different years.