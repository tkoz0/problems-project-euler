import libtkoz as lib

divisors = 500

# brute force, ~4 seconds (i7-7600u)
# divisors function is slow and based on brute force
num = 0
i = 1 # increment value
while True:
    num += i
    i += 1
    if lib.divisors1(num) > divisors:
        print(num)
        break
