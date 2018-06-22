import libtkoz as lib
import math
from functools import reduce

solutions = 1000

# 1/x+1/y=1/n, we must have x>n and y>n so use x=n+x0 and y=n+y0
# n(x+y)=xy --> n(2n+x0+y0)=n^2+nx0+ny0+x0y0 --> n^2=x0y0
# we need the smallest perfect square with enough distinct ways to factor it
# into x0*y0 such that x0<=y0. every factor x0<=n corresponds to a y0=n/x0 so
# n^2 must have 1000 divisors <= n, or 1999 overall (exclude counting n twice)
# any perfect square will have an odd number of divisors (counting divisors with
# the product of 1+ prime exponents) so we need a n^2 with >2*solutions divisors

primes = [] # find enough primes so that 3^(prime count)>2*solutions
n = 2
while 3**len(primes) <= 2*solutions:
    if lib.prime(n): primes.append(n)
    n += 1
print(': generated primes',primes)
smallest = reduce(lambda x,y:x*y, (p*p for p in primes))
print(': initial product of the squares is',smallest)
print(':',smallest,lib.divisors2(smallest),lib.prime_factorization(smallest))

# recurse on the prime list to find a smaller number with over 2000 divisors
# order exponents in decreasing order, 2^a*3^b has (a+1)(b+1) divisors so order
# a >= b (put the greater exponent on the smaller number
def recurse(number,primeindex,divisors,lastexp):
    global primes, smallest, solutions
    if divisors > 2*solutions:
        print(':',number,divisors,lib.prime_factorization(number),
              lib.divisors2(number))
        smallest = min(smallest,number)
        return # multiplying more would only make the number larger
    curexp = 2
    number *= primes[primeindex]**2
    divisors *= 3 # repeatedly multiply squares of current prime
    while number < smallest and curexp <= lastexp:
        recurse(number,primeindex+1,divisors,curexp)
        number *= primes[primeindex]**2
        curexp += 2
        divisors = divisors * (curexp+1) // (curexp-1)
recurse(1,0,1,2*solutions)
print(int(math.sqrt(smallest)))
