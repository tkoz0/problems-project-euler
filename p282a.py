from libtkoz import knuth_arrow

M = 14**8 # 2^8 * 7^8
Mtot = (M*1//2)*6//7
# map (m,n) to known ackermann function values to reduce recursion levels
cache:dict[tuple[int,int],int] = dict()
def A(m:int,n:int):
    global cache,M
    if (m,n) in cache: return cache[(m,n)]
    v = 0 # set to value of A(m,n), then insert in cache and return
    if m == 0: v = (n+1)%M
    elif n == 0: v = A(m-1,1)%M # m>0 and n=0
    else: v = A(m-1,A(m,n-1))%M # m>0 and n>0
    cache[(m,n)] = v
    print(f'A({m},{n})={v}')
    return v

# this does not work, recursion depth at n=4
#print(sum(A(n,n) for n in range(4)))

ret = 1 + 3 + 7 + 61 # A(0,0)+A(1,1)+A(2,2)+A(3,3)
ret += knuth_arrow(2,2,7,M) - 3
ret += knuth_arrow(2,3,8,M) - 3
ret += knuth_arrow(2,4,9,M) - 3
print(ret % M)

# answer is 1098988351
# about 5sec on i5-8265U
