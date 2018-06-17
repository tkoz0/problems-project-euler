import libtkoz as lib

Lval = 50000000
modulus = 10**9+7

def C(n):
    assert n > 0
    pin = len(lib.list_primes2(n))
    return 6*(5**(n-pin-1))*sum(5**(pin-i)*lib.binom_coeff(n-1,i) for i in range(pin+1))

def S(L): return sum(C(n) for n in range(1,L+1))

print(S(Lval)%modulus)
