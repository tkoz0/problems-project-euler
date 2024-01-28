from math import isqrt

def prime(n):
    if n < 4:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

n = 9
while True:
    if not prime(n) and \
        all(not prime(n - 2*r*r) for r in range(1,1+int(isqrt(n//2)))):
        print(n)
        break
    n += 2
