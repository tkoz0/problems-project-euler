import math

radmax = 100000
Eval = 10000

# sieve radicals my multiplying distinct prime factors
radsieve = [1] * (radmax+1)
for i in range(2,radmax+1):
    if radsieve[i] != 1: continue # not prime
    for j in range(i,radmax+1,i): radsieve[j] *= i

# max list of (rad(n),n) pairs and sort them
radlist = sorted((radsieve[i],i) for i in range(1,radmax+1))
#print(':',radlist)
print(':',radlist[Eval-1])
print(radlist[Eval-1][1]) # extract number from list
