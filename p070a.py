import libtkoz as lib
import math

nlim = 10000000

# minimize n/phi(n) but n and phi(n) must have same digits
# very slow brute force, took about 7.5min (i5-2540m)

minratio = nlim # start large
bestn = 0

for n in range(2, nlim):
    tn = lib.totient(n)
    # ratio must be better and they must have same number if digits
    if n / tn < minratio and int(math.log10(n)) == int(math.log10(tn)):
        if ''.join(sorted(str(n))) == ''.join(sorted(str(tn))):
            minratio = n / tn
            bestn = n
print(bestn)
