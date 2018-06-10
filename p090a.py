
# numbers that are made by the dice, 9s replaced with 6s
numbers = { (0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (6,4), (8,1) }

# for each die, pick 6 of 10 numbers so (10 6) = 10*9*8*7/24 = 210 choices / die
# when forming numbers, replace 9 with 6 (if it exists)

def dice_itr(nums):
    # if there are k more nums to pick, range is last+1 to max-k+1
    if len(nums) == 6:
        yield nums
    elif len(nums) > 0:
        for next in range(1+nums[-1], 1 + (10-6+len(nums))):
            yield from dice_itr(nums + [next])
    else: # nums=[]
        for next in range(0, 1 + (10-6)):
            yield from dice_itr([next])
dicel = list(dice_itr([])) # all possible dice

# try pairs of dice and find which ones can form all the required numbers
possibilities = 0
for i1 in range(len(dicel)): # dice order doesnt matter
    for i2 in range(i1,len(dicel)):
        d1 = dicel[i1]
        d2 = dicel[i2]
        # replace 9 with 6 for this problem
        if d1[-1] == 9: d1[-1] = 6
        if d2[-1] == 9: d2[-1] = 6
        numsmade = set()
        for n1 in d1: # insert all possible numbers that can be made with these
            for n2 in d2:
                numsmade.add((n1,n2))
                numsmade.add((n2,n1))
        # make sure all required numbers are present
        allmade = True
        for n in numbers:
            if not n in numsmade:
                allmade = False
                break
        if allmade: possibilities += 1
print(possibilities)
