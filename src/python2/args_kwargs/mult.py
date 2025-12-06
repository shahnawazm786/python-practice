def multiply(*args):
    if len(args)>0:
        result=1
        for i in args:
            result*=i
    else:
        return None
    return result

print(multiply(10,30,40))
print(multiply())