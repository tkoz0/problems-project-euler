
maxperim = 1000000000

# solution with diophantine equation (quadratic)
# triangle has sides a,a,a+-1
# by herons formula, s=(3a+-1)/2 must be integer so a must be odd
# solving a^2=h^2+((a+-1)/2)^2 in both cases gives
# ((3a+-1)/2)^2-3h^2=1 which is pells equation, y=h and x=(3a+-1)/2
# solving pells equation is based on p064 (a=x, b=y)

perimsum = 0
a, b, k = 2, 1, 1 # 2^2-3*1^2=1
while True:
    m = 0
    absk = abs(k)
    for mm in range(1, 1+absk): # floor(sqrt(3))=1
        if (a+b*mm) % absk == 0:
            m = mm
            break
    assert m != 0
    assert (a*m + 3*b) % absk == 0
    assert (a + b*m) % absk == 0
    assert (m**2 - 3) % absk == 0
    a, b, k = (a*m + 3*b) // absk, (a + b*m) // absk, (m**2 - 3) // k
    # after iteration of pells equation, if k==1 then test for triangles
    if k == 1:
        print(': pell solution', a, b, k)
        if (2*a+1) % 3 == 0: # x=(3a-1)/2, a,a,a+1 case
            aa = (2*a+1)//3
            perim = 3*aa-1
            if perim > maxperim: break
            print(': triangle', aa, aa, aa+1)
            perimsum += perim
        if (2*a-1) % 3 == 0: # x=(3a+1)/2, a-1,a,a case
            aa = (2*a-1)//3
            perim = 3*aa+1
            if perim > maxperim: break
            print(': triangle', aa-1, aa, aa)
            perimsum += perim
print(perimsum)
