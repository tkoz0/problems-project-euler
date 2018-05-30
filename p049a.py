import libtkoz as lib

seqlen = 3 # currently hardcoded, has no effect
digits = 4

# brute force
primes = lib.list_primes2(10**digits)
print(': listed', len(primes), 'primes')

def is_prime(n): # assumes it would be in the primes list, binary search
    global primes
    l, h = 0, len(primes)
    while l != h:
        mid = (l+h)//2
        if primes[mid] >= n: h = mid
        else: l = mid+1
    return l < len(primes) and primes[l] == n

# binary search for lowest 4 digit prime
l, h = 0, len(primes)
while l != h:
    m = (l+h)//2
    if primes[m] >= (10**(digits-1)): h = m
    else: l = m+1
print(': start prime index', l, 'is', primes[l])

done = False
for i in range(l, len(primes)): # select first prime
    pi = primes[i]
    if done: break
    for j in range(i+1, len(primes)): # select second prime
        pj = primes[j]
        pk = pj + (pj-pi) # next in arithmetic sequence
        if pk >= 10**digits: break
        if not is_prime(pk): continue
        # make sorted digit strings to test digit permutations
        si = ''.join(sorted(str(pi)))
        sj = ''.join(sorted(str(pj)))
        sk = ''.join(sorted(str(pk)))
        if si == sj == sk:
            if pi == 1487 and pj == 4817 and pk == 8147: # given sequence
                print(': given', pi, pj, pk)
            else: # the other remaining sequence
                print(pi, pj, pk, sep='')
                done = True
                break
