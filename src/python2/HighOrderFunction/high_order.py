def exp_num(N):
    def exp(X):
        return X**N
    return exp

f=exp_num(5)
print(f(2))