
limit = 10**17

# dynamic programming, zeckendorf representation requires that the fibonacci
# numbers used in the representation are not consecutive
# using f_2=1 and f_3=2, index in rtsum is sum of terms used in representations
# for the fibonacci numbers below f_i (for index i)
rtcount = [0,0,0,1] # (representation terms count)

# consider F_n in F_n = F_n-1 + F_n-2
# ways to represent numbers below F_n is ways to represent numbers below F_n-1
# plus ways to represent the F_n-2 numbers F_n-1 <= k < F_n
# this can me computed from F_n-2 + rtsum[n-2]
# in general rtcount[n] = rtcount[n-1] + F_n-2 + rtcount[n-2]
# the wikipedia diagram is very helpful in understanding this

a, b, c = 0, 1, 2
fib_i = 3
while True:
    a, b, c = b, c, b+c # c represents F_n, a represents F_n-2
    fib_i += 1
    rtcount.append(rtcount[-1] + a + rtcount[-2])
    print('f',fib_i,'=',c,'rtsum =',rtcount[-1])
    if c >= limit: break
