
summax = 3 # larger causes stack overflow
modulus = 14**8

# map (m,n) to known ackermann function values to reduce recursion levels
cache = dict()
def A(m,n):
    global cache, modulus
    if (m,n) in cache: return cache[(m,n)]
    v = 0 # set to value of A(m,n), then insert in cache and return
    if m == 0: v = (n+1)%modulus
    elif n == 0: v = A(m-1,1) % modulus # m>0 and n=0
    else: v = A(m-1,A(m,n-1)) % modulus# m>0 and n>0
    cache[(m,n)] = v
    print('A(',m,',',n,') =',v)
    return v

print(sum(A(n,n) for n in range(summax+1)))
