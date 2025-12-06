def make_fibonacci(n):
    def fibonacci():
        fib = []
        a, b = 0, 1
        
        for _ in range(n):
            fib.append(a)
            a, b = b, a + b
        
        return fib
    return fibonacci


# Test Case
n = int(input().strip())
fn = make_fibonacci(n)
print(fn())