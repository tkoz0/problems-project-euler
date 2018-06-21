import libtkoz as lib

pval = 10**8
modulus = 10**9+7

# brute force try all pi sequences, ~9min (pypy / i5-2540m)

# make prime list and binary search function for efficient calculation of pi(n)
primes = lib.list_primes2(pval)
primeset = set(primes) # for fast primality checking
print(': listed primes up to',pval)

def pi(n): # correct value for n < next prime after primes[-1]
    global primes
    # find index of first prime to exceed n, pi(n) is num primes below this
    l, h = 0, len(primes) # partition
    while l != h:
        m = (l+h)//2 # middle point, splits are [l,m] and [m+1,h)
        if primes[m] > n: h = m
        else: l = m+1
    return l

# find longest possible pi sequence
longest = 1
n = pval
while n != 1:
    n = pi(n)
    longest += 1
print(': longest pi sequence is',longest)
countnonprimes = [0]*(longest+1) # stores values of p(pval,k) (index k)

for n in range(2,pval+1): # starting numbers
    c = (0 if (n in primeset) else 1) # count composites
    while n != 1: # for sequences at least length 2
        n = pi(n)
        if not (n in primeset): c += 1
        countnonprimes[c] += 1
print(': counts c(u)=k',countnonprimes)

prod = 1
for c in countnonprimes:
    if c != 0: prod = (prod*c) % modulus
print(prod)
