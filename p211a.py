import libtkoz as lib

maxn = 64*10**6

# this is pretty much a brute force method, cpython needs over 2GiB RAM to solve
# it, pypy did it with 500MiB, ~22sec (pypy / i5-2540m)

# use a sieve to sum squares of divisors
sieve = [1]*(maxn+1)
sieve[0] = 0
for factor in range(2,maxn+1): # sum squares
    f2 = factor**2
    for i in range(factor,maxn+1,factor):
        sieve[i] += f2 # add square to sum for numbers factor divides

# sum all n that are perfect squares
print(sum(n for n in range(1,maxn+1) if lib.is_square(sieve[n])))
