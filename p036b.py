import libtkoz as lib
import math

limit = 1000000

# generate palindromes
total = 1 + 3 + 5 + 7 + 9 # consider single digit numbers separately
for digits in range(2, math.ceil(math.log10(limit))+1):
    palinhalf = digits // 2
    if digits % 2 == 1: # odd length, insert extra digit in middle
        for i in range(10**(palinhalf-1), 10**palinhalf):
            for j in '0123456789':
                palin = int(str(i) + j + str(i)[::-1])
                if lib.palindrome_base2(palin):
                    total += palin
                    print(':', palin)
    else: # even length
        for i in range(10**(palinhalf-1), 10**palinhalf):
            palin = int(str(i) + str(i)[::-1])
            if lib.palindrome_base2(palin):
                total += palin
                print(':', palin)
print(total)

