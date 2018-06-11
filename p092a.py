import math

numlim = 10000000

def digitsqsum(n):
    s = 0
    while n != 0:
        s += (n%10)**2
        n //= 10
    return s

def end89(n): # repeat sequence until either 1 or 89
    while n != 1 and n != 89: n = digitsqsum(n)
    return n == 89

# brute force with cache, ~30sec (i5-2540m)
# numbers go up to 7 digits so 7*9^2 is the highest the digit square sum can be
maxdigits = 1+math.floor(math.log10(numlim-1))
cachesize = maxdigits * (9**2)
# generate cache for 1,2,...,7*9^2
cache = [False] + list(end89(n) for n in range(1,cachesize+1))
count = sum(1 for v in cache if v) # how many end in 89 in cache
# try all remaining numbers
for n in range(cachesize+1,numlim):
    if cache[digitsqsum(n)]: count += 1
print(count)
