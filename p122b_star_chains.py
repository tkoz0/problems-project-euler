
# star addition chains add an additional constraint that next numbers in the
# addition chain are calculated by summing the last one with another one:
# (a1,...,an) can be extended with an+an,an+an-1,...,an+a1
# these are optimal for exponents < 12509 so it works for this problem but
# there exist optimal addition chains which are not star addition chains

LIMIT = 200

length = [LIMIT+1]*(LIMIT+1)
length[0] = 0
path = [0]*(LIMIT+1)

def backtrack(pow,depth):
    global path,length
    if pow>LIMIT or depth>length[pow]: return
    length[pow] = depth
    path[depth] = pow
    for i in range(depth,-1,-1): backtrack(pow+path[i],depth+1)

backtrack(1,0)
print(sum(length))

