n = 600851475143
d = 2
dmax = 1
while d*d <= n:
    while n % d == 0:
        n //= d
        dmax = max(dmax,d)
        print(f'factor {d}')
    d += 1
dmax = max(dmax,n)
if n != 1:
    print(f'factor {n}')
print(dmax)
