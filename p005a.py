import library

maxdiv = 20

# brute force, increments in largest
# in 2018, takes ~10 sec
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
