print(sum(x**x for x in range(1,1+1000)) % 10**10)
print(sum(pow(x,x,10**10) for x in range(1,1+1000)) % 10**10)

def modexp(b,p,m):
    sq = b # b^1,b^2,b^4,b^8,...
    ret = 1
    while p != 0:
        if p % 2 == 1:
            ret = (ret * sq) % m
        p //= 2 # shift to next binary digit
        sq = (sq * sq) % m
    return ret

print(sum(modexp(x,x,10**10) for x in range(1,1+1000)) % 10**10)
