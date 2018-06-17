
nlim = 10**7

def M(n):
    for a in range(n-1,-1,-1):
        if (a*a) % n == a: return a

if True:

    sieve = [1] * (nlim+1)
    sieve[0] = sieve[1] = 0
    
    for a in range(2,nlim+1):
    #    print('a =',a)
        istep = 1 # n=a+i, step size to next square
        i2 = 0 # this is i^2
        for n in range(a+1,nlim+1):
            i2 += istep
            istep += 2
            if i2 % n == a: sieve[n] = a
    
    print(sum(sieve))

print(sum(M(n) for n in range(1,nlim+1)))
