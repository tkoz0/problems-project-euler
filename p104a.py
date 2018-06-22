import math

phi = (1.0+math.sqrt(5.0))/2.0

a, b = 1, 1
k = 2 # index

while b < 10**8: # get to 9 digit number
    k += 1
    a, b = b, a+b

while True: # use last 9 digits, compute F_k when first 9 are pandigital
    k += 1
    a, b = b, (a+b)%(10**9) # b is next number
    end = ''.join(sorted(str(b))) == '123456789'
    if end:
        print(': fibonacci',k,'ends with digits')
        # to calculate first 9 digits, need F_k / 10^(floor(log10(Fk)-9))
        fl10 = k * math.log10(phi) - math.log10(math.sqrt(5.0))
        exp10 = math.floor(fl10-8) # divide F_k by 10^(this number)
        # dividing by 10^(floor(log10(F_k))) gives 1 digit so subtract 8 from
        # this to get 9 digits
        # ln(F_k/10^(exp10)) = k * ln(phi) - ln(sqrt(5)) - exp10*ln(10)
        digitslog = k*math.log(phi) - math.log(math.sqrt(5)) \
                    - exp10*math.log(10)
        digits = int(math.exp(digitslog))
        print(': start digits are',digits)
        start = ''.join(sorted(str(digits))) == '123456789'
        if start:
            print(': fibonacci',k,'starts with digits')
            print(k)
            break
