
# a(1) = 1
# a(2*n) = 2*a(n)
# a(2*n+1) = a(n) - 3*a(n+1)

# worst case O(n) time, but fast enough for the given value 10^12
# probably related to the hamming weight of the input
# particularly bad case example: 2^0 + 2^2 + 2^4 + 2^6 + ... + 2^(2*n)
# but improved with memoization, seems to be O(log(n)) but needs analysis
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

N = 10**12
#N = sum(2**z for z in range(0,32,2))
#import random; N = random.randint(2**255,2**256-1)
ans = 4 - a(N//2)
if N % 2 == 1:
    ans += a(N)
print(f': a(n) called {num_calls} times')
print(f': a(n) cached {len(mem_cache)} times')
print(ans)
