import libtkoz as lib
import math

modexceed = 10**10
assert modexceed > 7

# by expanding (p-1)^n and (p+1)^n and ignoring terms which are multiples of p^2
# we get 2 when n is even and 2np when n is odd
# p_1=2,p_2=3,p_3=5,p_4=7,p_5=11 so we get 2n<p_n for n>=5 (since n goes up in
# steps of 1 and p_n goes up in steps of at least 2)
# therefore for n>=5 we get (p-1)^n+(p+1)^n % p^2 = 2np
# n=1 gives 2, n=2 gives 3, n=3 gives 5, n=4 gives 7

# we must find the smallest n such that 2*n*p_n > modexceed
# prime number theorem tells us n ~= p_n / ln(p_n)
# pick a p_n estimate that gives 2*n*p_n ~= modexceed, then move up or down to
# find the solution

pn = 2 # approximate p_n with binary method
while 2*int(pn/math.log(pn))*pn < modexceed: pn *= 2
pn //= 2 # step back
add = pn // 2
while add != 0:
    pn += add
    if 2*int(pn/math.log(pn))*pn > modexceed: pn -= add
    add //= 2
print(': estimated p_n =',pn,'with n ~=',int(pn/math.log(pn)))
# step back to find prime near p_n
while not lib.miller_rabin_verified(pn): pn -= 1
print(': found prime value p_n =',pn)
# count primes
n = len(lib.list_primes2(pn))
print(': found n =',n)
# count down if needed
while 2*n*pn > modexceed:
    n -= 1
    pn -= 1 # find previous prime
    while not lib.miller_rabin_verified(pn): pn -= 1
# go up to first n value that exceeds
while 2*n*pn <= modexceed:
    n += 1
    pn += 1
    while not lib.miller_rabin_verified(pn): pn += 1
print(': found p_',n,' = ',pn,' with product 2*n*p_n = ',2*n*pn,sep='')
# the only thing left now is to make sure the prime index n is odd so we get
# 2*n*p_n instead of 2 as the remainder
if n % 2 == 0: n += 1
pn += 1
while not lib.miller_rabin_verified(pn): pn += 1
print(': solution p_',n,' = ',pn,' with product 2*n*p_n = ',2*n*pn,sep='')
print(n)
