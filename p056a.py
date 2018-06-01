import libtkoz as lib

numlim = 100

# brute force with python large integer support
maxsum = 0
for a in range(1,numlim):
    for b in range(1,numlim):
        dsum = lib.sum_digits(a**b)
        if dsum > maxsum:
            maxsum = dsum
            print(':', a, '**', b, 'has digit sum', dsum)
print(maxsum)
