sen=input()
set_of_sen=set(sen)
d={}
for a in set_of_sen:
    d[a]=sen.count(a)

print(d)
