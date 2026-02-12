import pandas as pd
import numpy as np
#[4969, 6642, 6001, 5196, 3109, 6376, 3851, 3825, 5997, 3881]
#list(np.random.randint(3000,7000,size=10))
employee={
    'emp_id':[4969, 6642, 6001, 5196, 3109, 6376, 3851, 3825, 5997, 3881],
    'ename':['Scott','Jabreel','Minhaj','Nick','Rajesh','Kamar','King','Sajid','Badar','Imam'],
    'jobs':['Analyst','Engineer','HR Admin','Salesman','Teacher','Principal','Salesman','Engineer','Analyst','HR Admin'],
    'mrg':[6642,3881,6642,6642,5196,5196,5196,None,6642,5196],
    'comm':[100,None,None,300,250,None,500,None,None,None],
    'deptid':[10,10,20,30,None,10,30,30,20,None]
}
dept={
    'deptid':[10,20,30,40,50],
    'deptname':['Sales','Finance','HR','IT','Education'],
    'locid':[2,3,4,1,None]
    }
print(employee)
print(dept)
emp_df=pd.DataFrame(employee)
dept_df=pd.DataFrame(dept)
print(emp_df)
print(dept_df)
# Merge employee and dept data inner join
emp_dept_df=pd.merge(emp_df,dept_df,on="deptid",how="inner")
print(emp_dept_df)

