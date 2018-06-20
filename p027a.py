import libtkoz as lib

arange = 999 # -999 to 999
brange = 1000 # -1000 to 1000
pseqlenparam = 100 # estimate for longer sequences to determine prime cache size

# quadratic function is x^2+ax+b
# computing next: f(x+1) - f(x) = (x^2+2x+1+ax+a+b) - (x^2+ax+b)
# = 2x+1+a --> use this as difference to compute next more efficiently

# generate a set of primes to quickly look up
# if x may go up to 100, 100^2+1000*100+1000 ~= 10^5 --> seems reasonable
# pick the largest term at x=100
ptablemax = max(pseqlenparam**2, pseqlenparam*arange, brange)
ptable = lib.list_primes2(ptablemax,return_set=True)
def prime(n):
    global ptable
    global ptablemax
    return (n <= ptablemax and n in ptable) or lib.prime(n)
print(': listed', len(ptable), 'primes <=', ptablemax)

# f(x) = x^2 + ax + b
# f(0) = b --> b must be prime
# f(1) = 1 + a + b --> if b odd then a must be odd
# f(x+1) - f(x) = 2x + 1 + a --> a must be odd so the step size is even
if arange % 2 == 0: arange -= 1 # ensure it is odd
mostprimes = 0
amost, bmost = 0, 0
for b in range(3, brange+1, 2):
    if not prime(b): continue
    for a in range(-arange, arange+1, 2):
        x = 1
        f = 1 + a + b # f(1)
        while prime(f):
            f += 2 * x + 1 + a
            x += 1
        if x > mostprimes:
            mostprimes = x
            amost, bmost = a, b
            print(': f(x) = x^2 +', a, '* x +', b, '-->', x, 'primes')
print(amost * bmost)
