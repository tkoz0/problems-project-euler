
maxperim = 1000

# is brute forceable, slow in python, ~45 sec (i5-2540m), still under 1 min
# brute force, for each perimeter p, try to find all a^2+b^2=c^2 with
# a+b+c=p and a<b<c, so a<=p/3, a<b<=a+(p-a)/2
mostsol = 0
bestnum = 0
for p in range(3, maxperim+1):
    solutions = 0
    for a in range(1, p//3+1):
        for b in range(a+1, a+(p-a)//2+1):
            c = p - a - b
            if a**2 + b**2 == c**2: solutions += 1
    if solutions > mostsol:
        print(': better perimeter', p)
        mostsol, bestnum = solutions, p
print(bestnum)
