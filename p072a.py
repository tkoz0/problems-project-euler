import libtkoz as lib

maxd = 1000000

# this is the sum of totients for 2<=d<=limit, ~15sec (i5-2540m)

print(sum(lib.totient(d) for d in range(2, maxd+1)))
