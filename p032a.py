import math

# n1 digits, n2 digits, n1*n2 digits
# n1*n2 will have either n1+n2 or n1+n2-1 digits
# suppose n1 has a digits and n2 has b digits
# min is 10^(a-1) * 10^(b-1) = 10^(a+b-2) has a+b-1 digits
# max is (10^a-1) * (10^b-1) < 10^(a+b) has a+b digits
# possibilities for digits in (n1,n2,n1*n2) are
# (1,4,4), (4,1,4), (2, 3, 4), (3, 2, 4) since
# 4+(4 or 3) cant be 9, 5+(5 or 4) can be 9, 6+(6 or 5) cant be 9
# n1,n2 must have 5 digits together

# a, b, c combined must have each digit 1-9 once
def has_all_digits(a, b, c):
    return '123456789' == ''.join(sorted(str(a)+str(b)+str(c)))

# method 1, for possible products, find factors
total = 0
for p in range(1000, 10000): # product must be 4 digits
    found_pandigital = False
    for f in range(2, int(math.sqrt(p))+1): # find a factor
        # not a factor or a pandigital was found for this product alreday
        if p % f != 0 or found_pandigital: continue
        if has_all_digits(f, p//f, p):
            total += p
            found_pandigital = True # dont count products more than once
            print(':', f, '*', p//f, '=', p)
print(total)

# method 2, create products from looping on factors
# multiple factor pairs may generate same product so use a set to ensure unique
prods = set() # store unique products in a set
# f1,f2 must have 1,4 or 2,3 digits (see above)
for f1 in range(2, 100):
    for f2 in range(f1+1, 10000//f1 + 1):
        if has_all_digits(f1, f2, f1*f2):
            prods.add(f1*f2)
            print(': found product', f1*f2)
print(sum(prods))

