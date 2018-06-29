import libtkoz as lib

ones = 10**9
numfactors = 40

def R(n): return (10**n-1)//9

primes = set()

i = 2
while len(primes) < numfactors:
    if ones % i == 0: # divisibility, ex: 111111 = 11*010101
        print(': factoring R(',i,') = ',R(i),sep='')
        for p in lib.prime_factorization(R(i)): primes.add(p)
        print(': found',len(primes),'primes')
    i += 1
print(sum(sorted(primes)[:numfactors])) # sum factors
