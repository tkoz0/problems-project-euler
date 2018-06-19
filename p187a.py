import libtkoz as lib
import math

limit = 10**8

# sieve, then pick a prime p and count how many primes q >= p such that
# pq <= limit, so its summing pi(limit/p)-pi(p-1) for every p<=sqrt(limit)
# sieving primes takes long but summing is fast since computing pi(n) can be
# done efficiently with a prime list and binary search
# ~18sec (cpython / i5-2540m)

# start by listing primes up to half the limit since 2*p 
plist = lib.list_primes2(limit//2)
limitsqrt = int(math.sqrt(limit))
print(': listed primes up to',limit//2)

# for every prime p up to sqrt(limit), count how many primes there are from p
# to limit/p, this can be done efficiently with binary search
# the desired value is pi(limit/p) - pi(p-1), pi(n) is count of primes <= n

# count primes up to n, correct results if n < next prime after plist[-1]
def pi(n):
    global plist
    # find index of first prime to exceed n, pi(n) is num primes below this
    l, h = 0, len(plist) # partition
    while l != h:
        m = (l+h)//2 # middle point, splits are [l,m] and [m+1,h)
        if plist[m] > n: h = m
        else: l = m+1
    return l

count = 0
for i,p in enumerate(plist): # i represents pi(p-1)
    if p > limitsqrt: break
    count += pi(limit//p) - i
print(count)
