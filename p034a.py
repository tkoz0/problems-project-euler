
factorials = [1]
for i in range(1, 10):
    factorials.append(i * factorials[-1])
print(': generated', factorials)

# took about 7 sec (i5-2540m)
# 9!*n < 10^n means maximum possible value is under highest number
# n=6 --> 9!*6 < 10^6 is false
# n=7 --> 9!*7 < 10^7 is true
# induction can show this is true for all n>=7
# go up to 7 digits, limit should be 9!*7
total = 0
for n in range(10, 7*factorials[9]):
    s = 0 # factorial sum
    for c in str(n):
        s += factorials[int(c)]
    if n == s:
        print(': found', n)
        total += n
print(total)
