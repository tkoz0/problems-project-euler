import libtkoz as lib
import math

limit = 1000000

primes = set(lib.list_primes2(limit))

# brute force with some reduction, not much faster, ~0.3 sec (i5-2540m)
# consider 2 and 5 separately, all other base 10 primes end in 1,3,7,9
# instead of a loop, recursively make primes ending in these
# since every digit ends up at the end from rotations, they must all be 1,3,7,9
circulars = {2, 5} # 2,5
def recurse(num):
    global circulars
    global primes
    if not num in circulars and num in primes:
        n = num
        max10pow = int(math.log10(n))
        circular = True
        for i in range(max10pow): # try all rotations
            n = (n // 10) + (n % 10) * (10**max10pow)
            if not n in primes:
                circular = False
                break
        if circular:
            print(': inserting rotations of', num)
            circulars.add(num)
            n = num
            for i in range(max10pow):
                n = (n // 10) + (n % 10) * (10**max10pow)
                circulars.add(n)
                print(':', n)
    num *= 10
    if num < limit: # 4 new digits
        recurse(num + 1)
        recurse(num + 3)
        recurse(num + 7)
        recurse(num + 9)
# begin recursion with each digit
recurse(1)
recurse(3)
recurse(7)
recurse(9)
print(':', sorted(list(circulars)))
print(len(circulars))

