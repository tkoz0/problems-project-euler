import math

startlim = 1000000
chainlen = 60

def next(n): # computes next in chain
    s = 0 # use division since its faster than string conversion stuff
    while n != 0:
        s += math.factorial(n % 10)
        n //= 10
    return s

# compute each chain by brute force

count = 0
for n in range(startlim):
    chain = [n]
    nn = n
    while True:
        nn = next(nn)
        if nn in chain: break # no repeating numbers
        chain.append(nn)
    if len(chain) == chainlen: count += 1
print(count)
