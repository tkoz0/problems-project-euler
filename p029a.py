import math

# limits for a^b
amax = 100
bmax = 100

# use a set and insert all to it, count unique values by set size
values = set()
for a in range(2, amax+1):
    for b in range(2, bmax+1):
        values.add(math.pow(a, b))
print(len(values))

# count those which arent duplicates based on prime factorization
# slower because many more operations per possibility are needed
# possible duplicates of b^e are (b^2)^(e/2), (b^3)^(e/3), ...
count = 0

# return a tuple (b,e) such that b^e=n, b is the smallest b>=2 integer
def with_prime_base(n):
    for b in range(2, int(math.sqrt(n))+1):
        e = 1
        num = b
        while num < n:
            num *= b
            e += 1
        if num == n: return (b, e)
    return (n, 1)

for a in range(2, amax+1):
    aexp = with_prime_base(a)
    for b in range(2, bmax+1):
        abexp = (aexp[0], aexp[1] * b) # a = ab^ae --> a^b = ab^(ae*b)
        base = abexp[0]
        exp = 1 # exponent on base, divide from abexp[1] (if divisible)
        # define strict ordering, must have larger base so dupes only count once
        while base <= a:
            base *= abexp[0]
            exp += 1
        founddupe = False # dupe found with larger base
        while base <= amax:
            if abexp[1] % exp == 0 and abexp[1] / exp >= 2: founddupe = True
            base *= abexp[0]
            exp += 1
        if not founddupe:
            count += 1

print(': counted', (amax-1)*(bmax-1) - count, 'dupes')
print(count)

