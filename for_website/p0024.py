from itertools import permutations
index = 1000000
perms = list(permutations('0123456789'))
print(''.join(perms[index-1]))

digits = set('0123456789')
I = 1000000
index = 0
def recur(perm):
    global index,digits
    if len(digits) == 0: # selected all 10 in some order
        index += 1
        if index == I:
            print(perm)
    elif index >= I: # terminate early
        return
    else:
        for d in sorted(digits):
            digits.remove(d) # select a digit
            recur(perm+d)
            digits.add(d) # backtrack
recur('')

digits = list('0123456789')
I = 1000000
index = 1
while index < I: # loop to advance permutation
    # decrease i until the digits stop increasing
    i = len(digits)-1
    while i != 0 and digits[i-1] >= digits[i]:
        i -= 1
    # choose i to be 1 before this
    i -= 1
    if i == -1: # the permutation is lexicographically highest
        break
    # choose digits[j] to be the smallest digit after digits[i]
    j = len(digits)-1
    while digits[j] <= digits[i]:
        j -= 1
    # swap these indexes
    digits[i],digits[j] = digits[j],digits[i]
    # finally, reverse the order of everything after index i
    i += 1
    j = len(digits)-1
    while i < j:
        digits[i],digits[j] = digits[j],digits[i]
        i += 1
        j -= 1
    index += 1
print(''.join(digits))
