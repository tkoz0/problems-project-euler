import libtkoz as lib
import math

divisors = 8
maximum = 10**6#10**12

primes = lib.list_primes2(maximum)#1+math.floor(math.sqrt(maximum)))

# find factorizations of how many divisors
# the prime factorization of numbers with that many divisors must have exponents
# 1 less than each factor
dfactorizations = []
def d_factor(factors,n,prevf):
    global dfactorizations, divisors
    if n == divisors:
        dfactorizations.append(factors)
    else: # factor remaining part recursively
        rem = divisors//n
        while prevf*prevf <= rem:
            if rem % prevf == 0:
                d_factor(factors+[prevf],n*prevf,prevf)
            prevf += 1
        d_factor(factors+[rem],divisors,rem)
d_factor([],1,2)
print(':',dfactorizations)

count = 0
def recurse(exps,expi,prod,nextpi): # count factorizations with required number of divisors
    global count, primes, maximum
#    print(' '*(4*expi),prod)
    if expi == len(exps): # finished
        count += 1
#        print(' '*(4*expi),prod,'counted')
    else: # try selecting next prime, pi = prime index
        primesafter = sum(exps[expi+1:]) # prime factors still needed
        for pi in range(nextpi,len(primes)): # select larger prime
            val = prod * (primes[pi]**exps[expi])
            # amount still need to multiply is too small
            if maximum//val < primes[pi]**primesafter: break # dont exceed limit
#            print(' '*(4*expi),'*',primes[pi],'**',exps[expi])
            recurse(exps,expi+1,val,pi+1)

for primeexp in dfactorizations:
    primeexp = list(n-1 for n in primeexp) # exponents of the prime factors
    hasnextpermutation = True
    # try all permutations of prime exponents, select primes in increasing order
    while hasnextpermutation:
        print(': prime exponent order',primeexp)
        # select primes recursively
        recurse(primeexp,0,1,0)
        hasnextpermutation = lib.lexico_next(primeexp)
print(count)
