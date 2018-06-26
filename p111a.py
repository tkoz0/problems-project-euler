import libtkoz as lib

Sn = 10

def MNS(n,d):
    Nnd, Snd = 0, 0
    for Mnd in range(n-1,0,-1):
        mask = ([0] * (n-Mnd)) + ([1] * Mnd) # 1=replaced digit, 0=other digits
        # mask is in big endian
        hasnextpermutation = True
        while hasnextpermutation: # try all mask permutations
            if d == 0 and mask[0] == 1: # cant have 0 at start of number
                hasnextpermutation = lib.lexico_next(mask)
                continue
            # use base 9 to select digits for replacement digits
            # if the b9 digit is b, b<d --> use itself, b>=d --> use b+1
            for b9 in range(0,9**(n-Mnd)): # form numbers with the digits
                if d != 0 and mask[0] == 0 and b9 % 9 == 0:
                    continue # cant put 0 at start of number
                num = 0
                for m in mask:
                    if m == 1: num = (num*10) + d # replaced digit
                    else: # other digits
                        b = b9 % 9
                        if b >= d: b += 1
                        num = (num*10) + b
                        b9 //= 9
                if lib.prime(num):
                    Nnd += 1 # count
                    Snd += num # sum
            hasnextpermutation = lib.lexico_next(mask)
        if Nnd != 0: # found primes with Mnd instances of d
            print(': M(',n,',',d,') = ',Mnd,sep='')
            print(': N(',n,',',d,') = ',Nnd,sep='')
            print(': S(',n,',',d,') = ',Snd,sep='')
            return (Mnd, Nnd, Snd)
    assert 0 # should not reach here

print(sum(MNS(Sn,d)[2] for d in range(10)))
