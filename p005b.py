import libtkoz as lib

maxdiv = 20

# build with the factorization
num = 1
for p in lib.list_primes1(maxdiv):
    val = p
    while val <= maxdiv: # multiply by p^a, such that p^a <= max
        num *= p
        val *= p
print(num)
