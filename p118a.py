import libtkoz as lib

# for each arrangement of the 9 digits, try recursively placing dividers to
# split into subsets, once a successful split occurs, keep track of a set of
# unique number sets made since they can be repeated
# ~45sec (cpython / i5-2540m) and ~8sec (pypy / i5-2540m)

uniquesets = set() # keep track of unique sets found
def recurse(nums,divs): # digits and dividers
    global uniquesets
    if divs[-1] == len(nums): # make set and insert
        s = set()
        prevdiv = 0
        for divi in range(1,len(divs)): # make numbers from dividers
            num = 0
            for i in range(prevdiv,divs[divi]): num = num*10 + nums[i]
            s.add(num)
            prevdiv = divs[divi]
        s = frozenset(s)
        if s in uniquesets: return
        uniquesets.add(s)
    else: # make prime number with next digits and place divider
        num = 0
        for d in range(divs[-1],len(nums)): # try each digit
            num = num*10 + nums[d]
            if lib.prime(num): # recurse with divider after last selected digit
                recurse(nums,divs+[d+1])

digits = list(range(1,10))
hasnextpermutation = True
# enumerate all permutations of digits and try splitting them recursively
while hasnextpermutation:
    recurse(digits,[0])
    hasnextpermutation = lib.lexico_next(digits)
print(len(uniquesets))
