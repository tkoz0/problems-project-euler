import libtkoz as lib

exceed = 1000000 # find M such that there are more than this many smaller
# cuboids with integer length shortest path

# if the cuboid has dimensions a<=b<=c then its 3 possible shortest paths are
# sqrt(a^2+(b+c)^2), sqrt((a+b)^2+c^2), sqrt(b^2+(a+c)^2)
# the shortest is sqrt(a^2+b^2+c^2+2ab)

# brute force, try all cubes, ~20min (i5-2540m)
intcount = 0 # with integer shortest path
M = 0 # maximum cuboid dimension
while intcount <= exceed:
    M += 1
    # use M=c, loop for a and b
    for b in range(M,0,-1):
        for a in range(b,0,-1):
            if lib.is_square(a*a+b*b+M*M+2*a*b): intcount += 1
print(': M =', M, 'with', intcount, 'solutions')
print(M)
