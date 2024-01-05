from math import factorial
print(sum(map(int,str(factorial(100)))))

num = [1] # start at 1
for n in range(1,1+100): # multiply 1,2,..,100
    carry = 0
    for i in range(len(num)):
        tmp = n*num[i] + carry
        num[i] = tmp % 10
        carry = tmp // 10
    # at the end, we may need to append extra digits for carry
    while carry > 0:
        num.append(carry % 10)
        carry //= 10
print(sum(num))
