import libtkoz as lib

nlim = 10**6

# brute force + cache for dynamic programming, ~2min (i5-2540m)

cache = [0,0] # cache mrds for smaller numbers
def mdrs(n): # assume len(cache) == n
    global cache
    bestmdrs = 0
    d = 2 # try to factor n
    while d*d <= n:
        if n % d == 0: bestmdrs = max(bestmdrs,lib.digital_root(d)+cache[n//d])
        d += 1
    bestmdrs = max(bestmdrs,lib.digital_root(n))
    cache.append(bestmdrs)
    return bestmdrs

mdrssum = 0
for n in range(2,nlim): mdrssum += mdrs(n)
print(mdrssum)
