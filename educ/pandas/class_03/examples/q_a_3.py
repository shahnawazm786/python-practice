# Extract hour from pickup datetime
import pandas as pd
df=pd.DataFrame([['2019-03-23 20:21:09', '2019-03-23 20:27:24', 1, 1.6], ['2019-03-04 16:11:55', '2019-03-04 16:19:00', 1, 0.79], ['2019-03-27 17:53:01', '2019-03-27 18:00:25', 1, 1.37], ['2019-03-10 01:23:59', '2019-03-10 01:49:51', 1, 7.70], ['2019-03-30 13:27:42', '2019-03-30 13:37:14', 3, 2.16]], columns = ['pickup', 'dropoff', 'passengers', 'distance'])

def timeOfDay(df):
    # Your Code Goes Here
    # Extract hour from pickup datetime
    hours = df['pickup'].dt.hour

    # Create time_of_day column
    df['time_of_day'] = pd.cut(
        hours,
        bins=[0, 6, 12, 18, 24],
        labels=['morning', 'day', 'afternoon', 'night'],
        right=False,
        include_lowest=True
    )

    # Count pickups and sort descending
    result = df['time_of_day'].value_counts().sort_values(ascending=False)

    # 🔑 Fix metadata to match expected output
    result.index.name = 'time_of_day'
    result.name = 'pickup'
    
    return result # a pandas series containing the number of pickups for each time_of_day. Sort the counts in descending order.