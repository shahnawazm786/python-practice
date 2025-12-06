import re
text="ab abb abbbb a aa abc acb"
# it will filter 'ab abb abbbb ab
pat=re.compile(r"ab+")
all_matching_text=re.findall(pat,text)
print(all_matching_text)

# zero or one time (?)

text1='ab abb a a a abbbb abbbbbb ac ca'
pat1=re.compile('ab?')
one_or_more_time=re.findall(pat1,text1)
print(one_or_more_time)