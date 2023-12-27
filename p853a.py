import libtkoz
import math

# pisano periods length 120 = 2*2*2*3*5
# factors 1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120

# known (m,n)=1 -> pi(mn)=lcm(pi(m),pi(n))
# if pi(p) divides n, then p divides fib(n)

# pi(p^k) divides p^(k-1)*pi(p) for primes p
# unknown if equal for all primes p, k > 1 (see wall-sun-sun prime)
# probably ok to assume equal for this problem
# not too hard to implement a fix to avoid assuming this

L = 120 # period length
M = 10**9 # limit
#import sys
#L = int(sys.argv[1])
Lf = libtkoz.prime_factorization(L)
print(':',L,Lf)

a,b = 0,1
for _ in range(1,L):
    a,b = b,a+b
Lfib = b
print(': fibonacci number',Lfib)

# find prime factors of fibonacci number
Lfibf = libtkoz.prime_factorization(Lfib)

primes = dict()
for p in Lfibf:
    if p not in primes:
        primes[p] = 0
    primes[p] += 1

print(': factorization',primes)

cycle = dict() # cycle length for each prime
for p in primes:
    a,b = 0,1
    i = 0
    while True:
        a,b = b%p,(a+b)%p
        i += 1
        if (a,b) == (0,1):
            break
    cycle[p] = i

print(': cycles',cycle)

primelist = list(primes.keys())

ret = 0 # sum satisfying numbers

# use these prime factors to build numbers with required cycle length = L
# recursively go through all divisors of the fibonacci number
def recur(p_index,num,factors):
    global primes,cycle,primelist,ret,L,M
    if p_index == len(primelist):
        #if num<1000:print(num,factors)
        #print(factors)
        cyclelen = 1
        for p,m in factors:
            mulval = 1
            if m > 0:
                mulval *= cycle[p]
            if m > 1:
                mulval *= p**(m-1)
            cyclelen = (cyclelen*mulval) // math.gcd(cyclelen,mulval)
        if cyclelen == L and num < M:
            #print(num)
            ret += num
        #if num<1000:print(num,cyclelen)
    else:
        for m in range(1+primes[primelist[p_index]]):
            recur(p_index+1,num*(primelist[p_index]**m),
                  factors+[(primelist[p_index],m)])

recur(0,1,[])
print(ret)
