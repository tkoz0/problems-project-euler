import libtkoz as lib
import math

limit = 1000000

primes = lib.list_primes2(limit,return_set=True)

# brute force try everything, ~0.5 sec (i5-2540m)
circulars = {2, 5}
for n in range(3, limit, 2):
    if not n in primes or n in circulars: continue
    nn = n
    max10pow = int(math.log10(n)) # largest exp of 10 in number
    circular = True
    for i in range(max10pow): # do all rotations
        nn = (nn // 10) + (nn % 10) * (10**max10pow)
        if not nn in primes:
            circular = False
            break
    if circular: # insert all rotations
        print(': inserting rotations of', n)
        circulars.add(n)
        nn = n
        for i in range(max10pow):
            nn = (nn // 10) + (nn % 10) * (10**max10pow)
            circulars.add(nn)
            print(':', nn)
print(':', sorted(list(circulars)))
print(len(circulars))

