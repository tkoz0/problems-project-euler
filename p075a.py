import libtkoz as lib

maxL = 1500000

# compute primitive triples and count their multiples
# if a,b,c is a primitive triple, lengths n*(a+b+c) can be formed based on it

# index i represents 2i length since all primitive triples have even sums
counts = [0] * (1 + maxL//2)

# generate triples with
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# if gcd(m,n)!=1 then a common factor can be divided out
# also signs must be different or 2 is a common factor
# a+b+c = 2m^2+2mn = 2m(m+n), n can be 1 at minimum
m = 1
while m**2 < maxL//2: # keep 2m^2 within bounds
    for n in range(1 if m%2==0 else 2,m,2):
        if lib.gcd_euclid(m,n) != 1: continue
        # index m(m+n) and its multiples in counts need to be incremented
        step = m*(m+n)
        for i in range(step, 1 + maxL//2, step):
            counts[i] += 1
    m += 1
print(sum(1 for i in counts if i == 1)) # count ones
