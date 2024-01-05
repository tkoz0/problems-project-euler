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

L = 10000
Ls = 15000 # sieve limit
sieve = [1]*(Ls) # 1 divides everything so start with this
sieve[0] = sieve[1] = 0
for d in range(2,L):
    # add d to indexes for 2*d,3*d,...
    for n in range(2*d,Ls,d):
        sieve[n] += d
# search for amicable pairs
total = 0
for a in range(2,L):
    b = sieve[a]
    if b <= a:
        continue # require a < b to avoid counting twice
    # make sure sieve[b] = a (if b is small enough)
    # if b is not in our sieve, we have to sum its divisors
    if b < Ls:
        if sieve[b] != a:
            continue # not an amicable pair
    elif sum_divisors(b) - b != a:
        continue # not amicable pair
    print(f'pair {a} {b}')
    total += a
    if b < L: # only include a if b is above limit
        total += b
print(total)
