
# a(1) = 1
# a(2*n) = 2*a(n)
# a(2*n+1) = a(n) - 3*a(n+1)

# O(log(n)) time to compute a(n)
def a(n):
    if n == 1: return 1
    n,r = divmod(n,2)
    if r == 0:
        return 2*a(n)
    else:
        return a(n) - 3*a(n+1)

# analyze the series
# a(1) + a(2) + a(3) + ... + a(N) (where N is even)
# = 1 + 2*a(1) + 2*a(2) + ... + 2*a(N//2)
#     + (a(1) - 3*a(2)) + (a(2) - 3*a(3)) + ... + (a(N//2-1) - 3*a(N//2))
# = 1 + 3*a(1) + 3*a(2) + ... + 3*a(N//2-1) + 2*a(N//2)
#              - 3*a(2) - ... - 3*a(N//2-1) - 3*a(N//2)
# = 4 - a(N//2)

N = 10**12
ans = 4 - a(N//2)
if N % 2 == 1:
    ans += a(N)
print(ans)
