def sum_divisors(n):
    total = 0
    d = 1
    while d*d < n:
        if n % d == 0:
            total += d
            total += n//d
        d += 1
    if d*d == n: # perfect square
        total += d
    return total

L = 28123
abundant = [False]*(L+1)
for n in range(1,L+1):
    # only consider unmarked numbers for possible abundance
    if not abundant[n] and sum_divisors(n) - n > n:
        for m in range(n,L+1,n):
            abundant[m] = True

# make a list of abundant numbers and double loop for sums
abundantlist = [i for i in range(L+1) if abundant[i]]
print(f'abundant number list has {len(abundantlist)} numbers')
abundantsum = [False]*(L+1)
for i in range(len(abundantlist)):
    for j in range(i,len(abundantlist)):
        # check bound to terminate inner loop early
        s = abundantlist[i] + abundantlist[j]
        if s > L:
            break
        abundantsum[s] = True

nonabundantsums = [i for i in range(L+1) if not abundantsum[i]]
print(f'largest non abundant sum number is {max(nonabundantsums)}')
print(sum(nonabundantsums))
