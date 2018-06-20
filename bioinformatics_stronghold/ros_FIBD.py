n = 96
m = 19

seq = [1,0]
def fib(n_adult,n_young,i,n,m):
    i += 1
    new_adult = n_adult + n_young
    new_young = n_adult
    if i>m:
        new_adult -= seq[i-m-1]
    n_new = new_adult + new_young
    seq.append(new_adult)
    if i >= n:
        print(n_new)
    else:
        fib(new_adult,new_young,i,n,m)

fib(0,1,1,n,m)
