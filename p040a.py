import libtkoz as lib

productof = list(10**n for n in range(6+1))
print(': multiplying these digits', productof)

# brute force count digits for everything
digits = 0 # total digits iterated
i = 1 # next number to append
prod = 1 # digit product
nexti = 0 # index of next digit to multiply (in productof)
while nexti < len(productof):
    digits += lib.digits_in(i)
    if digits >= productof[nexti]: # found next digit to multiply
        ii = i # extract digit
        for j in range(digits - productof[nexti]):
            ii //= 10
        prod *= ii % 10 # modulus 10 to extract ones digit
        print(': digit', productof[nexti], 'is', ii%10, 'from', i)
        nexti += 1
    i += 1
print(prod)

# use some arithmetic to compute the product faster
prod = 1
d = 1 # length of digits
cumulativelength = 0
nexti = 0
while nexti < len(productof):
    # there are 9*10^(d-1) numbers with d digits, 9*d*10^(d-1) digits total
    newdigits = 9*d*10**(d-1)
    startnum = 10**(d-1)
    while nexti < len(productof) and \
        productof[nexti] <= cumulativelength + newdigits:
        steps = productof[nexti] - cumulativelength # steps into new digits
        steps, extra = steps // d, steps % d # how many numbers to skip
        if extra != 0: # skip steps numbers
            num = startnum + steps
            for j in range(d-extra): num //= 10 # move digit to extract
            prod *= num % 10 # choose digit
            print(': digit', productof[nexti], 'is', num%10, 'from',
                  startnum+steps)
        else: # skip steps-1 numbers, use last digit
            num = startnum + steps - 1
            prod *= num % 10
            print(': digit', productof[nexti], 'is', num%10, 'from', num)
        nexti += 1
    cumulativelength += newdigits
    d += 1
print(prod)


