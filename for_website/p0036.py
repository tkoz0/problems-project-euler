L = 1000000
total = 0

# handle single digits separately
for n in range(1,10):
    dstr = str(n)
    bstr = f'{n:b}'
    if dstr == dstr[::-1] and bstr == bstr[::-1]:
        total += n
        print(f'palindrome {n}')

# generate base 10 palindromes
l = 1 # length of a half
while True:
    if 10**(2*l-1) >= L:
        break
    for h in range(10**(l-1),10**l): # even length loop
        dstr = str(h) + str(h)[::-1]
        n = int(dstr)
        if n >= L:
            break
        bstr = f'{n:b}'
        if bstr == bstr[::-1]:
            total += n
            print(f'palindrome {n}')
    for h in range(10**(l-1),10**l): # odd length loop
        end_loop = False
        for m in range(10): # middle digit
            dstr = str(h) + str(m) + str(h)[::-1]
            n = int(dstr)
            if n >= L:
                end_loop = True
                break
            bstr = f'{n:b}'
            if bstr == bstr[::-1]:
                total += n
                print(f'palindrome {n}')
            if end_loop:
                break
    l += 1
print(total)
