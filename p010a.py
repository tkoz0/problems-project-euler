import libtkoz as lib

limit = 2000000

psum = 0
pcount = 0

# could use sum(lib.list_primes(...))
# brute force approach will use loop to prevent using memory to store primes
# took ~6 sec (i7-7600u)
for n in range(limit):
    if lib.prime(n):
        psum += n
        pcount += 1
print(': prime count', pcount)
print(psum)
