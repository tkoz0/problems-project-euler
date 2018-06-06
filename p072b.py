
maxd = 1000000

# use a totient sieve, ~1.5sec (i5-2540m)
# make a list of numbers up to the limit
# for each prime, multiply it and each of its multiples by (1-1/p)=(p-1)/p
# primes can be identified in increasing order since they have no smaller
# factors and will not be multiplied beforehand

sieve = list(range(maxd+1))
sieve[1] = 0 # dont count 1

for p in range(2, maxd+1):
    if sieve[p] != p: continue # was multiplied so it has smaller factors
    for p2 in range(p, maxd+1, p): # multiply all multiples
        sieve[p2] = sieve[p2] * (p-1) // p
print(sum(sieve)) # result is sum of totients

