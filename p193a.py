import libtkoz as lib
import math

limit = 2**50

# count with inclusion-exclusion
# subtract numbers with 1 prime square as a factor
# add numbers with 2 prime squares as a factor
# continue until limit / (2^2*3^2*5^2*7^2*...) is 0
# ~45sec (pypy / i5-2540m)

plist = lib.list_primes2(int(math.sqrt(limit)))
print(': listed',len(plist),'primes up to',int(math.sqrt(limit)))

count = limit
# product of prime squares, count of prime squares, next prime index
def recurse(sqprod,sqcount,pi):
    global limit, plist, count
    if sqcount != 0: # count with inclusion-exclusion
        if sqcount % 2 == 0: count += limit//sqprod
        else: count -= limit//sqprod
    for nextp in range(pi,len(plist)):
        nsqprod = sqprod * (plist[nextp]**2)
        if nsqprod > limit: return # never call with too large square product
        recurse(nsqprod,sqcount+1,nextp+1)
recurse(1,0,0)
print(count)
