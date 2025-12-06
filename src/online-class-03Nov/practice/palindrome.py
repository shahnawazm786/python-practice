def isPalindrom(str):
    t=list(str)[::-1]
    t="".join(t)
    print(t)
    return str==t
flag=isPalindrom('level')
print(flag)