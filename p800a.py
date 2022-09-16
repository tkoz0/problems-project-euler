import libtkoz
import math

# n = 800800**800800
LN_N = 800800*math.log(800800)
primes = libtkoz.list_primes2(int(2*LN_N))
print(':',f'listed primes to {primes[-1]}')

# (ALMOST) COPIED FROM 609 solution
# values of pi(n) for O(1) computation, go up to maximum pi(n) value
picache = []
primeset = set() # make for fast primality checking of smaller numbers
for i,p in enumerate(primes): # pi(p)=i+1
    primeset.add(p)
    while len(picache) < p: picache.append(i)
    picache.append(i+1)
    #if p > len(primes): break
print(': generated pi(n) cache up to',len(picache)-1)

# find limit for p (p < q) in p^q*q^p
P_LIM = 1
nlogn = lambda z : z*math.log(z)
while nlogn(2*P_LIM) < LN_N/2:
    P_LIM *= 2
bit = P_LIM
while bit:
    if nlogn(P_LIM+bit) < LN_N/2:
        P_LIM += bit
    bit //= 2
print(': P_LIM =',P_LIM)

result = 0
# p loop
for i,p in enumerate(primes):
    if p > P_LIM: break
    # compute largest q so q*ln(p)+p*ln(q) <= ln(n)
    q = 1
    while 2*q*math.log(p)+p*math.log(2*q) <= LN_N:
        q *= 2
    bit = q
    while bit:
        if (q+bit)*math.log(p)+p*math.log(q+bit) <= LN_N:
            q += bit
        bit //= 2
    #print(':',p,q,picache[q]-picache[p])
    result += max(0,picache[q]-picache[p])

print(result)
