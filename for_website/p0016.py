print(sum(map(int,str(2**1000))))

P = 1000
number = [1] # start at 1
for _ in range(P):
    carry = 0
    for i in range(len(number)): # multiply by 2
        tmp = 2*number[i] + carry
        number[i] = tmp % 10
        carry = tmp // 10
    if carry > 0: # number gets a digit longer
        number.append(carry)
print(sum(number))
