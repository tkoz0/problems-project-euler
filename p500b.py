import libtkoz as lib

factorsexp = 500500
modulus = 500500507

# large enough so pi(sievelim) >= factorsexp # may need up to this many primes
# if not large enough, program will crash with list index out of bounds
sievelim = 8000000

# use a sieve (index i represents 2i+1) (prime=True)
# every time reaching a prime, mark its square
# requires only 1 sweep over the sieve, ~4sec (i5-2540m)

sieve = lib.list_primes2(sievelim,return_sieve=True)
evenval = 2
sievei = 1 # 2*1+1=3 initially
result = 1
counted = 0

while counted < factorsexp: # iterate over sieve
    if evenval < 2*sievei+1: # more optimal to pick exponent of 2
        result = (result*evenval) % modulus
        evenval *= evenval
        counted += 1
    else:
        if sieve[sievei]: # prime, multiply this one
            n = 2*sievei+1
            result = (result*n) % modulus
            n *= n # mark square in sieve
            n //= 2 # sieve index of square
            if n < len(sieve): sieve[n] = True # mark so it is multiplied
            counted += 1
        sievei += 1
print(result)
