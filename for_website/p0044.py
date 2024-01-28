from math import sqrt,ceil
P = lambda n : n*(3*n-1)//2

def pentagonal(x):
    n = ceil(sqrt(2*x/3))
    return 2*x == n*(3*n-1)

def divisors(n):
    # return a list of divisors in increasing order
    lo = []
    hi = []
    d = 1
    while d*d < n:
        if n % d == 0:
            lo.append(d)
            hi.append(n//d)
        d += 1
    if d*d == n:
        lo.append(d)
    return lo + hi[::-1]

def get_divisors(i):
    # divisors of i
    di = divisors(i)
    # divisors of 3*i-1
    dj = divisors(3*i-1)
    ret = []
    for d1 in di: # multiply 1 from each list
        for d2 in dj:
            d = d1*d2
            if d >= i:
                break
            ret.append(d)
    return sorted(ret)

i = 1
found = False
while True:
    Pi = P(i) # use as D
    # next search for j,k so P(k)-P(j)=P(i)
    # d must be = i (mod 3) and < i
    #divs = [d for d in range(i-3,0,-3) if (2*Pi) % d == 0]
    divs = get_divisors(i)
    for d in divs: # d=k-j
        tmp1 = (2*Pi)//d # 3(k+j)-1
        if tmp1 % 3 != 2:
            continue
        tmp2 = (tmp1+1)//3 # k+j
        # get k
        if (tmp2+d) % 2 != 0:
            continue
        k = (tmp2+d)//2
        j = k - d
        if j <= 0:
            continue
        if pentagonal(P(k)+P(j)):
            print(f'found {k},{j} with D={Pi}=P({i})')
            print(Pi)
            found = True
    i += 1

quit()

from math import sqrt,ceil
P = lambda n : n*(3*n-1)//2

def pentagonal(x):
    n = ceil(sqrt(2*x/3))
    return 2*x == n*(3*n-1)

# find a solution and continue until a better one is not possible
k = 2
minD = 0
while True:
    Pk = P(k)
    if minD != 0 and Pk - P(k-1) > minD:
        break
    for j in range(k-1,0,-1):
        Pj = P(j)
        D = Pk - Pj
        # stop if a solution was found already and D is too big
        if minD != 0 and D > minD:
            break
        S = Pk + Pj
        if pentagonal(D) and pentagonal(S):
            minD = D
            print(f'solution D={D} with j={j},k={k}')
            break
    k += 1
print(f'terminated main loop at k={k}')
print(minD)
