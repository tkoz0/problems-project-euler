
# brute force, ~10sec (cpython / i5-2540m)

# number is 1_2_3_4_5_6_7_8_9_0 (19  digits, >10**18)
# begin counting from 10**9
# since number ends in 0, square root must be a multiple of 10
# additionally, if we divide the number by 100 and its square root by 10, the
# last digit is 9 in the perfect square so the square root must be congruent
# to 30 or 70 modulo 100

root = 10**9 + 30
while True:
    num = root**2 # divide and check digits
    d = 9
    success = True
    while d != 0: # divide by 100 to check digits
        num //= 100
        if num % 10 != d:
            success = False
            break
        d -= 1
    if success: break
    if root % 100 == 30: root += 40 # to get to *70
    else: root += 60 # *70 to *30
print(root)
