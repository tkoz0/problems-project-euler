import libtkoz as lib

exceed = 1000000

# similar to last solution, start by picking c, longest side
# then a+b has some amount of solutions based on 2 cases since a can be varied
# as a function of b and vice versa, much faster ~3sec (i5-2540m)

c = 0
intcount = 0
while intcount <= exceed:
    c += 1
    # we have the shortest side is sqrt((a+b)^2+c^2)
    # find values for a+b that dont exceed 2c and make the sqrt integer
    # 2 cases to consider, if a+b<=c then solutions for a+b are (use a+b=z)
    # (1,z-1), (2,z-2), ..., (floor(z/2),ceil(z/2)) --> floor((a+b)/2) solutions
    # if a+b>c then (using a+b=z again) the solutions are
    # substitute cz as ceil(z/2) and fz as floor(z/2)
    # (cz,fz), (cz+1,fz-1), ..., (cz+(c-cz), fz-(c-cz)) --> 1+c-cz solutions
    for apb in range(2,c+1):
        if not lib.is_square(apb*apb+c*c): continue
        intcount += apb//2
    for apb in range(c+1,2*c+1):
        if not lib.is_square(apb*apb+c*c): continue
        intcount += 1 + c - (apb+1)//2 # ceil(apb/2) = floor((apb+1)/2)
print(': M =', c, 'with', intcount, 'solutions')
print(c)
