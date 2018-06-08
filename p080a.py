import libtkoz as lib
import math

digits = 100
maxnum = 100 # TODO change to 100
showapprox = False # display fraction approximation used
showdigits = False # display calculated digits

# begin by approximating each square root with a fraction by using the
# continued fraction expansion with its recurrence relation
# then use long division to calculate the digits

digitsum = 0
for num in range(2,maxnum+1):
    if lib.is_square(num): continue # only sum for irrational square roots
    n = math.floor(math.sqrt(num))
    # first 2 convergents are n/1 and (n*r+1)/r with r=floor(2n/(num-n^2))
    r = (2*n) // (num - n**2)
    a1, a2 = n, n*r+1 # numerator a2
    b1, b2 = 1, r # denomenator b2
    # fractional part, after a2/b2 convergent can be calculated to be
    # (sqrt(num)+n-r*(num-n^2))/(num-n^2)
    rem = (num, n-(num-n**2)*r, 0, num-n**2) # (sqrt,int) / (sqrt,int)
    # compute fraction until denomenator > 10**digits (error < 10**(-digits))
    while b2 < 10**digits:
        # calculating next constant based on p064 solution
        rem = (rem[2], rem[3], rem[0], rem[1])
        den = rem[2] - rem[3]**2 # denomenator for next fraction
        assert den % rem[1] == 0, 'theoretical assumption failure'
        rem = (rem[2], -rem[3], 0, den // rem[1])
        intpart = (rem[1] + n) // rem[3]
        rem = (rem[0], rem[1] - intpart*rem[3], rem[2], rem[3])
        # intpart is next constant, compute next approximation
        a1, a2 = a2, intpart*a2 + a1
        b1, b2 = b2, intpart*b2 + b1
    # a2/b2 is now an approximation of the square root
    a2 -= n*b2 # get fractional part
    if showapprox:
        print(': sqrt(', num, ') ~= ', n, ' + ', a2, ' / ', b2, sep='')
    if showdigits:
        print(': sqrt(', num, ') = ', n, '.', sep='', end='')
    # perform long division to calculate digits after decimal point
    for i in range(digits-lib.digits_in(n)):
        a2 *= 10
        digit = a2 // b2
        a2 -= digit*b2
        if showdigits: print(digit, sep='', end='')
        digitsum += digit
    digitsum += lib.sum_digits(n) # include digits from integer part
    if showdigits: print() # end line
print(digitsum)
