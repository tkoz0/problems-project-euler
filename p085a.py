import math

# suppose the large rectangle has dimensions R,C
# for some subrectangle r,c, there are (1+R-r)*(1+C-c) ways to shift it around
# summing all of these is summing (R-r)*(C-c) for r in [0,R-1], c in [0,C-1]
# this summation evaluates to (1/4)RC(RC+R+C+1)
# for some constant R, we can solve for C to get the total close to 2 million
# suppose (1/4)RC(RC+R+C+1)=X, the quadratic equation becomes
# (R^2/4+R/4)*C^2 + (R^2/4+R/4)*C - X = 0, substitute z=(R^2/4+R/4)
# zC^2+zC-X=0 --> C=(-1/2)+sqrt(1/4+X/z) (pick positive solution)
# if no rectangle has X subrectangles, floor(C),ceil(C) give smaller/larger

contains = 2000000

subrects = lambda R,C : R*C*(R*C+R+C+1)//4

closest = 0
bestR, bestC = 0, 0
R = 1
while True: # continue until with C=1, solutions > contains
    if subrects(R,1) >= contains:
        # subrects(R,1) only gets larger so try this for better approximation
        value = subrects(R,1)
        if value-contains < abs(closest-contains):
            closest = value
            bestR, bestC = R, 1
        break
    z = R*(R+1)/4
    C = math.floor(-0.5 + math.sqrt(0.25 + contains/z))
    # subrects(R,C) < contains and subrects(R,C+1) > contains
    # try both for better approximation
    small, large = subrects(R,C), subrects(R,C+1)
    if contains-small < abs(closest-contains):
        closest = small
        bestR, bestC = R, C
    if large-contains < abs(closest-contains):
        closest = large
        bestR, bestC = R, C+1
    R += 1
print(': best approximation is', bestR, 'x', bestC, 'rect with', closest)
print(bestR*bestC)
