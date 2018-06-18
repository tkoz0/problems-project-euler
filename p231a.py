
Cn = 2*10**7
Ck = 15*10**6

# sieve to count sum of factors for all required numbers, then count for
# the factors of the binomial coefficient, ~30sec (cpython / i5-2540m)

# sieve sum of factors for every number up to Cn
sieve = [0]*(Cn+1)
for p in range(2,Cn+1): # count every prime for its multiplicity
    if sieve[p] != 0: continue # skip non primes
    factor = p
    while factor <= Cn:
        for i in range(factor,Cn+1,factor):
            sieve[i] += p
        factor *= p
print(': sieved prime factor sums up to',Cn)

# then consider prime factors in the result Cn! / (Ck!) / (Cn-Ck)!
# sum prime factors for Cn*(Cn-1)*...*(Cn-Ck+1)
# then subtract prime factors in Ck!
print(sum(sieve[i] for i in range(Cn-Ck+1,Cn+1))
      - sum(sieve[i] for i in range(Ck+1)))
