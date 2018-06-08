
data = ''
with open('data_files/p083_matrix.txt') as file:
    data = file.read()
data = data.splitlines() # matrix rows
for i,r in enumerate(data): # split rows into each number
    data[i] = list(int(c) for c in r.split(','))

rows = len(data)
cols = len(data[0])

inf = rows * cols * max(max(r) for r in data) + 1 # value to use as infinity

# solve with dijkstra's algorithm, not an easy way to restrict the matrix to a
# smaller part and find the best solution for that part
# for simplicity, no priority queue, ~7sec (i5-2540m)

# use 0,0 as the source vertex, target vertex will be rows-1,cols-1
distances = list(list(inf for c in range(cols)) for r in range(rows))
distances[0][0] = data[0][0]
unvisited = set()
for i in range(rows): # all vertices initially unvisited
    for j in range(cols): unvisited.add((i,j))

while len(unvisited) != 0: # dijkstra's algorithm on every vertex
    u = next(enumerate(unvisited))[1] # pick something
    for u2 in unvisited: # find closest unvisited vertex to source
        if distances[u2[0]][u2[1]] < distances[u[0]][u[1]]: u = u2
    unvisited.remove(u)
    # try neighboring vertices now
    if u[1] < cols-1: # right: row,col+1
        dist = distances[u[0]][u[1]] + data[u[0]][u[1]+1]
        distances[u[0]][u[1]+1] = min(distances[u[0]][u[1]+1],dist)
    if u[0] > 0: # up: row-1,col
        dist = distances[u[0]][u[1]] + data[u[0]-1][u[1]]
        distances[u[0]-1][u[1]] = min(distances[u[0]-1][u[1]],dist)
    if u[1] > 0: # left: row,col-1
        dist = distances[u[0]][u[1]] + data[u[0]][u[1]-1]
        distances[u[0]][u[1]-1] = min(distances[u[0]][u[1]-1],dist)
    if u[0] < rows-1: # down: row+1,col
        dist = distances[u[0]][u[1]] + data[u[0]+1][u[1]]
        distances[u[0]+1][u[1]] = min(distances[u[0]+1][u[1]],dist)
# pick distance to target as solution
print(distances[-1][-1])
