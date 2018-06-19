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

def seq(n): # sequence length generated starting at n
    global sieve
    s = 1
    while n != 1:
        n = sieve[n]
        s += 1
    return s

# sum primes that produce required sequence length
print(sum(p for p in primes if seq(p) == seqlen))
