L = 100000000

# sieve primes
prime = [True]*L
prime[0] = prime[1] = False
primelist = []
for p in range(2,L):
    if not prime[p]:
        continue
    primelist.append(p)
    for i in range(p*p,L,p):
        prime[i] = False

llen = 1
lmin = 2
lmax = 2
lsum = 2
for i in range(len(primelist)):
    if primelist[i] * (llen+1) >= L:
        break # cannot form a longer sum under L
    s = 0
    for j in range(i,len(primelist)):
        s += primelist[j]
        if s >= L:
            break
        if prime[s] and j-i+1 >= llen:
            llen = j-i+1
            lmin = primelist[i]
            lmax = primelist[j]
            lsum = s
            print(f'sum of {llen} primes ({lmin},{lmax}) = {lsum}')

print(lsum)
