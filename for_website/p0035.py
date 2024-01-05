L = 1000000

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

# start with single digit circular primes
circulars = set([2,3,5,7])

def recur(n,l):
    global circulars
    # n with l digits, add one of the 4 digits to it
    for d in [1,3,7,9]:
        n2 = 10*n + d
        if n2 >= L:
            break
        # test if it is a circular prime
        if n2 not in circulars:
            iscircular = True
            # go through rotations to test primality
            for _ in range(l+1):
                if not prime(n2):
                    iscircular = False
                    break
                n2 = (n2%10)*10**l + (n2//10)
            # go through rotations and add them to set
            if iscircular:
                for _ in range(l+1):
                    circulars.add(n2)
                    n2 = (n2%10)*10**l + (n2//10)
        recur(n2,l+1)

# initialize recursion from single digit numbers
recur(1,1)
recur(3,1)
recur(7,1)
recur(9,1)

print(sorted(circulars))
print(len(circulars))
