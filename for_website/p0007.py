from math import sqrt

def is_prime(p):
    # handle 2 and even numbers first
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    # test possible odd divisors
    for d in range(3,1+int(sqrt(p)),2):
        if p % d == 0:
            return False
    return True

ind = 10001
p = 1
i = 0
while i < ind:
    p += 1
    if is_prime(p):
        i += 1
print(p)

from math import log,ceil

def sieve_size(ind):
    assert ind >= 3
    f = lambda x : x/log(x) - ind
    fp = lambda x : (log(x)-1)/log(x)**2
    x = 3.0
    while True:
        xold = x
        x -= f(xold)/fp(xold)
        if abs(x-xold)/xold < 2**-44:
            break
    return ceil(x)

ind = 10001
siz = sieve_size(ind)

sieve = [True]*(siz+1) # initially mark all as prime
sieve[0] = sieve[1] = False
for i in range(2,siz+1):
    # loop termination and ignore composite numbers
    if i*i > siz:
        break
    if not sieve[i]:
        continue
    # cross off multiples of i starting at i*i
    for j in range(i*i,siz+1,i):
        sieve[j] = False

i = 0
result = 0
for p in range(2,siz+1):
    if sieve[p]:
        i += 1
        if i == ind:
            result = p
            break

assert i == ind
print(result)
