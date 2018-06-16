import libtkoz as lib

nlim = 10**6

# brute force + cache for dynamic programming, ~8sec (i5-2540m)
# start with dr(n) (digital root) as optimal for each number
# loop with a smaller factor a, for every a*b up to limit, update the mdrs with
# mdrs(a)+mdrs(b) if it is better, this method picks all factors if each number
# and tests them using dynamic programming for mdrs of other factor

# start with the number itself for factorization
cache = [0] + list(lib.digital_root(n) for n in range(1,nlim))
mdrssum = 0
for a in range(2,(nlim+1)//2): # pick factor a
    bf = 2 # factor associated with b: number = bf * a
    for b in range(2*a,nlim,a): # for all its multiples
        cache[b] = max(cache[b],cache[a]+cache[bf])
        bf += 1
    mdrssum += cache[a] # since all factors up to a have been considered
for a in range((nlim+1)//2,nlim): # finish summing
    mdrssum += cache[a]
print(mdrssum)
