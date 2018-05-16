k = int(input("k: "))
m = int(input("m: "))
n = int(input("n: "))

import math

def p_dom(k,m,n):
    n_tot = math.factorial(k+m+n)/(math.factorial(2)*math.factorial(k+m+n-2))
    n_AA_AA = math.factorial(k)/(math.factorial(2)*math.factorial(k-2))
    n_AA_Aa = k * m
    n_AA_aa = k * n
    n_Aa_Aa = .75*math.factorial(m)/(math.factorial(2)*math.factorial(m-2))
    n_Aa_aa = .5*m*n
    return((n_AA_AA + n_AA_Aa + n_AA_aa + n_Aa_Aa + n_Aa_aa)/n_tot)


print(format(p_dom(k,m,n),'.5f'))
