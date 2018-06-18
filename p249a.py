import libtkoz as lib

primelim = 5000
modulus = 10**16

# generate primes and build sets 1 element at a time
# maintain a list than keeps track of how many subsets sum to each number
# keep a running cumulative sum of primes so the list can be dynamically
# expanded as the highest possible sum increases with each new prime
# lastly list primes up to the sum of primes in the set and use those as the
# indexes for computing the sum (count subsets with prime sums)
# takes ~2min (cpython / i5-2540m)

pset = lib.list_primes2(primelim-1)

# number of subsets with each sum
setswithsum = [1] # start with empty set

# build the set 1 element at a time
n=0
psumcumulative = 0 # keep track of this to dynamically grow the list
for p in pset:
    n+=1
    psumcumulative += p
    # sets with sum i = original amount + p added to sets with sum i-p
    newlist = setswithsum[:] + ([0]*p)
    for i in range(p,psumcumulative+1):
        newlist[i] = (newlist[i] + setswithsum[i-p]) % modulus
    setswithsum = newlist
#    assert sum(setswithsum)%modulus == (2**n)%modulus

# count sets with prime sums
print(sum(setswithsum[p] for p in lib.list_primes2(psumcumulative)) % modulus)
