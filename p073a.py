import libtkoz as lib

lower = (1, 3)
upper = (1, 2)
maxd = 12000

# compute by brute force, ~18sec (i5-2540m)
count = 0
for d in range(2, maxd+1):
    # we need n/d>a/b --> nb>ad (a/b=1/2), so n starts at 1+floor(ad/b)
    # and n/d<a/b --> nb<ad (a/b=1/3), so n maximum is floor(ad/b)
    minn = 1 + lower[0]*d//lower[1]
    maxn = upper[0]*d
    if maxn % upper[1] != 0: maxn //= upper[1]
    else: maxn = maxn // upper[1] - 1
    for n in range(minn, maxn+1):
        if lib.gcd_euclid(d, n) == 1: 
            count += 1 # reduced fraction
print(count)
