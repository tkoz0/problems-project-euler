import libtkoz as lib

pval = 10**8
modulus = 10**9+7

# improved to sublinear pi sequence checking (after generating prime list)
# primes uses O(n) memory, primeset uses O(n/logn) and so does picache
# pi sequences require about logn/loglogn steps
# main loop looks at all primes (O(n/logn)) so overall is about O(n/loglogn)

# make prime list for iteration and prime set for fast primality checking
primes = lib.list_primes2(pval)
print(': listed primes up to',pval)
# values of pi(n) for O(1) computation, go up to maximum pi(n) value
picache = []
primeset = set() # make for fast primality checking of smaller numbers
for i,p in enumerate(primes): # pi(p)=i+1
    primeset.add(p)
    while len(picache) < p: picache.append(i)
    picache.append(i+1)
    if p > len(primes): break
print(': generated pi(n) cache up to',len(picache)-1)

longest = 2 # find longest possible pi sequence length
n = len(primes) # (pval,pi(pval))
while n != 1:
    n = picache[n]
    longest += 1
print(': longest pi sequence length is',longest)

nonprimecounts = [0]*(longest+1)
# evaluate pi sequences, considering that many starting numbers are followed by
# identical sequences
prevp = 1
for i,p in enumerate(primes):
    # start by considering composite start numbers prevp+1 to p-1, pi(p-1)=i
    c = 1 # composite count
    n = i # number in pi sequence
    compositestarts = p-prevp-1 # amount of starting numbers being considered
    if not (n in primeset): c += 1 # 2 composites considered, ex: (p-1,i)
    nonprimecounts[c] += compositestarts
    while n > 1:
        n = picache[n]
        if not (n in primeset): c += 1
        nonprimecounts[c] += compositestarts
    # then consider p itself
    c = 0 # composite count
    n = i+1 # number in pi sequence
    if not (n in primeset): c += 1 # considered (p,i+1)
    nonprimecounts[c] += 1
    while n != 1:
        n = picache[n]
        if not (n in primeset): c += 1
        nonprimecounts[c] += 1
    prevp = p
# finish off with pi sequences from lastprime+1 to pval
compositestarts = pval-prevp
c = 1
n = len(primes)
if not (n in primeset): c += 1
nonprimecounts[c] += compositestarts
while n != 1:
    n = picache[n]
    if not (n in primeset): c += 1
    nonprimecounts[c] += compositestarts

print(': c(u) = k counts',nonprimecounts)
prod = 1 # compute product of the values
for c in nonprimecounts:
    if c != 0: prod = (prod*c) % modulus
print(prod)
