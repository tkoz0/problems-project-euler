import libtkoz as lib

nval = 10#10000
modulus = 10**100#10**9+7

# generate the Pn and Cn sequences
pn = []
cn = []
i = 2
while len(pn) < nval or len(cn) < nval:
    ip = lib.prime(i)
    if ip and len(pn) < nval: pn.append(i)
    if not ip and len(cn) < nval: cn.append(i)
    i += 1
pn = list(lib.digital_root(i) for i in pn)
cn = list(lib.digital_root(i) for i in cn)
print(': P_n',pn)
print(': C_n',cn)

superint = []
pi = 0 # indexes in pn an cn
ci = 0
while pi < len(pn):
    # start by picking smaller digit unless we can maximize intersecting digits
    # by picking the other
    if ci < len(cn):
        if pn[pi] < cn[ci]:
            superint += [pn[pi]]
            pi += 1
        elif cn[ci] < cn[pi]:
            superint += [cn[ci]]
            ci += 1
        else: # equal digits
            superint += [pn[pi]]
            pi += 1
            ci += 1
    else: # finished Cn digits
        superint += pn[pi:]
        pi = len(pn)
superint += cn[ci:] # pn finished, put remaining from cn

num = 0
for d in superint: num = (num*10 + d) % modulus
print(num)
