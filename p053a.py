import libtkoz as lib

nmax = 100
combmin = 1000000

# basic method since python supports large integers

count = 0
for n in range(nmax+1):
    for r in range(n+1):
        if lib.binom_coeff(n, r) > combmin:
            count += 1
print(count)

# faster solution using symmetry of pascal triangle

count = 0
for n in range(nmax+1):
    # find min r such that ncr > combmin (or reach middle)
    ncr = 1
    for r in range(1, n//2 + 1):
        ncr *= n+1-r
        ncr //= r
        if ncr > combmin:
            count += (n+1) - 2*r # r on each side (0,1,...,r-1) (symmetric)
            break
print(count)
