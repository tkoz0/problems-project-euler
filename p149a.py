
side = 2000

# start by generating grid, 4000000 length array, row major order
grid = list(list(0 for c in range(side)) for r in range(side))
randomstart = lambda k : (100003 - 200003*(k+1) + 300007*((k+1)**3)) % 1000000 \
    - 500000
randomseedcount = 55

def put(i,n):
    global grid
    grid[i//side][i%side] = n
def get(i):
    global grid
    return grid[i//side][i%side]

for i in range(randomseedcount): put(i,randomstart(i))
for i in range(randomseedcount,side**2): put(i, # lagged fibonacci part
    ((get(i-24) + get(i-55) + 1000000) % 1000000) - 500000)
print(': generated grid')

# search each line efficiently, create a sum and reset it to 0 when it becomes
# negative, a negative component will count against the sum

def search_line(indexes): # given range object, search this line
    global grid, side
    maxsum = 0
    s = 0
    for i in indexes:
        s += get(i)
        if s < 0: s = 0
        else: maxsum = max(maxsum,s)
    return maxsum

maxsum = 0
for r in range(side): # search rows
    maxsum = max(maxsum, search_line(range(r*side,(r+1)*side)))
print(': searched rows', maxsum)
for c in range(side): # search columns
    maxsum = max(maxsum, search_line(range(c,side**2,side)))
print(': searched cols', maxsum)
for r in range(side): # diagonal down right starting from left
    maxsum = max(maxsum, search_line(range(r*side,side**2,side+1)))
print(': searched diagonal down right starting from left', maxsum)
for c in range(side): # diagonal down right starting from top
    maxsum = max(maxsum, search_line(range(c,side*(side-c),side+1)))
print(': searched diagonal down right starting from top', maxsum)
for r in range(side): # diagonal up right starting from left
    maxsum = max(maxsum, search_line(range(r*side,-1,1-side)))
print(': searched diagonal up right starting from left', maxsum)
for c in range(side): # diagonal up right starting from bottom
    maxsum = max(maxsum, search_line(range(side*(side-1)+c,
                                           side*(c+1)-1,1-side)))
print(': searched diagonal up right starting from bottom', maxsum)
print(maxsum)
