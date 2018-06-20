import libtkoz as lib
import math

# brute force with prime cache
cache = lib.list_primes2(10000,return_set=True)
cachemax = max(cache)
def is_prime(n):
    if n <= cachemax: return n in cache
    return lib.prime(n)

n = 9
while True: # loop to test composites
    if not is_prime(n):
        satisfiesconjecture = False
        for s in range(1, int(math.sqrt(n//2))+1): # find a square that works
            if is_prime(n - 2*s*s):
                satisfiesconjecture = True
                break
        if not satisfiesconjecture:
            print(n)
            break
    n += 2
