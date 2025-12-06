def add_numbers(a,b):
    print(f"{a} and {b}")
    return sum([a,b])

print(add_numbers(10,12))
    
def add_number_args(*args):
    print(args)
    return sum(args)

print(add_number_args(3,4,5))

print(add_number_args(10,30,500))