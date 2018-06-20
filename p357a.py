import libtkoz as lib
import math

maximum = 10**8

# ~1min and 2GiB RAM (pypy / i5-2540m)
# start with a prime set for fast prime checking and a list of booleans for each
# number that starts as true, once a composite d+n/d is found mark it false
# only need to test d up to sqrt(n) because if d>sqrt(d) then n/d<sqrt(d) but
# n/d is also a divisor so we would have already tested n/d+n/(n/d)=d+n/d

# list primes up to 1 more since if d=n then n+n/n=n+1
# make a set of primes for fast prime testing (set containment)
primes = lib.list_primes2(maximum+1,return_set=True)
print(': listed primes up to',maximum+1)

# set to false once a composite d+n/d is found
nums = [True] * (maximum+1)

for d in range(1,1+int(math.sqrt(maximum))):
    nd = d # n/d value, d/d=1, 2d/d=2, ..., incremented in loop
    for n in range(d*d,maximum+1,d): # every number d divides
        if not ((d+nd) in primes): nums[n] = False
        nd += 1
# sum indexes in nums list
print(sum(n for n in range(maximum+1) if nums[n]))
