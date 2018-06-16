import libtkoz as lib
import math

mostdigits = 16
base = 16
musthave = set(['0', '1', 'A'])
assert len(musthave) <= mostdigits and len(musthave) <= base

# count with inclusion-exclusion
# all - (how many exclude 1 digit) + (how many exclude 2) - (how many exclude 3)
# 16^16 - 3*15^16 + 3*14^16 - 13^16
# problem is that numbers cant start with 0 so for each number length, consider
# numlen-1 sequence of digits, then prepend a nonzero number
# if prepending a must have digit, the sequence following must have the musthave
# digits other than that one, if prepending a nonmusthave digit, then the
# sequence following must have all the musthave digits
# the smaller sequence can be counted with inclusion exclusion
# with prepending digits, multiply how many there are (musthave and nonmusthave)
# by how many valid following digit sequences there are based on that choice

numhave = len(musthave)
musthave0 = '0' in musthave
counted = math.factorial(numhave) # permutations of the digits it must have
if musthave0: counted -= math.factorial(numhave-1) # if start digit is 0

for numlen in range(numhave+1,mostdigits+1): # count for each amount of digits
    # with numlen digits, pick first nonzero digit, count for length numlen-1
    countedtmpall = 0 # length numlen-1: how many have all required digits
    alloweddigits = base
    negative = False
    for exclude in range(numhave+1): # excluding 0 to all required digits
        value = lib.binom_coeff(numhave,exclude) * (alloweddigits**(numlen-1))
        if negative: countedtmpall -= value
        else: countedtmpall += value
        alloweddigits -= 1
        negative = not negative
    countedtmpe1 = 0 # length n-1: how many have at least all but 1 required
    alloweddigits = base
    negative = False
    for exclude in range(numhave): # exclude 0 to musthave-1
        value = lib.binom_coeff(numhave-1,exclude) * \
                (alloweddigits**(numlen-1))
        if negative: countedtmpe1 -= value
        else: countedtmpe1 += value
        alloweddigits -= 1
        negative = not negative
    if musthave0:
        # for start digits not in musthave, numlen-1 number must have all them
        counted += (base-numhave) * countedtmpall
        counted += (numhave-1) * countedtmpe1
    else:
        counted += numhave * countedtmpe1
        counted += (base-numhave-1) * countedtmpall # exclude 0
print('{0:X}'.format(counted))
