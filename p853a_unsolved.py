import sys
import libtkoz

# pisano periods length 120 = 2*2*2*3*5
# factors 1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120

# known (m,n)=1 -> pi(mn)=pi(m)*pi(n) (multiplicative function)

# pi(p^k) divides p^(k-1)*pi(p) for primes p
# unknown if equal for all primes p, k > 1 (see wall-sun-sun prime)

def pisano(n):
    a,b = 0,1
    i = 0
    while True:
        a,b = b%n,(a+b)%n
        i += 1
        if (a,b) == (0,1):
            return i

print(pisano(int(sys.argv[1])))

#for p in range(2,200000):
#    if libtkoz.prime(p) and pisano(p) < 120:
#        print(p)
