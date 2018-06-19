import libtkoz as lib

limit = 4*10**7
seqlen = 25

# with cpython it needs 1.5GiB RAM and 90sec (cpython / i5-2540m)
# with pypy it needs under 500MiB RAM and 10sec (pypy / i5-2540m)

# start at primes and find sequences with required length
# totient sieve will be useful
sieve = list(range(limit))
for p in range(2,limit): # for each prime
    if sieve[p] != p: continue # was updated, has smaller prime factor
    sieve[p] -= 1 # phi(p) for primes
    for i in range(2*p,limit,p): # multiply multiples by (p-1)/p
        sieve[i] = sieve[i]*(p-1)//p
primes = lib.list_primes2(limit-1)

# since totient chains are strictly decreasing, replace sieve values with the
# sequence length of the integers so they can be computed more quickly for
# larger starting numbers, considering the average prime gap, this does not
# actually do much to improve efficiency

# now loop over all integers
prevp = 2
total = 0
for p in primes:
    while prevp <= p: # compute sequence lengths for all integers
        sieve[prevp] = 1 + sieve[sieve[prevp]]
        prevp += 1
    # once sequence length for the prime is known, if its 25 add the prime
    if sieve[p] == seqlen: total += p
print(total)
quit()
