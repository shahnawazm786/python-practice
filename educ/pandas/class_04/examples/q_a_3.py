import pandas as pd
import PATH

sales=pd.read_csv(PATH.SALES_PATH)
print(sales)
print(sales.info())
sales['InvoiceDate'] = pd.to_datetime(sales['InvoiceDate'])
result =sales[sales['InvoiceDate'].dt.date == pd.to_datetime('2011-06-22').date()]['Customer ID'].nunique()
print(result)