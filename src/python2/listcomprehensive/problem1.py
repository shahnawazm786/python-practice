L=[1,2,3,4,5,6,7,8,9]
L1= [i**2 for i in L]
print(L1)

#range(10)
L2=[j**2 for j in range(10)]
print(L2)

# odd number square
L3=[k**2 for k in range(10) if k%2!=0]
print(L3)