
maxnum = 1000000

# generate a cache of divisor sums, more speed at higher memory cost
# for all numbers under limit/2, add them to the sums for their multiples
cache = [1] * (maxnum+1) # 1 divides everything
for d in range(2, 1+maxnum//2):
    for i in range(2*d, maxnum+1, d):
        cache[i] += d
print(': generated divisor sum cache')

# mark numbers visited, longest chain will be found when the smallest in it is
# visited first time, when exceeding maxnum or reaching 1, chain doesnt work
visited = [False] * (maxnum+1)
visited[0] = visited[1] = True

# try chains until either exceeding maxnum or reaching 1
# takes ~5.5 sec (i5-2540m)
longest = 0
minnum = 0
for n in range(2, maxnum+1):
    if visited[n]: continue
    start = n
    nums = [n]
    visited[n] = True
    n = cache[n]
    while n <= maxnum and not visited[n]: # find numbers in chain
        nums.append(n)
        visited[n] = True
        n = cache[n]
    nums.append(n)
    if nums[-1] > maxnum: continue # exceeded limit
    # last number was visited so see if it exists previously in the chain
    i = -1
    for j in range(len(nums)-1):
        if nums[j] == nums[-1]:
            i = j
            break
    if i == -1: continue # didnt find number
    if len(nums)-i > longest: # longer chain
        longest = len(nums)-i
        minnum = min(nums[i:])
        print(': longer chain', nums[i:])
        print(':   all nums visited to find it', nums)
print(minnum)
