
limit = 10**7

set1 = set()
set2 = set()
set3 = set()
set7 = set()

a = 1
while a*a < limit:
    a2 = a*a
    b = 1
    while a2+b*b < limit:
        set1.add(a2+b*b)
        b += 1
    b = 1
    while a2+2*b*b < limit:
        set2.add(a2+2*b*b)
        b += 1
    b = 1
    while a2+3*b*b < limit:
        set3.add(a2+3*b*b)
        b += 1
    b = 1
    while a2+7*b*b < limit:
        set7.add(a2+7*b*b)
        b += 1
    a += 1
print(':',len(set1),len(set2),len(set3),len(set7))
print(len(set1.intersection(set2).intersection(set3).intersection(set7)))
