import libtkoz as lib

# phi(n) is n * product of every (1-1/p) so n/phi(n) is 1/(product of (1-1/p))
# to maximize the ratio, we need as many distinct primes as possible
# multiply distinct primes in increasing order until multiplying the next one
# would exceed the limit, the solution is that (and all multiples of it within
# the limit have the same ratio)

maxn = 1000000

prod = 1
p = 2
while True:
    if lib.prime(p):
        prod *= p
    if prod > maxn:
        prod //= p
        break
    p += 1

if prod * 2 <= maxn:
    print(': multiple solutions, choosing the smallest')
print(':', prod, '/ phi(n) =', prod / lib.totient(prod))
print(prod)
