import pandas as pd
import os

#print(os.getcwd())

DIR_PATH=os.getcwd().replace("\\","/");
FILE_PATH='/educ/pandas/class_01/examples/additional/mckinsey.csv'
print("✒️  Path Setup ✒️")
DATA_PAHTS=DIR_PATH + FILE_PATH;
#print(DATA_PAHTS)
print()
print("📋 reading data from mckinsey.csv file")
data=pd.read_csv(DATA_PAHTS)
print("🚨 reading data completed\n")
print("🌟 Data operation has been started\n")
print("🔥 show first 5 records")
print(data.head())
print()
# show last 5 records
print("🔥 show 5 records from bottom")
print(data.tail())
print()

# row and cloumn count
print("🔥 show the number of row of the data set")
print(data.shape[0])
print()
print("🔥 show the number of columns of the data set")
print(data.shape[1])
print()
print("🔥 combined row and columns")
print(data.shape)
print()
