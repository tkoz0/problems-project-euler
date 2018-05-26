import libtkoz as lib

limit = 1000000

# brute force, do base 10 first since it should be a faster function
# ~0.75 sec (i5-2540m)
total = 0
for i in range(1, limit):
    if lib.palindrome(i) and lib.palindrome_base2(i):
        print(':', i)
        total += i
print(total)

