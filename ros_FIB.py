n = int(input("n: "))
k = int(input("k: "))

def fib(n_adult,n_young,i):
    i += 1
    new_adult = n_adult + n_young
    new_young = k*n_adult
    if i >= n:
        print(new_adult + new_young)
    else:
        fib(new_adult,new_young,i)

fib(0,1,1)
