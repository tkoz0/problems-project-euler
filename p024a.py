digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#permutation = 1000000
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

# combinatorics algorithm, assumes all digits are unique
# an algorithm based on combinatorics, for example: 10th permutation of 1234
# theres 3!=6 of digits starting with 1 so 7th is 2134
# with 3 to go to get to 10th, 10-7=3 --> 3/2! = 1 increments of the 1
# therefore the 9th permutation is 2314
# similarly 10-9=1 --> 1/1!=1 increments of the 1 so 2341 is 10th permutation
# one fact to note is sum n=1 to x of n*n! = (x+1)! - 1 (prove by induction)
# start at min, index 1, largest permutation that can be reached is:
# 1 + 9*9!+8*8!+...+1*1! = (9+1)! = 10! (total possible permutations)
# target permutation number cant be larger than this
array = digits[:]
array.sort()
print(':', array)
factorials = [1]
for i in range(1,len(array)):
    factorials.append(factorials[i-1]*i)
print(': factorials', factorials)
assert 1 <= permutation <= factorials[-1] * len(array) # 10!
index = 1
start_i = 0 # start of undetermined section in result
factorial_i = len(factorials)-1 # amount to increment index
while index != permutation:
    increms = (permutation - index) // factorials[factorial_i]
    if increms != 0: # select next digit in solution
        index += increms * factorials[factorial_i] # new index
        array[start_i], array[start_i+increms] = \
            array[start_i+increms], array[start_i]
        # move index start+increms back to sort
        i = start_i+increms
        while i > start_i+1:
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
            i -= 1
        print(':', array, 'index', index)
    start_i += 1
    factorial_i -= 1
print(''.join(str(i) for i in array))
