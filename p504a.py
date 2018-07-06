import libtkoz as lib

m = 100

# brute force, 4sec (pypy / i5-2540m)

# make a set of square numbers for fast checking, maximum is 2m^2
squares = set(z*z for z in range(2*m))

# gcd table for fast checking
gcd = list(list(lib.gcd_euclid(r,c) for c in range(m+1)) for r in range(m+1))

# brute force all possibilities
count = 0
for a in range(1,m+1):
    for b in range(1,m+1):
        for c in range(1,m+1):
            for d in range(1,m+1):
                # count contained vertices
                # for each quadrant determined by a,b, a*b vertices (>0 values)
                # subtract number on the line, divide by 2
                points = a+b+c+d - 3 # axis points (origin counted 4 times)
                # a*b area, exclude points on line, do for each quadrant
                # these can be shown to be true with pick's theorem
                ab = (a-1)*(b-1) + 1 - gcd[a][b]
                bc = (b-1)*(c-1) + 1 - gcd[b][c]
                cd = (c-1)*(d-1) + 1 - gcd[c][d]
                da = (d-1)*(a-1) + 1 - gcd[d][a]
                #assert ab%2==0 and bc%2==0 and cd%2==0 and da%2==0
                points += (ab+bc+cd+da)//2
                if points in squares: count += 1
print(count)
