limit = 100

# brute force
sum1 = 0
sum2 = 0
for i in range(limit+1):
    sum1 += i
    sum2 += i*i
print(sum1*sum1 - sum2)

# summation formulas
# (1+2+...)^2 = 1^3+2^3+...
# sum cubes = n^2(n+1)^2/4
# sum squares = n(n+1)(2n+1)/6
n = limit
value = (n**2 * (n+1)**2)//4 - n*(n+1)*(2*n+1)//6
print(value)
