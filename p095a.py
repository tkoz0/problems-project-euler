
maxnum = 1000000

# generate a cache of divisor sums, more speed at higher memory cost
# for all numbers under limit/2, add them to the sums for their multiples
cache = [1] * (maxnum+1) # 1 divides everything
for d in range(2, 1+maxnum//2):
    for i in range(2*d, maxnum+1, d):
        cache[i] += d
print(': generated divisor sum cache')

# try chains until either exceeding maxnum or reaching 1
longest = 0
minnum = 0
for n in range(2, maxnum+1):
    start = n
    nums = [n]
    n = cache[n]
    while n != 1 and n <= maxnum and not (n in nums): # find numbers in chain
        nums.append(n)
        n = cache[n]
    nums.append(n)
    if nums[0] == nums[-1] and len(nums) > longest:
        longest = len(nums)
        minnum = min(nums)
        print(': longer chain', nums)
print(minnum)
