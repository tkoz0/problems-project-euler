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

# suppose each bit is a random variable B and there are 32 of them
# B_i is how many ors were needed to make the ith bit 1
# for up to k steps to make it a 1, P(B_i<=k)=1-2^(-k)
# before Z=max(all B_i) so P(Z<=k)=P(B_i<=k)*... since all B are independent
# so P(Z<=k)=(1-2^(-k))^N (N bits total)
# P(Z=k) = P(Z<=k) - P(Z<=k-1)
# now compute E(Z)= sum k*P(Z=k) from k=1 to infinity
# by using some algebra and combinatorics and summations... (a bit complicated)
# this evaluates to -sum (N choose i) * (-1)^i / (1-2^(-i)) for i=1 to N

# unfortunately summing directly doesnt give the right answer because
# floating point math is garbage
print(':',-sum(lib.binom_coeff(bits,i)*((-1)**i)/(1-(2**(-i))) \
               for i in range(1,bits+1)))

# compute the fraction and do the division at the end
N, D = 0, 1
for i in range(1,bits+1):
    n = lib.binom_coeff(bits,i) * ((-1)**i) * (2**i)
    d = (2**i) - 1
    # N/D + n/d = (Nd+nD)/(Dd)
    N, D = N*d + n*D, D*d
    g = lib.gcd_euclid(abs(N),abs(D))
    N, D = N//g, D//g
print(':',N) # the fraction result
print(':',D)

expected = (-N)/D # decimal approximation needed for answer

# output similar to above with 10 decimal places
expected = round(expected * 10**precision)
print(expected//(10**precision),'.',expected%(10**precision),sep='')
