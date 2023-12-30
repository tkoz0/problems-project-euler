def is_prime(p):
    return p > 1 and all(p % d != 0 for d in range(2,p))

n = 20
primes = [p for p in range(n+1) if is_prime(p)]
result = 1
for p in primes:
    multiplicity = 1
    while p**(multiplicity+1) <= n:
        multiplicity += 1
    result *= p**multiplicity
print(result)

from math import gcd
n = 20
result = 1
for i in range(1,n+1):
    result = (result*i) // gcd(result,i)
print(result)
