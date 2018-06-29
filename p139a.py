import libtkoz as lib

perimlim = 10**8

# for some triangle a,b,c we must have b-a divides c to tile a c^2 area
# generate primitivte pythagorean triples and count integer multiples of them
# within perimeter constraint

# generate triples with a,b,c=m^2-n^2,2mn,m^2+n^2
# constraints m>n, gcd(m,n)=1, m%2 != n%2
# using a<lim/3, m can range from 2 until m^2-(m-1)^2 = 2m-1 >= lim/3
# so m can range from 2 to ((lim/3)+1)/2

# takes ~15sec (pypy / i5-2540m)

count = 0

for m in range(2,1+int((perimlim/3+1)/2)):
    m2 = m*m
    n = m-1
    a = m2 - n*n
    while n > 0 and a <= perimlim//3:
        if lib.gcd_euclid(m,n) != 1:
            n -= 2
            a = m2 - n*n
            continue
        # primitive triple
        b = 2*m*n
        c = m2 + n*n
        if c % abs(b-a) != 0:
            n -= 2
            a = m2 - n*n
            continue
        print(': can tile',a,b,c,'and',(perimlim)//(a+b+c),'integer multiples')
        count += (perimlim-1) // (a+b+c) # count all integer multiples
        n -= 2 # for next iteration
        a = m2 - n*n
print(count)
