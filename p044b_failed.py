# https://codereview.stackexchange.com/questions/93232/speedup-for-project-euler-44-pentagon-numbers

import libtkoz as lib
import math

pent = lambda n : n*(3*n-1)//2

# a strategy by using squares
# P(n)=n(3n-1)/2 --> ((6n-1)^2-1)/24 (by completing square)
# take P(k) and P(j), their difference + their sum gives
# 2P(k)=P(x)+P(y), P(x) is the dif, P(y) is the sum
# must find integers K=6k-1, X=6x-1, Y=6y-1 to satisfy 2K^2=X^2+Y^2
k = 5
foundfirst = False
maxD = 0
while (not foundfirst) or 3*k-2 < maxD:
    for x in range(5, k+1, 6):
        yy = 2*(k**2)-(x**2)
        if not lib.is_square(yy): continue
        y = int(math.sqrt(yy))
        if y % 6 != 5: continue
        # now use P(j)=P(k)-P(x) to test for pentagonality
        if not lib.is_pentagonal(pent(k) - pent(x)): continue
        foundfirst = True
        maxD = pent(x)
        print(':', pent(x))
        print(':', k, x, y)
    k += 6
    print(k)
print(': k stopped at', k)
print(maxD)

