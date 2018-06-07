import libtkoz as lib

digits = 100
maxnum = 2 # TODO change to 100

# compute the digits for each number

digitsum = 0
for num in range(2,maxnum+1):
    if lib.is_square(num): continue # only sum for irrational square roots

print(digitsum)
assert digitsum == 475 # given for sqrt(2)
