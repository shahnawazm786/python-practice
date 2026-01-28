import pandas as pd
import os

print(os.getcwd())

DIR_PATH=os.getcwd().replace("\\","/");
FILE_PATH='/educ/pandas/class_01/examples/additional/mckinsey.csv'

DATA_PAHTS=DIR_PATH + FILE_PATH;
print(DATA_PAHTS)

# show first 5 records 
data=pd.read_csv(DATA_PAHTS)
print(data.head())



