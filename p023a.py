import libtkoz as lib

largest = 28123 # everything larger known to be sum of 2 abundants

# this is pretty much a brute force solution, takes ~3 sec (i7-7600u)

def abundant(n): # proper divisor sum
    return lib.sum_divisors2(n) - n > n

# compute abundant numbers efficiently using the property that
# if n is abundant, all multiples of n are abundant
abundantstmp = [False] * (largest+1)
for n in range(1, largest+1):
    if not abundantstmp[n] and abundant(n):
        for i in range(n, largest+1, n):
            abundantstmp[i] = True

abundants = []
for i in range(len(abundantstmp)):
    if abundantstmp[i]:
        abundants.append(i)
print(':', len(abundants), 'abundants below', largest+1)

# array of numbers representable as sum of 2 abundants
# use double loop to mark numbers that are sum of 2 abundants
sumabundants = [False] * (largest+1)
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] > largest:
            break
        sumabundants[abundants[i] + abundants[j]] = True

# sum numbers that cant be summed by 2 abundant numbers
# also finds the largest such number
total = 0
largestnonsum = 0
for i in range(1, largest+1):
    if not sumabundants[i]:
        total += i
        largestnonsum = i
print(': largest that isnt sum of 2 abundants is', largestnonsum)
print(total)

