import math

startlim = 1000000
chainlen = 60
shownums = False # toggle to see satisfying numbers in output

facts = list(math.factorial(x) for x in range(10))
def next(n): # computes next in chain
    s = 0 # use division since its faster than string conversion stuff
    while n != 0:
        # use lookup table for speed, only makes it a little faster
        s += facts[n % 10]
        n //= 10
    return s

# compute each chain by brute force, with cache it takes ~35sec (i5-2540m)
# use a cache for finding cycles and solving larger start numbers faster
cache = [0] * startlim
cache[0] = 2 # numbers that repeat theirselves (and trivial 0)
cache[1] = 1
cache[2] = 1
cache[145] = 1
cache[40585] = 1 # from problem 34
# the only 3 existing cycles (given)
cache[169] = cache[363601] = cache[1454] = 3
cache[871] = cache[45631] = 2
cache[872] = cache[45632] = 2

count = 0
for n in range(3, startlim):
    if cache[n] != 0: # already known, determine counting by chain length
        if cache[n] == chainlen: count += 1
    else: # must find chain length
        nn = n
        ll = 1
        while True:
            nn = next(nn)
            if nn < startlim and cache[nn] != 0: # known subchain length
                ll += cache[nn]
                break
            ll += 1 # havent found subchain, continue
        if ll == chainlen:
            count += 1
            if shownums: print(':', n)
print(count)
