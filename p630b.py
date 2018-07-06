import libtkoz as lib

numpoints = 2500

# lines can be uniquely identified in different ways rather than intercepts
# since intercepts may not be inetgers, the need to use fractions makes the
# solution a lot slower
# 18sec with <1GiB RAM (cpython / i5-2540m)

def point_gen():
    S0 = 290797
    while True:
        S1 = (S0*S0) % 50515093 # S_2k-1
        S2 = (S1*S1) % 50515093 # S_2k
        yield ((S1 % 2000) - 1000, (S2 % 2000) - 1000) # (T_2k-1, T_2k)
        S0 = S2

pg = point_gen()
pointlist = list(next(pg) for z in range(numpoints))

# represent lines in form vy = ux + vb (where slope m=u/v)
linetable = dict() # maps (u,v) pairs to unique vb values

for i1,p1 in enumerate(pointlist):
    for i2 in range(i1+1,len(pointlist)):
        p2 = pointlist[i2]
        v = p2[0] - p1[0] # m = u/v = dy / dx
        u = p2[1] - p1[1]
        # u = 0 means horizontal line, v = 0 means vertical line
        g = lib.gcd_euclid(abs(u),abs(v))
        if g != 0: u,v = u//g, v//g # slope in minimum form
        else: continue # points are identical in this case, no line determined
        if v < 0: u, v = -u, -v # denomenator shouldnt be negative
        if u == 0: v = 1 # 0/1 for horizontal lines (for uniqueness)
        if v == 0: u = 1 # 1/0 for vertical lines (for uniqueness)
        vb = v*p1[1] - u*p1[0] # vb = vy - ux (with point p1)
        # insert into hash table
        if (u,v) in linetable: linetable[(u,v)].add(vb)
        else:
            linetable[(u,v)] = set()
            linetable[(u,v)].add(vb)

ML = sum(len(s) for s in linetable.values()) # count distinct lines

# for each line, lines that intersect it are those with different slopes
SL = sum((ML-len(s))*len(s) for s in linetable.values())

print(':',len(linetable),'unique slopes')
print(': M (',numpoints,') =',ML)
print(': S (',numpoints,') =',SL)
print(SL)
