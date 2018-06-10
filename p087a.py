import libtkoz as lib
import math

limit = 50000000

# brute force by looping over a prime list, ~1sec (i5-2540m)
# begin by listing primes up to sqrt(limit)
primes = lib.list_primes2(int(math.sqrt(limit)))
print(': generated primes up to', int(math.sqrt(limit)))
sieve = set() # numbers that are expressible as the sum
# this doubled speed, rather than allocate a length 50 million array

for p2 in range(len(primes)):
    sum2 = primes[p2]**2 # sum the square, wont exceed limit
    for p3 in range(len(primes)):
        sum23 = sum2 + primes[p3]**3
        if sum23 >= limit: break
        for p4 in range(len(primes)):
            sum234 = sum23 + primes[p4]**4
            if sum234 >= limit: break
            sieve.add(sum234)
print(len(sieve))
