
coins = [200, 100, 50, 20, 10, 5, 2, 1]
amount = 200

# recursive solution
ways = 0
def find_ways(amt, ci): # parameters are current sum and index in coins
    if ci == len(coins)-1: # speed up, only 1 way at this point
        global ways
        ways += 1
    else:
        global amount
        while amt <= amount:
            find_ways(amt, ci+1)
            amt += coins[ci]
find_ways(0, 0) # start by adding 200p coins to nothing
print(ways)

# dynamic programming solution
# to create amount n, if choosing coin c, how many ways to make n-c
# n=10, pick c=1 --> a way to make 9 is 1,1,1,1,5
# n=10, pick c=5 --> a way to make 5 is 1,1,1,1,1
# this results in a duplicate, allows picking coins in different orders for
# identical solutions, to avoid this, define strict ordering
# coins must always be picked in sorted order so duplicating identical solutions
# like above is avoided
# to create amount n, if choosing c, how many ways to make n-c by using only
# (larger/smaller) coins (or same)
# for this, go 1 coin at a time in small to large order

ways = [1] + ([0]*amount) # initially 1 way to make the sum 0 (no coins)
print(': begin', ways)
for c in coins[::-1]: # add a new coin each time, use small to large order
    # since ways contains how to make amounts with only smaller coins (or same)
    for amt in range(c, amount+1):
        ways[amt] += ways[amt - c]
    print(': coin', c, ways)
print(ways[amount])

