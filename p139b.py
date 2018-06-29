
perimlim = 10**8

# all primitive pythagorean triples a<b<c must have b-a=1 to satisfy b-a|c
# since any common factor could be divided out
# if b=a+d (d the length of the center) must be 1
# a^2+b^2=c^2 can be solved to (2a/d+1)^2+1=2y^2 using c=yd (integer y)
# this is because d must divide c
# substituting for x^2-2y^2=-1 (x=2a/d+1) gives a diophantine equation
# the perimeter is a+b+c=a+(a+d)+yd=2a+d+yd=xd+yd < limit
# since d=1 for primitive triples, x+y < limit

count = 0
x, y, k = 1, 1, -1 # x^2-2y^2=k
while True:
    m = 0
    absk = abs(k)
    for mm in range(1,1+absk):
        if (x+y*mm) % absk == 0:
            m = mm
            break
    assert m != 0
    assert (x*m+2*y) % absk == 0
    assert (x+y*m) % absk == 0
    assert (m*m-2) % absk == 0
    x, y, k = (x*m+2*y)//absk, (x+y*m)//absk, (m*m-2)//k
    print(': pell',x,y,k)
    assert x*x-2*y*y==k
    if x+y >= perimlim: break
    if k == -1: # solution to equation
        a, b, c = (x-1)//2, (x-1)//2+1, y
        print(': triangle',a,b,c)
        count += (perimlim-1) // (x+y)
print(count)

