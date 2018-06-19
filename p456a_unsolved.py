
Cval = 600 # 3sec with pypy, 3min with cpython

def pgen(): # returns coordinates
    x = 1248
    y = 8421
    while True:
        yield (x-16161,y-15051)
        x = (x*1248)%32323
        y = (y*8421)%30103

pg = pgen()
points = list(next(pg) for i in range(Cval))
print(':',points)

# brute force try every possible 3 point set, based on p102

def vec(o,p): # creates vector from 2 points
    return (p[0]-o[0],p[1]-o[1])
def cross(u,v): # cross product
    return u[0]*v[1] - u[1]*v[0]
def same_sign(a,b):
    return (a > 0 and b > 0) or (a < 0 and b < 0)
def twice_area_of(a,b,c): # computes 2x triangle area with cross product
    return abs(cross(vec(a,b),vec(a,c)))

P = (0,0) # contain origin
count = 0
for p1 in range(Cval):
    for p2 in range(p1+1,Cval):
        for p3 in range(p2+1,Cval):
            A = points[p1]
            B = points[p2]
            C = points[p3]
            if twice_area_of(A,B,C) == twice_area_of(A,B,P) + twice_area_of(A,C,P) \
                + twice_area_of(B,C,P):
                count += 1
print(count)
