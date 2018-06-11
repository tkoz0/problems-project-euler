import libtkoz as lib

xmax = 50
ymax = 50

# count based on locations of the right angle

# start with right angle between x and y axes, pick a x and y (nonzero)
# |\
# | \
# +---
triangles = xmax * ymax
# if right angle along x axis, pick an x and a y
#   /|
#  / |
# ---+
triangles += xmax * ymax
# similar for right angle along y axis
# +---
# | /
# |/
triangles += xmax * ymax

# pick a ray from (0,0) to (x,y) and make a right angle at not the origin
# slope of perpendicular line is -1/(y/x) = -x/y

for x in range(1,xmax+1):
    for y in range(1,ymax+1):
        # step sizes in lowest terms, slope is -x/y
        sy = x // lib.gcd_euclid(x,y)
        sx = y // lib.gcd_euclid(x,y)
        # count going lower right, how many steps until out of bounds
        triangles += min(y//sy, (xmax-x)//sx)
        # count going upper left, steps until out of bounds
        triangles += min(x//sx, (ymax-y)//sy)
print(triangles)
