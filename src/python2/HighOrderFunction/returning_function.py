def create_adder(x):
    print(x)
    def adder(y):
        print(y)
        return x+y
    return adder

# calling function 

my_adder=create_adder(10) # calling high order function
print(my_adder(15))  # calling inner order function

# output
# 25
