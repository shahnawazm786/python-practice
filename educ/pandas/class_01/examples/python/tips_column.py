import pandas as pd
TIPS_FILE_LOC='educ/pandas/class_01/examples/python/tips.csv'
tips=pd.read_csv(TIPS_FILE_LOC)
print(tips)
#print(pd.DataFrame(tips, columns=['time', 'total_bill', 'tip']))
df1=pd.DataFrame(tips)
#print(df[['time','total_bill','top']])
#print(df1.loc[:,['time','total_bill','top']])
print(df1.iloc[:,0:2])