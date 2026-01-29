import pandas as pd

df1 = pd.DataFrame({
    'cust_id': [101, 102, 103, 104],
    'name': ['rick', 'morty', 'pickle', 'jerry']})

df2 = pd.DataFrame({
    'order_id': ['OR1', 'OR3', 'OR23', 'OR42'],
    'cust_id': [102, 105, 101, 102],
    'amount': [1200, 650, 120, 989]})

print(df1)
print(df2)
#print(pd.concat([df1,df2],axis=1))
#print(df1.join(df2))
print(pd.merge(df1, df2, on='cust_id'))