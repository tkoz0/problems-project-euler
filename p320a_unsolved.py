import libtkoz as lib

pset = lib.list_primes2(1000,return_set=True)

sumtotal = 1

def largest_prime(i):
    global pset
    while not (i in pset): i -= 1
    return i

for i in range(2,1001):
    sumtotal += 1234567890*largest_prime(i)
print(sumtotal)
