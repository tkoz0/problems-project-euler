import libtkoz as lib

truncprimesexist = 11
primecachesize = 1000000 # maximum number to cache
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

# brute force, ~0.45 sec (i5-2540m)
# given 11 existing primes of this type, find all by a loop
found = 0
num = 11
total = 0
while found != truncprimesexist:
    if not is_prime(num):
        num += 2
        continue # num must be prime
    if right_trunc(num) and left_trunc(num):
        total += num
        found += 1
        print(':', num)
    num += 2
print(total)

