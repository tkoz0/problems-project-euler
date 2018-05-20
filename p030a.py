
# table of 5th powers so they arent calculated every time
fifths = list(x**5 for x in range(10))
print(':', fifths)

# must satisfy 9^5 * n < 10^n for n digits
# n=6 is satisfactory so pick an upper bound of 9^5 * 6

total = 0
for i in range(10, 6*(9**5)+1):
    ii = i
    s = 0
    while ii != 0: # sum digit exponents
        s += fifths[ii % 10]
        ii //= 10
    if s == i:
        print(':', s)
        total += s
print(total)
