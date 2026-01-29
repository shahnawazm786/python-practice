import pandas as pd

users=pd.DataFrame({"userid":[1,2,3],"name":["Sharadh","Shahid","Khusalli"]})
msgs = pd.DataFrame({"userid":[1, 1, 2, 4], "msg":['hmm', "acha", "theek hai", "nice"]})
print(users)
print(msgs)

# inner join default
merge_data=users.merge(msgs,on='userid',how='left')
print(merge_data)
merge_data_pd=pd.merge(users,msgs,on="userid",how='right')
print(merge_data_pd)
temp_df=pd.merge(users,msgs,left_on='userid',right_on="userid",how="left")
print(temp_df)
mask=temp_df['msg'].isnull()
print(temp_df[mask])
temp_df_null_msgs = pd.merge(users, msgs, left_on='userid', right_on='userid', how='left').loc[lambda df: df['msg'].isnull()]
print(temp_df_null_msgs)
