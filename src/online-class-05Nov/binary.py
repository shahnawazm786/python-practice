a=input()
#flag= '1' in a or '0' in a
#print(flag)
st=''
for i in a:
    if not (i=='1' or i=='0'):
        st="Not binary"
        break
    else:
        st='Binary'
print(st)    
    