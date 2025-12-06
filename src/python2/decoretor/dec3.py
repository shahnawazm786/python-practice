import time
def timer(x):
    def wrapper(a):
        import time
        start= time.time()
        x(a)
        print(start - time.time())
    return wrapper
    
@timer
def func(a):
    time.sleep(a)
    print("Hello..... Print")


func(1)