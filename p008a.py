from numpy import prod
adjlen = 13
digits = """\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450\
"""

# brute force, try all products
largest = 0
for i in range(adjlen, len(digits)+1):
    prod = 1
    for d in digits[i-adjlen:i]:
        prod *= int(d)
    largest = max(largest, prod)
print(largest)

# create product and use multiply and divide to move the 13 digits
largest = 0
i1 = 0 # start index of product
while i1 < len(digits):
    prod = 1
    i2 = i1 # end of product sequence
    if i2 + adjlen >= len(digits): # cannot form 13 digit product
        print(': cant start at', i2)
        break
    success = True
    while i2 < i1 + adjlen: # create product of 13 digits
        d = int(digits[i2])
        if d == 0: # found 0, try again
            success = False
            break
        else:
            prod *= d
        i2 += 1
    if not success:
        i1 = i2 + 1 # start after zero
        continue
    print(': made sequence', i1, i2)
    # multiply and divide until zero found
    # d************m, divide out d, multiply m, shift forward 1
    largest = max(largest, prod)
    while i2 < len(digits) and prod != 0:
        assert prod % int(digits[i1]) == 0
        prod //= int(digits[i1])
        prod *= int(digits[i2])
        i1 += 1
        i2 += 1
        largest = max(largest, prod)
    i1 = i2 # start after end
print(largest)
