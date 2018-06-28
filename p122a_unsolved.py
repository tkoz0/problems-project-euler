
maximum = 200

# incorrect results, not considering shared calculations
memoize = dict()
def min_mults(k):
    global memoize
    if k == 0 or k == 1: return 0 # n^0 and n^1 dont need multiplication
    if k in memoize: return memoize[k]
    result = k
    for a in range(1,(k+1)//2):
        result = min(result,min_mults(a)+min_mults(k-a)+1)
    if k % 2 == 0: result = min(result,min_mults(k//2)+1)
    memoize[k] = result
    return result
for i in range(20): print(i,min_mults(i))
quit()


# dynamic programming, each exponent is made from multiplying 2 smaller
# exponents so pick 2 that make the smallest amount of multiplications
# suppose a+b=c so we pick n^c=n^a*n^b but if n^a and n^b share some of the
# same multiplications in their calculation the result will be inaccurate
# to fix for this, pick some smaller a,b that sum to current exponent, then
# for each a,b pair subtract the amount of shared multiplications that will
# result in a minimum number of multiplications which means looking at all
# possible pairs of exponents that multiply to both a and b

mults = [0,0] # each index i is minimum multiplications to calculate n^i
# each index i is a list of tuple pairs for smaller exponents that can be
# multiplied together and make n^i with a minimum number of multiplications
smaller = [[],[]]

while len(mults) <= maximum:
    pass

print(sum(mults))
