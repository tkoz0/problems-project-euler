
exp = 200000
divby = 10**12

# the binomial coefficients are (exponent choose a and b)

count = 0
value = 1
numerator = exp
denomenator = 1
for a in range(exp+1):
    print(': a =',a)
    if a != 0:
        value *= numerator
        numerator -= 1
        value //= denomenator
        denomenator += 1
        value %= divby
    value2 = value # compute values for b choices
    numerator2 = numerator
    denomenator2 = 1
    for b in range(a,exp+1):
        if b != a:
            value2 *= numerator2
            numerator2 -= 1
            value2 //= denomenator2
            denomenator2 += 1
            value2 %= divby
#        print(exp,'choose',a,'and',b-a,'and',exp-b,'=',value2)
        if value2 == 0: count += 1
print(count)

