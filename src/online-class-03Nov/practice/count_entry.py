tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
s=set(tup)
print(s)
print(tup)
for num in s:
    print(f"{num}: {tup.count(num)}")