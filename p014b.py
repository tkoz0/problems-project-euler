
limit = 1000000

# improved, cache to speed up sequence length calculation, ~1 sec (i7-7600u)
# once reaching a previous calculated number, its sequence length can be used
# index i --> sequence length starting at i
cache = [0, 1] # 0 --> length 0, 1 --> length 1

maxnum = 0
maxseq = 0
for n in range(2, limit):
    n2 = n
    seql = 0
    while n2 >= n: # compute sequence until reaching previous number
        seql += 1
        if n2 % 2 == 0: n2 //= 2
        else: n2 = 3*n2 + 1
    seql += cache[n2] # use sequence length for smaller number
    cache.append(seql)
    if seql > maxseq:
        print(': longer num =', n, ', seq len =', seql)
        maxnum, maxseq = n, seql
print(maxnum)
