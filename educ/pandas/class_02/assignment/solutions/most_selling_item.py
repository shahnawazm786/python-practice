import pandas as pd
SALES_FILE='educ\pandas\class_02\data\sales.csv'.replace('\\','/')
sales=pd.read_csv(SALES_FILE)
print(sales)
print(sales.columns)
df=sales
#print(df['Description'].value_counts())
#print(sales[sales['StockCode']=='85123A'])
most_selling_product=sales[sales['Quantity']>0].groupby('Description')['Quantity'].sum()
print(most_selling_product.sort_values())
#print(most_selling_product.sort_values(ascending=False))
#print(sales[sales['Quantity']<0][['StockCode','Description','Quantity']])