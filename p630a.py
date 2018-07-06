from fractions import Fraction

numpoints = 2500

# 1.2 GiB RAM and 53sec (pypy / i5-2540m)
# the use of the Fraction objects requires a lot of memory

def point_gen():
    S0 = 290797
    while True:
        S1 = (S0*S0) % 50515093 # S_2k-1
        S2 = (S1*S1) % 50515093 # S_2k
        yield ((S1 % 2000) - 1000, (S2 % 2000) - 1000) # (T_2k-1, T_2k)
        S0 = S2

pg = point_gen()
pointlist = list(next(pg) for z in range(numpoints))

linetable = dict() # map slopes to distinct x,y intercept tuples

# find all distinct lines
for i1,p1 in enumerate(pointlist):
    for i2 in range(i1+1,len(pointlist)):
        p2 = pointlist[i2]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0: # vertical / undefined slope
            m = None
            pass
        else:
            m = Fraction(dy,dx)
            pass
        # lines can be uniquely determined by x,y interept (including not having
        # either due to being vertical / horizontal
        if m == 0: intercept = (None,p1[1]) # horizontal
        elif m == None: intercept = (p1[0],None) # vertical
        else: # compute intercepts
            yi = p1[1] - m*p1[0] # for y=mx+b form, y intercept
            xi = p1[0] - p1[1]/m # x intercept
            intercept = (xi,yi) # tuple of fractions
        if m in linetable: linetable[m].add(intercept)
        else:
            linetable[m] = set()
            linetable[m].add(intercept)

ML = sum(len(s) for s in linetable.values()) # number of distinct lines

# a line intersects every line with different slope
SL = sum((ML - len(s))*len(s) for s in linetable.values())

print(': M (',numpoints,') =',ML)#,sep='')
print(': S (',numpoints,') =',SL)#,sep='')
print(SL)
