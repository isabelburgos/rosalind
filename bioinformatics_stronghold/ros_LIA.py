k = int(input("k: "))
N = int(input("N: "))

import math

p = 2**k
def prob(n):
    prob = (math.factorial(p)/(math.factorial(n)*math.factorial(p-n))) * (.25**n) * (.75**(p-n))
    return prob

psum = 0
for i in range (N,p+1):
    psum += prob(i)

print(psum)
