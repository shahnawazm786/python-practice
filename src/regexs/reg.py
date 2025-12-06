import re
st='ABC 1234 abc def ABD 908 123 ghi klmn 124'
my_pattern='[^ABC]'
print(re.findall(my_pattern,st))
# filter digit from the st
digit_pattern="1234?"
print(re.findall(digit_pattern,st))
#M(r|s|rs).?\s[A-Z]\w*
