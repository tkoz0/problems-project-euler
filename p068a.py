import libtkoz as lib
from itertools import chain

sides = 5 # inner polygon

# problem is small enough to brute force every possibility, ~10sec (i5-2540m)
# could be sped up by skipping permutations where 10 is an inner node
# inner nodes are counted twice, outer are counted once
# with 15 digits, 10 must be counted only once so it must be an outer node

# outer nums are index [sides,2*sides)
# inner nums are index [0,sides)
# outer num i connects inward to index i-sides and i-sides-1 (or sides-1 if -1)
nums = list(range(1, 2*sides+1))
next_lexico = True
solutions = []
while next_lexico:
    linesum = nums[sides] + nums[0] + nums[sides-1] # first line
    samesum = True
    for start in range(sides+1, 2*sides): # make sure each line has same sum
        if nums[start] + nums[start-sides] + nums[start-sides-1] != linesum:
            samesum = False
            break
    if not samesum: # try next case
        next_lexico = lib.lexico_next(nums)
        continue
    string = ''
    start = 0 # start index for outer numbers
    minouter = sides*2+1 # greater than any
    for i in range(sides, 2*sides):
        if nums[i] < minouter:
            minouter = nums[i]
            start = i
    # create string going clockwise
    # increasing index goes counterclockwise since going clockwise inward uses
    # decreasing indexes, so go in decreasing order for starting outer nodes
    for i in chain(range(start, sides-1, -1), range(2*sides-1, start, -1)):
#    for i in chain(range(start, 2*sides), range(sides, start)):
        string += str(nums[i]) + str(nums[i-sides])
        if i == sides: string += str(nums[sides-1])
        else: string += str(nums[i-sides-1])
#    print(': sum =', linesum, ', string =', string)
    solutions.append(string)
    next_lexico = lib.lexico_next(nums)
#for s in solutions: print(s)
print(': unique solutions (16 and 17 digits) =', len(solutions))

# find maximum 16 digit string
best = 10**15 # smallest 16 digit number
for s in solutions:
    if len(s) == 16: best = max(best, int(s))
print(best)
