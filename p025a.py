import math

digits = 1000

# brute force, iterative
a, b = 0, 1
i = 1 # index of 1 is 1
while len(str(b)) < digits:
    a, b = b, a+b
    i += 1
print(i)

# calculate based on the nonrecursive fibonacci expression
# F_n = ( phi^n - (1-phi)^n ) / sqrt(5)
# F_n = closest integer to phi^n/sqrt(5) since |(1-phi)^n/sqrt(5)| is < 1/2 for
# n = 0, 1, 2, ... and since the result has to be an integer, to change the
# result for closest integer, this absolute value would have to be >= 1/2
# ln(10^999)=999*ln(10) (10^999 has 1000 digits)
# ln(phi^n/sqrt(5))=n*ln(phi)-ln(sqrt(5)) = 999*ln(10)
# n = (999*ln(10)+ln(sqrt(5)))/ln(phi) --> pick ceiling function of this
phi = 1.618033988749894848
lognum = (digits-1) * math.log(10)
n = (lognum + math.log(math.sqrt(5))) / math.log(phi)
print(math.ceil(n))
