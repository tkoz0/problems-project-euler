import library

index = 10001

# brute force
counter = 0
n = 1
while True:
    n += 1
    if library.prime(n):
        counter += 1
    if counter == index:
        print(n)
        break

