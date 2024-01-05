# cache factorials
f = [1]
while len(f) < 10:
    f.append(len(f)*f[-1])

total = 0
for n in range(10,7*f[9]+1):
    n2 = n
    s = 0 # digit factorial sum
    while n2: # take digits lowest to highest
        s += f[n2%10]
        n2 //= 10
    if s == n:
        print(f'solution {n}')
        total += n
print(total)
