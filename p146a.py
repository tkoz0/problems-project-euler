import libtkoz as lib

nlim = 150*10**6
steps = [1,3,7,9,13,27]

# brute force with a few things to speed it up
# ~1min (pypy / i5-2540m)

# test primality simultaneously
def primes(n):
    assert n % 10 == 0
    global steps
    n2 = n*n
    d = 3 # skip 2, odd steps so none are divisible by 2
    while d <= n: # search for factors
        for s in steps:
            if (n2+s) % d == 0: return False
        d += 2
    # make sure there arent any primes in between, miller rabin test
    for s in range(1,steps[-1],2):
        if (not s in steps) and lib.miller_rabin_verified(n2+s):
            return False
    return True

# n must be a multiple of 10
n = 10
total = 0
while n < nlim:
    if primes(n):
        print(':',n)
        total += n
    n += 10
print(total)
