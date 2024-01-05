di = [10**n for n in range(7)]

digits = []
l = 1 # length of next numbers to append
cl = 0 # cumulative preceding length
while cl < max(di):
    nmin,nmax = 10**(l-1),10**l-1
    numdigits = l*9*10**(l-1)
    imin,imax = cl+1,cl+numdigits
    for i in di:
        if imin <= i <= imax:
            offset_num,offset_digit = divmod(i-imin,l)
            num = nmin + offset_num
            num_str = str(num)
            digits.append(int(num_str[offset_digit]))
    cl += numdigits
    l += 1
print(digits)
prod = 1
for d in digits:
    prod *= d
print(prod)
