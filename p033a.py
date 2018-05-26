import libtkoz as lib

nummax = 100

def simplify_frac(n, d): # assumes 2 digit strings, returns integer tuple
    if sn[0] == sd[0]: return (int(sn[1]), int(sd[1])) # ax / ay
    if sn[0] == sd[1]: return (int(sn[1]), int(sd[0])) # ax / ya
    if sn[1] == sd[0]: return (int(sn[0]), int(sd[1])) # xa / ay
    if sn[1] == sd[1]: return (int(sn[0]), int(sd[0])) # xa / ya
    return None # if unable to find a simplification

# brute force
# n/d<1 --> n<d
product = (1, 1)
for n in range(10, nummax):
    for d in range(n+1, nummax):
        if n % 10 == 0 or d % 10 == 0:
            continue # should result in a 0 in any fraction component
        sn = str(n) # convert to strings for digits
        sd = str(d)
        simp = simplify_frac(sn, sd)
        if simp != None and simp[0] / simp[1] == n / d:
            print(':', n, '/', d, '=', simp[0], '/', simp[1])
            product = (product[0] * simp[0], product[1] * simp[1])
print(': product is', product)
gcd = lib.gcd_euclid(product[1], product[0])
print(': simplified', (product[0] // gcd, product[1] // gcd))
print(product[1] // gcd)

# working out possibilities
# 4 solution forms, i is cancellation digit, n and d are what will remain
# conditions: 1<=n<d<=9, 1<=i<=9
# (10i+n)/(10i+d)=n/d --> rearrange to n=d which cant be true
# (10n+i)/(10d+i)=n/d --> also rearranges to n=d
# (10i+n)/(10d+i)=n/d --> 10id+nd=10dn+in --> 10id-in=9nd
# --> 9id+i(d-n)=9nd --> i(d-n)=9d(n-i) --> n-i=i/9-(in)/(9d)
# d-n>0 so we must have n-i>0
# next we get n-i>=1 and i/9<=1, since next term >0, right side <1 so not true
# finally (10n+i)/(10i+d)=n/d --> 9nd=10in-id --> 9n(d-i)=i(n-d)
# n-d<0 so d-i<0 which means i>d so n<d<i
# loop for n,d,i and test equality of d(10n+i)=n(10i+d)
product = (1, 1)
for n in range(1, 10):
    for d in range(n+1, 10):
        for i in range(d+1, 10):
            if d * (10*n + i) == n * (10*i + d):
                print(':', 10*n+i, '/', 10*i+d, '=', n, '/', d)
                product = (product[0] * n, product[1] * d)
print(': product is', product)
gcd = lib.gcd_euclid(product[1], product[0])
print(': simplified', (product[0] // gcd, product[1] // gcd))
print(product[1] // gcd)

