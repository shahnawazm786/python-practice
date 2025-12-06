'''
# Question 3:

# You're debugging a snippet from a colleague. Given the variables below:
x = 4
y = 2
z = 3

result = (not x) + y * z == 10 or x < y and not z

# (not 4) + 2 * 3 == 10 or 4 < 2 and not 3
#  False or False and False

# What is the final value of the result?

# Options:
# A) True
# B) False
# C) SyntaxError
# D) TypeError

'''



x=4
y=2
z=3
result=(not x) +y *z ==10 or x<y and not z
print(result)