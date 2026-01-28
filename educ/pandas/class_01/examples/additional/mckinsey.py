import pandas as pd
import sys
print(sys.path)
data=pd.read_csv('educ/pandas/class_01/examples/additional/mckinsey.csv')
print(data)
#df=data.copy()
print(data.loc[1])
print(data.iloc[1])
