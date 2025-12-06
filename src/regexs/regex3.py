import re
text="ab abb abbbb a aa abc acb"
# it will filter 'ab abb abbbb ab
pat=re.compile(r"ab+")
all_matching_text=re.findall(pat,text)
print(all_matching_text)