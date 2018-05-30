import math
from encodings.punycode import digits

def prime(n): # requires sqrt(n) time
    if n < 2: return False;
    if n == 2 or n == 3: return True;
    if n % 2 == 0: return False;
    for d in range(3, int(math.sqrt(n))+1, 2):
        if n % d == 0:
            return False
    return True

def palindrome(x):
    return str(x) == str(x)[::-1]

def palindrome_base2(x):
    xx = '{0:b}'.format(x)
    return xx == xx[::-1]

# makes a list of primes from 2 to n (inclusive)
# slow, tests every prime
def list_primes1(n): # takes n*sqrt(n) time
    primes = []
    for p in range(2, n+1):
        if prime(p):
            primes.append(p)
    return primes

# uses a sieve, based on solution from p010
def list_primes2(n):
    if n < 2: return []
    primes = [2]
    sievesize = (n+1) // 2 # last index has largest odd, index i means 2i+1
    sieve = [True] * sievesize
    # loop for odds up to square root
    for nn in range(3, int(math.sqrt(n))+1, 2):
        i = nn//2 + nn # initial cross off index, represents 3*(2*i+1)
        while i < sievesize:
            sieve[i] = False
            i += nn # increment in n which increases number by 2n (cross off odds)
    for i in range(1, sievesize):
        if sieve[i]: primes.append(2*i+1)
    return primes

def gcd_euclid(m, n):
    assert m >= n > 0
    while m % n != 0:
        m, n = n, m % n
    return n

def is_square(n):
    s = int(math.sqrt(n))
    return s**2 == n

# slow loop for counting divisors, finds each factor
def divisors1(n): # requires sqrt(n) time
    assert n > 0
    count = 2 # 1 and n
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            count += 2
    if is_square(n): # its square was root counted twice
        count -= 1
    return count

# count divisors by factoring
def divisors2(n):
    assert n > 0
    total = 1 # will be multiplied by counting prime factors
    while n % 2 == 0: # factors of 2
        total += 1
        n //= 2
    d = 3 # loop over possible odd factors
    while d * d <= n: # d < square root, n will get smaller so calculate this
        if n % d != 0:
            d += 2
            continue
        count = 1
        n //= d
        while n % d == 0:
            n //= d
            count += 1
        total *= count + 1
        d += 2
    if n == 1: return total # all factors divided out
    else: return total * 2 # remaining value is a prime factor

# produce list of factors
def prime_factorization(n):
    result = []
    while n % 2 == 0:
        n //= 2
        result.append(2)
    d = 3
    while d * d <= n:
        while n % d == 0:
            n //= d
            result.append(d)
        d += 2
    if n != 1: result.append(n) # last remaining prime factor
    return result

def binom_coeff(n, k): # computes binomial coefficient
    assert n >= k >= 0
    num = n # for n, n-1, ..., 1
    result = 1 # this works because n consecutive integers is divisible by n!
    for i in range(min(k, n-k)):
        result *= num
        num -= 1
        result //= i+1
    return result

# based on divisors1 function, sums all divisors
def sum_divisors1(n): # requires sqrt(n) time
    assert n > 0
    if n == 1: return 1
    count = 1+n # 1 and n
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            count += d + n//d
    if is_square(n): # its square was root counted twice
        count -= int(math.sqrt(n))
    return count

# sum divisors with formula
# if n = p^a * q^b * ... then the divisor sum is
# (p^0+...+p^a)*(q^0+...+q^b)*... = product of (p^a-1)/(p-1) for primes p
def sum_divisors2(n):
    assert n > 0
    total = 1 # will be multiplied by counting prime factors
    factors = 0
    while n % 2 == 0: # factors of 2
        factors += 1
        n //= 2
    if factors != 0:
        total *= (2**(factors+1) - 1) # /(2-1) is just 1
    d = 3 # loop over possible odd factors
    while d * d <= n: # d < square root, n will get smaller so calculate this
        if n % d != 0:
            d += 2
            continue
        factors = 1
        n //= d
        while n % d == 0:
            n //= d
            factors += 1
        total *= (d**(factors+1) - 1) // (d-1)
        d += 2
    if n == 1: return total # all factors divided out
    else: return total * (n+1) # remaining value is a prime factor

def digits_in(n):
    if n == 0: return 1
    if n < 0: n = -n
    return int(math.log10(n)) + 1

def is_triangle(x):
    n = int(math.sqrt(2*x))
    return n**2 + n == 2*x

