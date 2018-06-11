import math

numlim = 10000000

def digitsqsum(n):
    if type(n) == list: return sum(a**2 for a in n)
    s = 0
    while n != 0:
        s += (n%10)**2
        n //= 10
    return s

def end89(n): # repeat sequence until either 1 or 89
    n = digitsqsum(n)
    if n == 0: return False # special case for all zeroes
    while n != 1 and n != 89: n = digitsqsum(n)
    return n == 89

# this works because every number up to 7 digits is considered
# combinatorics tells us for a digit set how many numbers have same digits
# 11440 possibilities, 9 items, place 7 dividers, how many items before the
# divider tells us the value of that digit so (9+7 7)=(16 7) = 11440 ways
# for each digit combination, choose how many permutations can be formed from
# the digits if its sequence ends in 89

maxdigits = 1+math.floor(math.log10(numlim-1))

factorials = list(math.factorial(x) for x in range(maxdigits+1))
count = 0
def recurse(digits):
    global maxdigits, count, factorials
    if len(digits) == maxdigits: # try this digit set
        if not end89(digits): return
        # count each type of digit
        dcounts = [0]*10
        for d in digits: dcounts[d] += 1
        # count permutations
        perms = factorials[maxdigits]
        for n in dcounts: perms //= factorials[n]
        count += perms # count permutations that end in 89
    elif len(digits) == 0:
        for next in range(10): recurse([next])
    else:
        for next in range(digits[-1],10): recurse(digits+[next])
recurse([])
print(count)
