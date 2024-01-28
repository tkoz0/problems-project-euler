from math import isqrt
given = 40755

hexn = lambda n : n*(2*n-1)

def pentagonal(x):
    # return 0 if not pentagonal, otherwise the index
    d = isqrt(1+24*x)
    if d*d == 1+24*x and d % 6 == 5:
        return (d+1)//6
    else:
        return 0

h = 1
while True:
    n = hexn(h)
    p = pentagonal(n)
    if p != 0: # n is pentagonal
        t = 2*h-1 # triangle number index
        print(f'T({t}) = P({p}) = H({h}) = {n}')
        if n > given: # terminate when finding the next one
            break
    h += 1
print(hexn(h))

T = lambda n : n*(n+1)//2
P = lambda n : n*(3*n-1)//2
H = lambda n : n*(2*n-1)
given = 40755

x,y = 1,1
while True:
    x,y = 2*x+3*y,x+2*y
    assert x*x - 3*y*y == -2
    print(f'diophantine solution {x}^2 - 3*{y}^2 = -2')
    if x % 6 == 5 and y % 4 == 3:
        m = (x+1)//6
        n = (y+1)//4
        assert H(n) == P(m)
        print(f'T({2*n-1}) = P({m}) = H({n}) = {H(n)}')
        if H(n) > given:
            print(H(n))
            break
