
maxn = 50*10**6

# if p | 2n^2-1, then p | 2m^2-1, for any m=kp+-n (k is a positive integer)
# for every T(n), divide it from these numbers it divides
# requires about 1GiB RAM, ~15sec (pypy / i5-2540m)

sieve = list(2*n*n-1 for n in range(maxn+1))

# once reaching T(n)=2n^2-1 is the sieve, is it prime?
# if p=T(np)=2*(np)^2-1 (np is 1 number) is the smallest prime dividing T(n)
# np < p because if np > p then p divides T(np-p) (see above)
# also np<p/2 because if np>p/2 then p divides t(p-np) which is smaller
# at T(n), factors p<=2n have already been divided out
# T(n) cant have 2 prime factors larger than 2n since (2n)^2=4n^2>T(n) so
# T(n) must be prime once reaching it

count = 0
for n in range(2,maxn+1):
    if sieve[n] == 1: continue # divided out all prime factors
    p = sieve[n]
    if p == 2*n*n-1: count += 1 # unchanged so it is prime
    for m in range(p+n,maxn+1,p):
        while sieve[m] % p == 0: sieve[m] //= p
    for m in range(p-n,maxn+1,p):
        while sieve[m] % p == 0: sieve[m] //= p
print(count)
