pow5 = [d**5 for d in range(10)]
total = 0
for n in range(10,6*(9**5)+1):
    powsum = sum(pow5[int(d)] for d in str(n))
    if n == powsum:
        total += n
        print(f'found {n}')
print(total)
