# -----------------------------------
# Newton Raphson Cube Root Example
# next_guess=guess - f(g)/f'(g)
# f(g) = (g^3 - x)
# f'(g) = (3 * g ^2 )
# next_guess = guess - ((g^3 -x)/(3*g^2))
#
#
x=int(input(' what x to find the cube root of?'))
g=int(input('What guess to start with?'))
print('Current estimate cubed =', g**3)
next_g=g-((g**3 - x)/(3*g**2)) 
print(next_g)
