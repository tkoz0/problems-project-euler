
funcs = { 3: lambda n : n*(n+1)//2,
          4: lambda n : n**2,
          5: lambda n : n*(3*n-1)//2,
          6: lambda n : n*(2*n-1),
          7: lambda n : n*(5*n-3)//2,
          8: lambda n : n*(3*n-2) }
types = len(funcs)
caches = dict()

# brute force, with caches to fast test numbers
# recurses on these numbers to find a cyclic set

# build caches of each type for 4 digit numbers
for k in funcs:
    n = 1
    f = funcs[k]
    while f(n) < 1000: n += 1
    nums = set()
    while f(n) < 10000:
        nums.add(f(n))
        n += 1
    caches[k] = nums

# recurse to find cyclic set of 4 digit numbers
numset = {} # initialize with 0
for k in funcs.keys(): numset[k] = 0
cycleorder = [] # will be initialized with cycle in order

# recurse on numbers, return true up the call stack as soon as solution is found
def recurse(prev, seqlen, seqbegtype):
    global numset, types, caches, cycleorder
    for t in numset.keys(): # try each type of number for next in sequence
        if numset[t] != 0: continue # skip type selected already
        for next in caches[t]: # possibilites for next if it is type t
            if next in numset.values(): continue # cant have a duplicate
            # make sure it is cyclic
            if next // 100 != prev % 100: continue
            numset[t] = next
            if seqlen == types-1: # last number is selected
                # digits dont form a cycle
                if numset[seqbegtype] // 100 != next % 100: continue
                cycleorder.insert(0, next)
                return True
            else: # recurse, return true up call stack if this branch finds it
                if recurse(next, seqlen+1, seqbegtype):
                    cycleorder.insert(0, next) # make cycle in order
                    return True
        numset[t] = 0 # backtrack
    return False

# begin with a triangle number and recurse
for tn in caches[3]:
    numset[3] = tn # make this first number
    if recurse(tn, 1, 3):
        cycleorder.insert(0, tn)
        break

print(': solution found is', numset)
print(': cycle order is', cycleorder)
print(sum(numset.values()))

