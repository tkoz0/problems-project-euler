import libtkoz as lib

maxdigits = 100 # given is count nonbouncies below 10**100

# counting, inclusion exclusion tells us that the solution is
# |increasing| + |decreasing| - |increasing and decreasing|
# increasing is n+8 choose 8 since there are n digits and we need 8 dividors
# for 9 possible digits (they cant start with 0)
# decreasing is n+9 choose 9 with the 9 divider requirement for 10 digits
# for each length n, there are 9 that are both increasing and decreasing which
# are those consisting of a single digit
# decreasing also will count an all zeroes number but since this is invalid
# we must also subtract another 1 for n digit non bouncy count

# sum n+9 choose 9, n+8 choose 8, and -9 from n=1 to n=100

print(sum((lib.binom_coeff(n+9,9) + lib.binom_coeff(n+8,8) - 9 - 1)
          for n in range(1,maxdigits+1)))

# simpler, without summation (consider numbers up to n digits)
# for increasing, consider all digits and use 9 dividers, if it starts with 0s
# then it is a number with fewer digits so there are n+9 choose 9 minus 1
# (the minus 1 is the number with all 0s)
# for decreasing, use 10 dividers, 0s followed by 9s,8s,...,1s,0s so we consider
# numbers of varying digits
# we get a number of all zeroes if the 10 dividers are in the same place which
# happens n+1 times, in total this has n+10 choose 10 possibilities minus n+1
# the numbers counted twice are those with same digits so subtract 9*n
# combining we get (n+9 choose 9) + (n+10 choose 10) - 2 - 10n
print(lib.binom_coeff(maxdigits+9,9) + lib.binom_coeff(maxdigits+10,10)
      - 2 - 10*maxdigits)
