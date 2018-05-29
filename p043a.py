digits = list(range(10))

def substr_divisibility(arr):
    # 2,3,5,7,11,13,17
    # 1,2,3 --> 7,8,9 (from 2,3,4 --> 8,9,10) (indexes)
    # arr[3] must be even
    # arr[2,3,4] must sum to a multiple of 3
    # arr[5] must me 0 or 5
    if not arr[5] in [0, 5]: return False
    if arr[3] % 2 != 0: return False
    if sum(arr[2:5]) % 3 != 0: return False
    if (100*arr[4]+10*arr[5]+arr[6]) % 7 != 0: return False
    if (100*arr[5]+10*arr[6]+arr[7]) % 11 != 0: return False
    if (100*arr[6]+10*arr[7]+arr[8]) % 13 != 0: return False
    if (100*arr[7]+10*arr[8]+arr[9]) % 17 != 0: return False
    return True

# brute force all permutations, reused code from problem 24, ~9 sec (i5-2540m)
array = digits[:]
array.sort()
total = 0
while True:
    if substr_divisibility(array):
        total += int(''.join(str(d) for d in array))
        print(':', ''.join(str(d) for d in array))
    i1 = len(array)-1 # position of digit breaking right to left nondecreasing
    while i1 != 0 and array[i1-1] >= array[i1]:
        i1 -= 1
    i1 -= 1 # previous breaks this ordering
    if i1 == -1: break # all digits in nonincreasing order
    i2 = len(array)-1 # find larger digit
    while array[i2] <= array[i1]:
        i2 -= 1
    # i2 now at index of larger digit
    array[i1], array[i2] = array[i2], array[i1] # swap
    i1 += 1 # start of section to sort
    i2 = len(array)-1 # end of section to sort
    while i1 < i2: # sorting loop
        array[i1], array[i2] = array[i2], array[i1]
        i1 += 1
        i2 -= 1
print(total)

