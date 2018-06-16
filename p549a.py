import libtkoz as lib

smax = 10**8

# sieving method, picking largest factorial required based on the prime
# factorization of the numbers, very slow ~1hour (i5-2540m)

sieve = [0] * (smax+1)

def lcount(l,n): # counts how many n are in l
    return sum(1 for f in l if f == n)

# pick a prime, all its multiples need at least p!
# then for p^2, all its multiples need at least (2p)!
# for p^3 and so on (unless p^3 | (2p)!)
# perform max operation on elements in the sieve for all primes

for p in range(2,smax+1): # pick a prime
    if sieve[p] != 0: continue # not prime, multiples of primes become nonzero
    pp = p # the factorial
    sievedm = 1 # highest exponent sieved so far
    m = 1 # multiplicity of p in pp!
    while p**sievedm <= smax:
        while sievedm <= m: # for each exponent up to that allowed by pp
            for q in range(p**sievedm,smax+1,p**sievedm):
                sieve[q] = max(sieve[q],pp)
            sievedm += 1
        pp += p # go to next multiple
        m += lcount(lib.prime_factorization(pp),p) # count multiplicity in pp
print(sum(sieve))
