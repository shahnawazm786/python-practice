def foo():
    print('Hello!!! I am trying some thing different')

def pretty(func):
    print("-"*50)
    func()
    print("-"*50)

pretty(foo)
