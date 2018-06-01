import libtkoz as lib

familysize = 8
# assert familysize in [8, 9, 10]

primecache = lib.list_primes2(100000)
primelim = primecache[-1]
primecache = set(primecache)
def is_prime(n):
    if n > primelim: return lib.prime(n)
    return n in primecache

# suppose we replace some number of digits, use digit sum for 3 divisibility
# if d digits are replaced, digit sum starts at s if the digits are 0 then
# the digit sums will be s,s+d,s+2d,...,s+9d
# at least 8 must not be divisible by 3
# if d is not divisible by 3 then 3 or 4 of the sums are divisible by 3
# at most 7 could be prime in that case so for 8,9,10 digit replacements,
# we must replace 3,6,9,... digits

def advance_permutation(l): # lexicographic order, increasing order
    i1 = len(l)-1
    while i1 > 0 and l[i1-1] >= l[i1]: i1 -= 1 # break decrease order
    i1 -= 1
    if i1 == -1: return None # already maximum
    i2 = len(l)-1
    while l[i2] <= l[i1]: i2 -= 1 # smaller digit to swap
    l[i1], l[i2] = l[i2], l[i1]
    i1 += 1 # range to sort (in dec order so reverse to inc order)
    i2 = len(l)-1
    while i1 < i2:
        l[i1], l[i2] = l[i2], l[i1]
        i1 += 1
        i2 -= 1
    return l

numlen = 2 if familysize <= 7 else 4 # must replace >=3 digits for 8,9,10 size
minimum = -1 # smallest solution found
looplimit = -1
while True:
    print(': numlen =', numlen)
    # make larger than max possible solution in this iteration
    if minimum == -1:
        minimum = 10**numlen
    looplimit = 10**numlen # no number in this loop exceeds this
    # with family size above 7, replace multiple of 3 amount of digits
    for num_replaced in range(1 if familysize <= 7 else 3, numlen,
                              1 if familysize <= 7 else 3):
        print(': replacing', num_replaced, 'digits')
        # 1 means replace digit, 0 means select fixed digit
        mask = ([0] * (numlen - num_replaced)) + ([1] * num_replaced)
        digits = [0] * numlen # both of these are little endian
        while mask != None: # loop for all digit mask permutations
            print(': mask =', mask)
            # conditions to skip mask permutation
            # 1s digit must be 1,3,7,9
            if familysize > 4 and mask[0] == 1:
                mask = advance_permutation(mask)
                continue
            # most significant digit cant be 0
            if familysize == 10 and mask[-1] == 1:
                mask = advance_permutation(mask)
                continue
            # fixed digit range must ensure most significant digit isnt 0
            for f in range(0 if mask[-1] == 1 else 10**(numlen-num_replaced-1),
                           10**(numlen-num_replaced)): # select fixed digits
                ff = f
                add_amt = 0
                # set digits in reverse order so min is increasing in whole loop
                for i in range(numlen-1, -1, -1):
                    if mask[i] == 1: digits[i] = ff % 10 # fixed digit
                    else:
                        digits[i] = 0 # will be replaced
                        add_amt += 10**i
                    ff //= 10
                # convert digits array to an integer
                int_num = int((''.join(str(d) for d in digits))[::-1])
                counted = 0
                times_added = 0 # also equal to the digits being replaced
                familymin = 0
                if mask[-1] == 1: # most significant digit cant be 0
                    times_added += 1
                    int_num += add_amt
                while times_added < 10: # loop through rest
                    # cant make large enough family with remaining numbers
                    if 10 - times_added + counted < familysize: break
                    if is_prime(int_num):
                        counted += 1
                        # make sure family min is better
                        if counted == 1:
                            familymin = int_num
                            if familymin >= minimum: break
                    int_num += add_amt
                    times_added += 1
                if counted == familysize:
                    minimum = family_min
                    print(': next best', minimum)
                    print(': with mask', (''.join(str(m) for m in mask))[::-1])
            mask = advance_permutation(mask)
    numlen += 1
print(minimum)
