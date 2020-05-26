from fractions import Fraction

def rng(count): # random number sequence
    s = 290797
    for _ in range(count):
        s = (s*s) % 50515093
        yield s

def seg_gen(count): # generates segments as (x1,y1,x2,y2)
    rand = rng(count*4)
    s = 290797
    for _ in range(count):
        yield tuple(next(rand) % 500 for _ in range(4))

def gcd(a,b):
    if a < b: a,b = b,a
    while b: a,b = b,a%b
    return a

def slope(line):
    dx = line[2]-line[0]
    dy = line[3]-line[1]
    if dx == 0: return (0, 1 if dy != 0 else 0) # vertical line
    if dx < 0: dx,dy = -dx,-dy # keep x >= 0
    g = gcd(dx,abs(dy))
    return (dx//g,dy//g) # use minimum integers necessary

def between(n,lo,hi):
    if lo > hi: lo,hi = hi,lo
    return lo <= n <= hi

# is point bounded by the closed rectangle determined by the line
# (checking if x,y is on the segment when known to be on the infinite line)
def box_bounded(x,y,line):
    return between(x,line[0],line[2]) and between(y,line[1],line[3])

def is_endpoint(x,y,line):
    return (x,y) == (line[0],line[1]) or (x,y) == (line[2],line[3])

def true_intersect(line1,line2):
    s1,s2 = slope(line1),slope(line2) # slope vectors
    if s1 == s2: return None # cannot have true intersection point
    if s1 == (0,0) or s2 == (0,0): return None # either is a single point
    # write lines in ax*by=c form
    a1,b1,c1 = s1[1],-s1[0],s1[1]*line1[0]-s1[0]*line1[1]
    a2,b2,c2 = s2[1],-s2[0],s2[1]*line2[0]-s2[0]*line2[1]
    # solve linear system to get x,y
    assert a1*b2 != b1*a2 # matrix is invertible
    # [x] = [a1 b1]-1 [c1]
    # [y] = [a2 b2]   [c2]
    frac = Fraction(1,a1*b2-b1*a2)
    x = frac*(b2*c1-b1*c2)
    y = frac*(-a2*c1+a1*c2)
    # check that (x,y) is interier to both lines
    # here, it is known to be the intersection of both infinite lines
    if not (box_bounded(x,y,line1) and box_bounded(x,y,line2)):
        return None # not bounded by both closed rectangles
    if is_endpoint(x,y,line1) or is_endpoint(x,y,line2):
        return None # cannot be an endpoint
    return (x,y)

segments = list(seg_gen(5000))

true_intersections = set() # set of (x,y)

for i in range(len(segments)):
    for j in range(i+1,len(segments)):
        point = true_intersect(segments[i],segments[j])
        if point is not None: true_intersections.add(point)

print(len(true_intersections))
# runs in 12 minutes
