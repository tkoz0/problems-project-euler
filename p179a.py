
limit = 10**7

# count divisors in a cache by starting at a number and adding 1 to multiples
# because theres a lot of numbers this takes ~30sec (i5-2540m)

cache = [1] * limit # start with 1 (counting the number itself

for n in range(1,(limit+1)//2):
    for i in range(2*n,limit,n): # count for multiples having this factor
        cache[i] += 1
print(': generated divisor count cache')

count = 0 # numbers for which n and n+1 have same number of divisors
for i in range(2,limit-1):
    if cache[i] == cache[i+1]: count += 1
print(count)
