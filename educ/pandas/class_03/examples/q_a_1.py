import pandas as pd
data=pd.read_csv('educ/pandas/class_03/examples/sales.csv')
print(data)
print(data.head())
print(data.columns)
print(data[['Quantity','Country','Price']])
data['Total']=data['Quantity'] * data['Price']
print(data[['Quantity','Price','Total','Country']])
print(data[data['Country']=='France'].max()['InvoiceDate'])