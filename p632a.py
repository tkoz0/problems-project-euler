import libtkoz as lib
import math
import functools

# ~3min with cpython / core2 q8200
# appears to scale linear to sqrt(N)

N = 10**16
modulus = 10**9+7
primes = lib.list_primes2(int(math.sqrt(N)))
print(': sieved primes')

# determine max value of k
prod = 1
ktable = [0]
for p in primes:
    prod *= p*p
    if prod > N: break
    ktable.append(0)

# for each k, count how many numbers are divisible by all prime squares in
# every combination of k prime squares

# product of squares, number of factors, next prime index
def recurse(sqprod,numpfactors,nextpi):
    global N, primes, ktable
    maxsq = N // sqprod
    while nextpi < len(primes) and primes[nextpi]**2 <= maxsq:
        recurse(sqprod*primes[nextpi]**2,numpfactors+1,nextpi+1)
        nextpi += 1
    ktable[numpfactors] += maxsq
#    for k in range(numpfactors+1):
#        if k%2 == numpfactors%2: ktable[k] += maxsq
#        else: ktable[k] -= maxsq
recurse(1,0,0)
print(': summing over combinations of k factors',ktable)

# the only correct value is for k_max since it will not count any numbers with
# over k_max prime squares more than once
# starting from k_max-1, it counts the numbers with k_max prime squares multiple
# times, for every combination of k_max-1 squares that is a subset of the k_max
# squares for the numbers with k_max prime squares, (k_max choose k_max-1)
# now the value for k_max-1 is correct
# similarly, for k_max-2, numbers with k_max-1 and k_max squares are counted
# multiple times, subtract how many repeats there are with combinatorics

for k1 in range(len(ktable)-2,-1,-1):
    for k2 in range(k1+1,len(ktable)):
        ktable[k1] -= lib.binom_coeff(k2,k1)*ktable[k2]

print(': C_k values',ktable)
assert sum(ktable) == N
print(functools.reduce(lambda x,y: x*y, ktable) % modulus)
