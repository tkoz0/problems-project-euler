import libtkoz as lib
import math

sumrange = range(5,10000+1)

# y=(n/k)^k, dy/dk = 0 when k=n/e (can be verified by derivative)
# 2nd derivative test confirms y''<0 at k=n/e so it is a maximum point
# 2nd derivaive evaluates to (-1/n)*e^k at k=n/e
# returns the optimal number of equal partitions k
def M(n): # maximum value for (n/k)^k, (k equal partitions multiplied together)
    k = n / math.e # point of maximum
    kf, kc = math.floor(k), math.ceil(k) # 2 possible best solutions
    pf, pc = kf*math.log(n/kf), kc*math.log(n/kc) # solutions, logarithmic
    return kf if pf > pc else kc

# n if M(n) is nonterminating decimal, -n otherwise
# only need n/k part from above, integer exponents maintain termination status
def D(n):
    # M(n) gives optimal partition amount, if n/k terminates then so will
    # (n/k)^k and k only has prime factors 2,5
    originaln = n # for return since n will be factored
    k = M(n) # optimal partitions
    g = lib.gcd_euclid(n,k)
    n, k = n // g, k // g # simplify fraction
    uf = set(lib.prime_factorization(M(n)))
    return -originaln if uf.issubset(set([2,5])) else originaln

print(sum(D(n) for n in sumrange))
