L = 4000000
a,b = 0,1
total = 0
while True:
    a,b = b,a+b
    if b > L:
        break
    if b % 2 == 0:
        total += b
print(total)

L = 4000000
a,b = 0,2
total = 2
while True:
    a,b = b,4*b+a
    if b > L:
        break
    total += b
print(total)
