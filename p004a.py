digits = 3
maxnum = 10**digits-1

def palindrome(x):
    return str(x) == str(x)[::-1]

def make_palindrome(x):
    return int(str(x) + str(x)[::-1])

largest = 0

# brute force solution
for a in range(maxnum+1):
    for b in range(a+1, maxnum+1):
        ab = a * b
        if ab > largest and palindrome(ab):
            largest = ab
#            print(': larger', a, '*', b, '=', ab)
print(largest)

largest = 0
# loop starting at largest
a = maxnum
while a > largest // (maxnum+1):
    b = maxnum
    while b > largest // a: # so a*b > largest
        ab = a * b
        if palindrome(ab):
            largest = ab
            print(': larger', a, '*', b, '=', ab)
        b -= 1
    a -= 1
print(largest)

# try creating palindromes
found = False
# loop in range of digits length numbers
for p_ in range(maxnum, maxnum//10, -1):
    if found: break # already found the largest solution
    pp = make_palindrome(p_)
    a = maxnum
    while (maxnum+1) * a > pp: # ensures b < 10^digits
        if pp % a == 0:
            print(':', pp, '=', a, '*', pp//a)
            print(pp)
            found = True
            break
        a -= 1

