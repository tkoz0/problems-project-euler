
# number constants: k*b^e+n, modulus m
k = 28433
b = 2
e = 7830457
n = 1
m = 10**10

# compute exponent with exponentiation by squaring
value = 1
while e != 0:
    if e % 2 == 1: # 1 occurs, multiply
        value = (value * b) % m
    b = (b*b) % m # square base
    e //= 2

# multiply constant and add extra number
value = (k*value+n) % m
print(value)
