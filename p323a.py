import libtkoz as lib

bits = 32
precision = 10 # number of digits after decimal point

expected = 0.0
y = 0 # number of random binary strings ored
while True:
    # consider probability of number of 1 bits already, multiply that by
    # probability of next random binary string being a success
    iteradd = 0.0 # amount added for this iteration
    for ones in range(bits): # ignore 32 bits already since thats success
        # probability of a given bit being a 1 is 1 - 2^(-y)
        # compute probability of this many ones with binomial theorem
        p = lib.binom_coeff(bits,ones) * (1-2**(-y))**ones * \
                                         (2**(-y))**(bits-ones)
        # remaining 0 bits must have corresponding ones for next to be success
        s = 2**(ones-bits)
        iteradd += p*s # amount to add to expected value (multiply y+1 later)
    iteradd *= y+1 # contribution weighted by iterations to success
    expected += iteradd
    # end when contribution to expected value is small enough
    if iteradd < 10**(-precision-1): break
    y += 1
# round by integer conversion, 10 least significant digits after decimal point
expected = round(expected * 10**precision)
print(expected//(10**precision),'.',expected%(10**precision),sep='')
