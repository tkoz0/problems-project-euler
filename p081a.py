
data = ''
with open('data_files/p081_matrix.txt') as file:
    data = file.read()
data = data.splitlines() # matrix rows
for i,r in enumerate(data): # split rows into each number
    data[i] = list(int(c) for c in r.split(','))

rows = len(data)
cols = len(data[0])

# dynamic programming approach, choose minimum for each
# start with the sides (top and left), there is only 1 way towards the corner
# for cell r,c, its best path sum is the minimum of r-1,c and r,c-1
for i in range(1,rows): # left
    data[i][0] += data[i-1][0]
for i in range(1,cols): # top
    data[0][i] += data[0][i-1]
# now for all other cells, pick min of above and left
for i in range(1,rows):
    for j in range(1,cols):
        data[i][j] += min(data[i-1][j], data[i][j-1])
print(data[-1][-1]) # lower right corner has solution
