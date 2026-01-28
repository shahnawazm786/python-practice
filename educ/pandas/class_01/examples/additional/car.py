import pandas as pd
data=pd.read_csv('educ/pandas/class_01/examples/additional/mtcars.csv')
#print(data)
#print(data['disp'])
#print(data.loc[:,'disp'])
#print(data.iloc[:,'disp'])
print(data.loc['disp':])