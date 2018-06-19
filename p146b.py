import libtkoz as lib
import math

nlim = 150*10**6
steps = [1,3,7,9,13,27]

# use an observation for efficiency, faster with miller rabin test
# prime list eliminates lots of candidates, then the amount of use of the
# miller rabin test is small so it can complete quickly after that
# ~7sec (pypy / i5-2540m)
# if some n=qx+r, a prime q, integer x, and remainder r,
# n^2+s = q^2*x^2 + 2qxr + r^2+s
# so if q | r^2+s then q | n^2+s

plistsize = int(math.sqrt(nlim))
plist = lib.list_primes2(plistsize)

candidates = []
for n in range(10,nlim,10):
    # for each n, if a prime q divides r^2+s then it cant be a solution number
    fail = False # n cant be a candidate if this becomes true
    for q in plist: # use primes to eliminate many possibilities
        # skip primes above n since for primality, we only need to test
        # up to n for n^2+s
        if fail or q>n: break
        r = n % q
        r *= r # represents r^2
        for s in steps:
            if (r+s)%q == 0:
                fail = True
                break
    if not fail: # n is a possible candidate
        candidates.append(n)

print(':',len(candidates),'candidates, used primes up to',plistsize)

# test primality simultaneously, same as previous solution
def primes(n):
    assert n % 10 == 0
    global steps, plistsize
    n2 = n*n
    for s in steps: # if any are composite
        if not lib.miller_rabin_verified(n2+s): return False
    for s in range(1,steps[-1],2): # make sure they are consecutive
        if (not s in steps) and lib.miller_rabin_verified(n2+s): return False
    return True

total = 0
for n in candidates:
    if primes(n):
        print(':',n)
        total += n
print(total)
