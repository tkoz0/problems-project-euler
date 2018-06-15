
exceeddiscs = 10**12

# the probability is (x/y)*((x-1)/(y-1)) = 1/2, x=blue, y=blue+red
# rearranging this gives a pell like equation: (2y-1)^2 - 2(2x-1)^2 = -1
# (not proven here) when D=2 from p066, the k value cycles -1,1,-1,1,...
# when k=-1 then there is a solution
# solve with a=2y-1, b=2x-1, then get x from b for solution

largestblue = 0
a, b, k = 1, 1, -1 # 1^2 - 2*1^2 = -1
while True: # iterate pell solution based on p066
    m = 0
    absk = abs(k)
    for mm in range(1,1+absk):
        if (a+b*mm) % absk == 0:
            m = mm
            break
    a, b, k = (a*m + 2*b) // absk, (a + b*m) // absk, (m**2 - 2) // k
    if k == -1 and (b+1) % 2 == 0 and (a+1) % 2 == 0: # x = (b+1)/2, y = (a+1)/2
        x, y = (b+1) // 2, (a+1) // 2
        if y > exceeddiscs: break # y is number of discs
        largestblue = x # x is number of blue discs
        print(': blue =', x, ', red =', y-x)
print(x)
