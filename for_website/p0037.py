# primality testing with caching
primecache = {0:False,1:False,2:True,3:True}
def prime(n):
    global primecache
    if n in primecache:
        return primecache[n]
    if n % 2 == 0:
        return False
    d = 3
    while d*d <= n:
        if n % d == 0:
            primecache[n] = False
            return False
        d += 2
    primecache[n] = True
    return True

def ltrunc(n,l):
    # test if l digit number n is left truncatable prime
    l -= 1
    while n >= 10:
        if not prime(n):
            return False
        # truncate a digit
        d = n//10**l
        n -= d*10**l
        l -= 1
    return prime(n)

lrtrunc = set()

def recur(n,l):
    # generate right truncatable primes
    global lrtrunc
    for d in [1,3,7,9]:
        n2 = 10*n + d
        if not prime(n2):
            continue
        if ltrunc(n2,l+1):
            lrtrunc.add(n2)
        recur(n2,l+1)

# begin recursion with single digit primes
recur(2,1)
recur(3,1)
recur(5,1)
recur(7,1)

print(sorted(lrtrunc))
print(sum(lrtrunc))