def is_pentagonal(x):
    n = 1 + math.floor(math.sqrt(2*x/3))
    return 2*x == 3*(n**2) - n

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
    #
    assert palindrome(2) and palindrome(7) and palindrome(33)
    assert not palindrome(23) and not palindrome(37)
    assert palindrome(15751) and palindrome(843348)
    assert not palindrome(15752) and not palindrome(832348)
    #
    assert palindrome_base2(1)
    assert palindrome_base2(3)
    assert palindrome_base2(73)
    assert palindrome_base2(2**9+1 + 2**6+8)
    assert palindrome_base2(2**8 + 2**4 + 2**0)
    #
    assert list_primes1(1) == [] and list_primes1(2) == [2]
    assert list_primes2(1) == [] and list_primes2(2) == [2]
    assert list_primes1(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert list_primes2(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert len(list_primes1(104742)) == 10000
    assert len(list_primes1(104743)) == 10001
    assert len(list_primes2(104742)) == 10000
    assert len(list_primes2(104743)) == 10001
    #
    assert gcd_euclid(2, 1) == 1
    assert gcd_euclid(73, 73) == 73
    assert gcd_euclid(2250, 1050) == 150
    assert gcd_euclid(72, 56) == 8 and gcd_euclid(96, 72) == 24
    #
    assert is_square(0) and is_square(1)
    assert is_square(64) and is_square(289)
    assert not is_square(65) and not is_square(288)
    assert is_square(4294967296) and not is_square(4294967295)
    #
    for p in list_primes1(200):
        assert divisors1(p) == 2
        assert sum_divisors1(p) == p + 1
    assert divisors1(72) == 12
    assert divisors1(9) == 3 and divisors1(289) == 3
    assert divisors1(64) == 7 and divisors1(4294967296) == 33
    assert divisors1(2*2*5*7*11*11*11) == 3 * 2 * 2 * 4
    assert divisors1(1) == 1
    #
    for p in list_primes1(200):
        assert divisors2(p) == 2
        assert sum_divisors2(p) == p + 1
    assert divisors2(72) == 12
    assert divisors2(9) == 3 and divisors2(289) == 3
    assert divisors2(64) == 7 and divisors2(4294967296) == 33
    assert divisors2(2*2*5*7*11*11*11) == 3 * 2 * 2 * 4
    assert divisors2(1) == 1
    #
    for i in range(1, 100):
        if i == 1: assert prime_factorization(i) == []
        if prime(i): assert len(prime_factorization(i)) == 1
        assert prime_factorization(15) == [3, 5]
        assert prime_factorization(77) == [7, 11]
        assert prime_factorization(72) == [2, 2, 2, 3, 3]
        assert prime_factorization(64) == [2] * 6
        assert prime_factorization(81) == [3] * 4
        assert prime_factorization(210) == [2, 3, 5, 7]
    #
    assert sum_divisors1(72) == (1+2+4+8)*(1+3+9) == sum_divisors2(72)
    assert sum_divisors1(9) == 1+3+9 == sum_divisors2(9)
    assert sum_divisors1(729) == 1+3+9+27+81+243+729 == sum_divisors2(729)
    assert sum_divisors1(289) == 1+17+289 == sum_divisors2(289)
    assert sum_divisors1(64) == 127 == sum_divisors2(64)
    assert sum_divisors1(2*2*5*7*11**3) == (1+2+4)*(1+5)*(1+7)*(1+11+121+1331)
    assert sum_divisors2(2*2*5*7*11**3) == (1+2+4)*(1+5)*(1+7)*(1+11+121+1331)
    assert sum_divisors1(1) == 1 and sum_divisors2(1) == 1
    #
    assert digits_in(0) == 1
    for i in range(1, 10): assert digits_in(i) == 1
    for i in range(10, 100): assert digits_in(i) == 2
    for i in range(100, 1000): assert digits_in(i) == 3
    assert digits_in(-6) == digits_in(6)
    assert digits_in(-73) == digits_in(73)
    #
    for i in range(100):
        assert is_triangle(i) == (i in [0,1,3,6,10,15,21,28,36,45,55,66,78,91])
    #
    for i in range(150):
        assert is_pentagonal(i) == (i in [1,5,12,22,35,51,70,92,117,145])
    #
    pascalsize = 50
    pascal = [] # generate pascal triangle (square)
    for i in range(pascalsize): pascal.append([0]*pascalsize)
    pascal[0] = [1]*pascalsize
    for i in range(pascalsize): pascal[i][0] = 1
    for i in range(1,pascalsize):
        for j in range(1,pascalsize):
            pascal[i][j] = pascal[i-1][j] + pascal[i][j-1]
    for i in range(pascalsize):
        for j in range(pascalsize):
            assert binom_coeff(i+j, i) == pascal[i][j]
            assert binom_coeff(i+j, j) == pascal[i][j]
    #
    print('passed all tests')

