
P = (0,0) # point to test if triangles contain

data = ''
with open('data_files/p102_triangles.txt') as file:
    data = file.read()
# convert to list of triangles, each is a list of 6 integers
data = list(list(int(n) for n in l.split(',')) for l in data.splitlines())

# cross product, for example, if P is inside triangle ABC, then
# AB cross AP and AB cross AC have same sign, cross product of a vector with
# 2 other vectors have same sign if they are on same side (180 degrees)
# repeat this using B and C as pivots

def vec(o,p): # creates vector from 2 points
    return (p[0]-o[0],p[1]-o[1])

def cross(u,v): # cross product
    return u[0]*v[1] - u[1]*v[0]

def same_sign(a,b):
    return (a > 0 and b > 0) or (a < 0 and b < 0)

def twice_area_of(a,b,c): # computes 2x triangle area with cross product
    return abs(cross(vec(a,b),vec(a,c)))

count = 0
for t in data:
    A = (t[0],t[1])
    B = (t[2],t[3])
    C = (t[4],t[5]) # for each pivot point, both vectors on same side
    if same_sign(cross(vec(A,B),vec(A,C)),cross(vec(A,B),vec(A,P))) \
        and same_sign(cross(vec(B,C),vec(B,A)),cross(vec(B,C),vec(B,P))) \
        and same_sign(cross(vec(C,A),vec(C,B)),cross(vec(C,A),vec(C,P))):
        count += 1
print(count)

# area method, if P inside ABC then ABP+BCP+ACP areas = ABC area
# |AB cross AC| = 2*ABC area

count = 0
for t in data:
    A = (t[0],t[1])
    B = (t[2],t[3])
    C = (t[4],t[5])
    if twice_area_of(A,B,C) == twice_area_of(A,B,P) + twice_area_of(A,C,P) \
        + twice_area_of(B,C,P):
        count += 1
print(count)

