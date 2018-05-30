import math

cachesize = 50000 # amount of pentagonal numbers to cache for faster testing

pent = lambda n : n*(3*n-1)//2

cache = set(pent(n) for n in range(1, cachesize+1))
cachelim = pent(cachesize+1)

# x=n(3n-1)/2 --> 2x/3=n^2-n/3 --> (n-1)^2<2x/3<n^2
# pick n=1+floor(sqrt(2x/3)) and test 2x=3n^2-n
def is_pentagonal(x):
    if x < cachelim: return x in cache
    n = 1 + math.floor(math.sqrt(2*x/3))
    return 2*x == 3*(n**2) - n

# brute force with some ways to optimize
# initially finding a pair gets the correct answer but
# verifying that the initial pair is the best takes ~15sec (i5-2540m)
# the cache gave about 33% speed up, changing it a bit wont affect speed much

# first find a pair whose sum and difference are pentagonal
k = 2
foundone = False
maxD = 0
while not foundone:
    Pk = pent(k)
    for j in range(k-1, 0, -1):
        Pj = pent(j)
        D = Pk - Pj
        S = Pk + Pj
        if is_pentagonal(D) and is_pentagonal(S):
            maxD = D
            print(': initial P(', k, ') - P(', j, ') =', D)
            foundone = True
            break
    k += 1

# continue with k as the larger pentagonal index
# this part verifies no smaller D values exist
# P(k)-P(k-1)=3k-2 --> once 3k-2>=D then stop
while 3*k-2 < maxD:
    Pk = pent(k)
    for j in range(k-1, 0, -1):
        Pj = pent(j)
        D = Pk - Pj
        if D >= maxD: break # cannot be a more optimal solution
        S = Pk + Pj
        if is_pentagonal(D) and is_pentagonal(S):
            maxD = D
            print(': better P(', k, ') - P(', j, ') =', D)
    k += 1
print(': k stopped at', k)
print(maxD)

