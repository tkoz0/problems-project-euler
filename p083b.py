
# modified to use a priority queue (binary heap) for greater efficiency in
# determining the vertex closest to the source
# additionally the algorithm can stop once the destination is visited
# the priority queue makes this solution about 30 times faster

data = ''
with open('data_files/p083_matrix.txt') as file:
    data = file.read()
data = data.splitlines() # matrix rows
for i,r in enumerate(data): # split rows into each number
    data[i] = list(int(c) for c in r.split(','))
rows = len(data)
cols = len(data[0])
inf = rows * cols * max(max(r) for r in data) + 1 # value to use as infinity

class pqueue: # min heap implementation with access to middle elements
    def __init__(self):
        # binary heap, children of i are 2i+1 and 2i+2
        self._heap = [] # store as tuple of (priority/distance, item)
        self._locs = dict() # map heap items to their index in the heap
    def _swap(self, a, b): # O(1), switch positions of 2 indexes in heap
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]
        self._locs[self._heap[a][1]] = a # update indexes in heap
        self._locs[self._heap[b][1]] = b
    def push(self, item, priority): # O(logn), append to heap, sift up
        i = len(self._heap)
        self._heap.append((priority, item))
        while i != 0 and self._heap[(i-1)//2][0] > self._heap[i][0]:
            self._swap(i,(i-1)//2)
            i=(i-1)//2
        self._locs[item] = i # insert data about location
    def pop(self): # move back to front, sift down
        self._locs.pop(self._heap[0][1]) # remove info about top from locations
        self._heap[0] = self._heap[-1] # remove top by replacing it with back
        self._heap.pop()
        i = 0 # sift down
        while 2*i+1 < len(self._heap): # child exists
            s = i
            if self._heap[2*i+1][0] < self._heap[s][0]: # left child is smaller
                s = 2*i+1
            # right child exists and is smaller
            if 2*i+2 < len(self._heap) \
                and self._heap[2*i+2][0] < self._heap[s][0]:
                s = 2*i+2
            if s != i:
                self._swap(i,s) # swap with child
                i = s
            else: break # valid position found
    def top(self): return self._heap[0]
    def size(self): return len(self._heap)
    def empty(self): return len(self._heap) == 0
    # for this problem, priorities only decrease so only sift up
    def update(self, item, priority):
        i = self._locs[item]
        assert priority < self._heap[i][0]
        self._heap[i] = (priority, item)
        while i != 0 and self._heap[(i-1)//2][0] > self._heap[i][0]:
            self._swap(i,(i-1)//2)
            i=(i-1)//2

# use 0,0 as the source vertex, target vertex will be rows-1,cols-1
distances = list(list(inf for c in range(cols)) for r in range(rows))
distances[0][0] = data[0][0]

unvisited = pqueue() # initialize a queue with distances as priority
for i in range(rows):
    for j in range(cols): unvisited.push((i,j),distances[i][j])

while not unvisited.empty(): # dijkstra's algorithm on every vertex
    nextvertex = unvisited.top() # (priority,item)
    unvisited.pop()
    u = nextvertex[1] # the coordinates
    # try neighboring vertices now
    if u[1] < cols-1: # right: row,col+1
        dist = distances[u[0]][u[1]] + data[u[0]][u[1]+1]
        if dist < distances[u[0]][u[1]+1]: # better distance
            distances[u[0]][u[1]+1] = dist
            unvisited.update((u[0],u[1]+1),dist) # fix position in queue
    if u[0] > 0: # up: row-1,col
        dist = distances[u[0]][u[1]] + data[u[0]-1][u[1]]
        if dist < distances[u[0]-1][u[1]]:
            distances[u[0]-1][u[1]] = dist
            unvisited.update((u[0]-1,u[1]),dist)
    if u[1] > 0: # left: row,col-1
        dist = distances[u[0]][u[1]] + data[u[0]][u[1]-1]
        if dist < distances[u[0]][u[1]-1]:
            distances[u[0]][u[1]-1] = dist
            unvisited.update((u[0],u[1]-1),dist)
    if u[0] < rows-1: # down: row+1,col
        dist = distances[u[0]][u[1]] + data[u[0]+1][u[1]]
        if dist < distances[u[0]+1][u[1]]:
            distances[u[0]+1][u[1]] = dist
            unvisited.update((u[0]+1,u[1]),dist)
    if u == (rows-1,cols-1): break # can stop once target is visited
# pick distance to target as solution
print(distances[-1][-1])
