import libtkoz as lib

limit = 1000000
primes = lib.list_primes2(limit)
primeset = set(primes) # for fast lookup

longestseq = 1
bestprime = 0

for i in range(len(primes)):
    if i > limit / longestseq: break # cant make longer sequence
    total = sum(primes[i:i+longestseq])
    seqlen = longestseq
    for j in range(i+longestseq, len(primes)):
        total += primes[j]
        if total >= limit: break # done for this starting number
        seqlen += 1
        if total in primeset:
            print(':', total, 'is sum of', seqlen, 'primes, start =', primes[i])
            longestseq, bestprime = seqlen, total
print(bestprime)
