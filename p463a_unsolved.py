
Sval = 100#3**37
modulus = 10**9

def f(n): # created from the given
    if n == 1: return 1
    if n == 3: return 3
    m = n % 4
    if m == 1: return 2*f((n+1)//2) - f(n//4)
    if m == 3: return 3*f(n//2) - 2*f(n//4)
    return f(n//2)

def S(n):
    global modulus
    s = 0
    for i in range(1,n+1): s = (s + f(i)) % modulus
    return s

print(S(Sval))
