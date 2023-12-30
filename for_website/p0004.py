D = 7
largest = 0
for a in range(10**D-1,10**(D-1)-1,-1):
    if a * (10**D-1) < largest:
        break
    for b in range(a,10**(D-1)-1,-1):
        n = a*b
        if n < largest:
            break
        s = str(n)
        if s == s[::-1]:
            largest = n
print(largest)

largest = 0
for a in range(100,1000):
    for b in range(100,1000):
        n = a*b
        s = str(n)
        if n > largest and s == s[::-1]:
            largest = n
print(largest)
