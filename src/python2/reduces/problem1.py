import functools as f
L=[10,15,20,25,30,35,40]
data=f.reduce(lambda x,y : x+y , L)
print(data)
# max value
L1=[10,200,30,40,150,11,30]
max_val= f.reduce(lambda x, y : x if x>y else y, L1)
print(max_val)
