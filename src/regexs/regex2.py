import re
text='ab abb acc abbb a a ac ad ae aab'
pat=re.compile(r"ab*")
t_all=re.findall(pat,text)
print(t_all)