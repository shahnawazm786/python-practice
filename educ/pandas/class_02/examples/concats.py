import pandas as pd
import numpy as np
data={
        'emp_id':list(np.arange(1001,1006,1,dtype='int')),
        'name':['Rahman','Sariq','Kalam','Abdul','Majeed'],
        'salary':list(np.linspace(40000,250000,5)),
        'designation':['HR Admin','Software Engineer','Sr. Manager','Vice Persident','Director'],
        'location':['India','USA','France','Saudi Arabia','Iran']
    }
print('🔥 Data ')
print(data)
df=pd.DataFrame(data)
print('🔥 DataFrame')
print(df)
print()
data1={
        'emp_id':tuple(np.arange(1001,1011,1,dtype='int')),
        'continent':['Asia','Asia','Europe','Middle East','America','Austrelia','Aferica','Europe','America','Middle East']

    }
print(data1)
df1=pd.DataFrame(data1)
print(df1)
print('🔥 concat column wise')
emp_continent_axis_1=pd.concat([df,df1],axis=1)
print(emp_continent_axis_1)
print('🔥 concat row wise')
emp_continent_axis_0=pd.concat([df,df1],axis=0)
print(emp_continent_axis_0)
