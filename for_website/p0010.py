L = 2000000

sieve = [True]*(L//2) # index i means number 2*i+1
sieve[0] = False
for i in range(1,L//2): # 3 is at index 1
    inum = 2*i+1
    if inum*inum >= L:
        break
    if not sieve[i]:
        continue
    # start at inum*inum and go in increments of
    # 2*inum because this sieve skips even numbers
    for jnum in range(inum*inum,L,2*inum):
        sieve[jnum//2] = False

# remember to include 2 in the sum
print(2 + sum(2*i+1 for i in range(L//2) if sieve[i]))
print(f'number of primes is {1 + sum(1 for i in range(L//2) if sieve[i])}')
