
seq = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
exceed = 10**15

# D: n%3==0 --> n//3, inverse in n --> 3n
# U: n%3==1 --> (4n+2)//3, inverse is n --> (3n-2)//4, require n%4==2
# d: n%2==2 --> (2n-1)//3, inverse is n --> (3n+1)//2, require n%2==1

# work backwards by first knowing the ratio by which the number changes
ratio = 1
for s in seq:
    if s == 'D': ratio=ratio/3.0
    elif s == 'U': ratio=ratio*4.0/3.0
    elif s == 'd': ratio=ratio*2.0/3.0
    else: assert 0
print(': start num changes by ratio',ratio)

# try starting numbers and find one that gets high enough by reversing
end = int(exceed*ratio)
print(': trying end num from',end)
while True:
    num = end
    success = True
    for s in seq[::-1]:
        if s == 'D': num *= 3
        elif s == 'U':
            if num % 4 != 2:
                success = False
                break
            num = (3*num - 2)//4
        elif s == 'd':
            if num % 2 != 1:
                success = False
                break
            num = (3*num + 1)//2
    if success and num > exceed:
        print(': start =',num,'end =',end)
        print(num)
        break
    end += 1
