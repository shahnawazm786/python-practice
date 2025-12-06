# mulitple 5 * 4 
# decomposition 5 +(5*3)
# decomposiitio  5 + (5 +(5*2))
# decomposiitio  5 + (5 +(5+(5*1))

def multiple(a,b):
    if b==1:
        return a
    else:
        return a + multiple(a,b-1)

print(multiple(5,10))
