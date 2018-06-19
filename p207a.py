import math

ratiobelow = 1/12345

def P(m): # based on given
    assert m >= 2
    # since 2^t must be integer, every k=z(z-1) where z>1 and z=2^t
    # largest z such that z(z-1) <= m gives us z-1 partitions
    maxz = math.floor(math.sqrt(m))
    if maxz*(maxz+1)<=m: maxz+=1
    # perfect partitions occur when z is a positive integer exponent of 2
    t = math.floor(math.log(maxz)/math.log(2.0))
    return t/(maxz-1)

# find the solution with binary search like method
# double m until going below ratio, then take a step back by halving
# now add halves of m at a time while staying at the ratio or higher
# add 1 to m at the end and then P(m) goes below the ratio
m = 2
while P(m) >= ratiobelow: m *= 2
else: # add halves until finding answer
    m //= 2
    bit = m//2
    while bit != 0:
        if P(m+bit) >= ratiobelow: m += bit
        bit //= 2
    m += 1
    print(m)

# using k=z(z-1), for P(k) there are z-1 partitions, perfect partitions occur
# when z is an integer exponent of 2, at those points, the ratio goes up then
# decreases, then increases at next z=2^i, etc
# we must find the largest z=2^i-1 such that the ratio is above ratiobelow
i = 2 # skip 1 because division by zero
while i/(2**i-2) >= ratiobelow: i += 1
i -= 1
print(': solution occurs when num perfect partitions =',i)
# now we must find z such that i/(z-1)<ratio --> z > 1+i/ratio
z = 1+i/ratiobelow # pick next integer
if math.fabs(z-round(z)) < 2**(-32): z = 1+round(z) # z is integer already
else: z = math.ceil(z)
print(z*(z-1)) # solution, m such that z(z-1)<=m

