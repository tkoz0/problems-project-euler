import libtkoz as lib
import math

s2val = 10**15
modulus = 10**9

# large input, square root measures relatively how long this solution takes,
# its still large, ~1min (cpython / i5-2540m)

# to solve floor(n/i)=k, i can be in range 1+floor(n/(k+1)) to floor(n/k)
# n/(n/k+1)=k+1 so taking floor of denomenator will make left larger so we cant
# get k on right side with floor, but if we increase the denomenator then the
# left side gets smaller so its floor is k
# n/(n/k)=k so if n/k is increased then floor of left side is smaller than k

# we need to sum squares of every factor and count it the number of times it is
# a factor up to the limit, so we get i^2 * floor(max/i) for i from 1 to max
# if floor(max/i) is constant then we can multiply it by square sum formula
# max/1,max/2,...,max/sqrt(max) change quickly so sum those separately but
# numerous values satisfy max//i=1,max//i=2,... so those can be sped up with
# square summation, main loop should loop up to floor(sqrt(max))

def sum_squares(a,b): # sum a^2 + (a+1)^2 + ... + b^2
    if a > b: return 0
    bsum = b*(b+1)*(2*b+1)//6 # use square summation formula
    asum = (a-1)*a*(2*a-1)//6 # squares smaller than a^2 not included
    return bsum - asum

value = 0
for i in range(1,1+int(math.sqrt(s2val))):
    value = (value + i*i*(s2val//i)) % modulus # for i below square root
    kmin = 1+s2val//(i+1)
    if kmin == i: # avoid counting square root twice in summation
        assert i == math.floor(math.sqrt(s2val))
        kmin = i+1
    kmax = s2val//i # for i above square root, max//i constant
    value = (value + i*sum_squares(kmin,kmax)) % modulus
print(value)
