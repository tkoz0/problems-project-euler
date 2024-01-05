largest = 0
for n in range(1,10000):
    s = str(n)
    for i in range(2,10):
        s += str(i*n)
        if len(s) >= 9:
            break
    if ''.join(sorted(s)) == '123456789':
        print(f'found {n} -> {s}')
        largest = max(largest,int(s))
print(largest)
