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
def list_primes1(n):
    primes = []
    for p in range(2, n+1):
        if prime(p):
            primes.append(p)
    return primes

def gcd_euclid(m, n):
    assert m >= n > 0
    while m % n != 0:
        m, n = n, m % n
    return n

def is_square(n):
    assert n >= 0
    s = int(math.sqrt(n))
    return s**2 == n

# some tests for these functions to check that they work properly
if __name__ == '__main__':
    assert not prime(1) and prime(2) and prime(3)
    assert not prime(4) and prime(5) and not prime(6) and prime(7)
    assert not prime(8) and not prime(9) and not prime(10)
    assert prime(11) and prime(13) and prime(17) and prime(19)
    assert prime(163)
    assert not prime(289) and not prime(561)
    assert not prime(1000013)
    assert prime(1000000007)
    assert palindrome(2) and palindrome(7) and palindrome(33)
    assert not palindrome(23) and not palindrome(37)
    assert palindrome(15751) and palindrome(843348)
    assert not palindrome(15752) and not palindrome(832348)
    assert list_primes1(1) == [] and list_primes1(2) == [2]
    assert list_primes1(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert len(list_primes1(104742)) == 10000
    assert gcd_euclid(2, 1) == 1
    assert gcd_euclid(73, 73) == 73
    assert gcd_euclid(2250, 1050) == 150
    assert gcd_euclid(72, 56) == 8 and gcd_euclid(96, 72) == 24
    assert is_square(0) and is_square(1)
    assert is_square(64) and is_square(289)
    assert not is_square(65) and not is_square(288)
    assert is_square(4294967296) and not is_square(4294967295)
    print('passed all tests')

