import libtkoz as lib

# brute force, generate lexicographic permutations decreasing
# by considering digit sums we can show that only
# 7*8/2=28 and 4*5/2=10 are not divisible by 3, then there is 1*2/2=1
# 1 is not prime so the largest must have 4 or 7 digits
for l in [7, 4]:
    digits = list(range(l, 0, -1))
    print(': permuting', digits)
    found_prime = False
    while True: # go through all permutations
        # test primality
        if lib.prime(int(''.join(str(d) for d in digits))):
            print(''.join(str(d) for d in digits))
            found_prime = True
            break
        i1 = len(digits)-1 # find position of digit breaking right->left decrease
        while i1 != 0 and digits[i1-1] <= digits[i1]: i1 -= 1
        i1 -= 1
        if i1 == -1:
            print(': finished all', l, 'length permutations')
            break
        i2 = len(digits)-1 # find largest smaller digit to swap with it
        while digits[i2] >= digits[i1]: i2 -= 1
        digits[i1], digits[i2] = digits[i2], digits[i1] # swap
        i1 += 1 # sort starting from here
        i2 = len(digits)-1
        while i1 < i2:
            digits[i1], digits[i2] = digits[i2], digits[i1]
            i1 += 1
            i2 -= 1
    if found_prime: break
