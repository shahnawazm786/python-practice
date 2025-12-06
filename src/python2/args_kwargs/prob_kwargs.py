def profile(**kwargs):
    print(kwargs)
    print(type(kwargs))

profile(name='Mohammad', age=40)

def profile1(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"Key is {key} and value is {value}")
    print(type(kwargs))

profile1(Name="Mohammad",age=40,role='developer')
