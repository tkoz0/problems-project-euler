import libtkoz as lib
import math

maxperim = 1000

# a^2+b^2=c^2, a+b+c=p
# a^2+b^2=(p-a-b)^2=p^2+a^2+b^2-2pa-2pb+2ab --> p^2-2pa-2pb+2ab=0
# rearrange to 2b(p-a)=p(p-2a), everything is an integer
# b = (p(p-2a)) / (2(p-a))
# a,b,c,p are integers so p must be even (numerator even, /2 in denomenator)
# if p is constant, b decreases as a increases (show by derivative)
# derivative is (-p^2)/(2(p-a)^2), top<0 and bottom>0 in problem parameters
mostsolutions = 0
bestperim = 0
for p in range(2, maxperim+1, 2):
    solutions = 0
    # this loop will count twice as many since it allows a,b and b,a pairs
    # p-a>0 in problem, must ensure p-2a>0 so b>0
    for a in range(1, p//2): # b is integer, solution found
        if (p*(p-2*a)) % (2*(p-a)) == 0: solutions += 1
    if solutions > mostsolutions:
        mostsolutions, bestperim = solutions, p
        print(':', solutions, 'solutions for perimeter', p)
print(bestperim)

# method with pythagorean triples, very similar to problem 9
mostsolutions = 0
bestperim = 0
for p in range(2, maxperim+1, 2):
    solutions = 0
    for m in range(1, int(math.sqrt(p//2))+1):
        if (p//2) % m != 0: continue # m must divide s/2
        for k in range(m+1+(m%2), 2*m, 2): # numbers with opposite parity
            if (p//2//m) % k != 0: continue # k must divide s/2/m
            if lib.gcd_euclid(k, m) != 1: continue # m and k must be coprime
            solutions += 1 # conditions satisfied for a triple to exist
            # no need to calculate the triple itself
    if solutions > mostsolutions:
        mostsolutions, bestperim = solutions, p
        print(':', solutions, 'solutions for perimiter', p)
print(bestperim)

