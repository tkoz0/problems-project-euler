import libtkoz as lib

limit = 10**9

# recursively make numbers with consecutive prime factors, for each find the
# pseudo fortunate number and keep track of distinct M
# takes ~5sec (cpython / i5-2540m)

pfset = set() # pseudo fortunate numbers
def recurse(n,p): # recurse admissible numbers, p is last prime factor used
    global limit, pfset
    p += 1 # find next prime
    while not lib.prime(p): p += 1
    n *= p
    while n < limit:
        # find M>1 such than N+M is prime
        M = 2
        while True:
            if lib.prime(n+M):
                pfset.add(M)
                break
            M += 1
        recurse(n,p)
        n *= p
recurse(1,1)
print(':',pfset)
print(sum(pfset))
