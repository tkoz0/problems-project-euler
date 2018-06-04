import libtkoz as lib
import math

maxnum = 10000
printsequences = False # toggle to see info about the expansions

# brute force, evaluate series for every square root
# at each step, we have some value x to write as i+f (integer + 0<f<1)
# initially, lets say we start with sqrt(n), use a=floor(sqrt(n))
# so we start with sqrt(n) = a + (sqrt(n) - a)/1
# we must repeatedly write the fractional part as 1/(some value > 1)

# the method used below is based on some observations and no justification is
# given to suggest they are always true

oddcount = 0
for n in range(2, maxnum+1):
    if lib.is_square(n): continue # skip perfect squares
    a = math.floor(math.sqrt(n))
    rem = (n, -a, 0, 1) # [sqrt(n) - a] / [sqrt(0) + 1]
    loop = [] # loop created in the continued fraction expansion
    while True: # perform an iteration, stop once denomenator is 1 again
        # this is an observation that cycling eventually results in a fractional
        # part with 1 denomenator so we get sqrt(n)-a as a fractional part again
        rem = (rem[2], rem[3], rem[0], rem[1]) # flip fraction
        den = rem[2] - rem[3]**2 # denonator after multiply by conjugate
        # obsernation that the numerator constant gets divided out
        assert den % rem[1] == 0, 'failure '+str(den)+' % '+str(rem[1])+' != 0'
        rem = (rem[2], -rem[3], 0, den // rem[1]) # after multiply by conjugate
        # rem[1] (constant) can be subtracted by up to rem[1]+a
        # it must be multiple of denomenator, this calculates integer part
        intpart = (rem[1] + a) // rem[3]
        # subtract integer component
        rem = (rem[0], rem[1] - intpart*rem[3], rem[2], rem[3])
        loop.append(intpart) # next in sequence
        if rem[3] == 1: break # 1 denomenator ends loop (observation)
    if printsequences:
        print(': sqrt(', n, '), period = ', len(loop),
              ', [', a, ';', tuple(loop), ']', sep = '')
    if len(loop) % 2 == 1: oddcount += 1 # count odd length periods
print(oddcount)

