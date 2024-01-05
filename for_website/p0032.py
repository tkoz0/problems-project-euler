c_set = set()
for a in range(2,100):
    for b in range(a+1,10000//a+1):
        c = a*b
        s = str(a) + str(b) + str(c)
        if ''.join(sorted(s)) == '123456789':
            print(f'product {a} * {b} = {c}')
            c_set.add(c)
print(sum(c_set))
