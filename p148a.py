import math

def C(n,k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n-k)

# rows 0 .. rows-1 (first rows rows)
# rows=100 -> 2361
# rows=1000 -> 118335
def brute_force(rows,divisor=7):
    total = 0
    for r in range(rows):
        row_total = 0
        s = ''
        for c in range((r+1)//2):
            n = C(r,c)
            if n % divisor:
                row_total += 1
                s += 'x'
            else:
                s += '.'
        row_total *= 2
        srev = s[::-1]
        if r % 2 == 0:
            if C(r,r//2) % divisor != 0:
                row_total += 1
                s += 'x'
            else:
                s += '.'
        print('%4d'%r,' '*(rows-r)+' '.join(s+srev))
        total += row_total
    print()
    return total

# unfinished, this ideas thought of while writing this
# led to the sierpinski triangle observation
def count_row(row):
    # starting from 1
    # multiply n/1
    # multiply (n-1)/2
    # multiply (n-2)/3 ...
    # multiply by 1/n
    # if n+1=0 (mod 7) then all the 7s line up
    # if n+1=0 (mod 49) then all the 49s line up ...
    # find the first one that gets "ahead" by introducing a 7 that is not
    #   cancelled by the denominator
    p = 0
    nval = row+1
    while nval % 7 == 0:
        nval //= 7
        p += 1
    n = row
    assert (n+1) % (7**p) == 0
    assert (n+1) % (7**(p+1)) != 0
    # every multiple of 7^p lines up
    # consider multiples of 7^(p+1)
    # if n+1=0 mod 7^(p+1) then its 7s get cancelled when denomenator is 7^p
    # when p+1 7s are introduced, need difference with when p+1 7s are cancelled
    # p+1 7s introduced when n,n-1,.. decreases until divisible by 7^(p+1)
    # this is cancelled when 1,2,.. increases until divisible by 7^(p+1)

# depends on unfinished count_row()
def with_row_func(rows):
    return sum(count_row(row) for row in range(rows))

#print(brute_force(100,7))

# each (exponentially) larger scale triangle consists of 28 smaller triangles
# 28 = 1+2+3+4+5+6+7
table = [0]*11
table[0] = 1
table[1] = 28
for n in range(2,11):
    table[n] = 28*table[n-1]
print(':','table (28^n) =',table)

# greedy algorithm
# find how many of a bigger size triangle fit in the remaining rows
# the next smaller scale triangle starts forming on the corner points
# - that is what the multiplier is for, counting these corner points
# continue down to the smallest triangle size (1 point)
rows_left = 10**9 # given number
multiplier = 1 # instances of smaller triangle created
not_div_by_7 = 0 # numbers in the triangle counted
for n in range(10,-1,-1):
    rows_counted = rows_left // (7**n) # rows of size 7^n triangle
    assert 0 <= rows_counted < 7
    triangles = rows_counted * (rows_counted + 1) // 2 # triangles of size 7^n
    not_div_by_7 += multiplier * triangles * table[n]
    multiplier *= rows_counted + 1
    rows_left -= rows_counted * (7**n)
    #print(rows_left)
print(not_div_by_7)
