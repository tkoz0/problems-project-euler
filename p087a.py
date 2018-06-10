import libtkoz as lib
import math

limit = 50000000

# brute force by looping over a prime list, ~2sec (i5-2540m)
# begin by listing primes up to sqrt(limit)
primes = lib.list_primes2(int(math.sqrt(limit)))
# true means the number is expressible as a prime 2nd, 3rd, and 4th power sum
sieve = [False] * limit

for p2 in range(len(primes)):
    sum2 = primes[p2]**2 # sum the square, wont exceed limit
    for p3 in range(len(primes)):
        sum23 = sum2 + primes[p3]**3
        if sum23 >= limit: break
        for p4 in range(len(primes)):
            sum234 = sum23 + primes[p4]**4
            if sum234 >= limit: break
            sieve[sum234] = True
print(sum(1 for v in sieve if v)) # sum true values
