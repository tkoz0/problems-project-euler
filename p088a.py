import math

maxk = 12000 # most integers in a product (for 2<=k<=maxk)

# recursive solution, ~20sec (i5-2540m)

# recurse on factors > 1, add remaining 1s to sum for equality
def factorize2(k, n, cursum, curprod, preva, prodlen):
    if curprod == n: return cursum + (k-prodlen) == n
    nexta = preva # start here
    remprod = n//curprod
    # try the remaining product itself (dont recurse deeper until needed)
    if factorize2(k,n,cursum+remprod,curprod*remprod,remprod,prodlen+1):
        return True
    # try a factor of remaining product amount, must be at least preva
    while nexta*nexta <= remprod:
        if remprod % nexta == 0:
            if factorize2(k,n,cursum+nexta,curprod*nexta,nexta,prodlen+1):
                return True
        nexta += 1
    return False

minnset = set()
for k in range(2,maxk+1):
    # find min n that can be factorized this way
    n = k # 1+1+...+1=k so start here as minimum
    while True:
        if factorize2(k, n, 0, 1, 2, 0):
            minnset.add(n)
            break
        n += 1
print(sum(minnset))
