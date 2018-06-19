import math

axisX = 5.0 # a in ellipse equation
axisY = 10.0 # b in ellipse equation
opening = 0.01 # width on x axis
start = (0.0, 10.1)
initial = (1.4, -9.6)

def solve_quadratic(a,b,c): # solve quadratic equation
    D = b**2 - 4.0*a*c
    if D < 0.0: return False # no real solutions
    D = math.sqrt(D)
    a *= 2.0 # for denomenator whet calculating results
    return ((-b-D)/a,(-b+D)/a)

# by differentation, slope is dy/dx = (-xb^2)/(ya^2), lambda takes a point tuple
slope = lambda p: -p[0]*(axisY**2) / (p[1]*(axisX**2))
vecmag = lambda p: math.sqrt(p[0]**2 + p[1]**2) # vector magnitude
vecdot = lambda a,b: a[0]*b[0] + a[1]*b[1] # vector dot product
floateq = lambda a,b: math.fabs(a-b) < 2**(-32) # 2 floats approximately equal

hits = 1 # keep track of hits and 2 positions to calculate next direction
prevpos = start
curpos = initial
print(': initial',prevpos,'-->',curpos)
while True: # iterate until leaving through opening again
    dydx = slope(curpos)
    n = (dydx,-1.0) # 1,dydx --> dydx,-1, normal vector to ellipse
    nmag = vecmag(n)
    n = (n[0]/nmag, n[1]/nmag) # unit normal vector
    # if we reflect vector d on the curve, (use n for unit normal vector)
    # projection d onto n is (d dot n)n
    # r (the reflection) will have a component -(d dot n)n
    # its component along the normal vector will be negated but its component
    # perpendicular to the normal vector will stay the same
    # so we subtract double the projection to negate a component of d to get r
    # r = d - 2(d dot n)n
    # here, compute the vector to reflect, vector from prev to current position
    curvec = (curpos[0]-prevpos[0], curpos[1]-prevpos[1])
    dotprod = vecdot(curvec,n) # subtract twice this times n components
    r = (curvec[0]-2*dotprod*n[0], curvec[1]-2*dotprod*n[1])
    # slope of reflection could be infinite, but that requires that the previous
    # vector also had an infinite slope so this should never happen
    # now we must find where this vector intersects the ellipse which will be
    # 2 points, so we pick the one that isnt the original as the next hit point
    # using components for r to form a line:
    # x = curx + t*rx, y = cury + t*ry
    # solving gives the line y = cury + x*ry/rx - curx*ry/rx
    # we get y=mx+c with m=ry/rx and c=cury-curx*ry/rx
    m = r[1]/r[0]
    c = curpos[1] - curpos[0]*m # c so not confusing with ellipse a and b
    # now substitute this to solve the ellipse equation (work not shown here)
    qa = axisY**2 + (m**2)*(axisX**2) # quadratic equation coefficients
    qb = 2.0*m*c*(axisX**2)
    qc = (axisX**2)*(c**2 - axisY**2)
    # solve this quadratic equation for x values of solution points
    # there should always be a solution since the reflection goes inside the
    # ellipse so it should intersect the ellipse at 2 points
    qsol = solve_quadratic(qa,qb,qc)
    if qsol is False:
        print(': quadratic solution failed')
        break
    sol1 = (qsol[0], m*qsol[0]+c) # 2 intersection points
    sol2 = (qsol[1], m*qsol[1]+c)
    # pick the one that is different from curpos
    prevpos = curpos
    if not floateq(sol1[0],prevpos[0]) and not floateq(sol1[1],prevpos[1]):
        curpos = sol1 # sol1 is a different point
    else: curpos = sol2
    print(': step',hits+1,prevpos,'-->',curpos,[4.0*curpos[0]**2+curpos[1]**2])
    # if hitting the opening (above x axis), end
    if curpos[1] > 0.0 and math.fabs(curpos[0]) <= opening: break
    hits += 1
print(hits)
