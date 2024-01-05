from math import sqrt,gcd

P = 1000
sols = [0]*(P+1) # count solutions for each perimeter

for m in range(1,1+int(sqrt(P//2))):
    n0 = 1 if m % 2 == 0 else 2
    for n in range(n0,m,2):
        if 2*m*(m+n) > P: # perimeter too big
            break
        if gcd(m,n) != 1:
            continue
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        d = 1
        while d*(a+b+c) <= P:
            sols[d*(a+b+c)] += 1
            d += 1

maxsol = max(sols)
maxp = [p for p in range(P+1) if sols[p] == maxsol]
print(f'found {maxsol} solutions for p = {maxp}')
print(maxp[0])
