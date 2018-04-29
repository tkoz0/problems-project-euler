digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation=1000000

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
