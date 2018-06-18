
gval = 5*10**8

# continuing from previous solution, expand the inner summation:
# phi(i)(1+i+i^2+...+i^(i-1)) mod i+1, replace terms with modular congruency
# phi(i)(1-1+1-1+....+-1) mod i+1
# so the summand is phi(i) for odd i and 0 for even i
# compute the sum of odd totients up to limit

# VERY IMPORTANT: requires about 2GiB RAM
# still slow, ~1min (pypy / i5-2540m)

# odd totients sieve
sieve = list(range(1,gval+1,2)) # index i represents 2i+1
for p in range(1,len(sieve)): # prime is 2p+1
    pval = 2*p+1
    if sieve[p] != pval: continue # already marked
    sieve[p] -= 1 # prime totient
    for i in range(p+pval,len(sieve),pval): # factor of 3*pval,5*pval,...
        sieve[i] = sieve[i]*(pval-1)//pval
print(sum(sieve))
