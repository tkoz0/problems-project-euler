import math

# brute force try everything
# if b>=10 then b^e >= 10^e --> has at least e+1 digits so b<10
count = 0
for b in range(1, 10):
    e = 1
    while True:
        if len(str(b**e)) == e:
            print(':', b, '^', e, '=', b**e)
            count += 1
        else: break
        e += 1
print(count)

# with some mathematics to count instead of brute forcing
# 10^(n-1) <= x^n < 10^n, for every n, how many x are solutions, x<10
# left side: x >= 10^((n-1)/n)
# count how many x are in this range
count = 0
n = 1
while True:
    xmin = int(math.ceil(math.pow(10, (n - 1) / n)))
    print(': for', n, 'digits, min x =', xmin)
    if xmin == 10: break # none since x<10 is a requirement
    count += 10-xmin
    n += 1
print(count)

