import math

def prime(n): # requires sqrt(n) time
    if n < 2: return False;
    if n == 2 or n == 3: return True;
    if n % 2 == 0: return False;
    for d in range(3, int(math.sqrt(n))+1, 2):
        if n % d == 0:
            return False
    return True

def miller_rabin_verified(n): # miller rabin test
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False # n is now odd integer > 1
    d = n-1
    s = 0
    while d % 2 == 0: # n-1 = 2^s * d
        s += 1
        d //= 2
    # select set of a values to test based on verified results (wikipedia)
    A = []
    if n < 2047: A = [2]
    elif n < 1373653: A = [2,3]
    elif n < 9080191: A = [31,73]
    elif n < 25326001: A = [2,3,5]
    elif n < 3215031751: A = [2,3,5,7]
    elif n < 4759123141: A = [2,7,61]
    elif n < 1122004669633: A = [2,13,23,1662803]
    elif n < 2152302898747: A = [2,3,5,7,11]
    elif n < 3474749660383: A = [2,3,5,7,11,13]
    elif n < 341550071728321: A = [2,3,5,7,11,13,17]
    elif n < 3825123056546413051: A = [2,3,5,7,11,13,17,19,23]
#    elif n < 18446744073709551616: A = [2,3,5,7,11,13,17,19,23,29,31,37]
    elif n < 318665857834031151167461: A = [2,3,5,7,11,13,17,19,23,29,31,37]
    elif n < 3317044064679887385961981: A = [2,3,5,7,11,13,17,19,23,29,31,37,41]
    else: assert 0,'too large for verified miller rabin' # probably wont happen
    for a in A: # perform test with smallest required witness set
        if pow(a,d,n) != 1: # for (2^r)*d, use e=d, multiply by 2 each time
            e = d
            neqneg1forall = True
            for r in range(s):
                if pow(a,e,n) == n-1: # a**e mod n == -1
                    neqneg1forall = False
                    break
                e *= 2
            if neqneg1forall: return False # composite
    return True # prime

def palindrome(x): return str(x) == str(x)[::-1]

def sum_digits(x):
    s = 0
    while x != 0:
        x, d = divmod(x,10)
        s += d
    return s

def digital_root(x):
    assert x > 0
    return 1 + (x-1)%9

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
# optionally return the sieve itself for other uses
# also added return_set, to get a set instead of list
def list_primes2(n,return_sieve=False,return_set=False):
    if n < 2: return []
    primes = [2]
    sievesize = (n+1) // 2 # last index has largest odd, index i means 2i+1
    sieve = [True] * sievesize
    # loop for odds up to square root
    for nn in range(3, int(math.sqrt(n))+1, 2):
        i = nn//2 + nn # initial cross off index, represents 3*(2*i+1)
        while i < sievesize:
            sieve[i] = False
            i += nn # increment in n, increases number by 2n (cross off odds)
    if return_sieve: return sieve
    if return_set:
        primes = set(primes) # make the 2 into a set
        for i in range(1, sievesize):
            if sieve[i]: primes.add(2*i+1)
    else:
        for i in range(1, sievesize):
            if sieve[i]: primes.append(2*i+1)
    return primes

def gcd_euclid(m, n):
    assert m > 0 and n > 0
    if n > m: m, n = n, m # fix order
    while m % n != 0:
        m, n = n, m % n
    return n

def is_square(n): return (int(math.sqrt(n)))**2 == n

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
    assert n > 0
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

# compute euler totient function, how many 1<=a<n are coprime to n
def totient(n):
    assert n > 0
    t = n # totient result
    if n % 2 == 0: # unique prime 2
        n //= 2
        t //= 2 # totient *= (2-1)/2, divide out remaining twos
        while n % 2 == 0: n //= 2
    d = 3 # odd divisors
    while d*d <= n:
        if n % d == 0: # another unique prime
            n //= d
            t = t*(d-1)//d
            while n % d == 0: n //= d # divide out this factor entirely
        d += 2
    if n != 1: t = t*(n-1)//n # last prime factor
    return t

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

# next lexicographic permutation in increasing order
# true if it advances the list, false if list is already max
def lexico_next(l):
    i1 = len(l)-1
    while i1 != 0 and l[i1-1] >= l[i1]: i1 -= 1 # find break in noninc order
    i1 -= 1 # index of digit to increase
    if i1 == -1: return False # already max
    i2 = len(l)-1
    while l[i2] <= l[i1]: i2 -= 1 # find smallest larger value
    l[i1], l[i2] = l[i2], l[i1] # swap, i1+1 to end are now in dec order
    i1 += 1
    i2 = len(l)-1
    while i1 < i2: # sort by swapping
        l[i1], l[i2] = l[i2], l[i1]
        i1 += 1
        i2 -= 1
    return True

# similar to lexico_next, reverse order, same code with some signs changed
def lexico_prev(l):
    i1 = len(l)-1
    while i1 != 0 and l[i1-1] <= l[i1]: i1 -= 1
    i1 -= 1
    if i1 == -1: return False
    i2 = len(l)-1
    while l[i2] >= l[i1]: i2 -= 1
    l[i1], l[i2] = l[i2], l[i1]
    i1 += 1
    i2 = len(l)-1
    while i1 < i2:
        l[i1], l[i2] = l[i2], l[i1]
        i1 += 1
        i2 -= 1
    return True

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
    pl = set(list_primes2(100000))
    for p in pl: assert miller_rabin_verified(p)
    for p in range(10000,30000): assert (p in pl) == miller_rabin_verified(p)
    for p in range(10**9,10**9+10000):
        assert prime(p) == miller_rabin_verified(p)
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
    for i in range(10): assert sum_digits(i) == i
    for i in range(11,100,11): assert sum_digits(i) == (i//11)*2
    assert sum_digits(123456789) == 45
    #
    assert digital_root(467) == 8
    assert digital_root(9999999999999994) == 4 # 139 --> 13 --> 4
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
    for i in range(1,100):
        for j in range(1,100):
            assert gcd_euclid(i,j) == gcd_euclid(j,i)
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
    for i in range(2,100): # primes
        assert prime(i) == (totient(i) == i-1) # totient of primes is n-1
    for i in range(2,100): # semi primes
        if not prime(i): continue
        for j in range(2,100):
            if not prime(j): continue
            if i == j: assert totient(i**2) == i*(i-1)
            else: assert totient(i*j) == (i-1)*(j-1)
    assert totient(216) == 72 and totient(273) == 144 and totient(430) == 168
    assert totient(2*2*3*3*5*7) == (2*2*3*3*5*7)*1//2*2//3*4//5*6//7
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
    lstates = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    l = [1,2,3]
    for i in range(1,6):
        assert lexico_next(l)
        assert l == lstates[i]
    assert not lexico_next(l)
    lstates = lstates[::-1]
    for i in range(1,6):
        assert lexico_prev(l)
        assert l == lstates[i]
    assert not lexico_prev(l)
    l = [7,2,6,5,4,3,1] # --> [7,3,1,2,4,5,6]
    l2 = [7,2,6,5,4,3,1]
    l3 = [7,3,1,2,4,5,6]
    assert lexico_next(l)
    assert l == l3
    assert lexico_prev(l)
    assert l == l2
    #
    print('passed all tests')

