
side = 1001

total = 1 # center number
delta = 2
lastnum = 1

while delta < side:
    # (lastnum+delta) + ... + (lastnum+4*delta) = 4*lastnum+10*delta
    total += 4 * lastnum + 10 * delta
    lastnum += 4 * delta
    delta += 2
print(total)

# define a sequence side length = 1, 3, 5, ... for i = 0, 1, ... --> side=2*i+1
# if i > 0 then inner square has (2i-1)^2 nums
# the added amounts are 2i, 4i, 6i, 8i
# summing: 4(2i-1)^2 + 20i = 16i^2 + 4i + 4
# now sum this from i=1 to s (s = (side-1)/2) since side should be odd
# 16s(s+1)(2s+1)/6 + 4s(s+1)/2 + 4s
totalsum = lambda s : 8*s*(s+1)*(2*s+1)//3 + 2*s*(s+1) + 4*s
print(totalsum(side // 2) + 1) # add center num, summations counts outer rings
