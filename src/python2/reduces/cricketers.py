from functools import reduce
cricket=['Azhar','Saba','Zaheer','Irfan','Munaf']
cricket_join=reduce(lambda x,y : x+' '*3+y,cricket)
print(cricket_join)

movies=['jolly lib','PK','dhOOm','ddlj']
movies_upper=list(map(lambda x:x.upper(),movies))
print(movies_upper)