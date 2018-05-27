import libtkoz as lib

truncprimesexist = 11
primecachesize = 100000 # maximum number to cache
# cut down from 1 million made it a lot faster
primecache = set(lib.list_primes2(primecachesize))

# test primality with cache
def is_prime(p):
    global primecachesize
    global primecache
    if p < primecachesize: return p in primecache
    else: return lib.prime(p)

# functions to test prime truncatable properties, assumes number itself is prime
def right_trunc(p): # just divide by 10 (integer division)
    p //= 10
    while p != 0:
        if not is_prime(p): return False
        p //= 10
    return True
def left_trunc(p): # use strings for simplicity
    while p >= 10: # at least 2 digits, can truncate another
        p = int(str(p)[1:])
        if not is_prime(p): return False
    return True

# properties of digits in left-right truncatable primes
# if 2 digits: ab, a=2,3,5,7, b=1,3,7,9
# if 3 digits: abc, a=2,3,5,7, b=1,3,7,9, c=3,7 (c has to be prime)
# general case: axx...xxc, a=2,3,5,7, x=1,3,7,9, c=3,7
# a and c must be prime, c and every x are ones digits in some trunc results
# to find them all, begin with 2,3,5,7 then recursively add digits
total = 0

# add new digits, if end in 3 or 7, test left truncatability
# for all 1,3,7,9 endings, if its prime, continue recursively building numbers
# since each num built left-to-right is prime, no need to test right trunc
def recurse(n):
    global total
    n *= 10 # new digit will be in ones place
    if is_prime(n+1): recurse(n+1)
    if is_prime(n+3): # ends in 3 so test for left truncatability
        if left_trunc(n+3):
            total += n+3
            print(':', n+3)
        recurse(n+3)
    if is_prime(n+7): # similarly for ending in 7
        if left_trunc(n+7):
            total += n+7
            print(':', n+7)
        recurse(n+7)
    if is_prime(n+9): recurse(n+9)

# begin recursion with starting digits
recurse(2)
recurse(3)
recurse(5)
recurse(7)
print(total)
