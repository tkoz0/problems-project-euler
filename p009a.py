import libtkoz as lib
import math

sumabc = 1000

# brute force, with restructions on number ranges
# a<b<c --> a<sum/3, b<sum/2
done=False
for a in range(1, sumabc//3 + 1):
    if done: break
    for b in range(a+1, sumabc//2 + 1):
        c = sumabc - b - a
        if a**2 + b**2 == c**2:
            print(':', a, b, c)
            print(a*b*c)
            done=True
            break

# method with generating pythagorean triples
# a=m^2-n^2, b=2mn, c=m^2+n^2, requires m>n
# b must be even, if a,c even then can divide by 2 for primitive triple
# therefore a odd, b even, c odd, a+b+c is even
# (a+b+c)*d = d*(2m^2+2mn) = 2m(m+n)d (d is a multiple of a primitive triple)
# so we get s=2mkd (k=m+n)
# if d is minimum (1), s=2mk --> s/2=mk, since k>m, m cant exceed sqrt(s/2)
# choose m first, it factors s/2, then k which factors s/2/m
# with the restriction m>n we get k<2m
# m,n must be coprime since a,b,c would all have a common factor otherwise

assert sumabc % 2 == 0 # sum has to be even

for m in range(1, int(math.sqrt(sumabc//2))+1):
    if (sumabc//2) % m != 0: continue # m must divide s/2
    for k in range(m+1+(m%2), 2*m, 2): # numbers with opposite parity
        if (sumabc//2//m) % k != 0: continue # k must divide s/2/m
        if lib.gcd_euclid(k, m) != 1: continue # m and k must be coprime
        n = k-m
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        d = sumabc//2//m//k
        print(': primitive triple', a, b, c)
        print(': triple', a*d, b*d, c*d)
        print(a*b*c * d**3) # d cubed since a,b,c each multiplied by d


