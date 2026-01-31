import pandas as pd
SALES_FILE='educ\pandas\class_02\data\sales.csv'.replace('\\','/')
sales=pd.read_csv(SALES_FILE)
#print(sales)
print(sales.columns)
'''
Mention the Invoice number and Customer ID of the highest amount of purchase based on the given Sales data?
'''

print(sales[['Price','Quantity','Customer ID','Invoice']])

print(sales['Quantity']*sales['Price'])
print(sales.shape)
print(sales['Price'].shape)
print(sales['Quantity'].shape)
df=sales.copy(deep=True)
print(df)
df['Total_Price']=df['Price'] * df['Quantity']
print(df.columns)
customer_invoice_number=df.groupby(['Invoice','Customer ID'])['Total_Price'].sum()
print(customer_invoice_number.sort_values(ascending=False).max())