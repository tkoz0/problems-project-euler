import libtkoz as lib

limit = 10000
itrlim = 50 # can go as low as 25 and same answer will be produced

# try each number by brute force, use python support for large integers
# caching numbers under the limit could make it faster
# speed increase wont be much for a problem this small
count = 0
for n in range(limit):
    start = n
    lychrel = True
    for itr in range(1,itrlim):
        rev = int(str(n)[::-1]) # convert to string, reverse, convert to int
        n += rev
        if lib.palindrome(n):
            lychrel = False
            break
    if lychrel:
        print(':', start, '-->', n, '(', itrlim-1,'iterations)')
        count += 1
print(count)
