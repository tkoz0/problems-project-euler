print(len(set(a**b for a in range(2,101) for b in range(2,101))))

L = 100
# express each integer 2,3,..,L as an integer power
intpow = [(n,1) for n in range(L+1)]
p = 2
while 2**p <= L:
    n = 2
    while n**p <= L:
        intpow[n**p] = (n,p)
        n += 1
    p += 1
# make set of (a,b) pairs with a reduced to smallest possible integer
values = set()
for a in range(2,L+1):
    for b in range(2,L+1):
        # rewrite a^b as n^(bp) using a=n^p
        n,p = intpow[a]
        values.add((n,b*p))
print(len(values))
