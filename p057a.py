import math

iterations = 1000

def digits(n): # number of base 10 digits
    return 1 + math.floor(math.log10(n))

# brute force with python large integer support
# x = 1 + (1 / (2 + 1 / (2 + 1 / ...)) --> x = 1 + 1 / (1 + x) --> x = sqrt(2)
# suppose we have x_n = 1 + 1 / (1 + x_n-1)
# this sequence results from recursively substituting x into itself for
# successive approximations of sqrt(2)
# if x_0 = 1 then we get x_1 = 1+3/2 (given), and so on

n, d = 1, 1 # fraction for approximation, initially x_0
count = 0
for itr in range(iterations):
    # compute next iteration by performing operations on x_n-1 to get x_n
    n += d # add 1
    n, d = d, n # 1 / (1+x_n-1), multiplicative inverse
    n += d # add 1 again
    if digits(n) > digits(d): count += 1 # more digits in numerator
print(count)
