
# a(1) = 1
# a(2*n) = 2*a(n)
# a(2*n+1) = a(n) - 3*a(n+1)

# worst case O(n) time, but fast enough for the given value 10^12
# probably related to the hamming weight of the input
# particularly bad case example: 2^0 + 2^2 + 2^4 + 2^6 + ... + 2^(2*n)
# but improved with memoization, to O(log(n)) time
num_calls = 0
mem_cache = dict()
mem_cache[1] = 1
def a(n):
    global num_calls,mem_cache
    num_calls += 1
    if n in mem_cache:
        return mem_cache[n]
    nn,r = divmod(n,2)
    if r == 0:
        ret = 2*a(nn)
    else:
        ret = a(nn) - 3*a(nn+1)
    mem_cache[n] = ret
    return ret

# analyze the series
# a(1) + a(2) + a(3) + ... + a(N) (where N is even)
# = 1 + 2*a(1) + 2*a(2) + ... + 2*a(N//2)
#     + (a(1) - 3*a(2)) + (a(2) - 3*a(3)) + ... + (a(N//2-1) - 3*a(N//2))
# = 1 + 3*a(1) + 3*a(2) + ... + 3*a(N//2-1) + 2*a(N//2)
#              - 3*a(2) - ... - 3*a(N//2-1) - 3*a(N//2)
# = 4 - a(N//2)

# analyze the memoized time complexity
# if n ends in k zeros, we just compute a(n),a(n//2),a(n//4),...,a(n//2**k)
# if n ends in k ones, think of it as ...011...11
# (this analysis also works if it is all ones)
# to compute a(n) we need a(n//2) -> odd, continue
#                 and a((n+1)//2) -> even and divisible by 2**k
# then to compute a(n//2) we need a(n//4) -> odd, continue
#                         and a((n+1)//4) -> even, computed for a((n+1)//2)
# ...
# continues to a(n//2**k) (even)
#          and a((n+1)//2**k) (odd)
# from here, a(n//2**k) depends on a(n//2**(k+1))
# a((n+1)//2**k) depends on a(n//2**(k+1))
#                       and a(n//2**(k+1) + 1)
# from here, use the following which applies to the odd case above
# if we depend on n,n+1 then
# if n is even, we need n//2,n//2+1
# if n is odd, we need (n-1)//2,(n+1)//2
# in both cases, we depend on consecutive integers
# this continues down to bottom and can be used to show the limits
# a(n) is memoized for <= 2*(1+ceil(log2(n))) values
# a(n) is called <= 3*(1+ceil(log2(n))) times

N = 10**12
#N = sum(2**z for z in range(0,32,2))
#import random; N = random.randint(2**255,2**256-1)
ans = 4 - a(N//2)
if N % 2 == 1:
    ans += a(N)
print(f': a(n) called {num_calls} times')
print(f': a(n) cached {len(mem_cache)} times')
print(ans)
