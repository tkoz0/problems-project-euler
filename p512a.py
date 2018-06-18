import libtkoz as lib

gval = 5*10**8

# due to the large sieve size, this solution was near the point of being
# infeasible, with pypy it still took a long time: ~8min (pypy / i5-2540m)
# VERY IMPORTANT: requires about 4GiB of RAM (sieve is gigantic)

# since we need totients up to gval, sieve totients
# start with sieve[i]=i, for i>1 phi(i)<i
sieve = list(range(gval+1))
for p in range(2,gval+1): # for each prime
    if sieve[p] != p: continue # was updated, has smaller prime factor
    sieve[p] -= 1 # phi(p) for primes
    for i in range(2*p,gval+1,p): # multiply multiples by (p-1)/p
        sieve[i] = sieve[i]*(p-1)//p

# g(n) = sum for i=1 to n: (sum for j=1 to i: phi(i**j)) mod (i+1)
# simplifies to
# sum i=1 to n: phi(i) * (i**i-1)/(i-1) mod (i+1)

# for computing the summand, use modulus (i-1)*(i+1) so (i-1) can be divided out
# the numerator is a multiple of i-1 so lets say it is k(i-1)
# divide this by (i-1)(i+1) and we get k/(i+1) so we want k mod (i+1) but since
# we use modulus (i-1)(i+1) we already have 0<=k<=i

def f(i): # the summand
    if i == 1: return 1
    global sieve
    v = (sieve[i]*(pow(i,i,i*i-1)-1))%(i*i-1)
#    assert v % (i-1)==0
    return v//(i-1)

print(sum(f(i) for i in range(1,gval+1)))
