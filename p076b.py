
sumto = 100

# much faster dynamic programming approach

ways = [0] * (sumto + 1)
ways[0] = 1 # sum to 0 in 1 way

# to sum to s, for all n<s how many ways to sum to s-n with integers <= n
for i in range(1,sumto+1): # i is largest integer considered so far
    for j in range(i,sumto+1): # j is the sum to number
        ways[j] += ways[j-i] # using i, add ways to sum j-i using ints <= i
print(ways[sumto]-1) # exclude the number by itself
