import libtkoz as lib
import math

maxD = 1000
showminx = False # toggle to show/hide some output

# diophantine equations x^2 - D * y^2 = 1
# no solutions if D is a perfect square, find minimal x

largestminx = 0
bestD = 0
for D in range(2, maxD+1):
    if lib.is_square(D): continue # only trivial (x,y)=(1,0) solution
    # chakravala method, starting values
    a, b = int(math.floor(math.sqrt(D))), 1
    k = a**2 - D
    while k != 1: # eventually terminates with k=1, solution to pells equation
        # pick m congruent to -a (mod k), m <= floor(sqrt(D)) < m+abs(k)
        m = 0 # find with a loop
        absk = abs(k)
        intD = math.floor(math.sqrt(D))
        for mm in range(intD, intD + absk):
            if (a + b*mm) % absk == 0:
                m = mm
                break
        assert m != 0 # by induction, these can be shown to be true
        assert (a*m + D*b) % absk == 0
        assert (a + b*m) % absk == 0
        assert (m**2 - D) % absk == 0
        a, b, k = (a*m + D*b) // abs(k), (a + b*m) // abs(k), (m**2 - D) // k
    if showminx: print(': for D =', D, ', min x =', a)
    if a > largestminx: largestminx, bestD = a, D
print(bestD)

