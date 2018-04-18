import math

limit = 2000000

# faster method with prime sieve, odds only to reduce memory needs by 50%
# sum starts at 2 since sieve is only considering odds
psum = 2
pcount = 1
sievesize = (limit+1) // 2 # last index has largest odd, index i means 2i+1
sieve = [True] * sievesize

# loop for odds up to square root
for n in range(3, int(math.sqrt(limit))+2, 2):
    i = n//2 + n # initial cross off index, represents 3*(2*i+1)
    while i < sievesize:
        sieve[i] = False
        i += n # increment in n which increases number by 2n (cross off odds)

for i in range(1, sievesize): # sum numbers
    if sieve[i]:
        pcount += 1
        psum += 2*i + 1
print(': prime count', pcount)
print(psum)
