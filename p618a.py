import libtkoz as lib

smax = 24
modulus = 10**9

# ~4sec (pypy / i5-2540m) and ~50sec (cpython / i5-2540m)

fib = [0,1] # generate fibonacci numbers
while len(fib) <= smax: fib.append(fib[-2]+fib[-1])

numsums = [0]*(fib[-1]+1) # i: sum of numbers whose prime factors sum to i
numsums[0] = 1 # needed for dynamic programming
primes = lib.list_primes2(fib[-1])

for p in primes:
    # if p is added to factorizations of i, those numbers get multiplied by p
    # numsums[i] is sum for numbers using prime factors at most p
    # suppose numsums has sums for numbers using factors below p
    # if p is considered at index i, then we take numbers whose factors sum to
    # i-p and add a p to them, this is equivalent to multiplying those numbers
    # by p so we add that quantity to the index for i
    for i in range(p,len(numsums)):
        numsums[i] = (numsums[i] + p*numsums[i-p]) % modulus
# sum fibonacci indexes
print(sum(numsums[fib[f]] for f in range(2,smax+1)) % modulus)
