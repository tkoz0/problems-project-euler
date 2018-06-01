
multiples = 6

# brute force, 3 digits minimum since 6 permutations are required
d = 3
found = False
while not found:
    for i in range(10**(d-1), 10**d//multiples + 1):
        digits = sorted(int(c) for c in str(i))
        matched = True
        for m in range(2, multiples+1):
            mdigits = sorted(int(c) for c in str(i*m))
            if mdigits != digits:
                matched = False
                break
        if matched:
            for m in range(1, multiples+1): print(':', i*m)
            print(i)
            found = True
            break
    d += 1

