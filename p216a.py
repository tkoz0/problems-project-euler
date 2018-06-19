import libtkoz as lib

maxn = 50*10**6

t = lambda n : 2*n*n - 1

# very simple brute force, extremely slow, ~20min (pypy / i5-2540m)

count = 0
for n in range(2,maxn+1):
    if n%(10**6)==0:print(n)
    if lib.miller_rabin_verified(t(n)): count += 1
print(count)
