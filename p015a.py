import libtkoz as lib

width = 20
height = 20

# too large to solve by brute force, dynamic programming
# direction is left and up for this array
# 0 1 2 ...
# 1 .
# 2   .
grid = [[0] * (width+1)] * (height+1)
grid[0] = [1] * (width+1) # 1 path starting from top row
for i in range(height+1):
    grid[i][0] = 1 # 1 path starting from left side
# now fill in with dynamic solution, paths(x,y) = paths(x-1,y)+paths(x,y-1)
for i in range(1, height+1):
    for j in range(1, width+1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]
print(grid[height][width])

# can be computed faster as a binomial coefficient
# the path is a sequence of 20 ups and 20 lefts, 40 steps
# therefore it is 40!/20!/20!
print(lib.binom_coeff(height+width, height))
