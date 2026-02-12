'''
Which of the following line of code will throw an error?

Use the code below in order to create the given dataframe:
'''
import pandas as pd

data = {
    'cust_id': [101, 102, 103, 104],
    'name': ['rick', 'morty', 'pickle', 'jerry'],
}

df = pd.DataFrame(data)
print(df)
print(df.isin([101,102,120]))
print(df.isin({'cust_id':[101,102,120]}))
print(df.isin(df.cust_id))
print(df.cust_id)
print(df.name.isin('rick')) # string 