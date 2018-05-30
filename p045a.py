import libtkoz as lib
import math

firstH = 40755 # given, find next one after this

# brute force solution is very quick

# if x is hexagonal, x=2n^2-n --> x/2=n^2-n/2 --> (n-1)^2<x/2<n
# find n=1+floor(sqrt(x/2)) for hexagonal index
firstHn = 1+math.floor(math.sqrt(firstH//2))
assert firstH == 2*(firstHn**2) - firstHn

# important fact: every hexagonal number is also triagonal
# suppose m=2n-1, T(m)=m(m+1)/2=H(n)
# loop numbers which are triagonal and hexagonal, (loop m above)
m = 2*firstHn + 1 # start at next hexagonal index (also triangle)
while True: # loop m, index of the triagonal number
    if lib.is_pentagonal(m*(m+1)//2): # also pentagonal
        # taken from lib, 1+floor(sqrt(2x/3)) to find index for x
        Pn = 1 + math.floor(math.sqrt(m*(m+1)/3)) # pentagonal index
        print(': T P H indexes are', m, Pn, (m+1)//2)
        print(m*(m+1)//2)
        break
    m += 2

