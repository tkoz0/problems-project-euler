import libtkoz as lib

seq = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
exceed = 10**15

# D: n%3==0 --> n//3, inverse in n --> 3n
# U: n%3==1 --> (4n+2)//3, inverse is n --> (3n-2)//4, require n%4==2
# d: n%2==2 --> (2n-1)//3, inverse is n --> (3n+1)//2, require n%2==1

# starting with a = (m*a+b)/d, compute what a becomes after the 30 steps
m, b, d = 1, 0, 1
for s in seq:
    if s == 'D': d *= 3
    # (m*a+b)//d --> (4(m*a+b)//d + 2)//3 --> (4*m*a+4*b+2*d)//(3*d)
    elif s == 'U': m, b, d = 4*m, 4*b + 2*d, 3*d
    # (m*a+b)//d --> (2*(m*a+b)//d - 1)//3 --> (2*m*a+2*b-d)//(3*d)
    elif s == 'd': m, b, d = 2*m, 2*b - d, 3*d
    else: assert 0
print(': this must be integer (',m,'* a +',b,') //',d)
# must find smallest a such that (a*m+b)%d == 0
# from there, add any multiple of d/gcd(m,d)=d and the fraction is still integer
# gcd(m,d)=0 since m only has factors of 2 and d only has factors of 3
# modify b so equation becomes a*m==b (mod d)
b = (-b) % d
# solve a*m == b (mod d)
# begin with bezout identity gcd(m,d)=1=xm+yd
# we get xm==1 (mod d) --> bxm==b (mod d) --> am = bxm --> a = bx
geresult = lib.gcd_euclid_ext(m,d)
assert geresult[0] == 1 # gcd
assert geresult[1]*m + geresult[2]*d == 1 # bezout identity
a = b*geresult[1]
assert (a*m) % d == b
print(': found a*m==b (mod d):',a,'*',m,'==',b,'( mod',d,')')
# now to get minimum a, (a-zd)m = am - zdm == b (mod d)
# largest possible choice for z (above equation) would cause a --> a%d
a %= d
print(': minimum a is',a)
# now just add multiples of d to a so it exceeds the required value
a += (1+(exceed-a)//d)*d
print(a)
