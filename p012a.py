import libtkoz as lib

divisors = 500

# brute force, ~4 seconds in 2018
# divisors function is slow and based on brute force
num = 0
i = 1 # increment value
while True:
    num += i
    i += 1
    if lib.divisors1(num) > divisors:
        print(num)
        break
