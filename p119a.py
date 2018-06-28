import libtkoz as lib

index = 30

# keep a limit and consider exponentiation bases up to maximum digit sum
# increase the limit until enough numbers are discovered
# finally, sort them and select the proper index

maxdigits = 2 # will increase, max digit sum is 9 times this
nums = set()
expvals = [0,1] # index is digit sum, list stores exponentiated value

while len(nums) < index:
    # update existing digit sums (except 0 and 1) until reaching 10**maxdigits
    for dsum in range(2,len(expvals)):
        while expvals[dsum] < 10**maxdigits:
            if lib.sum_digits(expvals[dsum]) == dsum:
                nums.add(expvals[dsum])
            expvals[dsum] *= dsum
    # add new possible digit sums within constraints and similarly
    # exponentiate them until reaching 10**maxdigits
    for dsum in range(len(expvals),1+9*maxdigits):
        expvals.append(dsum)
        while expvals[dsum] < 10: expvals[dsum] *= dsum # cant be single digit
        while expvals[dsum] < 10**maxdigits:
            if lib.sum_digits(expvals[dsum]) == dsum:
                nums.add(expvals[dsum])
            expvals[dsum] *= dsum
    maxdigits += 1
print(':',sorted(nums))
print(sorted(nums)[index-1])
