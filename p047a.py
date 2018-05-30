import libtkoz as lib

consec = 4
factors = 4

def distinct_prime_factors(n): # calculates distinct prime factors
    total = 0
    if n % 2 == 0:
        total += 1
        n //= 2
        while n % 2 == 0: n //= 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            total += 1
            n //= d
            while n % d == 0: n //= d
        d += 2
    if n != 1: total += 1 # last remaining prime factor
    return total

# brute force it, ~1 sec (i5-2540m)

n = 2 # could be 210=2*3*5*7 for the case of 4 distinct prime factors
seq = 0
while True:
    if distinct_prime_factors(n) == factors:
        seq += 1 # count towards required consecutive numbers
        if seq == consec: # found
            for i in range(n, n-consec, -1):
                print(':', i, lib.prime_factorization(i))
            print(n - consec + 1) # first in the sequence
            break
    else: seq = 0 # reset
    n += 1
