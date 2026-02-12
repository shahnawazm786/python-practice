'''
Problem Description:

Given a dataset about salesperson and customer orders, the task is to group the data as per salesman_id and customer_id, and return a new dataframe with the ord_no count for each salesman_id and customer_id pair.

Refer to sample input and output for better understanding.
Input Format: (NOTE: No need to take the input explicitly — the input-handling code is already in place.)

The first line of the input contains the dataframe, in the form of a dictionary.
Output Format:

The new dataframe

'''
import pandas as pd
order={'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]}
df=pd.DataFrame(order)
print(df)
result=df.groupby(['salesman_id','customer_id'])['ord_no'].count()
print(result)
result1=(df.groupby(['salesman_id', 'customer_id'], as_index=False).agg(ord_no=('ord_no', 'count')))

print(result1)