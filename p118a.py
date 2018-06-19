import libtkoz as lib

# for each arrangement of the 9 digits, try recursively placing dividers to
# split into subsets, once a successful split occurs, keep track of a set of
# unique number sets made since they can be repeated
# ~35sec (cpython / i5-2540m) and ~5sec (pypy / i5-2540m)

count = 0
def recurse(digits,nums,prevdiv): # digits numbers made, last divider
    global uniquesets, count
    if prevdiv == len(digits): count += 1 # found a set with increasing primes
    else: # make prime number with next digits and place divider
        num = 0
        for d in range(prevdiv,len(digits)): # try each digit
            num = num*10 + digits[d]
            # only make sets with primes in increasing order for uniqueness
            if lib.prime(num) and (len(nums) == 0 or num > nums[-1]):
                recurse(digits,nums+[num],d+1)

digits = list(range(1,10))
hasnextpermutation = True
# enumerate all permutations of digits and try splitting them recursively
while hasnextpermutation:
    recurse(digits,[0],0)
    hasnextpermutation = lib.lexico_next(digits)
print(count)
