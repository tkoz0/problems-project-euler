S = 1000
for a in range(1,1+S//3):
    for b in range(a+1,1+S//2):
        c = S - a - b
        if a*a + b*b == c*c:
            print(f'triple ({a},{b},{c})')
            print(a*b*c)

from math import sqrt,gcd

S = 1000
assert S % 2 == 0

for m in range(1,1+int(sqrt(S//2))):
    if (S//2) % m != 0:
        continue # m must be a factor of S/2
    n0 = 1 if m % 2 == 0 else 2 # m odd -> n even, m even -> n odd
    for n in range(n0,m,2):
        if (S//2//m) % (m+n) != 0:
            continue # m+n must be a factor of S/(2m)
        if gcd(m,n) != 1:
            continue # m,n must be coprime for a primitive triple
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        d = S//2//m//(m+n)
        print(f'triple {d} * ({a},{b},{c})')
        print(a*b*c * d**3)
