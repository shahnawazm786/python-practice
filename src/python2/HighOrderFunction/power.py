def power_fun(n):
    def pow(x):
        return x**n
    return pow

square=power_fun(2)
cube=power_fun(3)
square_of_five=square(5)
cube_of_five= cube(5)
print(square_of_five)
print(cube_of_five)