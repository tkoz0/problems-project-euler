
# brute force with reduced possibilities
# given 9 --> 918273645 so the first number must start with 9
# 2 digit --> 2+3+3=8, 2+3+3+3=11 so cant make length 9
# 3 digit --> 3+4=7, 3+4+4=11 so also cant make length 9
# 4 digit --> 4+5=9 so first number is 4 digit
# reduce range to between 9876 and 9123
for n in range(9876, 9123-1, -1):
    result = str(n) + str(2*n)
    if ''.join(sorted(result)) == '123456789': # has each digit
        print(result)
        break

