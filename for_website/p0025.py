L = 1000
a = [0]
b = [1]
i = 1 # represents the fibonacci index of b
while len(b) < L:
    # add b to a (a < b is maintained)
    # this is for the step a,b -> b,a+b
    j = 0
    c = 0 # carry
    while j < len(a): # add to existing elements of a
        a[j] += b[j] + c
        if a[j] >= 10: # determine carry
            a[j] -= 10
            c = 1
        else:
            c = 0
        j += 1
    while j < len(b): # if b is longer, a grows
        a.append(b[j] + c)
        if a[j] >= 10:
            a[j] -= 10
            c = 1
        else:
            c = 0
        j += 1
    if c != 0: # carry extends length of 1
        a.append(c)
    # swap to maintain a < b (a,b -> b,a+b)
    a,b = b,a
    i += 1
print(i)
