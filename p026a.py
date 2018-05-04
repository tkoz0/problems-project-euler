limit = 1000

# try all, start from maximum since the longer ones are probably larger
# for divisor d, the remainder is from 0 to d-1 for each step
# by this, after d+1 steps, there must be a cycle (pidgeonhole principle)
# once a remainder is repeated, a cycle starts
# we can take this a step further, since 0 ends cycling, after d steps, there
# must be a cycle
# longest cycle of length d-1 would use values 1 through d-1

longestcycle = 0
lcyclenum = 0
rems = [0] * limit

for d in range(limit-1, 1, -1):
#for d in range(2, limit):
    if d <= longestcycle: break # d-1 is max possible cycle length
    rem = 1
    rems[0] = 1 # start with remainder 1
    # many numbers have shorter cycles, primes seem to have the longest and if
    # their cycle is the max length, a 1 will be encountered again
    i = 1 # index in rems list
    cyclic = True
    while i < d:
        rem *= 10 # shift left 1
        rem %= d
        if rem == 0:
            cyclic = False
            break
        rems[i] = rem
        i += 1
    if not cyclic: continue
    # start from end and search backwards to find same number
    endnum = rems[i-1]
    for j in range(i-2, -1, -1):
        if rems[j] == endnum:
            if i-1-j > longestcycle:
                print(': found', d, 'with cycle', i-1-j)
                longestcycle = i-1-j
                lcyclenum = d
            break
print(lcyclenum)
