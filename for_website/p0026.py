L = 1000
num = 1 # number generating longest cycle
cycle = 0 # longest cycle length
rems = [0]*L # track remainders in iteration
#for d in range(2,L): # loop increasing
for d in range(L-1,1,-1): # loop decreasing
    if d <= cycle: # cycle cannot be longer than d-1
        break
    rems[0] = 1
    i = 1
    while i < d: # generate remainder sequence
        rems[i] = (10*rems[i-1]) % d
        if rems[i] == 0:
            break # not cyclic
        i += 1
    if i < d: # stopped early because result is not cyclic
        continue
    # find the start point of the cycle
    i -= 1 # end index
    j = i-1
    while rems[j] != rems[i]:
        j -= 1
    if i-j > cycle:
        print(f'cycle {i-j} with d={d}')
        num = d
        cycle = i-j
print(num)
