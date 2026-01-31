'''
Find out the number of unique StockCode in the United Kingdom according to the given Sales data?
'''
import pandas as pd
SALES_FILE='educ\pandas\class_02\data\sales.csv'.replace('\\','/')
sales=pd.read_csv(SALES_FILE)
#print(sales)
print(sales.columns)
print(sales['StockCode'].nunique())