digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation=1000000

# find by incrementing the permutation, does not assume digit uniqueness
# first find some digit that breaks right to left nondecreasing: 4(3)521
# this is finding a section of the digits that is maximum
# there is a larger digit to the right of the selected one
# swap with the smallest digit that is larger: 4(5)321
# sort everything after selected position which are still in decreasing order
# since they are in decreasing order, a simple swapping algorithm will work
# this algorithm will take ~2 sec (i5-2540m)
array = digits[:]
array.sort()
index = 1
while index != permutation:
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
    index += 1
print(': found index', index)
print(''.join(str(i) for i in array))
