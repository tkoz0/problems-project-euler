R = 20
C = 20

# dp[r][c] is the solution for a r*c grid
dp = [[0]*(C+1) for _ in range(R+1)]

# 1 path along the edges
for r in range(R+1):
    dp[r][0] = 1
for c in range(C+1):
    dp[0][c] = 1

# fill in the rest of the sub problems
for r in range(1,R+1):
    for c in range(1,C+1):
        dp[r][c] = dp[r-1][c] + dp[r][c-1]

# the solution is dp[20][20]
print(dp[R][C])
