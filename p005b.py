import library

maxdiv = 20

# build with the factorization
num = 1
for p in library.list_primes(maxdiv):
    val = p
    while val <= maxdiv: # multiply by p^a, such that p^a <= max
        num *= p
        val *= p
print(num)
