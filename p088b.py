import math

maxk = 12000

# create all factorizations recursively this time and add 1s separately
# upper bound can be 2k since 2k=k+2+(k-2)=k+2+1+1+...+1

prodlenmax = 1+math.floor(math.log2(maxk)) # log2(2k)
bestn = list(2*k for k in range(maxk+1)) # update these with better results
bestn[1] = 0 # skip 1 since range is 2<=k<=...

# recursively make factorizations
def recurse(curprod, cursum, prodlen, prevnum):
    global maxk, prodlenmax
    # try current product and sum
    if prodlen != 1: # has prodlen nums, need curprod-cursum more for k
        k = prodlen + (curprod-cursum) # add 1s to make cursum==curprod
        if k <= maxk: bestn[k] = min(bestn[k], curprod)
    while True: # recursively make factorizations
        nextprod = curprod * prevnum
        if nextprod > 2*maxk: break
        recurse(nextprod, cursum+prevnum, prodlen+1, prevnum)
        prevnum += 1
recurse(1,0,0,2)
print(sum(set(bestn)))
