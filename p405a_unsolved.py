
kval = 10**18
modulus = 17**7

def f10(k): # evaluate f(10**k)
    pass

# start with a sideways tile, its length is 2, for T_n, consider the width to be
# 2^(n+1) units, s tiles are sideways, t tiles are tall/upright
# for T_0 there is 1 s tile and 0 t tiles
# for T_1 there is 1 s tile and 2 t tiles
# conjecture that 2s+t=2^(n+1) for every tiling
# also conjecture this for T_n:
# n even: t = floor(2^(n+1)/3), s=t+1
# n odd: s = floor(2^(n+1)/3), t=s+1
# these are all true for T_0 and T_1, by induction this can be shown to be true
# for all n=0,1,2,...
# some tools for proof: n even: 2^n=1 (mod3), n odd: 2^n=2 (mod3)
# at each step, t tiles become s tiles along the edge, s tiles split to become
# 2 t tiles and 1 s tile along the edge
# this induction tells how many of each tile type are along the long edge
# for the shorter edge, just use T_n-1

# intersection points of 4 tiles occur where a + sign like cross happens
# to build the next tiling, start with a sideways tile, place a copy of it on
# top, then place 2 copies by the sides
# the number of 4 tile intersection points T_n is f(n) and probably satisfies
# some recurrence relation like f(n) = 4*f(n-1) + (crosses at tile joinings)

# need way to compute the crosses at a joining of tall tile with 2 sideways
# tiles, possible conjecture is that it is half of the joinings between the 2
# sideways tiles
# between the 2 sideways tiles, the number of joinings is (tiles on edge)-1

