st="this is my first find and is second one"
print(st.find("is",6))
print(st.title())
print(st.istitle())

word="abcdefj123456"
ind=word.find('6')
print(word[ind])

word="pop"
l=list(word)
print(l)
m=l[::-1]
print(m)
if l==m:
    print("Plaindrome")
else:
    print("Not palindrome")


l=[10,20,40]
print(id(l))
l=['A','B','C']
print(id(l))