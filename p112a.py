
proportion = 0.99

# brute force, ~3 sec (cpython / i5-2540m)

def float_geq(a, b): return a - b >= -(2**(-32))

def bouncy(n): # test if its digits both increase and decrease
    inc, dec = False, False
    prev = n % 10
    n //= 10
    while n != 0:
        n, tmp = divmod(n, 10) # extract next digit
        if tmp > prev: inc = True # set increasing/decreasing if appropriate
        elif tmp < prev: dec = True
        prev = tmp # remember previous digit
    return inc and dec

bouncycount = 0
n = 100 # no bouncy numbers smaller than 100
while not float_geq(bouncycount / (n-1), proportion):
    if bouncy(n): bouncycount += 1
    n += 1
print(n-1)
