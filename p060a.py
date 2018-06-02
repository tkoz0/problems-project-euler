import libtkoz as lib

setsize = 5 # number of primes in prime pair set
assert setsize >= 2

# prime cache to speed up primality checking
pclim = 1000000
pcset = set(lib.list_primes2(pclim))
def is_prime(n):
    if n <= pclim: return n in pcset
    return lib.prime(n)
print(': generated primality checking cache with limit =', pclim)

# brute force with some optimizations, took ~23min (i5-2540m) (very long !!!)
# first observation: 2 or 5 cant be in the set
# every prime in the set must have same mod3 value (all 1 or all 2)
# if 1 and 2 are mixed, concatenating those 2 gives a number divisible by 3
# based on this, split the prime caches based on their mod3 value
# additionally, 3 may be used in these so each cache half must have 3

# the caches take a very long time to generate relative to how long the
# recursion spends searching candidate prime sets
# just by observation, recursing was almost instant, even for large limits

primecache1, primecache2 = [], [] # split based on mod3 value
paircache1, paircache2 = [[]], [[]]
def initialize_caches(primemax):
    print(': initializing caches with prime limit =', primemax)
    global primecache1, primecache2, paircache1, paircache2
    primelist = lib.list_primes2(primemax) # starts with 2,3,5,7
    primecache1, primecache2 = [3], [3] # separately insert 3
    for i in range(3, len(primelist)): # split cache
        if primelist[i] % 3 == 1: primecache1.append(primelist[i])
        else: primecache2.append(primelist[i]) # will have mod3 value = 2
    print(': generate split prime lists, len(mod3=1) =', len(primecache1),
          ', len(mod3=2) =', len(primecache2))
    paircache1 = list(list(False for c in range(len(primecache1)))
                      for r in range(len(primecache1)))
    paircache2 = list(list(False for c in range(len(primecache2)))
                      for r in range(len(primecache2)))
    for i,pi in enumerate(primecache1): # generate mod3=1 pair primality cache
        ibase = pi # use to shift left based on digits in prime index j
        nextleftshift = 1
        for j,pj in enumerate(primecache1):
            if i == j: continue # would have factor 11 or 101 or 1001, ...
            if pj >= nextleftshift:
                ibase *= 10
                nextleftshift *= 10
            conc = ibase + pj
            paircache1[i][j] = is_prime(conc)
    print(': generated lookup table for mod3=1')
    for i,pi in enumerate(primecache2): # generate mod3=2 pair primality cache
        ibase = pi
        nextleftshift = 1
        for j,pj in enumerate(primecache2):
            if i == j: continue
            if pj >= nextleftshift:
                ibase *= 10
                nextleftshift *= 10
            conc = ibase + pj
            paircache2[i][j] = is_prime(conc)
    print(': generated lookup table for mod3=2')
    print(': done')

bestsum = 0

def recurse1(indexes, s): # indexes is for cache1, s is sum of primes
    global primecache1, paircache1, bestsum, setsize
    if len(indexes) == setsize:
        bestsum = s
        print(': sum =', s, ', primes =', list(primecache1[i] for i in indexes))
        return
    starti = 0 if indexes == [] else indexes[-1]+1
    for nexti in range(starti, len(primecache1)):
        # stop loop if it wont get a better set sum
        if s + (setsize - len(indexes)) * primecache1[nexti] >= bestsum: break
        new_are_prime = True # make sure all new pairs will be prime
        for i in indexes:
            if (not paircache1[i][nexti]) or (not paircache1[nexti][i]):
                new_are_prime = False
                break
        if new_are_prime: recurse1(indexes + [nexti], s + primecache1[nexti])

def recurse2(indexes, s): # indexes is for cache2, s is sum of primes
    global primecache2, paircache2, bestsum, setsize
    if len(indexes) == setsize:
        bestsum = s
        print(': sum =', s, ', primes =', list(primecache2[i] for i in indexes))
        return
    starti = 0 if indexes == [] else indexes[-1]+1
    for nexti in range(starti, len(primecache2)):
        if s + (setsize - len(indexes)) * primecache2[nexti] >= bestsum: break
        new_are_prime = True
        for i in indexes:
            if (not paircache2[i][nexti]) or (not paircache2[nexti][i]):
                new_are_prime = False
                break
        if new_are_prime: recurse2(indexes + [nexti], s + primecache2[nexti])

itrmax = 32
while True: # first find a prime pair set
    initialize_caches(itrmax)
    bestsum = itrmax * setsize # larger than any set sum initially
    recurse1([], 0) # try with all possible sets of primes
    print(': finished recursing mod3=1 primes')
    recurse2([], 0)
    print(': finished recursing mod3=2 primes')
    if bestsum != itrmax * setsize:
        print(': initial candidate set sum found =', bestsum)
        break
    itrmax *= 2
initial_set_sum = bestsum

# now verify that no better solutions exist
# no better solutions can have a prime larger than the sum
print(': attempting to find better solutions')
if initial_set_sum > itrmax: # havent tested high enough yet
    initialize_caches(initial_set_sum)
    bestsum = initial_set_sum
    recurse1([], 0)
    print(': finished recursing mod3=1 primes')
    recurse2([], 0)
    print(': finished recursing mod3=2 primes')
else:
    print(': no need since set sum doesnt exceed what was already tested')
print(bestsum) # will now have the optimal solution

