import libtkoz as lib

dlim = 1000000
fracn = 3
fracd = 7
printapproximations = False # toggle to display improved approximations

# brute force with floating point, continue to find larger fractions that are
# still smaller than the target fraction, takes ~1.5sec (i5-2540m)

# n/d<3/7 --> 7n<=3d-1 --> n<=(3d-1)/7 so pick n=floor((3d-1)/7)
# suppose r/s is best found, r/s<n/d --> rd<sn (new n/d must be greater)
# we could check for a better solution with integers like this or use floats

floatval = 0
bestn, bestd = 0, 0
print(': target value ', fracn, '/', fracd, '=', fracn / fracd)
# go in decreasing order since larger d means smaller 1/d steps that could get
# a better approximation to 3/7
for d in range(dlim, 1, -1):
    if d == fracd: continue # skip target fraction
    # pick largest n such that n/d=fracn/fracd
    # n=fracn*d/fracd
    n = (fracn * d - 1) // fracd # results in n/d < fracn/fracd
    if n == 0 or lib.gcd_euclid(d, n) != 1: continue # must be reduced
    newfloatval = n / d
    if newfloatval > floatval:
        floatval = newfloatval
        if printapproximations:
            print(': better value', n, '/', d, '=', newfloatval)
        bestn, bestd = n, d
print(': best approximation', bestn, '/', bestd, '=', bestn / bestd)
print(bestn)

# analyze the problem to find a faster solution, a changing lower bound
# suppose r/s is a possible solution (best found)
# 3/7-r/s = (3s-7r)/(7s) > 0 --> 3s-7r >= 1 so (3s-7r)/(7s) > 1/(7s)
# for a better solution, this difference must be larger than 3/7-p/q
# supposing that p/q is a solution being tested
# 3/7-p/q = (3q-7p)/(7q), this difference must be smaller
# we must have (3s-7r)/(7s) > (3q-7p)/(7q) >= 1/(7q)
# the >= 1/(7q) is because 3q-7p must be positive for positive fraction
# take the 2 ends: (3s-7r)/(7s) > 1/(7q) --> s/(3s-7r) < q
# this gives us a lower bound for q
r, s = 0, 0 # best solution
floatval = 0
lowerlim = 1
for q in range(dlim, 1, -1):
    # need different denomenator, dont go below lower bound
    if q == fracd or q <= lowerlim: continue
    p = (fracn * q - 1) // fracd # best fraction with denomenator q
    if p/q > floatval:
        floatval = p/q
        r, s = p, q
        lowerlim = s // (fracn*s - fracd*r)
        print(': set lower bound to', lowerlim)
r, s = r // lib.gcd_euclid(s, r), s // lib.gcd_euclid(s, r)
print(': found best', r, '/', s, '=', r/s)
print(r)

