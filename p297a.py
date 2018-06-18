
limit = 10**17
printgeninfo = False
printcountinfo = False

# dynamic programming, zeckendorf representation requires that the fibonacci
# numbers used in the representation are not consecutive
# using f_2=1 and f_3=2, index in rtsum is sum of terms used in representations
# for the fibonacci numbers below f_i (for index i)
rtcount = [0,0,0] # (representation terms count)
fiblist = [0,1,1]

# consider F_n in F_n = F_n-1 + F_n-2
# ways to represent numbers below F_n is ways to represent numbers below F_n-1
# plus ways to represent the F_n-2 numbers F_n-1 <= k < F_n
# this can me computed from F_n-2 + rtsum[n-2]
# in general rtcount[n] = rtcount[n-1] + F_n-2 + rtcount[n-2]
# the wikipedia diagram is very helpful in understanding this

# use above to generate fibonacci numbers and counts of how many terms are used
# in representing all the numbers below each
a, b, c = 0, 1, 1
fib_i = 2
while True:
    a, b, c = b, c, b+c # c represents F_n, a represents F_n-2
    fib_i += 1
    rtcount.append(rtcount[-1] + a + rtcount[-2])
    fiblist.append(c)
    if printgeninfo: print(': f',fib_i,'=',fiblist[-1],'rtsum =',rtcount[-1])
    if c >= limit: break

# break the number into smaller pieces recursively by picking the largest
# fibonacci up to the limit and counting those, this leaves leftover numbers
# from this fibonacci choice up to below limit that arent counted so for those
# count how many there are (1st term) plus terms in representation of fibonacci
# numbers below (limit - fibonacci choice), do this until picking a fibonacci
# number equal to limit
def count(lim):
    global rtcount, fiblist
    if lim == 0: return 0 # nothing to count
    fi = 0 # find largest fibonacci number up to limit
    while fiblist[fi+1] <= lim: fi += 1
    rem = lim - fiblist[fi] # how many left to count recursively
    if printcountinfo:
        print(': counting',rtcount[fi],'terms below',fiblist[fi],'and',rem,
              'numbers left')
    return rtcount[fi] + rem + count(rem)
print(count(limit))
