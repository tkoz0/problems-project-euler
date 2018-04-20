
limit = 1000000

# simple brute force solution, ~15 sec in 2018
def seq_len(a):
    l = 1
    while a != 1:
        l += 1
        if a % 2 == 0: a //= 2
        else: a = 3*a + 1
    return l

maxnum = 0
maxseq = 0
for n in range(1, limit):
    seql = seq_len(n)
    if seql > maxseq:
        print(': longer num =', n, ', seq len =', seql)
        maxnum, maxseq = n, seql
print(maxnum)
