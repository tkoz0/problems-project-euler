
MAXV = 4000000

# faster solution, iterative
# a,b store 2 fibonacci numbers
sum_ = 0
a,b = 0,1
while True:
    # calculate next number, store 2 needed for calculation of next
    a,b = b, a+b
    if b > MAXV: break
    if b % 2 == 0:
        sum_ += b
print(sum_)

# an even faster sequence can be computed
# starting with F_0=0,F_1=1, we get the following
# even,odd,odd,even,odd,odd,even,... (evens are at index that is multilpe of 3)
# we know F_0 = 0, F_3 = 2
# start with F_n and use the recurrence F_n=F_(n-1)+F_(n-2) to derive
# F_n = 4*F_(n-3) + F_(n-6)
sum_ = 2
a,b = 0,2
while True:
    a,b = b, 4*b+a
    if b > MAXV: break
    sum_ += b
print(sum_)
