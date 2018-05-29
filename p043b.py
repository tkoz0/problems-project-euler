
digits = list(range(10))
# at index i, the digits i-2,i-1,i must be divisible by this
div = [1, 1, 1, 2, 3, 5, 7, 11, 13, 17]

assert len(digits) == len(div)

# use recursion for brute force
total = 0
def recurse(num, available):
    global total
    if available == []: # finished using all digits
        number = int(''.join(str(d) for d in num))
        if (number % 1000) % div[-1] == 0: # satisfies last requirement
            total += number
            print(':', number)
        return
    endi = len(num)-1
    # at least 3 digits to test
    if endi >= 2 and int(''.join(str(d) for d in num[-3:])) % div[endi] != 0:
        return # doesnt satisfy divisibility requirement
    for i in range(len(available)): # choose digit to recursively make solutions
        recurse(num + [available[i]], available[:i] + available[i+1:])

recurse([], digits[:])
print(total)

