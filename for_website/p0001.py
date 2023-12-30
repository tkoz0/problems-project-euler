L = 1000
total = 0
for i in range(1,L):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

L = 999
S = lambda d: d*(L//d)*(L//d+1)//2
print(S(3)+S(5)-S(15))
