
def divcount(n):
    factors = 1
    while n % 2 == 0: # divide out 2s
        factors += 1
        n //= 2
    d = 3
    while d*d <= n: # find multiplicity of prime factors
        multiplicity = 0
        while n % d == 0:
            multiplicity += 1
            n //= d
        factors *= multiplicity+1
        d += 2
    if n != 1: # last prime factor
        factors *= 2
    return factors

D = 500
n = 1
while True: # try n(n+1)/2
    if n % 2 == 0: # n/2,n+1
        d1 = divcount(n//2)
        d2 = divcount(n+1)
    else: # n,(n+1)/2
        d1 = divcount(n)
        d2 = divcount((n+1)//2)
    if d1*d2 > D:
        print(n*(n+1)//2)
        print(f'{d1*d2} divisors, n = {n}')
        break
    n += 1
