sen=input()
d={}
for ch in sen:
    if d.get(ch)==True:
        val=d[ch]
        val+=1
        d[ch]=val
    else:
        d[ch]=1
print(d)   