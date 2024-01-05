A = 999
B = 1000
S = 10000 # prime cache

# sieve of eratosthenes
sieve = [True]*S
sieve[0] = sieve[1] = False
for i in range(2,S):
    if i*i >= S:
        break
    if not sieve[i]:
        continue
    for j in range(i*i,S,i):
        sieve[j] = False

# check primality using the sieve for small numbers
def prime(n):
    global S,sieve
    if n < 0:
        return False
    elif n < S:
        return sieve[n]
    else:
        if n % 2 == 0:
            return False
        d = 3
        while d*d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

xmax = 40
amax = 1
bmax = 41

# loop b first over positive numbers since b must be prime
for b in range(2,B+1):
    if not prime(b):
        continue
    # 1+a+b must be prime so restrict the range for a
    # use a+b > 0 -> a > -b
    for a in range(max(-A,-b),A+1,1):
        if not prime(1+a+b):
            continue
        f = lambda n : n*n + a*n + b
        x = 2
        while prime(f(x)):
            x += 1
        if x > xmax: # new better quadratic
            print(f'found a={a},b={b} wih {x} primes')
            xmax,amax,bmax = x,a,b
print(amax*bmax)
