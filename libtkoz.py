import math

def prime(n):
    if n < 2: return False;
    if n == 2 or n == 3: return True;
    if n % 2 == 0: return False;
    for d in range(3, int(math.sqrt(n))+1, 2):
        if n % d == 0:
            return False
    return True

def palindrome(x):
    return str(x) == str(x)[::-1]

# makes a list of primes from 2 to n (inclusive)
# slow, tests every prime
def list_primes(n):
    primes = []
    for p in range(2, n+1):
        if prime(p):
            primes.append(p)
    return primes

def gcd_euclid(m, n):
    assert m > n
    while m % n != 0:
        m, n = n, m % n
    return n

