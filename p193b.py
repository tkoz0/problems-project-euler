import math

limit = 2**50

# the mobius function can help since it is the sign for inclusion-exclusion
# it is 0 if it isnt square free,
# -1 if it has an odd number of prime factors
# 1 if it has an even number of prime factors
# if mobius(k)=v then consider k^2 as a factor, we need to exclude/include
# all numbers up to limit with k^2 as factor
# this is summarized by the summation: floor(N/k^2)*mobius(k) for k=1 to sqrt(N)
# ~4.5sec (pypy / i5-2540m)

# sieve mobius function values
msieve = [-2]*(1+int(math.sqrt(limit)))
msieve[1] = 1 # special case mobius(1)=1 (has 0 prime factors)
for k in range(2,len(msieve)):
    if msieve[k] != -2: continue # -2 is indicator that k is prime
    for kk in range(k,len(msieve),k): # alternate values
        if msieve[kk] == 1: msieve[kk] = -1
        elif msieve[kk] == -1: msieve[kk] = 1
        elif msieve[kk] == -2: msieve[kk] = -1 # 1 prime factor found
    for kk in range(k*k,len(msieve),k*k): # zeroes for non square free numbers
        msieve[kk] = 0
print(': sieved mobius function values up to',int(math.sqrt(limit)))
print(sum((limit//(k*k) * msieve[k]) for k in range(1,1+int(math.sqrt(limit)))))
