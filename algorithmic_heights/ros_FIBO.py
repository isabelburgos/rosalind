n = 20

def fib(n_prev,n_last,i):
    i += 1
    n_new = n_last + n_prev
    if i >= n:
        print(n_new)
    else:
        fib(n_last,n_new,i)

fib(0,1,1)
