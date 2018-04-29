
maxdiv = 20

# brute force, increments in largest
# takes ~10 sec (i7-7600u)
n = 0
while True:
    n += maxdiv
    div_by_all = True
    for d in range(1, maxdiv):
        if n % d != 0:
            div_by_all = False
            break
    if div_by_all:
        print(n)
        break
