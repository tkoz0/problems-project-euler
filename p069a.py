import libtkoz as lib

maxn = 1000000

# use brute force to maximize n/phi(n), ~18sec (i5-2540m)
maxratio = 0
bestn = 0
for n in range(1, maxn+1):
    ratio = n / lib.totient(n)
    if ratio > maxratio:
        maxratio = ratio
        bestn = n
print(':', n, '/', 'phi(n) =', maxratio)
print(bestn)

