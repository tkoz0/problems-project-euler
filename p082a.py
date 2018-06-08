
data = ''
with open('data_files/p082_matrix.txt') as file:
    data = file.read()
data = data.splitlines() # matrix rows
for i,r in enumerate(data): # split rows into each number
    data[i] = list(int(c) for c in r.split(','))

rows = len(data)
cols = len(data[0])

# use a dynamic programming approach, from each cell, pick the min path by going
# up/down in its column and then right
paths = list(r[-1] for r in data) # starting from last column

for c in range(cols-2,-1,-1):
    # first go down and pick right or up as the better direction
    paths[0] += data[0][c] # no up for this one so right is better of the 2
    for r in range(1,rows):
        # include current cell, is going up or right shorter from it
        paths[r] = min(paths[r] + data[r][c], paths[r-1] + data[r][c])
    # now determine if going down would be better for any
    for r in range(rows-2,-1,-1):
        paths[r] = min(paths[r], paths[r+1] + data[r][c])
print(min(paths))
