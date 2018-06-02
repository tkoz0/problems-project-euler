import libtkoz as lib
import math

setsize = 5 # number of primes in prime pair set
assert setsize >= 2

# changing the cache method made it significantly faster, ~45sec (i5-2540m)
# since the caches took so long to generate and pairs of primes that concatenate
# to primes both ways are relatively rare its probably more effective to test
# the concatenations during the recursion instead of generating all of them when
# many probably will not be used, build a cache based on what is tested

# this time, use a set (hash table) to store pairs which concatenate to primes
paircache = dict()
def concat_primes(a, b): # are ab and ba (concatenations) prime
    global paircache
    if (a,b) in paircache: return paircache[(a,b)]
    result = lib.prime(a*(10**(1+int(math.log10(b))))+b) and \
             lib.prime(b*(10**(1+int(math.log10(a))))+a)
    paircache[(a,b)] = result
    return result

# generator for prime lists
plist1, plist2 = [], []
def generate_lists(primemax):
    global plist1, plist2
    plist = lib.list_primes2(primemax)
    plist1, plist2 = [3], [3]
    for i in range(3, len(plist)):
        if plist[i] % 3 == 1: plist1.append(plist[i])
        else: plist2.append(plist[i])
    print(': generated lists, max =', primemax, ', mod3=1 size =', len(plist1),
          ', mod3=2 size =', len(plist2))

bestsum = 0

def recurse1(indexes, s): # indexes is for cache1, s is sum of primes
    global plist1, bestsum, setsize
    if len(indexes) == setsize:
        bestsum = s
        print(': sum =', s, ', primes =', list(plist1[i] for i in indexes))
        return
    starti = 0 if indexes == [] else indexes[-1]+1
#    starti = len(plist1)-1 if indexes == [] else indexes[-1]-1
    for nexti in range(starti, len(plist1)):
#    for nexti in range(starti, -1, -1):
        # stop loop if it wont get a better set sum
        if s + (setsize - len(indexes)) * plist1[nexti] >= bestsum: break
        new_are_prime = True # make sure all new pairs will be prime
        for i in indexes:
            if not concat_primes(plist1[i], plist1[nexti]):
                new_are_prime = False
                break
        if new_are_prime: recurse1(indexes + [nexti], s + plist1[nexti])

def recurse2(indexes, s): # indexes is for cache2, s is sum of primes
    global plist2, bestsum, setsize
    if len(indexes) == setsize:
        bestsum = s
        print(': sum =', s, ', primes =', list(plist2[i] for i in indexes))
        return
    starti = 0 if indexes == [] else indexes[-1]+1
#    starti = len(plist2)-1 if indexes == [] else indexes[-1]-1
    for nexti in range(starti, len(plist2)):
#    for nexti in range(starti, -1, -1):
        if s + (setsize - len(indexes)) * plist2[nexti] >= bestsum: break
        new_are_prime = True
        for i in indexes:
            if not concat_primes(plist2[i], plist2[nexti]):
                new_are_prime = False
                break
        if new_are_prime: recurse2(indexes + [nexti], s + plist2[nexti])

itrmax = 1024
while True: # first find a prime pair set
    generate_lists(itrmax)
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
    generate_lists(initial_set_sum)
    bestsum = initial_set_sum
    recurse1([], 0)
    print(': finished recursing mod3=1 primes')
    recurse2([], 0)
    print(': finished recursing mod3=2 primes')
else:
    print(': no need since set sum doesnt exceed what was already tested')
print(bestsum) # will now have the optimal solution
